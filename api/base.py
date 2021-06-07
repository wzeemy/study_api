# 主要实现的是基础接口的封装.

# 导入配置
from setting import BASE_URL

# 导入loguru
from loguru import logger

# 导入requests
import requests

# 导入cacheout
from cacheout import Cache
cache = Cache()  # 调用

class Base():

    # 实现URL拼接
    def get_url(self,path,params=None):
        # 功能返回一个完整的URL , http://ip:port/接口地址/参数
        # path : 接口地址            port : 端口
        # params : 查询参数,默认无

        if params:
            full_url = BASE_URL + path + '?' + params
        else:
            full_url = BASE_URL + path

            logger.info("接口地址:{}".format(full_url))
        return full_url

    # 定义一个get方法
    def get(self,url):
        # 作用: 主要是对requests.get()进行封装,目的是满足后面的需求

        result = None
        response = requests.get(url,headers=self.get_headers())
        try:
            result = response.json()
            logger.debug("请求地址:{},请求接口返回结果:{}".format(url,result))
            return result
        except Exception as e:
            logger.error("请求get方法异常,返回数据:{}".format(result))

    # 定义一个post方法
    def post(self,url,data):
        result = None
        response = requests.post(url,json=data,headers=self.get_headers())
        try:
            result = response.json()
            logger.debug("请求地址:{},请求接口返回结果:{}".format(url,result))
            return result
        except Exception as e:
            logger.error("请求post法异常,返回数据:{}".format(result))

    # 定义一个请求头的处理
    def get_headers(self):
        headers = {'Content-type':'application/json'}
        token = cache.get('token')
        if token:
            headers.update({'X-Litemall-Admin-Token':token})
        logger.warning("请求头信息返回数据:{},注意:多数接口需要token".format(headers))
        return headers

    # 定义登录
    def login(self,username,password):
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        login_data = {'username':username,'password':password}
        response = self.post(login_url,login_data)
        try:
            if response.get('errno') == 0:
                logger.info("请求登录接口成功")
                token = response.get('data').get('token')
                cache.set('token',token)
            else:
                logger.error("请求登录接口失败".format(response))
        except Exception as e:
            logger.error('请求登录接口返回异常'.format(response))






if __name__ == '__main__':
    b = Base()
    # print(b.get_url('/admin/auth/login'))
    # print(b.get_url('/admin/auth/login','q=iphone'))
    print(b.login('admin123','admin123'))