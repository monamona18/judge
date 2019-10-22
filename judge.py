import tkinter
import tkinter.font as font

def judge():
    one = entry1.get()
    two = entry2.get()
    if one == two:
        result["text"] = "同じ"
    else:
        result["text"] = "違う"

def delete1():
    entry1.delete(0, tkinter.END)

def delete2():
    entry2.delete(0, tkinter.END)

root = tkinter.Tk()
root.title("同じかな？")
root.minsize(640, 480)

# 結果のフォント設定
result_font = font.Font(root, family=u"HGP行書体", size=40)

# テキストボックス1
txt1 = tkinter.Label(text="１つ目")
txt1.place(x=50, y=50)
entry1 = tkinter.Entry(width=64, bd=1)
entry1.place(x=100, y=50)
delete_btn1 = tkinter.Button(text="削除", width=10, bg="white")
delete_btn1.place(x=500, y=50)
delete_btn1["command"] = delete1
# テキストボックス2
txt2 = tkinter.Label(text="2つ目")
txt2.place(x=50, y=150)
entry2 = tkinter.Entry(width=64, bd=1)
entry2.place(x=100, y=150)
delete_btn2 = tkinter.Button(text="削除", width=10, bg="white")
delete_btn2.place(x=500, y=150)
delete_btn2["command"] = delete2

# 判定ボタン
judge_btn = tkinter.Button(text="判定する", width=40,height=3, bg="white")
judge_btn.place(x=160, y=225)
judge_btn["command"] = judge
# 結果
result = tkinter.Label(text="結果", font=result_font)
result.place(x=250, y=300)
root.mainloop()
