import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import ExamPaper from '../pages/exam/examPaper'
import Exam from '../pages/exam/exam'
import ExamList from '../pages/exam/examList'
import ExamRecord from '../pages/exam/examRecord'
import Storeup from '../pages/storeup/list'
import payList from '../pages/pay'

import xueshengList from '../pages/xuesheng/list'
import xueshengDetail from '../pages/xuesheng/detail'
import xueshengAdd from '../pages/xuesheng/add'
import xinlizixunshiList from '../pages/xinlizixunshi/list'
import xinlizixunshiDetail from '../pages/xinlizixunshi/detail'
import xinlizixunshiAdd from '../pages/xinlizixunshi/add'
import psychologicaldataList from '../pages/psychologicaldata/list'
import psychologicaldataDetail from '../pages/psychologicaldata/detail'
import psychologicaldataAdd from '../pages/psychologicaldata/add'
import xinlizixunList from '../pages/xinlizixun/list'
import xinlizixunDetail from '../pages/xinlizixun/detail'
import xinlizixunAdd from '../pages/xinlizixun/add'
import chatmessageList from '../pages/chatmessage/list'
import chatmessageDetail from '../pages/chatmessage/detail'
import chatmessageAdd from '../pages/chatmessage/add'
import friendList from '../pages/friend/list'
import friendDetail from '../pages/friend/detail'
import friendAdd from '../pages/friend/add'
import discussxinlizixunList from '../pages/discussxinlizixun/list'
import discussxinlizixunDetail from '../pages/discussxinlizixun/detail'
import discussxinlizixunAdd from '../pages/discussxinlizixun/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'examPaper',
					component: ExamPaper
				},
				{
					path: 'examList',
					component:ExamList
				},
				{
					path: 'examRecord/:type',
					component:ExamRecord
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'xuesheng',
					component: xueshengList
				},
				{
					path: 'xueshengDetail',
					component: xueshengDetail
				},
				{
					path: 'xueshengAdd',
					component: xueshengAdd
				},
				{
					path: 'xinlizixunshi',
					component: xinlizixunshiList
				},
				{
					path: 'xinlizixunshiDetail',
					component: xinlizixunshiDetail
				},
				{
					path: 'xinlizixunshiAdd',
					component: xinlizixunshiAdd
				},
				{
					path: 'psychologicaldata',
					component: psychologicaldataList
				},
				{
					path: 'psychologicaldataDetail',
					component: psychologicaldataDetail
				},
				{
					path: 'psychologicaldataAdd',
					component: psychologicaldataAdd
				},
				{
					path: 'xinlizixun',
					component: xinlizixunList
				},
				{
					path: 'xinlizixunDetail',
					component: xinlizixunDetail
				},
				{
					path: 'xinlizixunAdd',
					component: xinlizixunAdd
				},
				{
					path: 'chatmessage',
					component: chatmessageList
				},
				{
					path: 'chatmessageDetail',
					component: chatmessageDetail
				},
				{
					path: 'chatmessageAdd',
					component: chatmessageAdd
				},
				{
					path: 'friend',
					component: friendList
				},
				{
					path: 'friendDetail',
					component: friendDetail
				},
				{
					path: 'friendAdd',
					component: friendAdd
				},
				{
					path: 'discussxinlizixun',
					component: discussxinlizixunList
				},
				{
					path: 'discussxinlizixunDetail',
					component: discussxinlizixunDetail
				},
				{
					path: 'discussxinlizixunAdd',
					component: discussxinlizixunAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
		{
			path: '/exam',
			component: Exam
		}
	]
})
