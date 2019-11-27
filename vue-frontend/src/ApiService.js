import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5000';

export default class ApiService {
    getPokemons(offset, limit) {
        return axios.get('', { params: { offset: offset, limit: limit }});
    }

    getPokemonByFilter(type, filter) {
        if (type === 'id') {
            return axios.get(`/pokemon/id/${filter}`);
        }  else if (type === 'name') {
            return axios.get(`/pokemon/name/${filter}`);
        }  else if (type === 'type') {
            return axios.get(`/pokemon/type/${filter}`);
        }
    }
}
