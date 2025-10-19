#coding:utf-8
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
import numbers
from django.db.models.aggregates import Count,Sum
from django.db.models import Case, When, IntegerField, F
from django.forms import model_to_dict
import requests
from util.CustomJSONEncoder import CustomJsonEncoder
from .models import examrecord
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config


def examrecord_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")


        error = examrecord.createbyreq(examrecord, examrecord, req_dict)
        if error is Exception or (type(error) is str and "Exception" in error):
            msg['code'] = crud_error_code
            msg['msg'] = "用户已存在,请勿重复注册!"
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        datas = examrecord.getbyparams(examrecord, examrecord, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        try:
            __sfsh__= examrecord.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='是':
            if datas[0].get('sfsh')!='是':
                msg['code']=other_code
                msg['msg'] = "账号已锁定，请联系管理员审核!"
                return JsonResponse(msg, encoder=CustomJsonEncoder)
                
        req_dict['id'] = datas[0].get('id')


        return Auth.authenticate(Auth, examrecord, req_dict)


def examrecord_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "登出成功",
            "code": 0
        }

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def examrecord_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  examrecord.getallcolumn( examrecord, examrecord)

        try:
            __loginUserColumn__= examrecord.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'
        recordsParam = {}
        recordsParam[username_str] = req_dict.get("username")
        records=examrecord.getbyparams(examrecord, examrecord, recordsParam)
        if len(records)<1:
            msg['code'] = 400
            msg['msg'] = '用户不存在'
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        eval('''examrecord.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg, encoder=CustomJsonEncoder)



def examrecord_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = examrecord.getbyparams(examrecord, examrecord, req_dict)[0]

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def examrecord_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"是"})
        data=examrecord.getbyparams(examrecord, examrecord, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        global examrecord
        #当前登录用户信息
        tablename = request.session.get("tablename")
        # 判断当前表的表属性isAdmin,为真则是管理员
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:
                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break
        if __isAdmin__!="是":
            req_dict["userid"]=request.session.get("params").get("id")

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =examrecord.page(examrecord, examrecord, req_dict, request)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_autoSort(request):
    '''
    ．智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
主要信息列表（如商品列表，新闻列表）中使用，显示最近点击的或最新添加的5条记录就行
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in examrecord.getallcolumn(examrecord,examrecord):
            req_dict['sort']='clicknum'
        elif "browseduration"  in examrecord.getallcolumn(examrecord,examrecord):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = examrecord.page(examrecord,examrecord, req_dict)

        return JsonResponse(msg, encoder=CustomJsonEncoder)

#分类列表
def examrecord_lists(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":[]}
        msg['data'],_,_,_,_  = examrecord.page(examrecord, examrecord, {})
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_query(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        try:
            query_result = examrecord.objects.filter(**request.session.get("req_dict")).values()
            msg['data'] = query_result[0]
        except Exception as e:

            msg['code'] = crud_error_code
            msg['msg'] = f"发生错误：{e}"
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_list(request):
    '''
    前台分页
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        #获取全部列名
        columns=  examrecord.getallcolumn( examrecord, examrecord)
        if "vipread" in req_dict and "vipread" not in columns:
          del req_dict["vipread"]
        #表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
        try:
            __foreEndList__=examrecord.__foreEndList__
        except:
            __foreEndList__=None
        try:
            __foreEndListAuth__=examrecord.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        #authSeparate
        try:
            __authSeparate__=examrecord.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="是" and __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and request.session.get("params") is not None:
                req_dict['userid']=request.session.get("params").get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#判断是否存在userid列名
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "是":
                if req_dict.get("userid"):
                    # del req_dict["userid"]
                    pass
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if "userid" in columns:
                    try:
                        pass
                    except:
                        pass
        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=examrecord.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="是":
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    try:
                        del req_dict['userid']
                    except:
                        pass
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        
        if examrecord.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass


        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = examrecord.page(examrecord, examrecord, req_dict, request, q)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_save(request):
    '''
    后台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        #获取全部列名
        columns=  examrecord.getallcolumn( examrecord, examrecord)
        if tablename!='users' and req_dict.get("userid")==None and 'userid' in columns  and __isAdmin__!='是':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']

        idOrErr= examrecord.createbyreq(examrecord,examrecord, req_dict)
        if idOrErr is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = idOrErr
        else:
            msg['data'] = idOrErr

        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_add(request):
    '''
    前台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=request.session.get("tablename")

        #获取全部列名
        columns=  examrecord.getallcolumn( examrecord, examrecord)
        try:
            __authSeparate__=examrecord.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=examrecord.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']
        error= examrecord.createbyreq(examrecord,examrecord, req_dict)
        if error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_thumbsup(request,id_):
    '''
     点赞：表属性thumbsUp[是/否]，刷表新增thumbsupnum赞和crazilynum踩字段，
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=examrecord.getbyid(examrecord,examrecord,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = examrecord.updatebyparams(examrecord,examrecord, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)


def examrecord_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = examrecord.getbyid(examrecord,examrecord, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= examrecord.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"  and  "clicknum"  in examrecord.getallcolumn(examrecord,examrecord):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}
            ret=examrecord.updatebyparams(examrecord,examrecord,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =examrecord.getbyid(examrecord,examrecord, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= examrecord.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"   and  "clicknum"  in examrecord.getallcolumn(examrecord,examrecord):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}

            ret=examrecord.updatebyparams(examrecord,examrecord,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys() and req_dict['clicktime']=="None":
            del req_dict['clicktime']
        if req_dict.get("mima") and "mima" not in examrecord.getallcolumn(examrecord,examrecord) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in examrecord.getallcolumn(examrecord,examrecord) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = examrecord.updatebyparams(examrecord, examrecord, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def examrecord_delete(request):
    '''
    批量删除
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=examrecord.deletes(examrecord,
            examrecord,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def examrecord_vote(request,id_):
    '''
    浏览点击次数（表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1）
统计商品或新闻的点击次数；提供新闻的投票功能
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= examrecord.getbyid(examrecord, examrecord, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=examrecord.updatebyparams(examrecord,examrecord,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def examrecord_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        excel_file = request.FILES.get("file", "")
        if excel_file.size > 100 * 1024 * 1024:  # 限制为 100MB
            msg['code'] = 400
            msg["msg"] = '文件大小不能超过100MB'
            return JsonResponse(msg)

        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    examrecord.createbyreq(examrecord, examrecord, req_dict)
                    
            except:
                pass
                
        else:
            msg = {
                "msg": "文件类型错误",
                "code": 500
            }
                
        return JsonResponse(msg)

def examrecord_autoSort2(request):
    return JsonResponse({"code": 0, "msg": '',  "data":{}})


#选项统计接口
def examrecord_options_num(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        # 处理参数
        try:
            page1 = int(req_dict.get("page"))
        except:
            page1 = 1
        try:
            limit1 = int(req_dict.get("limit"))
        except:
            limit1 = 10
        start = limit1 * (page1 - 1)
        end = limit1 * (page1 - 1) + limit1 + 1
        try:
            del req_dict["page"]
            del req_dict["limit"]
        except:
            pass
        datas = examrecord.objects.filter(**req_dict).annotate(paperids=Count('paperid')).all()
        try:
            data = [model_to_dict(i) for i in datas]
            for item in data:
                anum = datas.filter(questionid=item['questionid']).aggregate(
                    anum=Sum(Case(When(myanswer__contains='A', then=1), default=0, output_field=IntegerField())))[
                    'anum']
                bnum = datas.filter(questionid=item['questionid']).aggregate(
                    bnum=Sum(Case(When(myanswer__contains='B', then=1), default=0, output_field=IntegerField())))[
                    'bnum']
                cnum = datas.filter(questionid=item['questionid']).aggregate(
                    cnum=Sum(Case(When(myanswer__contains='C', then=1), default=0, output_field=IntegerField())))[
                    'cnum']
                dnum = datas.filter(questionid=item['questionid']).aggregate(
                    dnum=Sum(Case(When(myanswer__contains='D', then=1), default=0, output_field=IntegerField())))[
                    'dnum']
                item['anum']=anum
                item['bnum']=bnum
                item['cnum']=cnum
                item['dnum']=dnum
        except:
            data = datas
        result_list = []
        for item in data:
            has_questionname_one = any(i['questionname'] == item['questionname'] for i in result_list)
            if not has_questionname_one:
                result_list.append(item)
        data = result_list
        # 赋值分页查询所得数据
        try:
            div = divmod(len(data), limit1)
            if div[1] > 0:
                totalPage = div[0] + 1
            else:
                totalPage = div[0]
        except:
            totalPage = 1
        # 赋值分页参数
        msg["data"] = {"pageSize": limit1,
                       "total": len(data),
                       "totalPage": totalPage,
                       "currPage": page1,
                       "list": data[start:end]
                       }
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_groupby(request):
    '''
    管理员用户：当表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        #处理参数
        try:
            page1 = int(req_dict.get("page"))
        except:
            page1 = 1
        try:
            limit1 = int(req_dict.get("limit"))
        except:
            limit1 = 10

        #值为"是"仅能查看自己的记录和add接口后台赋值userid的值
        try:
            __authSeparate__ = examrecord.__authSeparate__
        except:
            __authSeparate__ = None

        # print(examrecord.getallcolumn(examrecord,examrecord))
        if __authSeparate__=="是":
            #print("req_dict==============>",req_dict)
            #如果当前表有userid字段,且通过身份认证
            if "userid"  in examrecord.getallcolumn(examrecord,examrecord) and request.session.get("params")!=None:
                #参数增加userid
                req_dict["userid"]=request.session.get("params").get("id")
        #如果当前表没有userid字段,且参数里有userid键值对
        if  "userid" not  in examrecord.getallcolumn(examrecord,examrecord) and "userid" in list(req_dict.keys()):
            #删除参数userid
            del req_dict["userid"]
        try:
            del req_dict["page"]
            del req_dict["limit"]
        except:
            pass
        tablename=request.session.get("tablename")

        if tablename=="users" and req_dict.get("userid")!=None:
            del req_dict["userid"]
        else:
            #判断当前登陆表是否具有管理员权限
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            #是,则删除userid参数
            if __isAdmin__=="是":
                del req_dict["userid"]
            else:
                #否,则赋值userid参数
                req_dict["userid"]=request.session.get("params").get("id")
        print("req_dict===========>",req_dict)

        #本次分页查询
        start=limit1 * (page1 - 1)
        end=limit1 * (page1 - 1)+limit1+1
        papername = ''
        if 'papername' in req_dict.keys():
            papername = req_dict['papername'].replace("%", "")
            req_dict = {}
        datas = examrecord.objects.filter(**req_dict).filter(papername__icontains=papername).\
                    annotate(userids=Count('userid'),usernames=Count('username'),paperids=Count('paperid'),papernames=Count('papername')). \
                values("userid", "username", "paperid", "papername","myscore","ismark","type"). \
                    all()
        print("datas=============>", datas)
        print("datas=============>", datas.aggregate(myscore=Sum('myscore')))

        #做对的题数
        condition_count = 0
        #总题数
        total_count = 0

        #处理分页查询所得数据
        try:
            data = [model_to_dict(i) for i in datas]
        except:
            data = datas
        dataDict = {}
        isMark = 0
        for i in data:
            keyName1="{}#{}#{}#{}#{}".format(i.get("userid"),i.get("username"),i.get("paperid"),i.get("papername"),i.get("ismark"))
            if int(i.get("type")) == 4 and int(i.get("ismark")) == 0:
                isMark = 1
            if dataDict.get(keyName1)==None:
                total_count=0
                condition_count=0
                dataDict[keyName1]={"userid":i.get("userid"),"username":i.get("username"),"paperid":i.get("paperid"),"papername":i.get("papername"),"myscore":i.get("myscore")}
            else:
                dataDict[keyName1]["myscore"]=dataDict.get(keyName1).get("myscore")+i.get("myscore")
            if i.get("myscore") > 0:
                condition_count += 1
            total_count += 1
            dataDict[keyName1]["ismark"] =isMark
            dataDict[keyName1]['accuracy']= round(condition_count / total_count, 2)
        #赋值分页查询所得数据
        dataList =list(dataDict.values())

        # 处理所有查询,计算总页数
        total = len(dataList)
        try:
            div = divmod(total, limit1)
            if div[1] > 0:
                totalPage = div[0] + 1
            else:
                totalPage = div[0]
        except:
            totalPage = 1

        # 赋值分页参数
        msg["data"] = {"pageSize": limit1,
                       "total": total,
                       "totalPage": totalPage,
                       "currPage": page1,
                       "list":dataList[start:end]
                       }

        return JsonResponse(msg, encoder=CustomJsonEncoder)

def examrecord_deleterecords(request):
    '''
    按键值对参数添加删除记录
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        error=examrecord.deletebyparams(examrecord,examrecord,req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)

def examrecord_security(request):
    '''
    获取密保接口
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        req_dict = request.session.get("req_dict")
        
        sql = "SELECT * FROM examrecord where ='{0}'".format(req_dict['username'])
        record = None
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            record = online_dict
        msg['data'] = record

        return JsonResponse(msg)










