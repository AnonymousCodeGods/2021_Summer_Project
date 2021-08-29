<template>
  <div id="sentout" >
    <div class="head">
      <img alt="Vue logo" src="../assets/logo.png" style="position:absolute;top:5%;height: 75%;left: 5%">

      <div class="demo-type">
        <div>
          <el-avatar icon="el-icon-user-solid" size="small"></el-avatar>
        </div>
        <!--        <div>-->
        <!--          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>-->
        <!--        </div>-->
      </div>

      <el-dropdown style="position:absolute;top:40%;height: 80%;left: 93%">
      <span class="el-dropdown-link">
        {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="退出">退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>


    <div class="body">
      <div id="chart" style="position:absolute;left:30%;width: 400px;top: 10%;
      border: #eaeaea 1px solid;border-radius: 4px;box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
        <div id="left" :style="{width:'400px',height:'400px'}"></div>
      </div>

      <div id="charts" style="position:absolute;left:60%;width: 400px;top: 10%;
      border: #eaeaea 1px solid;border-radius: 4px;box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
        <div id="right" :style="{width:'400px',height:'400px'}"></div>
      </div>

      <button
          type="button"
          class="button button--login button--round-s button--text-thick button--inverted button--size"
          style="position:absolute;left: 5%; top: 10%;width: 200px; height: 65px"
          @click="back"
      >返回列表
      </button>
    </div>
  </div>
</template>

<script>
const echarts = require('echarts');
export default {
  name: "SentOut",
  data() {
    return {
      username: '',
      sorts:[],
      pieData:[],
      colData:[]
    }
  },
  created() {
    this.username = this.$cookies.get('username')
    this.sorts = this.$route.query.sorts
    this.pieData = this.$route.query.pies
    this.colData = this.$route.query.cols
    console.log('aaaaaa')
    console.log(this.pieData)
    console.log(this.colData)
  },
  methods: {
    back: function () {
      this.$router.go(-1);
    },
  },
  mounted() {
    /*ECharts图表*/
    const leftChart = echarts.init(document.getElementById('left'));
    const rightChart = echarts.init(document.getElementById('right'));
    rightChart.setOption({
      title: {
        text: '柱状图',
        left: 'center'
      },
      xAxis: {
        type: 'category',
        data: this.sorts
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        data: this.colData,
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        }
      }]
    });
    leftChart.setOption({
      title: {
        text: '饼图',
        left: 'center'
      },
      tooltip: {
        trigger: 'item'
      },
      legend: {
        top: '5%',
        left: 'center'
      },
      series: [
        {
          name: '访问来源',
          type: 'pie',
          radius: ['40%', '70%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: '#fff',
            borderWidth: 2
          },
          label: {
            show: false,
            position: 'center'
          },
          emphasis: {
            label: {
              show: true,
              fontSize: '40',
              fontWeight: 'bold'
            }
          },
          labelLine: {
            show: false
          },
          data: this.pieData
        }
      ]
    })
  }
}
</script>

<style scoped>

.head {
  position: absolute;
  top: 0;
  left: 0;
  height: 62px;
  min-height: 60px;
  width: 100%;
  background-color: #ffffff;
}

.demo-type {
  position: absolute;
  left: 90%;
  top: 30%;
}

.body {
  position: absolute;
  top: 8%;
  left: 0;
  height: 92%;
  width: 100%;
  background-color: #f5f4f4;
  border-top: 1px transparent solid;
  box-shadow: #c6c5c5;
  border-image: linear-gradient(0deg, #979696, #e7e7e7) 1 10;
}

.button {
  float: left;
  min-width: 150px;
  max-width: 500px;
  display: block;
  margin: 1em;
  padding: 1em 2em;
  border: none;
  background: none;
  color: inherit;
  position: relative;
  z-index: 1;
  -moz-osx-font-smoothing: grayscale;
}

.button:focus {
  outline: none;
}

.button > span {
  vertical-align: middle;
}

/* Sizes */
.button--size {
  font-size: 16px;

}


/* Typography and Roundedness */
.button--text-thick {
  font-weight: 300;
}

.button--round-s {
  border-radius: 2px;
}


/* Wapasha */
.button.button--login {
  background: #176c97;
  color: #fff;
  -webkit-transition: background-color 0.3s, color 0.3s;
  transition: background-color 0.3s, color 0.3s;
}


.button--login.button--inverted {
  background: #0b92e8;
  color: #fdfeff;
}

.button--login::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: inherit;
  opacity: 0;
  -webkit-transform: scale3d(0.6, 0.6, 1);
  transform: scale3d(0.6, 0.6, 1);
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
  transition-timing-function: cubic-bezier(0.75, 0, 0.125, 1);
}

.button--login:hover {
  background-color: #fff;
  color: #3f51b5;
}

.button--login.button--inverted:hover {
  background-color: #0d78ad;
  color: #fcfcfd;
}
</style>