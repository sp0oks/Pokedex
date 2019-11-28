<template>
    <md-toolbar class="md-accent" md-elevation="0">
        <h4 class="md-title" style="flex: 1"><router-link to="/"><md-button id="home" class="md-icon-button"><md-icon>home</md-icon></md-button><md-button>Pokedex</md-button></router-link></h4>
        <div class="md-layout md-gutter">
            <div class="md-layout-item">
                <md-field>
                    <md-select v-model="filterBy" name="filterBy" id="filterBy" placeholder="Filter By...">
                        <md-option value="name">Name</md-option>
                    </md-select>
                </md-field>
            </div>
            <div class="md-layout-item">
                <md-field md-inline>
                <label for="search"><md-icon>search</md-icon>Find Pokemon...</label>
                    <md-input type="search" v-model="search"></md-input>
                    <span class="md-helper-text">{{ this.filterBy }}</span>
                </md-field>
            </div>
            <div class="md-layout-item">
                <md-button id="submit" @click="onSubmit" :disabled="filterBy==null || search==null">Submit</md-button>
            </div>
        </div>
    </md-toolbar>
</template>

<script>
export default {
    name: "Navbar",
    data: function() {
        return {
            filterBy: null,
            search: null,
            errors: []
        };
    },
    methods: {
        onSubmit() {
            if (this.filterBy === "name") {
                this.$router.push(`/poke/?filterBy=name&filter=${this.search}`);
            } else if (this.filterBy === "type") {
                this.$router.push(`/?type=${this.search}`);
            }
        }
    }
}
</script>

<style scoped>
.md-title {
    color: white;
}
.md-field {
    color: white !important;
}
#home {
    top: 3px;
}
#submit {
    top: 10px;
}
</style>
