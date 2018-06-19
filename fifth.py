from sys import argv    # 导入argv包

script, filename = argv           # 赋予变量

txt = open(filename)              # 打开文件

print('Here\'s your file %r:' % filename)         # 打印文件名
print(txt.read())                                 # 打印文件内容

print('Type the filename again:')                 # 打印
file_again = input('> ')                          # 用户输入值

txt_again = open(file_again)                      # 打开用户输入的文件

print(txt_again.read())                           # 打印文件内容