<template>
  <v-layout>
    <v-flex xs6 offset-sm3>
      <v-card style="margin-left:10px" flat>
        <p class="display-1" style="margin-left: 60px">密码修改</p>
        <v-flex xs8 offset-sm1>
          <v-card flat style="width: 400px; padding-bottom: 10px">
            <v-text-field style="margin-top: 5px" v-model="oldPasswordNumber" type="password" label="原密码:"></v-text-field>
            <v-text-field style="margin-top: 5px" v-model="newPasswordNumber" type="password" label="新密码:"></v-text-field>
            <v-text-field style="margin-top: 5px" v-model="newPasswordNumbers" type="password" label="再次确认输入的密码:"></v-text-field>
            <v-btn color="info" block @click=";">保存</v-btn>
          </v-card>
        </v-flex>
      </v-card>    
    </v-flex>
  </v-layout>
</template>


<script>
  export default {
    data () {
      return {
        oldPasswordNumber: '',
        newPasswordNumber: '',
        newPasswordNumbers: ''
      }
    }
  }
</script>

