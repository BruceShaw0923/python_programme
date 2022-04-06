#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#棋盘初始化
finish = False
flagNum = 1
flagch = '*'
x = 0
y = 0
print('\033[1;37;41m--------简易五子棋---------\033[0m')

checkerboard = []
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append('-')


##打印胜利棋盘并输出结果
def msg():
    print("\033[1;30;46m-------------------------]")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + " ", end = ' ');
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end = ' ')
        print()
    print("------------------------------------\033[0m")
    if flagNum == 1:
        print('\033[32m*棋胜利！---、033[0m')
    else:
        print('\033[32mo棋胜利！---、033[0m')

while not finish:
    #打印棋盘
    print("\033[1;30;46m-------------------------]")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + " ", end = ' ');
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end = ' ')
        print()
    print("------------------------------------\033[0m")

    ##判断当前下棋者
    if flagNum == 1:
        flagch = '*'
        print('\033[1;37;45m请*输入棋子坐标（例如A1）:\033[0m', end='')
    else:
        flag = 'o'
        print('\033[1;30;42m请o输入棋子坐标（例如B2）:\033[0m', end='')

    ##输入棋子坐标
    try:
        str = input()
        ch = str[0]
        x = ord(ch) - 65
        y = int(str[1]) - 1
    except ValueError:
        str = input("输入有误，请按格式重新输入：")
        ch = str[0]
        x = ord(ch) - 65
        y = int(str[1]) - 1

    ##判断所输入坐标是否在棋盘内
    if(x < 0 or x > 9 or y < 0 or y > 9):
        print('\033[31m***输入的坐标有误，请重新输入！***\033[0m')
        continue

    ##判断所在位置是否有棋子
    if checkerboard[x][y] == '-':
        if flagNum == 1:
            checkerboard[x][y] = '*'
        else:
            checkerboard[x][y] = 'o'
    else:
        print('\033[31m******该输入位置已有棋子，请重新输入！\033[0m')


    # 算法 判断是否满足胜利条件
    if y-4 >= 0:
        if (checkerboard[x][y-1] == flagch
                and checkerboard[x][y-2] == flagch
                and checkerboard[x][y-3] == flagch
                and checkerboard[x][y-4] == flagch):
            finish = True
            msg()

    if y+4 <= 9:
        if (checkerboard[x][y+1] == flagch
                and checkerboard[x][y+2] == flagch
                and checkerboard[x][y+3] == flagch
                and checkerboard[x][y+4] == flagch):
            finish = True
            msg()

    if x-4 >= 0:
        if (checkerboard[x-1][y] == flagch
                and checkerboard[x-2][y] == flagch
                and checkerboard[x-3][y] == flagch
                and checkerboard[x-4][y] == flagch):
            finish = True
            msg()

    if x+4 <= 9:
        if (checkerboard[x+1][y] == flagch
                and checkerboard[x+2][y] == flagch
                and checkerboard[x+3][y] == flagch
                and checkerboard[x+4][y] == flagch):
            finish = True
            msg()

    if x - 4 >= 0 and y - 4 >= 0:
        if(checkerboard[x-1][y-1] == flagch
                and checkerboard[x-2][y-2] == flagch
                and checkerboard[x-3][y-3] == flagch
                and checkerboard[x-4][x-4] == flagch):
            finish = True
            msg()

    if x - 4 >= 0 and y + 4 <= 9:
        if(checkerboard[x-1][y+1] == flagch
                and checkerboard[x-2][y+2] == flagch
                and checkerboard[x-3][y+3] == flagch
                and checkerboard[x-4][x+4] == flagch):
            finish = True
            msg()

    if x + 4 <= 9 and y - 4 >= 0:
        if(checkerboard[x+1][y-1] == flagch
                and checkerboard[x+2][y-2] == flagch
                and checkerboard[x+3][y-3] == flagch
                and checkerboard[x+4][x-4] == flagch):
            finish = True
            msg()

    if x + 4 <= 9 and y + 4 <= 9:
        if(checkerboard[x+1][y+1] == flagch
                and checkerboard[x+2][y+2] == flagch
                and checkerboard[x+3][y+3] == flagch
                and checkerboard[x+4][x+4] == flagch):
            finish = True
            msg()
            
    flagNum *= -1;#下棋人更换
    

