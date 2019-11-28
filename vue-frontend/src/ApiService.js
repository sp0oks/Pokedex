import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5000';

export default class ApiService {
    getPokemons(offset, limit) {
        return axios.get('', { params: { offset: offset, limit: limit }});
    }

    getPokemonByFilter(type, filter) {
        if (type === 'name') {
            return axios.get(`/pokemon/name/${filter}`);
        }
    }
}
