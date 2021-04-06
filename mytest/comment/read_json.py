import json
aaaa="C:\project\mytest\data\depend.json"

#读取json文件的类，传入文件名，返回读取的json数据
class Read_Json(object):
    def __init__(self,fildname):
        self.fildname=fildname

    def readjson(self,key=None):
        with open(self.fildname, "r+") as fp:
            result=json.load(fp)[key]
            return result

if __name__ == '__main__':
    a=Read_Json(aaaa)
    b=a.readjson('depend_mbf')
    print(b,type(b))