import re
from datetime import datetime, timedelta
from threading import Thread

import requests
from pymongo import MongoClient


class ApiCache:
    def __init__(self, max_lifetime=300):
        # Url - Time of request pairs
        self.requests = {}
        # Url - Content of response pairs
        self.responses = {}
        # Url - Response code (other than 200) pairs
        self.errors = {}
        self.max_lifetime = max_lifetime

    def cache_request(self, url):
        response = requests.get(url)
        # If response is valid, cache it
        if response.ok:
            self.requests[url] = datetime.now()
            self.responses[url] = response.json()
        else:
            self.errors[url] = response.status_code

    def purge_request(self, url):
        self.requests.pop(url, None)
        self.responses.pop(url, None)
        self.errors.pop(url, None)

    def is_cached(self, url):
        if url in self.requests.keys():
            if url not in self.errors.keys() and \
                    datetime.now() - self.requests[url] <= timedelta(seconds=self.max_lifetime):
                return True
            # Content is expired or empty, remove key
            self.purge_request(url)
        return False


class PokedexData:
    def __init__(self, db_url, cache_limit=300):
        # PokeAPI static information
        self.api_url = 'https://pokeapi.co/api/v2/pokemon/'
        self.sprites_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'
        self.IMG_PATTERN = re.compile(r'/pokemon/(?P<id>[0-9]+)/')
        # API requests cache
        self.api_cache = ApiCache(cache_limit)
        # Mongo data sources
        self.client = MongoClient(db_url)
        self.pokedex = self.client.pokedex

    def get_pokemon_basic(self, limit=20, offset=0):
        """
        Gets basic information from the api of a number of Pokemon
        """
        request_url = self.api_url + f'?limit={int(limit)}&offset={int(offset)}'

        if not self.api_cache.is_cached(request_url):
            self.api_cache.cache_request(request_url)

        response = self.api_cache.responses.get(request_url)

        if response:
            for poke in response['results']:
                poke_id = re.search(self.IMG_PATTERN, poke['url']).group('id')
                img_url = self.sprites_url + f'{poke_id}.png'
                poke['id'] = poke_id
                poke['img'] = img_url
            Thread(target=self.store_pokemon, args=[response['results']]).start()
            return response

        return {'error': self.api_cache.errors[request_url]}

    def get_pokemon_info(self, poke_id):
        """
        Gets specific information from the api of one Pokemon
        """
        request_url = self.api_url + poke_id
        if not self.api_cache.is_cached(request_url):
            self.api_cache.cache_request(request_url)
        info = self.api_cache.responses.get(request_url)
        query_result = self.store_pokemon(info)
        if len(query_result):
            # If information was successfully added to db, purge it from cache for performance
            self.api_cache.purge_request(request_url)
        return info

    def store_pokemon(self, data=None):
        """
        Updates information of a list of Pokemon (creating new records if needed)
        """
        results = []
        if data:
            for pokemon in data:
                result = self.pokedex.pokemon.find_one_and_update({'id': pokemon['id']},
                                                                  {'$set': pokemon}, upsert=True)
                if result:
                    results.append(result['id'])
        return results

    def find_pokemon(self, **kwargs):
        """
        Finds information from one Pokemon given it's ID or (part of) Name
        """
        result = ({}, 204)

        if kwargs.get('id'):
            info = self.pokedex.pokemon.find_one({'id': kwargs['id']})
            # Information about this Pokemon is unknown or incomplete
            if not info or 'moves' not in info.keys():
                info = self.get_pokemon_info(kwargs['id'])
                if info:
                    result[0][info['id']] = info

        elif kwargs.get('name'):
            info = self.pokedex.pokemon.find({'name': {'$regex': kwargs['name'], '$options': 'i'}})
            for pokemon in info:
                # Information about this Pokemon is incomplete
                if 'moves' not in pokemon.keys():
                    pokemon = self.get_pokemon_info(pokemon['id'])
                    if pokemon:
                        result[0][pokemon['id']] = pokemon
        # If there was at least one result, change HTTP status from 204 (No Content) to 200 (OK)
        if len(result[0].keys()):
            result = (result[0], 200)
        return result
