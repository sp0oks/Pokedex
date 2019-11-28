<template>
    <div>
        <div class="nav-buttons row">
            <div class="md-layout md-gutter">
                <md-button id="previous" class="md-accent" :disabled="previous==null" @click="onClick(previous)"><i class="material-icons">chevron_left</i></md-button>
                <p class="nav-text">{{ getPokeFirstID() }} - {{ getPokeLastID() }}</p>
                <md-button id="next" class="md-accent" @click="onClick(next)"><i class="material-icons">chevron_right</i></md-button>
            </div>
        </div>
        <div class="row">
           <div class="card-table">
                <md-card md-with-hover v-for="pokemon in pokemons.results" v-bind:key="pokemon.id">
                    <md-card-media md-medium>
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
import ApiService from '../ApiService';
const apiService = new ApiService();

export default {
    name: "Home",
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
        onClick(url) {
            if (url == null) {
                return this.$router.push('#');
            }
            const params = url.split('?')[1].split('&');
            const offset = params[0].split('=')[1];
            const limit = params[1].split('=')[1];
            url = `/?offset=${offset}&limit=${limit}`;
            return this.$router.push(url);
        }
    }
}
</script>

<style lang="scss" scoped>
.capitalize {
    text-transform: capitalize;
}
.nav-buttons {
    margin-left: 40%;
    margin-top: 30px;
    margin-bottom: -20px;
}
#next, #previous {
    margin-top: 15px;
}
.nav-buttons .material-icons {
    font-size: 50px;
}
.nav-text {
    font-size: 20px;
    color: white;
}
.card-table {
    padding: 10px;
    display: flex;
    flex-wrap: wrap;
    margin-left: 12%;
}
.md-card {
    width: 200px;
    height: 200px;
    margin: 64px;
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
