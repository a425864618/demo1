import unittest
from comment.do_excel import DoExcel
from comment.every_path import datayaml_payh,excelpath

#实例化EXCEl对象，不然的话，不会回写结果
de=DoExcel(excelpath)

def load_all():

    discover=unittest.defaultTestLoader.discover("cases",pattern='*.py',top_level_dir=None)
    return discover

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(load_all())
