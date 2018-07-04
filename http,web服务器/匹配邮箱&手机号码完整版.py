import re

# 作业1：匹配邮箱完整版
# 邮箱格式：邮件名称@域名
# 几种不同格式的邮箱
mail1 = "yannan_zhu@gmail.com"  # 域名含一个"."
mail2 = "aaaaa-bbbb_ccc123@sina.com.cn"  # 域名含多个".",邮件名称部分含"-","_"等字符
mail3 = "张三@某公司.cn"  # 中国频道、新浪、icoremail等数家域名注册代理商已能够提供中文邮件服务

# (.[a-zA-Z0-9-]+)+$ 用来匹配域名含多个"."的情况
ret1 = re.match(r"^[\u4e00-\u9fa5,a-zA-Z0-9_-]+@[\u4e00-\u9fa5,a-zA-Z0-9_-]+(.[a-zA-Z0-9-]+)+$", mail1).group()
print(ret1)
ret2 = re.match(r"^[\u4e00-\u9fa5,a-zA-Z0-9_-]+@[\u4e00-\u9fa5,a-zA-Z0-9_-]+(.[a-zA-Z0-9-]+)+$", mail2).group()
print(ret2)
ret3 = re.match(r"^[\u4e00-\u9fa5,a-zA-Z0-9_-]+@[\u4e00-\u9fa5,a-zA-Z0-9_-]+(.[a-zA-Z0-9-]+)+$", mail3).group()
print(ret3)

# 作业2：匹配手机号码完整版
# 网上查了目前的号段
tel_num1 = "13955556666"
# tel_num2 = "021-12345678" 这种的号码貌似是座机，就不匹配了
print(re.match(r"^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$", tel_num1).group())

