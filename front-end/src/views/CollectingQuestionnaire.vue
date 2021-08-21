<template>
  <div>
    <el-card style="width: 800px; margin: auto">
      <div slot="header" class="clearfix">
        <span style="font-size: larger">{{que.title}}</span>
      </div>
      <div v-for="item in que.QList"
           :key="item.id" style="margin: 15px">
        <div v-if="item.type===0">
          <div class="queLabel">
            {{item.id+1}}.{{item.title}}
          </div>
          <div style="margin-left: 10%;margin-right: 10%">
            <el-radio-group
                v-model="item.selection" style="width: 100%">
              <el-radio
                  v-for="subItem in item.options"
                  :key="subItem.id"
                  :label="subItem.id"
                  style="width: 100%;margin: 5px;display: flex;align-items: flex-start;">
                {{subItem.text}}
              </el-radio>
            </el-radio-group>
          </div>
        </div>
        <div v-if="item.type===1">
          <div class="queLabel">
            {{item.id+1}}.{{item.title}}
          </div>
          <div style="margin-left: 10%;margin-right: 10%">
            <el-checkbox-group
                v-model="item.selections" style="width: 100%">
              <el-checkbox
                  v-for="subItem in item.options"
                  :key="subItem.id"
                  :label="subItem.id"
                  style="width: 100%;margin: 5px;display: flex;align-items: flex-start;">
                {{subItem.text}}
              </el-checkbox>
            </el-checkbox-group>
          </div>
        </div>
        <div v-if="item.type===2">
          <div class="queLabel">
            {{item.id+1}}.{{item.title}}
          </div>
          <div style="margin: 7px 10%;">
            <el-input v-model="item.input"/>
          </div>
        </div>
        <div v-if="item.type===3">
          <div style="margin-left: 10%;margin-bottom:8px;text-align: start;">
            {{item.id+1}}.{{item.title}}
          </div>
          <div class="queLabel">
            <el-rate
                v-model="item.rating"
                :colors="colors">
            </el-rate>
          </div>
        </div>
      </div>
      <div style="margin-top: 30px">
        <el-button type="primary" style="width: 15%">提交</el-button>
        <el-button type="danger" style="width: 15%">取消</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    name: 'NewQue',
    data: function(){
      return {
        que:{
          id:0,
          title:"holo",
          QList:[{
            id:0,
            type:0,
            title:"主要用于课堂测试等场景，发布者应该可以设置每道题目的评分和答案，也可以设置问" +
                "卷整体的限时时间，超时将自动回收。针对填写者，问卷题目应该可以乱序展示，在填写者" +
                "提交后，问卷应该可以对客观题目进行自动评分，并使填写者可以查看答案。",
            options:[{
              id:0,
              text:"你好"
            },{
              id:1,
              text:"hello"
            },{
              id:2,
              text:"hi"
            }],
            selection:-1
          },{
            id:1,
            type:1,
            title:"到底什么是hello",
            options:[{
              id:0,
              text:"你好"
            },{
              id:1,
              text:"hello"
            },{
              id:2,
              text:"hi"
            }],
            selections:[

            ]
          },{
            id:2,
            type:2,
            title:"到底到底什么是hello",
            input:""
          },{
            id:3,
            type:3,
            title:"到底到底到底什么是hello",
            rating:0
          }]
        },
        colors: ['#99A9BF', '#F7BA2A', '#FF9900']
      }
    },
    methods: {

    }
  }
</script>

<style>
.queLabel {
  margin-left: 10%;
  margin-bottom: 8px;
  margin-right: 10%;
  text-align: start;
}
</style>