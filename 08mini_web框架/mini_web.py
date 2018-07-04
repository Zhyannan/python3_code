# 服务器给数据，然后返回数据给服务器
import re

from pymysql import connect

url_dict = dict()


# start_response用来框架给服务器传递响应头的数据
# environ 用来得到服务器传过来的文件路径
def application(environ, start_response):
    """返回具体展示的界面给服务器"""
    start_response('200 OK', [("Content-Type", "text/html;charset=utf-8")])

    # 根据不同的地址进行判断
    file_name = environ['file_name']  # /index.html

    for key, value in url_dict.items():
        match = re.match(key, file_name)

        if match:
            return value(match)  # 匹配到了就返回函数的引用，并调用返回匹配的页面结果

        else:
            return 'not page is found'


# 这个装饰器传参，用来完成路由的功能
def route(url_address):
    """用来自动添加 路径 & 匹配的函数 到 全局变量 url_dict 字典中"""

    def set_fun(func):
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        # 根据不同的函数名称添加到字典中
        url_dict[url_address] = call_fun
        return call_fun

    return set_fun


# 步骤
# 1.打开或读取前端的界面文件
# 2.拿到数据库的数据
# 3.拼接数据
# 4.返回拼接完的数据给服务器

# 首页
@route("/index.html")
def index(match):
    # 打开
    with open("./templates/index.html") as f:
        content = f.read()

    # 从数据库拿到数据
    # 连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()

    # 执行sql语句
    sql = """select * from info;"""
    cs.execute(sql)
    # 得到数据
    row_data1 = cs.fetchall()

    # 关闭
    cs.close()
    conn.close()

    # 处理数据
    # 从html复制一行的代码
    row_str = """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
            </td>
            </tr>"""
    table_str = ""
    for temp in row_data1:
        table_str += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[1])

    # 使用正则去替换页面的数据 {%content%} 替换成row_data
    content = re.sub(r"\{%content%\}", table_str, content)

    # 返回给服务器
    return content


# 个人中心
@route(r"center.html")
def center(match):
    # 读取前端的数据
    with open("./templates/center.html") as f:
        content = f.read()

    # 从数据库拿到数据
    # 连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()

    # 执行sql语句
    sql = """select info.code,info.short,info.chg,info.turnover,info.price,info.highs,focus.note_info from info inner join focus on info.id = focus.info_id;"""
    cs.execute(sql)
    # 得到数据
    row_data = cs.fetchall()

    # 关闭
    cs.close()
    conn.close()

    # html一行的代码
    row_str = """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>"""
    # 拼接数据
    table_str = ""
    for temp in row_data:
        table_str += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[0], temp[0])

    content = re.sub(r"\{%content%\}",table_str,content)
    return content


# 添加
@route(r"/add/(\d+).html")
def add(match):
    # 得到要添加的code
    code = match.group(1)

    # 连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()

    # 执行sql语句
    sql = """select * from focus where info_id = (select id from info where code = %s)"""
    cs.execute(sql,(code,))

    # 数据存在，提示已存在；不存在，添加并提示添加成功
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了"
    else:
        add_sql = """insert into focus(info_id) (select id from info where code = %s);"""
        cs.execute(add_sql,(code,))
        conn.commit()
        cs.close()
        conn.close()
        return "添加成功！"


# 删除个人中心的数据
@route("/del/(\d+).html")
def del_method(match):
    # 获取要删除的code
    code = match.group(1)

    # 连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()

    # 执行sql语句
    sql = """delete from focus where info_id = (select id from info where code = %s);"""
    cs.execute(sql,(code,))

    # 提交
    conn.commit()
    #关闭
    cs.close()
    conn.close()

    return  "删除成功！"