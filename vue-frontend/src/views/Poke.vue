<template>
    <div>
        <div class="row">
            <div v-for="poke in pokemon" v-bind:key="poke.name">
              <div id="name">
                <h3 class="md-title capitalize">{{ poke.name }}</h3>
              </div>
              <div class="sprite-cards">
                    <md-card md-with-hover v-for="sprite in stripNull(poke.sprites)" :key="sprite">
                        <md-card-media>
                            <img :src="sprite" :alt="poke.name">
                        </md-card-media>
                    </md-card>
              </div>
            </div>
        </div>
    </div>
</template>

<script>
import ApiService from '../ApiService';
const apiService = new ApiService();

export default {
    name: "Poke",
    data: function () {
        return {
            pokemon: null,
            errors: []
        }
    },
    created: function () {
        apiService.getPokemonByFilter(this.$route.query.filterBy, this.$route.query.filter)
        .then(res => { this.pokemon = res.data.pokemon; })
        .catch(err => { this.errors = err; });
    },
    updated: function () {
        this.$nextTick( function () {
            apiService.getPokemonByFilter(this.$route.query.filterBy, this.$route.query.filter)
            .then(res => { this.pokemon = res.data.pokemon; })
            .catch(err => { this.errors = err; }); 
        })
    },
    methods: {
        stripNull(obj) {
            for (let key in obj) {
                if (obj[key] == null) {
                    delete obj[key];
                }
            }
            return obj;
        }
    }
}
</script>

<style lang="scss" scoped>
.md-title {
    margin-top: 30px;
    margin-left: 48%;
}
.sprite-cards {
    padding: 10px;
    display: flex;
    flex-wrap: wrap;
    margin-left: 12%;
}
.md-card {
    width: 200px;
    height: 200px;
    margin-left: 30x;
    margin-right: 80px;
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
