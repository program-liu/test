<template>
  <v-app>
    <AppToolbar></AppToolbar>
    <DormitoryKepper v-if="flag == 2"></DormitoryKepper>
    <Student v-if="flag == 0"></Student>
    <Teacher v-if="flag == 1"></Teacher>
    <SuperAdminstrator v-if="flag == 3"></SuperAdminstrator>
    <v-content>
      <v-container fluid>
        <v-layout>
          <v-flex shrink style="width: 100%">
            <v-content v-if="mini == true">
              <v-container fluid fill-height>
                <v-layout align-center justify-center>
                  <v-flex xs12 sm8 md4>
                    <v-card class="headline">
                      <v-toolbar dark color="primary">
                        <v-toolbar-title>四川轻化工大学</v-toolbar-title>
                      </v-toolbar>
                      <v-card-text>
                        <v-form>
                          <v-text-field
                            label="学号"
                            type="text"
                            v-model="inputUsername"
                          ></v-text-field>
                          <v-text-field
                            label="密码"
                            id="password"
                            type="password"
                            v-model="inputPassword"
                          ></v-text-field>
                          <v-radio-group v-model="column" row>
                            <v-radio label="学生" value="student"></v-radio>
                            <v-radio label="辅导员" value="teacher"></v-radio>
                            <v-radio label="宿管" value="dormitorykepper"></v-radio>
                            <v-radio label="超级管理员" value="superadminstrator"></v-radio>
                          </v-radio-group>
                        </v-form>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" bottom @click="Login">登录</v-btn>
                        <v-btn color="primary" bottom>取消</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-content>
            <router-view></router-view>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios'
import AppToolbar from "@/components/AppToolbar";
import DormitoryKepper from "@/components/DormitoryKepper";
import Student from "@/components/Student";
import SuperAdminstrator from "@/components/SuperAdminstrator";
import Teacher from "@/components/Teacher";
export default {
  name: "App",
  components: {
    AppToolbar,
    DormitoryKepper,
    Student,
    SuperAdminstrator,
    Teacher
  },
  data() {
    return {
      flag: null,
      mini: true,
      column: '',
      inputUsername:'',
      inputPassword: '',
    }
  },
  methods: {
    Login: function() {
      let flag = null;
      let username = this.inputUsername;
      let password = this.inputPassword;

      let self = this;
      if(self.column == 'student')
      {
       flag=0;
      } else if(self.column == 'teacher')
      {
        flag=1;
      } else if(self.column == 'dormitorykepper')
      {
        flag=2;
      }
      else {
        flag=3;
      }
      axios.post('http://127.0.0.1:8000/login/', {
          'uno': username,
          'password': password,
          'flag': flag,
        }).then(function (response) {
          if(response.data.msg === 'Succeeded') {
            self.flag = response.data.flag;
            self.mini = false;
            if(self.flag == 0) {
              self.$router.push({
                path: "/waterElectricity",
              });
            }else if(self.flag == 1) {
              self.$router.push({
                path: "/studentMangement",
              });
            }else if(self.flag == 2) {
              self.$router.push({
                path: "/studentMangement",
              });
            }else {
              self.$router.push({
                path: "/dormitoryManagement",
              });
            }
          }
        }).catch(function (error) {
          console.log(error);
        });



     
      // if(self.column == 'student')
      // {
      //   self.flag=0;
      //   self.mini=false;
      //   self.$router.push({
      //     path: "/waterElectricity",
      //   });
      // } else if(self.column == 'teacher')
      // {
      //   self.flag=1;
      //   self.mini=false;
      //   self.$router.push({
      //     path: "/studentMangement",
      //   });
      // } else if(self.column == 'dormitorykepper')
      // {
      //   self.flag=2;
      //   self.mini=false;
      //   self.$router.push({
      //     path: "/studentMangement",
      //   });
      // }
      // else {
      //   self.flag=3;
      //   self.mini=false;
      //   self.$router.push({
      //     path: "/dormitoryManagement",
      //   });
      // }
    }
  },
  mounted() {
    this.flag = null;
    this.mini = true;
  },
};
</script>
