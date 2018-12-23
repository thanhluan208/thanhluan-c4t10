from turtle import*

shape ("turtle")
color ("red")
a = int(input("nhập 1 số vào đây ^_^:"))
b = 360 // a
for i in range(a):
    forward(100)
    left(360//a)
mainloop()