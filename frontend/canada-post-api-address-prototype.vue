<template>
  <div>
    <input v-model="addressInput" type="text" placeholder="Enter address" />
    <button @click="getAddress">Get Address</button>
    <div v-if="loading" >Loading...</div>
    <div v-else-if="addressData">
      <h2>Address Data:</h2>
      <pre>{{ addressData }}</pre>
    </div>
    <div v-else-if="errorMessage">
      <h2>Error:</h2>
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      addressInput: '',
      addressData: null,
      errorMessage: null,
      loading: false,
    };
  },
  methods: {
    async getAddress() {
      this.loading = true;
      this.errorMessage = null;
      this.addressData = null;
      try {
        const response = await axios.post('/complete_address/', {
          address: this.addressInput,
        });
        this.addressData = response.data;
      } catch (error) {
        console.error(error);
        this.errorMessage = `Error: ${error.message}`;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
