<template>
  <div>
    <input type="file" @change="onFileChange">
    <button @click="upload">Upload</button>
    <DataSet v-if="columns" :columns="columns" />
  </div>
</template>

<script>
import axios from 'axios'
import DataSet from './DataSet.vue'

export default {
  components: {
    DataSet
  },
  data() {
    return {
      file: null,
      columns: null
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
    },
    async upload() {
      const formData = new FormData();
      formData.append('file', this.file);
      
      const response = await axios.post('http://localhost:5000/upload', formData);
      this.columns = response.data.columns;
    }
  }
}
</script>
