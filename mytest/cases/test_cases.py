# --utf-8--
import unittest
from comment import context
from comment.request_util import Request
from ddt import ddt, data
from datetime import datetime
from testrun import de
from comment.log import get_logger
from comment.every_path import conf_path
from comment.readini import Readini

time = datetime.now().strftime('%Y/%m/%d/%H:%M:%S')
# host = "http://120.24.33.253:8080/futureloan/mvc/api/"

cases = de.ReadExcel('充值')
request = Request()
readini=Readini(conf_path)
host=readini.readini("conf","host")


@ddt
class Testlogin(unittest.TestCase):
    # 该类为注册测试用例，通过ddt解包，传入用例
    logger = get_logger("接口测试")

    @data(*cases)
    def testlogin(self, case):
        new_case = context.content(case)
        try:
            # url,method,data=None,content_type=None
            result = request.sendrequest(host + new_case['url'], new_case['method'], new_case['data'])
            self.assertEqual(result['code'], str(new_case['assert']))
            self.logger.info("用例标题：%s 执行通过,%s"%(new_case['title'],result['msg']))
            # print(result)
            de.Write("充值",new_case["id"]+1,None,"Pass",time)
        except Exception as e:
            self.logger.debug("用例标题：%s 执行失败"%new_case['title'])
            de.Write("充值",new_case["id"]+1,e,"Pass",time)
            raise e

if __name__ == '__main__':
    unittest.main()
