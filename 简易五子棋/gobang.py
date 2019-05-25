'''
author:zhangyazhong
time:2019-05-25
'''

finish = False #结束标识
flagNum = 1 #下棋者标识
flagch = "*" #下棋者棋子
x = 0
y = 0
print("\033[1;30;41m------简易五子棋游戏------(控制台)-------\033[0m")
#初始化棋盘
checkboard = []
for i in range(10):
    checkboard.append([])
    for j in range(10):
        checkboard[i].append('-')

#打印棋盘
print('\033[1;30;41m------------------------')
print("  1 2 3 4 5 6 7 8 9 10")
for i in range(len(checkboard)):
    print(chr(i + ord('A')) + ' ', end='')
    for j in range(len(checkboard)):
        print(checkboard[i][j] + ' ', end='')
    print()
print("------------------------\033[0m")

