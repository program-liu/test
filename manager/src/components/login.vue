<template>
  <v-app>
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="headline">
              <v-toolbar dark color="primary">
                <v-toolbar-title>四川轻化工大学</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <span>Source</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    name="login"
                    label="学号"
                    type="text"
                    v-model="inputUsername"
                    :hint="hintUsername"
                  ></v-text-field>
                  <v-text-field
                    name="password"
                    label="密码"
                    id="password"
                    :type="passwordInputType"
                    :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                    @click:append="TogglePasswordVisibility"
                    v-model="inputPassword"
                  ></v-text-field>

                  <v-radio-group v-model="column" row>
                    <v-radio label="辅导员" value="radio-1"></v-radio>
                    <v-radio label="学生" value="radio-2"></v-radio>
                    <v-radio label="宿管" value="radio-3"></v-radio>
                    <v-radio label="超级管理员" value="radio-4"></v-radio>
                  </v-radio-group>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" bottom @click="login">登录</v-btn>
                <v-btn color="primary" bottom>取消</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {},
  data() {
    return {
      isUserLogged: false,
      passwordInputType: "password",
      dialogLoginFailure: false,
      showPassword: false,
      hintPassword: "",
      inputPassword: "",
      column: ""
    };
  },
  mounted() {
    // Check local storage for user login status
    let status = this.login();

    if (status === true) {
      this.isUserLogged = true;
    } else {
      this.GenerateHash();
      this.isUserLogged = false;
    }
  },
  methods: {
    TogglePasswordVisibility: function() {
      if (this.passwordInputType === "password") {
        this.passwordInputType = "text";
      } else {
        this.passwordInputType = "password";
      }
      this.showPassword = !this.showPassword;
    },
    login: function() {
      if (this.column === "radio-1") {
        this.$router.push({
          path: "/conservator",
          query: {
            id: 1
          }
        });
      } else if (this.column === "radio-2") {
        this.$router.push({
          path: "/conservator",
          query: {
            id: 2
          }
        });
      } else if (this.column === "radio-3") {
        this.$router.push({
          path: "/conservator",
          query: {
            id: 3
          }
        });
      } else if (this.column === "radio-4") {
        this.$router.push({
          path: "/conservator",
          query: {
            id: 4
          }
        });
      }
    },
    CheckLoginStatus: function() {
      return true;
    }
  }
};
</script>

