<template>
  <div class="bin">
      <el-table
          :data="tableData"
          style="width:85%; margin: auto"
          border
          stripe
          :default-sort = "{prop: 'date', order: 'descending'}"
      >
        <el-table-column
            align="center"
            prop="date"
            label="发布日期"
            sortable
            min-width="25">
        </el-table-column>
        <el-table-column
            align="center"
            prop="name"
            label="问卷名"
            min-width="25">
        </el-table-column>
        <el-table-column
            align="center"
            prop="count"
            label="答卷数"
            min-width="10">
        </el-table-column>
        <el-table-column
            align="center"
            prop="clear"
            label="清空问卷"
            min-width="15">

          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-s-promotion" @click="clearR(scope.row)" v-show="scope.row.isempty">清空问卷</el-button>
          </template>

        </el-table-column>
        <el-table-column
            align="center"
            prop="recover"
            label="恢复"
            min-width="10">

          <template slot-scope="scope">
            <el-button type="success" size="mini" icon="el-icon-refresh-right" @click="recoverR(scope.row)">恢复</el-button>
          </template>

        </el-table-column>
        <el-table-column
            align="center"
            prop="delete"
            label="删除"
            min-width="10">
          <el-popconfirm width="180"
                         title="确定要删除问卷吗？"
                         confirm-button-type="danger"
                         cancel-button-type="infomation"
                         icon="el-icon-info"
                         slot-scope="scope"
                         @confirm="deleteR(scope.row)">
            <el-tooltip slot="reference" class="item" effect="dark" content="删除该问卷" placement="top">
              <el-button type="danger" size="mini" icon="el-icon-delete">删除</el-button>
            </el-tooltip>
          </el-popconfirm>
        </el-table-column>
      </el-table>

  </div>
</template>

<script>

export default {
  data: function () {
    return {
      tableData: [{
        date: '2021-05-02',
        name: '时间统计',
        count: '0',
        isempty: parseInt(this.count)!==0
      }, {
        date: '2021-05-04',
        name: '作业统计',
        count: '7',
        isempty: parseInt(this.count)!==0
      }, {
        date: '2021-05-04',
        name: '作业统计',
        count: '7',
        isempty: parseInt(this.count)!==0
      }]
    }
  },
  methods: {
    deleteR(row) {
      this.$notify({
        message: '问卷已删除',
        type: 'warning',
        position: 'bottom-left'
      });
      this.tableData.splice(this.tableData.indexOf(row), 1);
    },
    recoverR(row) {
      this.$notify({
        message: '问卷已恢复',
        type: 'success',
        position: 'bottom-left'
      });
      this.tableData.splice(this.tableData.indexOf(row), 1);
    },
    clearR(row) {
      this.$notify({
        message: '问卷已清空',
        type: 'info',
        position: 'bottom-left'
      });
      this.tableData.indexOf(row);
    }
  }
}
</script>

<style>

</style>