<template>
  <div>
    <md-ripple>
      <md-card  class="md-size-50 md-with-hover">
        <md-card-header>
          <div class="md-title">Login</div>
        </md-card-header>
        <md-card-content>
          <md-field>
            <label>Username</label>
            <md-input></md-input>
          </md-field>
          <md-field>
            <label>Password</label>
            <md-input></md-input>
          </md-field>
        </md-card-content>
        <md-card-actions>
          <md-button>Sign Up</md-button>
          <md-button>Log In</md-button>
        </md-card-actions>
      </md-card>
    </md-ripple>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .md-card {
    width: 500px;
    height: 500px;
    margin: 5px;
    display: inline-block;
  }
</style>
