(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-68e267d7"],{"5b05":function(t,e,n){},c1a0:function(t,e,n){"use strict";n("5b05")},dbea:function(t,e,n){"use strict";n.r(e);var s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"components-container"},[n("div",{staticClass:"viewer-wrapper"},[n("div",{staticClass:"post"},[n("div",{staticClass:"user-block"},[n("img",{staticClass:"img-circle",attrs:{src:"https://myshopsite.oss-cn-hangzhou.aliyuncs.com/avatar/3c4e671b-4ebc-4187-b379-441d8bebc86d.png"}}),t._v(" "),n("span",{staticClass:"username text-muted"},[t._v("滑稽.jpg")]),t._v(" "),n("span",{staticClass:"description"},[t._v("图片共 "+t._s(t.images.length)+" 张")])]),t._v(" "),t.checkPermission(["SYSTEM","EDITOR"])?n("img-inputer",{staticClass:"upload",attrs:{autoUpload:"",action:t.url,"on-change":t.getUpToken,"extra-data":t.params,"on-success":t.onSuccess,"on-error":t.onError,"upload-key":"file",size:"small"}}):t._e(),t._v(" "),n("p",[t._v("\n          分享一些有趣的图片和我觉得好看哒图片 (●'◡'●)，需要可以拿走哈！\n        ")])],1),t._v(" "),n("viewer",{ref:"viewer",staticClass:"images clearfix",attrs:{images:t.images},on:{inited:t.inited},scopedSlots:t._u([{key:"default",fn:function(e){return t._l(e.images,(function(e,s){return n("div",{key:s,staticClass:"image-wrapper"},[n("img",{staticClass:"image",attrs:{src:e.imgUrl,alt:"图片"}}),t._v(" "),n("span",{staticClass:"mask"},[n("span",{staticClass:"mask-icon"},[n("i",{staticClass:"el-icon-search",on:{click:function(e){return t.show(s)}}})]),t._v(" "),n("span",{staticClass:"mask-icon delete"},[n("i",{staticClass:"el-icon-delete",on:{click:function(n){return t.del(s,e.id)}}})])])])}))}}])})],1)])},a=[],i=n("e498"),c=(n("5f87"),n("2bd9"),n("0808"),n("657c"));n("4360");function o(t){if(t&&t instanceof Array&&t.length>0){var e=!0;return!!e}return console.error("need roles! Like v-permission=\"['admin','editor']\""),!1}var r={name:"Album",components:{ImgInputer:c["a"]},data:function(){return{images:[],url:"https://up-z1.qiniup.com",params:{}}},created:function(){this.fetchData(),this.getUpToken()},computed:{},methods:{fetchData:function(){var t=this;Object(i["c"])().then((function(e){t.images=e.data}))},onError:function(){this.$router.push({path:"/403"})},getUpToken:function(){var t=this;console.log("sss"),Object(i["d"])().then((function(e){console.log(e.data),t.params=e.data})),console.log(this.params)},onSuccess:function(t,e){var n=this;console.log(t),Object(i["a"])({path:t.key}).then((function(t){n.images.push(t.data)}))},show:function(t){this.$viewer.view(t)},del:function(t,e){var n=this;Object(i["b"])(e).then((function(e){2e4===e.code&&n.images.splice(t,1)})).catch((function(){n.$router.push({path:"/403"})}))},inited:function(t){this.$viewer=t},checkPermission:o}},u=r,l=(n("c1a0"),n("2877")),d=Object(l["a"])(u,s,a,!1,null,"8bd7cb26",null);e["default"]=d.exports},e498:function(t,e,n){"use strict";n.d(e,"a",(function(){return a})),n.d(e,"c",(function(){return i})),n.d(e,"b",(function(){return c})),n.d(e,"d",(function(){return o}));var s=n("b775");function a(t){return Object(s["a"])({url:"/album/add",method:"post",data:t})}function i(){return Object(s["a"])({url:"/album/list",method:"get"})}function c(t){return Object(s["a"])({url:"/album/delete",method:"get",params:{path:t}})}function o(){return Object(s["a"])({url:"/album/get_token",method:"get"})}}}]);