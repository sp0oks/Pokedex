<template>
    <nav class="red">
    <div class="nav-wrapper">
        <div class="container">
        <router-link to="/" class="brand-logo"><i class="material-icons left">home</i>Pokedex</router-link>
        <ul class="right hide-on-med-and-down">
            <li><router-link to="/"></router-link></li>
            <li>
                <form class="form" v-on:submit.prevent="onSubmit">
                    <!--<div class="input-field">
                        <select v-model="selected">
                            <option disabled value="">Filter By...</option>
                            <option>PokeID</option>
                            <option>Name</option>
                            <option>Type</option>
                        </select>
                        <span> Selected: {{ selected }} </span>
                    </div>-->
                    <div class="input-field">
                        <input name="search" type="search" v-model="search" placeholder="Find Pokemon..." required>
                        <label class="label-icon" for="search"><i class="material-icons left">search</i></label><i class="material-icons">close</i>
                    </div>
                </form>
            </li>
        </ul>
        </div>
    </div>
    </nav>
</template>

<script>
export default {
    name: "Navbar",
    data: function() {
        return {
//            selected: '',
            search: null,
            errors: []
        };
    },
    methods: {
        onSubmit() {
            this.$router.push(`/poke/?filterBy=name&filter=${this.search}`);
        }
    }
}
</script>

<style scoped>
::placeholder {
    color: white;
}
</style>
