from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("360x480")

root.resizable(False, False)

display = Entry(root)
display.grid(row=0, column=0, columnspan=4)

def btn_mul_cmd():
    display.insert(END, "*")

def btn_div_cmd():
    display.insert(END, "/")

def btn_rem_cmd():
    display.insert(END, "%")

def btn_delA_cmd():
    display.delete(0, END)

# btn row 1
btn_mul = Button(root, width=10, text="*", command=btn_mul_cmd)
btn_mul.grid(row=1, column=0)

btn_div = Button(root, width=10, text="/", command=btn_div_cmd)
btn_div.grid(row=1, column=1)

btn_rem = Button(root, width=10, text="%", command=btn_rem_cmd)
btn_rem.grid(row=1, column=2)

btn_delA = Button(root, width=10, text="C", command=btn_delA_cmd)
btn_delA.grid(row=1, column=3)

# btn row 2
def btn_num_cmd_1():
    display.insert(END, "1")

def btn_num_cmd_2():
    display.insert(END, "2")

def btn_num_cmd_3():
    display.insert(END, "3")

def btn_plus_cmd():
    display.insert(END, "+")

btn_num_1 = Button(root, width=10, text="1", command=btn_num_cmd_1)
btn_num_1.grid(row=2, column=0)

btn_num_2 = Button(root, width=10, text="2", command=btn_num_cmd_2)
btn_num_2.grid(row=2, column=1)

btn_num_3 = Button(root, width=10, text="3", command=btn_num_cmd_3)
btn_num_3.grid(row=2, column=2)

btn_plus = Button(root, width=10, text="+", command=btn_plus_cmd)
btn_plus.grid(row=2, column=3)

# btn row 3
def btn_num_cmd_4():
    display.insert(END, "4")

def btn_num_cmd_5():
    display.insert(END, "5")

def btn_num_cmd_6():
    display.insert(END, "6")

def btn_min_cmd():
    display.insert(END, "-")

btn_num_4 = Button(root, width=10, text="4", command=btn_num_cmd_4)
btn_num_4.grid(row=3, column=0)

btn_num_5 = Button(root, width=10, text="5", command=btn_num_cmd_5)
btn_num_5.grid(row=3, column=1)

btn_num_6 = Button(root, width=10, text="6", command=btn_num_cmd_6)
btn_num_6.grid(row=3, column=2)

btn_min = Button(root, width=10, text="+", command=btn_min_cmd)
btn_min.grid(row=3, column=3)

# btn row 4
def btn_num_cmd_7():
    display.insert(END, "7")

def btn_num_cmd_8():
    display.insert(END, "8")

def btn_num_cmd_9():
    display.insert(END, "9")

btn_num_7 = Button(root, width=10, text="7", command=btn_num_cmd_7)
btn_num_7.grid(row=4, column=0)

btn_num_8 = Button(root, width=10, text="8", command=btn_num_cmd_8)
btn_num_8.grid(row=4, column=1)

btn_num_9 = Button(root, width=10, text="9", command=btn_num_cmd_9)
btn_num_9.grid(row=4, column=2)

def btn_result_cmd():
    equ = display.get() # 수식 문자열을 저장
    print(equ)
    result = eval(equ) # 수식 문자열을 계산해주는 eval() 함수
    print(result)
    display.delete(0, END) # 입력된 수식의 결과값을 출력하기 위해 화면 초기화
    display.insert(0, result) # 결과값을 화면에 출력

btn_result = Button(root, width=10, text="=", command=btn_result_cmd)
btn_result.grid(row=4, column=3, rowspan=1)

# btn row 5
def btn_num_cmd_0():
    display.insert(END, "0")

btn_num_0 = Button(root, width=10, text="0", command=btn_num_cmd_0)
btn_num_0.grid(row=5, column=0, columnspan=2, sticky=W+E+N+S)

root.mainloop()
