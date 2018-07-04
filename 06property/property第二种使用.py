# property属性的第二种定义方式:类属性定义方式
class Goods(object):
    def get_price(self):
        print("get price...")
        return 100

    def set_price(self, value):
        """必须两个参数"""
        print("set price...")
        print(value)

    def del_price(self):
        print("del price")

    # property方法中有个四个参数
    # 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
    # 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
    # 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
    # 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
    price = property(get_price, set_price, del_price, "相关描述...")  # property参数顺序


obj = Goods()

obj.price  # 自动调用第一个参数中定义的方法：get_price
obj.price = "价格"  # 自动调用第二个参数中定义的方法：set_price方法，并将“价格”当作参数传入
desc = Goods.price.__doc__  # 自动获取第四个参数中设置的值："相关描述..."
print(desc)
del obj.price  # 删除时，会自动调用第三个参数中定义的方法：del_price方法

"""
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goods()
obj.PRICE          # 获取商品价格
obj.PRICE = 200    # 修改商品原价
del obj.PRICE      # 删除商品原价
Goods.PRICE.__doc__# 获取价格的描述信息
"""
