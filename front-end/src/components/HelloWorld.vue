<template>
  <div id="charts">
    <div id="main" :style="{width:'100%',height:'3.54rem'}"></div>
  </div>
</template>

<script>
var echarts = require('echarts');
export default {
  name: 'Bank',
  data() {
    return {}
  },
  components: {},
  computed: {},
  methods: {},
  mounted() {
    /*ECharts图表*/
    var myChart = echarts.init(document.getElementById('main'));
    myChart.setOption({
      series: [
        {
          name: '访问来源',
          type: 'pie',
          radius: '55%',
          itemStyle: {
            normal: {
              // 阴影的大小
              shadowBlur: 200,
              // 阴影水平方向上的偏移
              shadowOffsetX: 0,
              // 阴影垂直方向上的偏移
              shadowOffsetY: 0,
              // 阴影颜色
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          },
          data: [
            {value: 400, name: '搜索引擎'},
            {value: 335, name: '直接访问'},
            {value: 310, name: '邮件营销'},
            {value: 274, name: '联盟广告'},
            {value: 235, name: '视频广告'}
          ]
        }
      ]
    })
  }
}
</script>
