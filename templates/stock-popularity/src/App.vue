<template>
  <div id="app">
    <md-app>
      <md-app-content>
        <Popularity/>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>
//import Home from './components/Home.vue'
import Popularity from './components/Popularity.vue'

export default {
  name: 'App',
  components: {
    Popularity
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
