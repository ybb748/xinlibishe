<template>
	<div class="home-preview">




		<!-- 商品推荐 -->
		<div id="animate_recommendxinlizixun" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">心理资讯推荐</span>
				<span class="recommend_subhead">{{'xinlizixun'.toUpperCase()}} RECOMMEND</span>
			</div>
			<!-- 样式一 -->
			<div class="list list1 index-pv1">
				<div v-for="(item,index) in xinlizixunRecommend" :key="index" @click="toDetail('xinlizixunDetail', item)" class="list-item animation-box">
					<img v-if="preHttp(item.fengmian)" :src="item.fengmian.split(',')[0]" alt="" />
					<img v-else :src="baseUrl + (item.fengmian?item.fengmian.split(',')[0]:'')" alt="" />
					<div class="name line1">{{item.biaoti}}</div>
				
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间：</span>
						<span class="text">{{item.addtime.split(' ')[0]}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞：</span>
						<span class="text">{{item.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏：</span>
						<span class="text">{{item.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-liulan04"></span>
						<span class="label">浏览次数：</span>
						<span class="text">{{item.clicknum}}</span>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('xinlizixun')">
				<span class="text">更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],
				xinlizixunRecommend: [],





			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},

			listIndexClick11(index, name) {
				this['listIndex11' + name] = index[this['listColumn11' + name]]
				this.getList()
			},

			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendxinlizixun',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "xinlizixun/autoSort";
				data = {
					page: 1,
					limit: 6,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.xinlizixunRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0px auto;
		flex-direction: column;
		background: #fff;
		display: flex;
		width: 100%;
		.recommend {
			padding: 0;
			margin: 15px 0;
			background: #fff;
			width: 100%;
			position: relative;
			.recommend_title_box {
				padding: 0px;
				margin: 0 auto 10px;
				background: none;
				width: 1200px;
				position: relative;
				text-align: left;
				.recommend_title {
					margin: 0;
					color: #000;
					background: none;
					width: auto;
					font-size: 24px;
					line-height: 36px;
				}
				.recommend_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: auto;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0s;
			}
			.list1 {
				padding: 0;
				margin: 0 auto;
				background: #fff;
				width: 1200px;
				border-color: #eaeaea;
				border-width: 0 0 0 1px;
				border-style: solid;
				height: auto;
				.list-item {
					cursor: pointer;
					padding: 10px;
					margin: 0;
					color: #888;
					display: inline-block;
					font-size: 14px;
					border-color: #eaeaea;
					background: #fff;
					width: calc(16.66% - 0px);
					border-width: 1px 1px 1px 0;
					position: relative;
					border-style: solid;
					height: auto;
					img {
						margin: 0 0 5px;
						object-fit: cover;
						display: block;
						width: 100%;
						height: 180px;
					}
					.name {
						padding: 0 10px;
						overflow: hidden;
						color: #333;
						white-space: nowrap;
						font-weight: 600;
						width: 100%;
						font-size: 14px;
						line-height: 30px;
						text-overflow: ellipsis;
					}
					.price {
						padding: 0 10px;
						color: #f00;
						font-size: 14px;
						line-height: 1.5;
					}
					.time_item {
						padding: 0 10px;
						display: none;
						.icon {
							margin: 0 2px 0 0;
							color: inherit;
							display: none;
							font-size: inherit;
							line-height: 1.5;
						}
						.label {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
						.text {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
					}
					.publisher_item {
						padding: 0 10px;
						display: none;
						.icon {
							margin: 0 2px 0 0;
							color: inherit;
							display: none;
							font-size: inherit;
							line-height: 1.5;
						}
						.label {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
						.text {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
					}
					.like_item {
						padding: 0 10px;
						display: none;
						.icon {
							margin: 0 2px 0 0;
							color: inherit;
							display: none;
							font-size: inherit;
							line-height: 1.5;
						}
						.label {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
						.text {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
					}
					.collect_item {
						padding: 0 10px;
						display: none;
						.icon {
							margin: 0 2px 0 0;
							color: inherit;
							display: none;
							font-size: inherit;
							line-height: 1.5;
						}
						.label {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
						.text {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
					}
					.view_item {
						padding: 0 10px;
						display: none;
						.icon {
							margin: 0 2px 0 0;
							color: inherit;
							display: none;
							font-size: inherit;
							line-height: 1.5;
						}
						.label {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
						.text {
							color: inherit;
							font-size: inherit;
							line-height: 1.5;
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #999;
				cursor: pointer;
				padding: 0;
				margin: 0;
				display: inline-block;
				line-height: 32px;
				right: calc((100% - 1200px)/2);
				float: right;
				top: 5px;
				background: none;
				width: auto;
				position: absolute;
				text-align: right;
				.text {
					color: #999;
					font-size: 14px;
				}
				.icon {
					color: #999;
					font-size: 14px;
				}
			}
		}
	}
</style>
