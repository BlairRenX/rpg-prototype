from tkinter import *


def hollowSquare(C, x1, x2, y1, y2):
    blackSquare = C.create_polygon(x1, y1, x1, y2, x2, y2, x2, y1)
    line1 = C.create_line(x1, y1, x1, y2, fill="#22ee22", width=3)
    line2 = C.create_line(x1, y1, x2, y1, fill="#22ee22", width=3)
    line3 = C.create_line(x1, y2, x2, y2, fill="#22ee22", width=3)
    line4 = C.create_line(x2, y1, x2, y2, fill="#22ee22", width=3)

root = Tk()
root.geometry("620x600")

# Now width and height are in pixels. They are not now the number of columns and the number of lines respectively
#Text2(root, width=600,height=600).pack()

C = Canvas(root, bg="#000000", width = 600, height = 600)
C.place(x=0,y=0)


lines = []
for i in range(60):
    lines.append(C.create_line(10*i, 0, 10*i, 600, fill="#22ee22"))
    lines.append(C.create_line(0, 10*i, 600, 10*i, fill="#22ee22"))

x = 300
y = x + 100

#square = C.create_polygon(x, x, x, y, y, y, y, x, fill="#22ee22")
hollowSquare(C, 150, 300, 150, 300)


##coord = 10, 50, 240, 210
##arc = C.create_arc(coord, start=0, extent=150, fill="blue", outline="blue")


root.mainloop()
