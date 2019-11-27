<template>
    <div>
        <div class="row">
            <ul class="pagination">
                <p class="center-align">{{ getPokeFirstID() }} - {{ getPokeLastID() }}</p>
                <router-link id="previous" class="btn-floating waves-effect waves-light red left" :to="getRedirect(pokemons.previous)">
                    <i class="material-icons">chevron_left</i>
                </router-link>
                <router-link id="next" class="btn-floating waves-effect waves-light red right" :to="getRedirect(pokemons.next)">
                    <i class="material-icons">chevron_right</i>
                </router-link>
            </ul>
        </div>
        <div class="row">
           <div class="col s4" v-for="pokemon in pokemons.results" v-bind:key="pokemon.id">
                <div class="card hoverable">
                    <div class="card-image">
                        <img class="responsive-img" :src="pokemon.img">
                    </div>
                    <div class="card-content">
                        <p class="card-title capitalize"><b>#{{ pokemon.id }} {{ pokemon.name }}</b></p>
                        <a class="btn-floating halfway-fab waves-effect waves-light red" href="#"><i class="material-icons">add</i></a>
                    </div>
                </div>
           </div>
        </div>
    </div>
</template>

<script>
import ApiService from '../ApiService';
const apiService = new ApiService();

export default {
    name: "Home",
    data: function () {
        return {
            pokemons: [],
            errors: []
        }
    },
    created: function () {
        apiService.getPokemons(this.$route.query.offset, this.$route.query.limit)
        .then(res => { this.pokemons = res.data.pokemon; })
        .catch(err => { this.errors = err; });
    },
    updated: function () {
        this.$nextTick( function () {
            apiService.getPokemons(this.$route.query.offset, this.$route.query.limit)
            .then(res => { this.pokemons = res.data.pokemon; })
            .catch(err => { this.errors = err; });
        })
    },
    methods: {
        getPokeFirstID() {
            if ("results" in this.pokemons) { return this.pokemons.results[0].id }
            return null;
        },
        getPokeLastID() {
            if ("results" in this.pokemons) { return this.pokemons.results[this.pokemons.results.length - 1].id }
            return null;
        },
        getPokeCount() {
            if ("count" in this.pokemons) { return this.pokemons.count }
            return null;
        },
        getRedirect(url) {
            if (url !== null) {
                const params = url.split('?')[1].split('&');
                const offset = params[0].split('=')[1];
                const limit = params[1].split('=')[1];
                url = `/?offset=${offset}&limit=${limit}`;
                return url;
            }
            return "#"
        }
    }
}
</script>

<style scoped>
.capitalize {
    text-transform: capitalize;
}
.container {
    position: center;
}
.center-align {
    font-size: 20px;
    color: white;
}
.col.s4 {
    margin-left: 30px;
    margin-right: -30px;
}
.card {
    width: auto;
    height: 200px;
    max-width: 200px;
}
.card .card-image {
    height: auto;
    width: auto;
    max-width: 120px;
    max-height: 120px;
    left: 35px;
    top: 15px;
}
.card .card-content .card-title {
    font-size: 17px;
    margin-left: 0;
}
.card .card-content .btn-floating {
    bottom: 15px;
    right: 10px;
    margin-left: 10px;
}
</style>
