<template>
  <div>
    <div v-for="rate in rates" :key="rate.service_code">
      <p>Service: {{ rate.service_name }} ({{ rate.service_code }})</p>
      <p>Price: {{ rate.price }}</p>
      <p>Estimated Delivery Date: {{ rate.estimated_delivery_date }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      rates: [],
    };
  },
  async created() {
    const response = await axios.post('/api/rates');
    this.rates = response.data;
  },
};
</script>
