from tkinter import *

# 窗口初始化
win = Tk()
win.title("盲打")
win.geometry("300x120+500+100")

# 记录变量
num = 1
alphabet = 'A'

# 汉字表
def chinese_dict(val):
    return {
        'A': "爱人",
        'B': "不见",
        'C': "冲出",
        'D': "大门",
        'E': "恶魔",
        'F': "飞起",
        'G': "高空",
        'H': "回旋",
        'I': "i,i.i/",
        'J': "警察",
        'K': "开枪",
        'L': "连续",
        'M': "命中",
        'N': "农夫",
        'O': "偶遇",
        'P': "婆娘",
        'Q': "前来",
        'R': "任性",
        'S': "摔倒",
        'T': "天真",
        'U': "u;u'",
        'V': "v[v]v\\",
        'W': "我们",
        'X': "向前",
        'Y': "乐器",
        'Z': "奏响"
    }[val]

# 输入框回车处理函数
def handler_return(event):
    global num
    global alphabet
    if txt_entry.get() == chinese_dict(alphabet):
        num += 1
        if num > 10:
            num = 1
            if alphabet == 'Z':
                alphabet = 'A'
            else:
                alphabet = chr(ord(alphabet) + 1)
            txt_A_to_Z.set("练习" + alphabet + ": " + chinese_dict(alphabet))
        txt_count.set(str(num) + "/10")
        entry.delete(0, 'end')
    else:
        pass

# 变化文本定义
txt_A_to_Z = Variable()
txt_A_to_Z.set("练习" + alphabet + ": " + chinese_dict(alphabet))
txt_count = Variable()
txt_count.set(str(num) + "/10")
txt_entry = Variable()
txt_entry.set("")

# 字母显示
lable = Label(win, textvariable = txt_A_to_Z, font="宋体 20 bold")
lable.pack()

# 次数统计
count = Label(win, textvariable = txt_count, font="宋 15")
count.pack()

# 输入框
entry = Entry(win, textvariable = txt_entry, font="宋体 20")
entry.bind('<Return>', handler_return)
entry.pack()

win.mainloop()
