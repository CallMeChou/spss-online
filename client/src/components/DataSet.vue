<template>
  <div>
    <h2>Select two columns for correlation analysis:</h2>
    <select v-model="selectedColumn1">
      <option v-for="column in columns" :value="column">{{ column }}</option>
    </select>
    <select v-model="selectedColumn2">
      <option v-for="column in columns" :value="column">{{ column }}</option>
    </select>
    <button @click="analyze">Analyze</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['columns'],
  data() {
    return {
      selectedColumn1: '',
      selectedColumn2: ''
    }
  },
  methods: {
    async analyze() {
      const response = await axios.post('http://localhost:5000/analyze', {
        column1: this.selectedColumn1,
        column2: this.selectedColumn2
      });
      alert('Correlation: ' + response.data.correlation);
    }
  }
}
</script>
