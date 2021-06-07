from api.user_manage import UserManager
import unittest

class TestUserManagerCase(unittest.TestCase):
    manager_id = None

    # 初始化
    @classmethod
    def setUpClass(cls) -> None:

        cls.user = UserManager()
        cls.newname = 'qwewqr'

    # case1:只输出用户名和密码,请求添加管理员接口
    def test01_add_user(self):
        #1 初始化定义数据
        username = 'test41'
        password = 'test41'
        get_id = None
        #2 请求接口(添加管理员),输入的参数就是用户名和密码
        response = self.user.add_user(username,password)
        data = response.get('data')
        if data:
            get_id = data.get('id')
        if get_id:
            TestUserManagerCase.manager_id = get_id
        #3 获取Jsno数据进行断言
        self.assertEqual(0,response['errno'])
        self.assertEqual(username,response['data']['username'])

    #case2:编辑管理员
    def test02_edit(self):
        response = self.user.edit_user(TestUserManagerCase.manager_id,self.newname,password= '1232144')
        self.assertEqual(0,response['errno'])
        self.assertEqual(self.newname, response['data']['username'])

    #case3:查询管理员
    def test03_get(self):
        response = self.user.get_user()
        self.assertEqual(0, response['errno'])
        self.assertEqual(self.newname,response['data']['list'][0]['username'])

    #case4:删除管理员
    def test04_delete(self):
        response = self.user.delete_user(TestUserManagerCase.manager_id)
        self.assertEqual(0,response['errno'])




if __name__ == '__main__':
    unittest.main()
