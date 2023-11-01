<script setup>
import { onMounted } from 'vue'
import * as echarts from 'echarts';
import axios from 'axios';
onMounted(async () => {
    const { data } = await axios.get('/api/comment_top10');
    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    console.log(data)
    myChart.setOption({
        title: {
            text: '评论数前十的标题',
            left: 'right',  // 设置标题靠右
        },
        xAxis: {
            type: 'category',
            axisLabel: {
                interval: 0,  // 强制显示所有标签
                formatter: function (value) {
                    // 将标签字符串按适当的位置加上换行符
                    var label = value.split(''); // 将字符串转换为字符数组
                    var maxLength = 7; // 每行最多显示的字符数（根据实际情况调整）

                    // 将标签字符串按每行最大字符数进行分割
                    for (var i = 0; i < label.length; i += maxLength) {
                        label.splice(i + maxLength, 0, '\n');
                    }

                    return label.join('');
                },
                textStyle: {
                    fontSize: 12  // 设置字体大小
                }
            },
        },
        yAxis: {
            type: 'value',

        },
        dataset: {
            dimensions: ['title', 'icon_comment'],
            source: data.result
        },
        series: [
            {
                type: 'bar',
                smooth: true,
                label: {
                    show: true,
                    position: 'top'
                },
               
            }
        ]
    })

})

</script>
<template>
    <div id="main"></div>
</template>
<style scoped>
#main {
    width: 1300px;
    height: 85vh;
}
</style>