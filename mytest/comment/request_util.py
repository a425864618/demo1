from requests import Session

class Request(object):
    def __init__(self):
        self.session=Session()

    def sendrequest(self,url,method,data=None,content_type=None):
        method=method.upper()
        if method=="GET":
            try:
                result=self.session.request(method=method,url=url,params=data).json()
                return result
            except:
                print("http请求报错")

        elif method=="POST":

            try:
                result=self.session.request(method=method,url=url,data=data).json()
                return result
            except:
                print('http请求报错')
        else:
            print('暂时不支持本方法')
if __name__ == '__main__':
    a=Request()
    b=a.sendrequest('http://120.24.33.253:8080/futureloan/mvc/api/loan/generateRepayments','get',{"id":100})
    print(b)
