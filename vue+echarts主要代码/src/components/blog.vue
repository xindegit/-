<script setup>
import { ref,onMounted } from 'vue'
import * as echarts from 'echarts';
import axios from 'axios';
let dataList = ref([])
onMounted(async () => {
    const { data } = await axios.get('/api/blog');
    dataList.value.push(...data.result)
    console.log(dataList.value)

})

</script>
<template>
<u>
    <li v-for="(item,index) in dataList" :key="index">{{ item.title }}</li>
</u>
</template>
<style scoped>

</style>
