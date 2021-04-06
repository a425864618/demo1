from configparser import ConfigParser
from comment.every_path import conf_path

class Readini(object):
    def __init__(self,fildname):
        self.fildname=fildname
        self.cf=ConfigParser()

    def readini(self,section,option):
        self.cf.read(conf_path,encoding="utf-8")

        return self.cf[section][option]

if __name__ == '__main__':
    pass