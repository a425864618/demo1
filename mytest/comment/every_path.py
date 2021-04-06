import os

#根目录
BaseDir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#data文件夹路径
datapath=os.path.join(BaseDir,'data')

#excel文件路径
excelpath=os.path.join(datapath,"cases.xlsx")

#data.yaml文件路径
datayaml_payh=os.path.join(datapath,"data.yaml")

#jsonpath
jsonpath=os.path.join(datapath,"depend.json")

#ini文件地址
conf_path=os.path.join(datapath,"conf.ini")

#C:\project\mytest\data\data.yaml
#C:\project\mytest\data\data.yaml
# print(datayaml_payh)
