from tkinter import *

# 窗口初始化
win = Tk()
win.title("盲打")
win.geometry("500x200+400+100")

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
        'J': "急忙",
        'K': "开出",
        'L': "螺旋",
        'M': "摩托",
        'N': "哪知",
        'O': "偶遇",
        'P': "朋友",
        'Q': "前来",
        'R': "忍者",
        'S': "射箭",
        'T': "突然",
        'U': "u;u'",
        'V': "v[v]v\\",
        'W': "我们",
        'X': "向前",
        'Y': "乐器",
        'Z': "再见"
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
lable = Label(win, textvariable = txt_A_to_Z)
lable.pack()

# 次数统计
count = Label(win, textvariable = txt_count)
count.pack()

# 输入框
entry = Entry(win, textvariable = txt_entry)
entry.bind('<Return>', handler_return)
entry.pack()

win.mainloop()
