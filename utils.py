# coding=utf8

import sys, traceback

def catch_traceback():
    """
    获取异常信息文件路径
    :return: str
    """
    exc_type, exc_value, exc_traceback = sys.exc_info()
    ex = traceback.format_exception(exc_type, exc_value, exc_traceback)
    lines = ''.join(ex)
    return lines

