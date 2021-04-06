# -*- coding:utf-8 -*-#
# -------------------------------------------------------------------------
# ProjectName:       mytest
# FileName:          log.py
# Author:            zhoubo
# Date:              2021/3/21 19:13
# Description:
# --------------------------------------------------------------------------
import logging
import logging.handlers#可以使用滚动日志RotatingFileHandler
import os


def get_logger(logger_name):
    #创建一个日志收集器对象
    logger = logging.getLogger(logger_name)
    #设置日志收集器的日志级别，一般默认最低级别
    logger.setLevel('DEBUG')

    # 格式:规定日志输出的格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formate = logging.Formatter(fmt)

    file_name = os.path.join("C:\project\mytest\data", 'case.log')
    #设置日志输出的渠道，这里是输出到文件，之前用的是 logging.FileHandler
    #写入文件，如果文件超过20M，仅保留10个日志文件
    #RotatingFileHandler 是用来生成滚动日志的，适用于需要控制日志文件大小的场景
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20 * 1024 * 1024, backupCount=10,encoding="utf-8")
    #ini文件中读取日志的级别

    level = "DEBUG"
    #设置日志级别
    file_handler.setLevel(level)
    ##添加日志格式
    file_handler.setFormatter(formate)

    #设置日志输出的渠道--输出到控制台
    console_handler = logging.StreamHandler()
    # ini文件中读取日志的级别
    level = "DEBUG"
    # 设置日志级别
    console_handler.setLevel(level)
    #添加日志格式
    console_handler.setFormatter(formate)

    # 对接 日志收集器与输出渠道 进行对接--相亲成功
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    #清除日志，如不不清除日志是追加模式
    # logger.removeHandler(file_handler)

    return logger
