from pymysql import connect


def search_all_goods():
    """1-查询所有商品信息"""
    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="mysql", database="jing_dong", charset="utf8")
    # 获取cursor对象
    cs = conn.cursor()
    # 执行sql语句
    sql = """ select * from goods;"""
    cs.execute(sql)
    row_data = cs.fetchall()
    # 关闭
    cs.close()
    conn.close()

    # 处理拿到的数据
    for temp in row_data:
        print(temp)


def search_all_cates():
    """2-查询所有商品在种类信息"""
    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="mysql", database="jing_dong", charset="utf8")
    # 获取cursor对象
    cs = conn.cursor()
    # 执行sql语句
    sql = """ select name from goods_cates;"""
    cs.execute(sql)
    row_data = cs.fetchall()
    # 关闭
    cs.close()
    conn.close()

    # 处理数据
    for temp in row_data:
        print(temp)


def search_all_brand():
    """3-查询所有商品在品牌信息"""
    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="mysql", database="jing_dong", charset="utf8")
    # 获取cursor对象
    cs = conn.cursor()
    # 执行sql语句
    sql = """ select name from goods_brands;"""
    cs.execute(sql)
    row_data = cs.fetchall()
    # 关闭
    cs.close()
    conn.close()

    # 处理数据
    for temp in row_data:
        print(temp)


def add_goods_cate(input_cate):
    """4-添加商品种类"""
    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="mysql", database="jing_dong", charset="utf8")
    # 获取cursor对象
    cs = conn.cursor()

    # 执行sql语句
    sql = """ insert into goods_cates(name) values(%s);"""
    print("成功添加商品种类：%s " % input_cate)
    cs.execute(sql, (input_cate,))
    row_data = cs.fetchall()

    # 修改了数据，所以要提交
    conn.commit()

    # 关闭
    cs.close()
    conn.close()


def search_goods_by_id(input_id):
    """5-根据id查询商品信息"""
    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="mysql", database="jing_dong", charset="utf8")
    # 获取cursor对象
    cs = conn.cursor()

    # 执行sql语句
    sql = """ select * from goods where id = %s;"""
    cs.execute(sql, (input_id,))
    row_data = cs.fetchall()

    # 关闭
    cs.close()
    conn.close()

    # 处理数据
    for temp in row_data:
        print(temp)


def main():
    """京东服务器"""
    while True:
        print()
        print("*" * 30)
        print("1-查询所有商品信息")
        print("2-查询所有商品在种类信息")
        print("3-查询所有商品在品牌信息")
        print("4-添加商品种类")
        print("5-根据id查询商品信息")
        print("*" * 30)

        # 获取用户输入
        cmd = input("请输入要执行的操作：")
        print("action:", cmd)

        if cmd == "1":
            # 1-查询所有商品信息
            search_all_goods()

        elif cmd == "2":
            # 2-查询所有商品在种类信息
            search_all_cates()

        elif cmd == "3":
            # 3-查询所有商品在品牌信息
            search_all_brand()

        elif cmd == "4":
            # 4-添加商品种类
            input_cate = input("请输入要添加的商品的种类：")
            add_goods_cate(input_cate)

        elif cmd == "5":
            """5-根据id查询商品信息"""
            input_id = int(input("请输入要查询的商品id："))
            search_goods_by_id(input_id)

        else:
            print("输入有误，请重新输入！")


if __name__ == '__main__':
    main()
