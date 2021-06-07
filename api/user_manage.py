# 主要是完成管理员接口的实现
from setting import BASE_URL
import requests
from loguru import logger
from api.base import Base

class UserManager(Base):

    def __init__(self):
        self.add_user_path = '/admin/admin/create'
        self.edit_user_path = '/admin/admin/update'
        self.get_user_path = '/admin/admin/list?page=1&limit=20&sort=add_time&order=desc'
        self.delete_user_path = '/admin/admin/delete'
        self.b = Base()

    # 添加管理员
    def add_user(self,username,password,**kwargs):
        add_data = {'username':username,'password':password}
        if kwargs:
            logger.info("添加管理员接收可选参数为{}".format(kwargs))
            add_data.update(**kwargs)
        add_url = self.get_url(self.add_user_path)
        return self.post(add_url,add_data)

    # 编辑管理员
    def edit_user(self,id,username,password,**kwargs):
        edit_url = self.get_url(self.edit_user_path)
        edit_data = {'id':id,'username':username,'password':password}
        if kwargs:
            edit_data.update(**kwargs)
        return self.post(edit_url,edit_data)



    # 查询管理员
    def get_user(self):
        get_url = self.get_url(self.get_user_path)
        return self.get(get_url)

    # 删除管理员
    def delete_user(self,id,**kwargs):
        delete_url = self.get_url(self.delete_user_path)
        delete_data = {'id':id}
        if kwargs:
            delete_data.update(**kwargs)
        return self.post(delete_url,delete_data)


if __name__ == '__main__':
    um = UserManager()
    # um.add_user('testqqqq','testqqqq')
    # um.delete_user('145')
