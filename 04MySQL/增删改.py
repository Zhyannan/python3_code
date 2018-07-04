from pymysql import *


def main():
    # 创建connect连接
    conn = connect(host='127.0.0.1', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，并返回受影响的行数，添加一条数据
    # 增加
    count = cs1.execute('select * from goods_cates;')
    # 打印受影响的行数
    print(count)
    # 提交之前的所有excute操作
    conn.commit()
    # 关闭cursor对象
    cs1.close()
    # 关闭connect连接
    conn.close()


if __name__ == '__main__':
    main()
