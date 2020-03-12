<template>
  <div>
    <v-layout row wrap>
      <v-flex xs7>
        <v-card flat>
          <p class="display-1" style="margin-left:10px">宿舍职工信息查询</p>
          <v-layout wrap row>
      <v-flex class="px-4" xs4>
        <v-text-field style="margin-top: 5px" v-model="dormitoryManageNumber1" label="职工号:"></v-text-field>
      </v-flex>
      <v-flex class="px-4" xs4>
        <v-text-field style="margin-top: 5px" v-model="dormitoryManageName1" label="姓名:"></v-text-field>
      </v-flex>
      <v-flex class="px-4" xs2>
        <v-btn color="info" block @click="DormitoryManagementGet">点击查询</v-btn>
      </v-flex>
      <v-flex xs8>
        <v-card style="margin-left: 20px">
          <v-card-title>{{ item1.name }}</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <p>校区:     {{ item1.xiaoqu }}</p>
            <p>宿舍楼号: {{ item1.ulou }}</p>
            <p>职工号: {{ item1.uno }}</p>
            <p>姓名: {{ item1.username }}</p>
            <p>联系方式: {{ item1.uphone }}</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
        </v-card>
      </v-flex>
      <v-flex xs5>
        <v-card style="margin-left:10px" flat>
          <p class="display-1" style="margin-left: 60px">宿舍职工信息登记</p>
          <v-flex xs8 offset-sm1>
            <v-card flat style="width: 400px; padding-bottom: 10px">
              <v-select :items="campuses" v-model="cva" label="请选择校区:"></v-select>
              <v-text-field style="margin-top: 5px" v-model="dormitoryManageNumber" label="职工号:"></v-text-field>
              <v-text-field style="margin-top: 5px" v-model="dormitoryManageName" label="姓名:"></v-text-field>
              <v-select :items="sexs" style="margin-top: 5px" v-model="sex" label="性别:"></v-select>
              <v-text-field style="margin-top: 5px" v-model="password" label="密码:"></v-text-field>
              <v-text-field style="margin-top: 5px" v-model="dormitoryBuilding" label="宿舍楼号:"></v-text-field>
              <v-text-field style="margin-top: 5px" v-model="contactInformation" label="联系方式:"></v-text-field>
              <v-text-field style="margin-top: 5px" v-model="fg" label="标识"></v-text-field>
              <v-btn color="info" block @click="NewDormitoryManagement">保存</v-btn>
            </v-card>
          </v-flex>
        </v-card>
        <v-dialog v-model="dialog" max-width="300px" dark>
          <v-card>
            <v-card-text>添加成功，请点击确认返回。</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="green" @click="dialog = false">确认</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
 import axios from 'axios'
  export default {
    data: () => ({
      dialog: false,
      cav: '',
      fg:'',
      dormitoryManageNumber: '',
      dormitoryManageNumber1: '',
      dormitoryBuilding: '',
      sex: '',
      dormitoryManageName: '',
      dormitoryManageName1: '',
      password: '',
      contactInformation: '',
      campuses: [ //校区
        {value: '汇南校区', text: '汇南校区'},
        {value: '汇北校区', text: '汇北校区'},
        {value: '营盘校区', text: '营盘校区'},
        {value: '宜宾校区', text: '宜宾校区'},
        {value: '黄岭校区', text: '黄岭校区'},
      ],
      sexs: [
        {value: '男', text:'男'},
        {value: '女', text:'女'}
      ],
      item1: {
        name: '宿舍职工详情表',
  
      },
    }),
    methods: {
      DormitoryManagementGet: function() {
        let self = this;
        axios.get(`http://127.0.0.1:8000/api/UserViewSet/${self.dormitoryManageNumber1}`
        ).
        then(function(response) {
          self.item1=response.data;
        }).
        catch(function(error) {
          console.log(error);
        });
      },
       NewDormitoryManagement: function() {
        let self = this;
        let myDate = new Date();
        axios.post('http://127.0.0.1:8000/api/UserViewSet/', {
          'xiaoqu': self.cav,
          'uno': self.dormitoryManageNumber,
          'username': self.dormitoryManageName,
          'usex': self.sex,
          'password': self.password,
          'ulou': self.dormitoryBuilding,
          'uphone': self.contactInformation,
          'flag':self.fg
        }).
        then(function(response){
          self.dialog = true;
        }).
        catch(function(error) {
          console.log(error);
        });     
      },
    },
  }
  
</script>


