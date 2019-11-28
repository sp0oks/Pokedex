<template>
    <div>
        <head>
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons">
        </head>
        <Navbar/>
        <router-view/>
    </div>
</template>

<script>
import Navbar from './components/Navbar';

export default {
  name: 'app',
  components: {
    Navbar,
  }
};
</script>

<style>
html {
    background-color: #90a4ae !important;
}
.capitalize {
    text-transform: capitalize;
}
</style>
