<template>
    <div>
        <Navbar/>
        <h2>Pokedex</h2>
    </div>
</template>

<script>
import Navbar from './components/Navbar';

import '..node_modules/materialize-css/dist/js/materialize.min.js';
import '..node_modules/materialize-css/dist/css/materialize.min.css';

export default {
  name: 'app',
  components: {
    Navbar
  }
};
</script>

<style>
</style>
