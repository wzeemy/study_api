# 可以复用的代码(重复的)可以写入utils(公共库)

# 例:公共断言
def same_assert(obj,response,except_res = 0):
    obj.assertEqual(except_res,response['errno'])
