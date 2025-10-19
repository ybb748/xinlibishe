<template>
	<div>
		<div class="top-content">
			<div class="top-content-left">{{paper.name}} （ 共 <el-tag type="danger">{{questionList.length}}</el-tag> 题 ）
			</div>
			<div class="top-content-center" v-cloak>距离问卷结束还有 <el-tag type="danger">{{this.hour}}</el-tag> 时 <el-tag
					type="danger">{{this.minute}}</el-tag> 分 <el-tag type="danger">{{this.second}}</el-tag> 秒</div>
			<div class="top-content-right">
				<el-button type="danger" @click="doneExam(0)">结束问卷</el-button>
			</div>
		</div>
		<el-card v-if="end" style="width: 90%;margin: 10px auto;">
			<div style="width: 100%;display: flex;flex-direction: column;align-items: center;">
				<div>
					问卷已完成，感谢填写！
				</div>
				<div class="question-btn">
					<el-button type="success" @click="doneExam(1)">退出问卷</el-button>
				</div>
			</div>
		</el-card>
		<el-card style="width: 90%;margin: 10px auto;" v-if="!end||isSubmit">
			<div class="question-content" v-for="(item, index) in questionList" :key="item.id">
				<div class="question-title">
					{{index + 1}} 、<span class="ql-snow ql-editor" v-html="item.questionname"></span>
					<el-tag type="success" v-if="item.type==0">{{questionType(item)}}</el-tag>
					<el-tag type="warning" v-if="item.type==1">{{questionType(item)}}</el-tag>
				</div>
				<div class="question-answer">
					<div v-if="!isSubmit && !end">
						作答：
						<el-select v-model="item.myanswer" placeholder="请选择您的答案"
							v-if="item.type == 0 ">
							<el-option v-for="(option, idx) in JSON.parse(item.options)" :key="idx" :label="option.text"
								:value="option.code">
							</el-option>
						</el-select>
						<el-select v-model="item.myanswer" multiple placeholder="请选择您的答案" v-if="item.type == 1">
							<el-option v-for="(option, idx) in JSON.parse(item.options)" :key="idx" :label="option.text"
								:value="option.code">
							</el-option>
						</el-select>
					</div>
				</div>
			</div>
			<div class="question-btn">
				<el-button v-if="!isSubmit && !end" type="primary" @click="submitAnswer">提交答案</el-button>
			</div>
		</el-card>
	</div>
</template>

<script>
	export default {
    //数据集合
		data() {
			return {
				questionList: [],
				isSubmit: false,
				end: false,
				maxtime: 0,
				timer: null,
				hour: '',
				minute: '',
				second: '',
				user: {},
				hassubject:false,
				paper:{},
			}
		},
		created() {
			this.$http.get(`exampaper/info/${this.$route.query.id}`, {}).then(res => {
				if (res.data.code == 0) {
					this.paper = res.data.data
					this.maxtime = this.paper.time * 60;
					this.deleteRecords(this.paper.id);
					this.getQuestion(this.paper.id);
					this.hour = Math.floor(this.maxtime / 60 / 60);
					this.minute = Math.floor(this.maxtime / 60 % 60);
					this.second = Math.floor(this.maxtime % 60);
					this.timer = setInterval(this.countDown, 1000);
				}
			})
			this.$http.get(localStorage.getItem('UserTableName') + '/session', {
				emulateJSON: true
			}).then(res => {
				if (res.data.code == 0) {
					this.user = res.data.data;
				}
			});
		},
		//方法集合
		methods: {
			questionType(item) {
				switch (item.type) {
					case 0:
						return '单选题';
					case 1:
						return '多选题';
				}
			},
			deleteRecords(paperid) {
				this.$http.post(`examrecord/deleteRecords?userid=${localStorage.getItem('frontUserid')}&paperid=${paperid}`).then(res => {});
			},
			getQuestion(paperid) {
				this.$http.get('examquestion/list', {params: {page: 1, limit: 1000, paperid}}).then(res => {
					if (res.data.code == 0) {
						for(let x in res.data.data.list){
							res.data.data.list[x].questionname = res.data.data.list[x].questionname.replace(/img src/gi,"img style=\"width:100%;\" src");
							if(res.data.data.list[x].type==4){
								this.hassubject = true
							}
						}
						res.data.data.list.sort(function (a, b) {
							return (b.sequence - a.sequence)
						});
						this.questionList = res.data.data.list;
					}
				});
			},
			submitAnswer() {
				for(let i in this.questionList){
					if(this.questionList[i].type==1){
						if(!this.questionList[i].myanswer||(this.questionList[i].myanswer&&this.questionList[i].myanswer.length==0)){
							this.$message.error('还有问卷未完成作答')
							return false
						}
					}else{
						if(!this.questionList[i].myanswer||(this.questionList[i].myanswer&&this.questionList[i].myanswer=='')){
							this.$message.error('还有问卷未完成作答')
							return false
						}
					}
				}
				this.$confirm(`是否完成作答，提交调查问卷？`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(()=>{
					for (let x in this.questionList) {
						if (this.questionList[x].type == 1) {
							this.questionList[x].myanswer = this.questionList[x].myanswer.sort().join(',')
						}
						this.saverecord(this.questionList[x])
					}
					this.end = true;
				})
			},
			scoreChange() {
				let score = 0
				for (let x in this.questionList) {
					if (this.questionList[x].myscore) {
						score += Number(this.questionList[x].myscore) || 0
					}
				}
				return score
			},
			saverecord(row) {
				let record = {
					userid: this.user.id,
					paperid: this.paper.id,
					papername: this.paper.name,
					questionid: row.id,
					questionname: row.questionname,
					options: row.options,
					myscore: 0,
					myanswer: row.myanswer,
					type: row.type,
					ismark: this.hassubject ? 0 : 1
				}
				this.$http.post('examrecord/add', record).then(res => {})
			},
			doneExam(type) {
				if (type == 0) {
					this.$confirm('确定离开问卷?', '提示', {
						confirmButtonText: '确定',
						cancelButtonText: '取消',
						type: 'warning'
					}).then(() => {
						this.end = true;
						if (this.questionList.length == 0) {
							this.$router.push('/index/examPaper');
						}
					});
				} else {
					this.$router.push('/index/examPaper');
				}
			},
			countDown() {
				if (this.maxtime > 0) {
					this.hour = Math.floor((this.maxtime - 1) / 60 / 60);
					this.minute = Math.floor((this.maxtime - 1) / 60 % 60);
					this.second = Math.floor((this.maxtime - 1) % 60);
					--this.maxtime;
				} else {
					clearInterval(this.timer);
					this.end = true;
				}
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.top-content {
		height: 80px;
		width: 100%;
		background-color: #409EFF;
		display: flex;
		justify-content: space-between;
	}
	.top-content-left, .top-content-center, .top-content-right {
		font-size: 18px;
		line-height: 80px;
		color: #fff;
	}
	.top-content-left {
		padding-left: 20px;
	}
	.top-content-right {
		padding-right: 20px;
	}
	.question-content {
		width: 90%;
		margin: 0 auto;
		margin-top: 30px;
		border-bottom: 1px solid #eee;
	}
	.question-content:last-of-type {
		border: none;
	}
	.question-title, .question-answer, .question-btn {
		padding: 20px 0;
	}
</style>
