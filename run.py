# 批量运行及生成测试报告

import unittest
from HTMLTestRunner import HTMLTestRunner
from api.base import Base
from setting import username,password,test_reporter_file

if __name__ == '__main__':

    Base().login(username,password)

    suite = unittest.TestLoader().discover('./cases','test*.py')

    with open(test_reporter_file,'wb') as f:
        runner = HTMLTestRunner(f,title="管理员项目测试报告")
        runner.run(suite)
