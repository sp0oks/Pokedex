from flask import Flask, jsonify, request

from database import PokedexData

server = Flask(__name__)
server.config.from_object('config.Config') 
server.db = PokedexData(server.config['MONGODB_URL'])


@server.route('/', methods=['GET'])
def index():
    limit = request.args.get('limit') or 20
    offset = request.args.get('offset') or 0
    data = server.db.get_pokemon_basic(limit, offset)
    msg = 'Welcome to the Pokedex API!'

    if data.get('error'):
        return jsonify(msg='Could not access the API, received HTTP error.'), data.get('error')

    return jsonify(msg=msg, pokemon=data), 200


@server.route('/pokemon/<string:_filter>', methods=['GET'])
@server.route('/pokemon/<int:_filter>', methods=['GET'])
def poke_info(_filter):
    data = {'error': 'Invalid parameters, expected Pokemon name/id'}
    status_code = 400
    if isinstance(int, _filter):
        data, status_code = server.db.find_pokemon(id=_filter)
    elif isinstance(str, _filter):
        data, status_code = server.db.find_pokemon(name=_filter)
    return jsonify(pokemon=data), status_code
