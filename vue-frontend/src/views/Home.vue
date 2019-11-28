<template>
    <div>
        <NavButtons :next="next" :previous="previous" :firstID="getPokeFirstID()" :lastID="getPokeLastID()"/>
        <div class="row">
           <div class="card-table">
                <md-card md-with-hover v-for="pokemon in pokemons.results" v-bind:key="pokemon.id">
                    <md-card-media>
                        <img :src="pokemon.img" :alt="pokemon.name">
                    </md-card-media>
                    <md-card-content>
                        <p class="capitalize"><b>#{{ pokemon.id }} {{ pokemon.name }}</b></p>
                    </md-card-content>
                    <md-card-actions>
                        <md-button class="md-icon-button">
                            <router-link class="red" :to="getPokeURL(pokemon.name)"><md-icon>add</md-icon></router-link>
                        </md-button>
                    </md-card-actions>
                </md-card>
           </div>
        </div>
    </div>
</template>

<script>
import NavButtons from '../components/NavButtons'
import ApiService from '../ApiService';
const apiService = new ApiService();

export default {
    name: "Home",
    components: {
        NavButtons,
    },
    data: function () {
        return {
            next: null,
            previous: null,
            pokemons: [],
            errors: []
        }
    },
    created: function () {
        apiService.getPokemons(this.$route.query.offset, this.$route.query.limit)
        .then(res => {
                        this.pokemons = res.data.pokemon;
                        this.next = res.data.pokemon.next;
                        this.previous = res.data.pokemon.previous;
                    })
        .catch(err => { this.errors = err; });
    },
    updated: function () {
            apiService.getPokemons(this.$route.query.offset, this.$route.query.limit)
            .then(res => {
                            this.pokemons = res.data.pokemon;
                            this.next = res.data.pokemon.next;
                            this.previous = res.data.pokemon.previous;
                        })
            .catch(err => { this.errors = err; });
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
        getPokeURL(name) {
            return `/poke/?filterBy=name&filter=${name}`;
        }, 
    }
}
</script>

<style lang="scss" scoped>
.card-table {
    padding: 10px;
    display: flex;
    flex-wrap: wrap;
    margin-left: 12%;
}
.md-card {
    width: 200px;
    height: 200px;
    margin-left: 64px;
    margin-right: 64px;
    margin-top: 20px;
    margin-bottom: 30px;
}
.md-card-media img {
    width: auto;
    margin-left: 50px;
    margin-top: 30px;
    margin-bottom: -10px;
}
.md-card-actions {
    margin-top: -50px;
}
</style>
