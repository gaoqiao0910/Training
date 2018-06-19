from sys import argv      # 导入包

script, filename = argv           # 赋予变量

print('We\'re going to erase %r.' % filename)         # 打印
print('If you don\'t want that, hit CTRL-C (^C).')    # 打印
print('If you do want that, hit RETURN.')             # 打印

input('?')                        # 用户输入值

print('Opening the file...')      # 打印
target = open(filename, 'w')      # 打开文件，W：文件若存在，首先要清空，然后（重新）创建

print('Truncating the file. Goodbye!')      # 打印
target.truncate()                           # 清空文件

print('Now I\'m going to ask you for three lines.')    # 打印

line1 = input('line 1:')                   # 用户输入值
line2 = input('line 2:')                   # 用户输入值
line3 = input('line 3:')                   # 用户输入值

print('I\'m going to write these to the file.')     # 打印

#target.write(line1)                         # 调用write方法
#target.write('\n')                          # 换行
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

target.write('%s\n%s\n%s\n' % (line1, line2, line3))

print('And finally, we close it.')          # 打印
target.close()                              # 关闭函数








