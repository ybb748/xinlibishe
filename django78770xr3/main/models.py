#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    zhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    youxiang=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class xinlizixunshi(BaseModel):
    __doc__ = u'''xinlizixunshi'''
    __tablename__ = 'xinlizixunshi'

    __loginUser__='zixunshizhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zixunshizhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='是'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zixunshizhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='咨询师账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    zixunshixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='咨询师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    zixunshizhanghao=VARCHAR
    mima=VARCHAR
    zixunshixingming=VARCHAR
    xingbie=VARCHAR
    lianxidianhua=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'xinlizixunshi'
        verbose_name = verbose_name_plural = '心理咨询师'
class psychologicaldata(BaseModel):
    __doc__ = u'''psychologicaldata'''
    __tablename__ = 'psychologicaldata'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    studentid=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学号' )
    gender=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    age=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    gradelevel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='所在年级' )
    professionalcategory=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业类别' )
    scoreofmentalhealthscale=models.IntegerField  (  null=True, unique=False, verbose_name='心理健康量表得分' )
    selfratingdepressionscalesdsscore=models.IntegerField  (  null=True, unique=False, verbose_name='抑郁自评量表（SDS）得分' )
    selfratinganxietyscalesasscore=models.IntegerField  (  null=True, unique=False, verbose_name='焦虑自评量表（SAS）得分' )
    scoreonthestressscale=models.IntegerField  (  null=True, unique=False, verbose_name='压力量表得分' )
    emotionalstabilityscore=models.IntegerField  (  null=True, unique=False, verbose_name='情绪稳定性得分' )
    gpagpa=models.IntegerField  (  null=True, unique=False, verbose_name='平均绩点（GPA）' )
    perceivedleveloflearningstress=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学习压力感知程度' )
    socialactivitylevel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='社交活跃度' )
    dailysleepduration=models.CharField ( max_length=255, null=True, unique=False, verbose_name='每日睡眠时长' )
    regularityofdailyroutine=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作息规律性' )
    '''
    studentid=VARCHAR
    gender=VARCHAR
    age=Integer
    gradelevel=VARCHAR
    professionalcategory=VARCHAR
    scoreofmentalhealthscale=Integer
    selfratingdepressionscalesdsscore=Integer
    selfratinganxietyscalesasscore=Integer
    scoreonthestressscale=Integer
    emotionalstabilityscore=Integer
    gpagpa=Integer
    perceivedleveloflearningstress=VARCHAR
    socialactivitylevel=VARCHAR
    dailysleepduration=VARCHAR
    regularityofdailyroutine=VARCHAR
    '''
    class Meta:
        db_table = 'psychologicaldata'
        verbose_name = verbose_name_plural = '心理数据'
class xinlizixun(BaseModel):
    __doc__ = u'''xinlizixun'''
    __tablename__ = 'xinlizixun'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    biaoti=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    jianjie=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    fabushijian=models.DateField   (  null=True, unique=False, verbose_name='发布时间' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    neirong=models.TextField   (  null=True, unique=False, verbose_name='内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    biaoti=VARCHAR
    jianjie=Text
    fabushijian=Date
    fengmian=Text
    neirong=Text
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'xinlizixun'
        verbose_name = verbose_name_plural = '心理资讯'
class chatmessage(BaseModel):
    __doc__ = u'''chatmessage'''
    __tablename__ = 'chatmessage'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    uid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户ID' )
    fid=models.BigIntegerField  ( null=False, unique=False, verbose_name='好友用户ID' )
    content=models.CharField ( max_length=255, null=True, unique=False, verbose_name='内容' )
    format=models.IntegerField  (  null=True, unique=False, verbose_name='格式(1:文字，2:图片)' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='消息已读(0:未读，1:已读)' )
    '''
    uid=BigInteger
    fid=BigInteger
    content=VARCHAR
    format=Integer
    isread=Integer
    '''
    class Meta:
        db_table = 'chatmessage'
        verbose_name = verbose_name_plural = '消息表'
class friend(BaseModel):
    __doc__ = u'''friend'''
    __tablename__ = 'friend'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    uid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户ID' )
    fid=models.BigIntegerField  ( null=False, unique=False, verbose_name='好友用户ID' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    role=models.CharField ( max_length=255, null=True, unique=False, verbose_name='角色' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    alias=models.CharField ( max_length=255, null=True, unique=False, verbose_name='别名' )
    type=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='类型(0:好友申请，1:好友，2:消息)' )
    '''
    uid=BigInteger
    fid=BigInteger
    name=VARCHAR
    picture=Text
    role=VARCHAR
    tablename=VARCHAR
    alias=VARCHAR
    type=Integer
    '''
    class Meta:
        db_table = 'friend'
        verbose_name = verbose_name_plural = '好友表'
class exampaper(BaseModel):
    __doc__ = u'''exampaper'''
    __tablename__ = 'exampaper'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='调查问卷名称' )
    time=models.IntegerField  ( null=False, unique=False, verbose_name='问卷时长(分钟)' )
    status=models.IntegerField  ( null=False, unique=False,default='0', verbose_name='调查问卷状态' )
    '''
    name=VARCHAR
    time=Integer
    status=Integer
    '''
    class Meta:
        db_table = 'exampaper'
        verbose_name = verbose_name_plural = '调查问卷表'
class examquestion(BaseModel):
    __doc__ = u'''examquestion'''
    __tablename__ = 'examquestion'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    paperid=models.BigIntegerField  ( null=False, unique=False, verbose_name='所属调查问卷id（外键）' )
    papername=models.CharField ( max_length=255,null=False, unique=False, verbose_name='调查问卷名称' )
    questionname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='问卷名称' )
    options=models.TextField   (  null=True, unique=False, verbose_name='选项，json字符串' )
    score=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='分值' )
    answer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='正确答案' )
    analysis=models.TextField   (  null=True, unique=False, verbose_name='答案解析' )
    type=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='问卷类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）4:主观题' )
    sequence=models.BigIntegerField  (  null=True, unique=False,default='100', verbose_name='问卷排序，值越大排越前面' )
    '''
    paperid=BigInteger
    papername=VARCHAR
    questionname=VARCHAR
    options=Text
    score=BigInteger
    answer=VARCHAR
    analysis=Text
    type=BigInteger
    sequence=BigInteger
    '''
    class Meta:
        db_table = 'examquestion'
        verbose_name = verbose_name_plural = '问卷'
class examquestionbank(BaseModel):
    __doc__ = u'''examquestionbank'''
    __tablename__ = 'examquestionbank'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    questionname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='问卷名称' )
    options=models.TextField   (  null=True, unique=False, verbose_name='选项，json字符串' )
    score=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='分值' )
    answer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='正确答案' )
    analysis=models.TextField   (  null=True, unique=False, verbose_name='答案解析' )
    type=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='问卷类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空） 4:主观题' )
    sequence=models.BigIntegerField  (  null=True, unique=False,default='100', verbose_name='问卷排序，值越大排越前面' )
    '''
    questionname=VARCHAR
    options=Text
    score=BigInteger
    answer=VARCHAR
    analysis=Text
    type=BigInteger
    sequence=BigInteger
    '''
    class Meta:
        db_table = 'examquestionbank'
        verbose_name = verbose_name_plural = '问卷'
class examrecord(BaseModel):
    __doc__ = u'''examrecord'''
    __tablename__ = 'examrecord'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __examinationPaper__='是'#[examinationPaper:是/否]后台生成普通试卷功能
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    paperid=models.BigIntegerField  ( null=False, unique=False, verbose_name='调查问卷id（外键）' )
    papername=models.CharField ( max_length=255,null=False, unique=False, verbose_name='调查问卷名称' )
    questionid=models.BigIntegerField  ( null=False, unique=False, verbose_name='问卷id（外键）' )
    questionname=models.CharField ( max_length=255,null=False, unique=False, verbose_name='问卷名称' )
    options=models.TextField   (  null=True, unique=False, verbose_name='选项，json字符串' )
    score=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='分值' )
    answer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='正确答案' )
    analysis=models.TextField   (  null=True, unique=False, verbose_name='答案解析' )
    ismark=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='是否批卷' )
    type=models.BigIntegerField  (  null=True, unique=False,default='0', verbose_name='问卷类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空） 4:主观题' )
    myscore=models.BigIntegerField  ( null=False, unique=False,default='0', verbose_name='问卷得分' )
    myanswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='考生答案' )
    '''
    userid=BigInteger
    username=VARCHAR
    paperid=BigInteger
    papername=VARCHAR
    questionid=BigInteger
    questionname=VARCHAR
    options=Text
    score=BigInteger
    answer=VARCHAR
    analysis=Text
    ismark=BigInteger
    type=BigInteger
    myscore=BigInteger
    myanswer=VARCHAR
    '''
    class Meta:
        db_table = 'examrecord'
        verbose_name = verbose_name_plural = '问卷记录表'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class discussxinlizixun(BaseModel):
    __doc__ = u'''discussxinlizixun'''
    __tablename__ = 'discussxinlizixun'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussxinlizixun'
        verbose_name = verbose_name_plural = '心理资讯评论表'
