<template>
  <div>
    <p class="display-1">发布公告<span class="font-weight-thin"> New Announcement</span></p>
    <v-flex xs6>
    <v-text-field label="填写公告标题:" v-model="articleTitle"></v-text-field>
    <v-textarea label="填写公告内容:" v-model="editorContent"></v-textarea>
    <v-layout row wrap>
      <v-flex class="px-4">
        <v-btn block>保存为草稿</v-btn>
      </v-flex>
      <v-flex class="px-4">
        <v-btn color="info" block @click="NewAnnouncement()">发表公告</v-btn>
      </v-flex>
    </v-layout>
    </v-flex>
    <v-dialog v-model="dialog" max-width="300px" dark>
      <v-card>
        <v-card-text>发布成功，请点击确认返回。</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat color="green" @click="dialog = false">确认</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    components: {
    },
    data: () => ({
      dialog: false,
      articleTitle: '',
      editorContent: '',
    }),
    methods: {
      NewAnnouncement: function() {
        let self = this;
        let myDate = new Date();
        axios.post('http://127.0.0.1:8000/api/NoticeViewSet/', {
          'n_tag':self.articleTitle,
          'n_time': myDate.toLocaleString('chinese', {hour12: false}).replace(/\//g,"-"),
          'n_content': self.editorContent,
        }).
        then(function(response){
          self.dialog = true;
        }).
        catch(function(error) {
          console.log(error);
        });     
      },
    }
  }
</script>