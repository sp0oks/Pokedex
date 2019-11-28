from flask import Flask, jsonify, request

from database import PokedexData

server = Flask(__name__)
server.config.from_object('config.Config') 
server.db = PokedexData(server.config['MONGODB_URL'])

default_headers = {'Access-Control-Allow-Origin': '*'}


@server.route('/', methods=['GET'])
def index():
    limit = request.args.get('limit') or 21
    offset = request.args.get('offset') or 0
    data = server.db.get_pokemon_basic(limit, offset)
    msg = 'Welcome to the Pokedex API!'

    if data.get('error'):
        return jsonify(msg='Could not access the API, received HTTP error.'), data.get('error')

    return jsonify(msg=msg, pokemon=data), 200, default_headers


@server.route('/pokemon/<filter_type>/<_filter>', methods=['GET'])
def poke_info(filter_type, _filter):
    data = {'error': 'Invalid parameters, expected Pokemon name'}
    status_code = 400
    if filter_type == 'name':
        data, status_code = server.db.find_pokemon(name=_filter)
    return jsonify(pokemon=data), status_code, default_headers
