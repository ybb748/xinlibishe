<template>
	<div :style='{"padding":"0 0 20px","margin":"0px auto","color":"#666","background":"#fff","width":"1200px","fontSize":"16px","position":"relative"}'>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="section-title" :style='{"padding":"0","margin":"20px 0","borderColor":"#0063CD","color":"#333","textAlign":"left","background":"none","borderWidth":"0 0 2px","width":"110%","lineHeight":"50px","fontSize":"26px","borderStyle":"solid","order":"0"}'>问卷</div>
		<el-table :data="tableData" style="width: 100%">
			<el-table-column label="调查问卷名称" prop="papername"> </el-table-column>
			<el-table-column label="操作" width="150">
				<template slot-scope="scope">
					<el-button type="danger" size="mini" @click="handleView(scope.$index, scope.row)">查看</el-button>
				</template>
			</el-table-column>
		</el-table>
	
		<el-pagination
			background
			id="pagination" class="pagination"
			:pager-count="7"
			:page-size="pageSize"
			prev-text="上一页"
			next-text="下一页"
			:hide-on-single-page="false"
			:layout='["total","prev","pager","next","sizes","jumper"].join()'
			:total="total"
			:style='{"padding":"0 calc((100% - 1200px)/2)","margin":"20px auto","whiteSpace":"nowrap","overflow":"hidden","color":"#333","textAlign":"center","width":"100%","clear":"both","fontSize":"16px","fontWeight":"500","order":"50"}'
			@current-change="curChange"
			@size-change="sizeChange"
			@prev-click="prevClick"
			@next-click="nextClick"
			></el-pagination>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				layouts: '',
				tableData: [],
				total: 1,
				pageSize: 10,
				totalPage: 1,
			}
		},
		created() {
			this.getExamList(1);
		},
		methods: {
			backClick() {
				this.$router.push('/index/center')
			},
			getExamList(page) {
				this.$http.get('examrecord/groupby', {params: {page, limit: this.pageSize, userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
					if (res.data.code == 0) {
						this.tableData = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
					}
				});
			},
			curChange(page) {
				this.getExamList(page);
			},
			prevClick(page) {
				this.getExamList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getExamList(1);
			},
			nextClick(page) {
				this.getExamList(page);
			},
			handleView(index, row) {
				this.$router.push({path: '/index/examRecord/1', query: {paperid: row.paperid}})
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.section {
		width: 900px;
		margin: 0 auto;
	}

</style>
