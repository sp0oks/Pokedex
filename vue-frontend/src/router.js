import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import Poke from './views/Poke.vue';

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        { path: '/', component: Home },
        { path: '/poke', component: Poke },
    ]
});
