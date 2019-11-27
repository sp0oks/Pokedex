<template>
    <div>
        <head>
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        </head>
        <Navbar/>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script>
import Navbar from './components/Navbar';

import '../node_modules/materialize-css/dist/js/materialize.min.js';
import '../node_modules/materialize-css/dist/css/materialize.min.css';

export default {
  name: 'app',
  components: {
    Navbar
  }
};
</script>

<style>
html {
    background-color: #90a4ae;
}
</style>
