const axios = require('axios').default
const Vue = require('vue').default

import { MdContent, MdList, MdApp, MdCard, MdButton, MdField, MdRipple } from 'vue-material/dist/components';
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import App from './App.vue';

Vue.use(MdApp);
Vue.use(MdContent);
Vue.use(MdCard);
Vue.use(MdList);
Vue.use(MdButton);
Vue.use(MdField);
Vue.use(MdRipple);
Vue.use(axios)

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
