"""
符号    ASCII码      意义
\n        10        换行NL
\r        13        回车CR

回车 \r 本义是光标重新回到本行开头，r的英文return，控制字符可以写成CR，即Carriage Return
换行 \n 本义是光标往下一行（不一定到下一行行首），n的英文newline，控制字符可以写成LF，即Line Feed

在不同的操作系统这几个字符表现不同，比如在WIN系统下，这两个字符就是表现的本义，
在UNIX类系统，换行\n就表现为光标下一行并回到行首，
在MAC上，\r就表现为回到本行开头并往下一行，
至于ENTER键的定义是与操作系统有关的。通常用的Enter是两个加起来
"""
"""
Mac Linux Unix ---> \n
Window  ---> \r\n
"""
