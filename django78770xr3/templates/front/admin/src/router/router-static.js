import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Board from '@/views/board'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
import adminexam from '@/views/modules/exampaperlist/exam'
	import xuesheng from '@/views/modules/xuesheng/list'
	import psychologicaldata from '@/views/modules/psychologicaldata/list'
	import examquestion from '@/views/modules/examquestion/list'
	import exampaper from '@/views/modules/exampaper/list'
	import xinlizixunshi from '@/views/modules/xinlizixunshi/list'
	import config from '@/views/modules/config/list'
	import examrecord from '@/views/modules/examrecord/list'
	import discussxinlizixun from '@/views/modules/discussxinlizixun/list'
	import xinlizixun from '@/views/modules/xinlizixun/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/xuesheng',
		name: '学生',
		component: xuesheng
	}
	,{
		path: '/psychologicaldata',
		name: '心理数据',
		component: psychologicaldata
	}
	,{
		path: '/examquestion',
		name: '问卷管理',
		component: examquestion
	}
	,{
		path: '/exampaper',
		name: '调查问卷管理',
		component: exampaper
	}
	,{
		path: '/xinlizixunshi',
		name: '心理咨询师',
		component: xinlizixunshi
	}
	,{
		path: '/config',
		name: '轮播图管理',
		component: config
	}
	,{
		path: '/examrecord',
		name: '问卷记录',
		component: examrecord
	}
	,{
		path: '/discussxinlizixun',
		name: '心理资讯评论',
		component: discussxinlizixun
	}
	,{
		path: '/xinlizixun',
		name: '心理资讯',
		component: xinlizixun
	}
	]
	},
	{
		path: '/adminexam',
		name: 'adminexam',
		component: adminexam,
		meta: {icon:'', title:'adminexam'}
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/board',
		name: 'board',
		component: Board,
		meta: {icon:'', title:'board'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
