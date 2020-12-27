import tkinter

mouse_x = 0
mouse_y = 0
click = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global click
    click = 1

def mouse_release(e):
    global click
    click = 0

def game_main():
    fnt = ("Times New Roman", 30)
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, click)
    cvs.delete("TEST")
    cvs.create_text(456,384,text=txt,fill="black", font=fnt,tag="TEST")
    root.after(100,game_main)

root = tkinter.Tk()
root.title("Mouse Check")
root.resizable(False, False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
game_main()
root.mainloop()
