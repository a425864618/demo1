#上下文管理器

from comment.read_yaml import readyaml
from comment.every_path import datayaml_payh,jsonpath
from comment.sql_util import SqlUtil
from comment.read_json import Read_Json
import datetime
import string
import random



str1=string.ascii_letters

len1=random.randint(1,8)
name=''.join(random.sample(string.ascii_letters + string.digits, 6))
time=datetime.datetime.now().strftime('%d%H%M%S')
mbf="157"+str(time)

#实例化对象读取json
readjson=Read_Json(jsonpath)

def content(case):

    data = readyaml(datayaml_payh,case['data'])
    case['data'] = data
    if case['title']=="注册成功":
        case["data"]["mobilephone"]=mbf
        case["data"]["regname"]=name

    if case['is_depend'].upper()=='Y':
        if case["title"]=="投资":
            json_data = readjson.readjson("depen")
            # print(json_data[0], json_data[1], json_data[2],json_data[3],json_data[4],json_data[5])
            secrch = SqlUtil()
            __result = secrch.findall('select %s from `%s`;' % (json_data[1], json_data[0]))

            __result1 = secrch.findall('select %s from `%s`;' % (json_data[4], json_data[3]))
            # print(__result[-1],__result1[-1])
            case["data"][json_data[2]] =__result[-1][json_data[1]]
            case["data"][json_data[5]]=__result1[-1][json_data[4]]
        else:
            json_data=readjson.readjson(case['depend_data'])
            # print(json_data[0],json_data[1],json_data[2])
            secrch=SqlUtil()
            __result=secrch.findall('select %s from `%s`;'%(json_data[1],json_data[0]))
            case["data"][json_data[2]] =__result[-1][json_data[1]]
    return case



if __name__ == '__main__':
    case={'id': 1, 'title': '注册成功', 'method': 'post', 'url': 'member/register', 'run': 'yes', 'data': 'registersuccess', 'assert': 10001, 'real_result': None, 'is_pass': None, 'update_time': None, 'sql_form': None, 'is_depend': 'n', 'depend_cookies': 'n', 'depend_id': None, 'depend_data': None}

