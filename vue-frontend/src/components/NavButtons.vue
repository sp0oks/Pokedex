<template>
    <div class="nav-buttons row">
        <div class="md-layout md-gutter">
            <md-button id="previous" class="md-accent" :disabled="previous==null" :to="onClick(previous)"><i class="material-icons">chevron_left</i></md-button>
            <p class="nav-text">{{ firstID }} - {{ lastID }}</p>
            <md-button id="next" class="md-accent" :to="onClick(next)"><i class="material-icons">chevron_right</i></md-button>
        </div>
    </div>
</template>

<script>
export default {
    name: "NavButtons",
    props: [ "next", "previous", "firstID", "lastID"],
    methods: {
        onClick(url) {
            if (url == null) {
                return this.$router.push('#');
            }
            const params = url.split('?')[1].split('&');
            const offset = params[0].split('=')[1];
            const limit = params[1].split('=')[1];
            url = `/?offset=${offset}&limit=${limit}`;
            return url;
        }
    }
}
</script>

<style lang="scss" scoped>
.nav-buttons {
    margin-left: 40.5%;
    margin-top: 30px;
    margin-bottom: -20px;
}
#next, #previous {
    margin-top: 15px;
}
.material-icons {
    font-size: 50px;
}
.nav-text {
    font-size: 20px;
    color: white;
}
</style>

