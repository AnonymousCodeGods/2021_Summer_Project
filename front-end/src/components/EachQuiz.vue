<template>
  <div class="quiz">
    <a style="float: left;padding-left: 40px;padding-top: 20px;width: 300px;text-align:left;">{{ type }}</a>
    <a class="bas" style="float: left;padding-left: 50px;padding-top: 20px">ID：{{ id }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px;">状态：{{ state === true ? '已发布' : '未发布' }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px">创建日期：{{ date.substring(0, 10) }}</a>
    <a class="bas" style="float: left;padding-left: 30px;padding-top: 20px">回收量：{{ num }}</a>
    <!--分割线-->
    <div class="midText"></div>
    <a style="float:right;padding-right: 70px;padding-top: 60px;height: 20px;cursor:pointer;" @click="del">删除</a>
    <img src="../assets/del.png" style="float:right;padding-right: 10px;padding-top: 60px;height: 20px;cursor:pointer;">
    <a style="float:right;padding-right: 80px;padding-top: 60px;height: 20px;width: 60px;cursor:pointer;" @click="pub"
       v-if="state===false">发布</a>
    <a style="float:right;padding-right: 80px;padding-top: 60px;height: 20px;width: 60px;cursor:pointer;"
       @click="suspend"
       v-else>暂停</a>
    <img src="../assets/suspend.png" v-if="state===true"
         style="float:right;padding-right: 0;padding-top: 61px;height: 20px;cursor:pointer;">
    <img src="../assets/open.png" v-else
         style="float:right;padding-right: 0;padding-top: 61px;height: 20px;cursor:pointer;">
    <a class="fun" style="float: right;padding-right: 190px;padding-top: 58px" @click="edit"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">编辑问卷</a>
    <!--    暂时先写成导出结果-->

    <download-excel
        :data="json_data"
        :fields="json_fields"
        worksheet="My Worksheet"
        type="excel"
        name="filename.xls">
      <a class="fun" style="float: right;padding-right: 30px;padding-top: 58px"
         @mouseover="mouseOver($event)"
         @mouseleave="mouseLeave($event)"
         @click="exported">导出数据</a>
    </download-excel>

    <a class="fun" style="float: right;padding-right: 30px;padding-top: 58px" @click="toResult"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">查看结果</a>
    <a class="fun" style="float: right;padding-right: 30px;padding-top: 58px" @click="links"
       @mouseover="mouseOver($event)"
       @mouseleave="mouseLeave($event)">发送链接</a>


  </div>
</template>

<script>
export default {
  name: "EachQuiz",
  props: {
    type: String,
    id: String,
    state: Boolean,
    date: String,
    num: String,
  },
  data() {
    return {
      json_fields: {},
      json_data: [],
    }

  },
  methods: {
    mouseOver($event) {
      $event.currentTarget.className = 'active';
    },
    mouseLeave($event) {
      $event.currentTarget.className = 'fun';
    },
    del() {
      const formData = new FormData();
      formData.append("ID", this.id)
      this.$axios.post('/quiz/recycle', {"ID": this.id})
          .then(result => {
            console.log(result)
            this.$router.go(0);
          })
    },
    pub() {
      const formData = new FormData();
      formData.append("ID", this.id)
      this.$axios.post('/quiz/publish', {"ID": this.id})
          .then(result => {
            console.log(result)
            this.state = true;
            this.$router.go(0);
          })
    },
    suspend() {
      const formData = new FormData();
      formData.append("ID", this.id)
      this.$axios.post('/quiz/suspend', {"ID": this.id})
          .then(result => {
            console.log(result)
            this.state = false;
            this.$router.go(0);
          })
    },
    edit() {
      this.$router.push({
        path: "/creatingQuestionnaire",
        query: {
          id: this.id,
        }
      });
    },
    toResult() {
      if (this.num !== '0') {
        this.$router.push({
          path: "/result",
          query: {
            id: this.id
          }
        });
      } else {
        this.$notify({
          title: '抱歉',
          message: '暂时没有答卷',
          position: 'bottom-left',
          type: "warning"
        });
      }

    },
    exported() {
      if (this.num !== '0') {
        this.$axios.post('/quiz/result', {"ID": this.id})
            .then(result => {
              this.json_data = result.data.AnswerList;
              for (let i = 0; i < this.json_data.length; i++) {
                this.json_data[i].Qnum = i+1;
                console.log(this.json_data[i].type === 0)
                if (this.json_data[i].type === 0)
                  this.json_data[i].type = '单选';
                else if (this.json_data[i].type === 1)
                  this.json_data[i].type = '多选';
                else if (this.json_data[i].type === 2)
                  this.json_data[i].type = '填空';
                else if (this.json_data[i].type === 3)
                  this.json_data[i].type = '评分';
              }
              console.log(this.json_data)
            });
        this.json_fields = {
          'num': 'Qnum',
          'type': 'type',
          'answer': 'selection',
          'input': 'input'

        };
      } else {
        this.$notify({
          title: '抱歉',
          message: '暂时没有答卷',
          position: 'bottom-left',
          type: "warning"
        });
      }
    },
    links() {
      this.$router.push({path: "/sentout", query: {id: this.id}});
    }
  }
}
</script>

<style scoped>
.quiz {
  min-width: 855px;
  max-width: 855px;
  padding-left: 0;
  width: 100%;
  height: 130px;
  background-color: white;
  border: #d5d5d5 solid 1px;
}

.midText {
  position: absolute;
  margin-top: 60px;
  left: 31%;
  width: 850px;
  height: 2px;
  max-width: 800px;
  background-color: #e5e4e4;
}

.bas {
  font-size: 5px;
}

.fun {
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  height: 50px;
}

.active {
  color: #0b92e8;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  height: 50px;
}
</style>