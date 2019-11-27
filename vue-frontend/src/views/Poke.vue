<template>
    <div>
    {{ this.pokemon }}
    </div>
</template>

<script>
import ApiService from '../ApiService'
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
    }
}
</script>
