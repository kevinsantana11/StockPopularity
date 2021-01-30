<template>
    <div>
        <md-list>
            <md-list-item v-for="stock in stocks" :value="stock.symbol" :key="stock.symbol">
                <span class="md-list-item-text">{{ stock.symbol }}</span>
                <span class="md-list-item-text">{{ stock.count }}</span>
            </md-list-item>
        </md-list>
        <md-field>
        <label>Sub Reddits</label>
        <md-input v-model="subreddits"></md-input>
        </md-field>
        <md-field>
        <label>Limit</label>
        <md-input v-model="limit"></md-input>
        </md-field>
        <md-button @click="refresh_data">Refresh</md-button>
        <md-button @click="sort_data">Sort</md-button>
    </div>
</template>

<script>
const axios = require('axios');

export default {
    data: function () {
        return {
            subreddits: "",
            limit: "",
            stocks: []
        }
    },
    methods: {
        refresh_data: function () {
            let url = `http://127.0.0.1:5000/Popular?subreddits=${this.subreddits}&limit=${this.limit}`;
            axios.get(url).then(
                response => this.stocks = response.data
            )
        },
        sort_data: function () {
            this.stocks.sort((a, b) => b.count - a.count)
        }
    }
}
</script>

<style scoped>
</style>