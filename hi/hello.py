from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("375x667")
window.configure(bg = "#5aebad")
canvas = Canvas(
    window,
    bg = "#5aebad",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 90, y = 534,
    width = 190,
    height = 49)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    189.0, 251.5,
    image=background_img)




window.resizable(False, False)
window.mainloop()
