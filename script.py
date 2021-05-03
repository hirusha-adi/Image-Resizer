from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()

def resize_png():
    wpng = int(eW.get())
    hpng = int(eH.get())
    imagepng = Image.open("image.png")
    img_png_new_resized = imagepng.resize((wpng, hpng))
    img_png_new_resized.save("resized.png")

def resize_jpg():
    wjpg = int(eW.get())
    hjpg = int(eH.get())
    imagejpg = Image.open("image.jpg")
    img_jpg_new_resized = imagejpg.resize((wjpg, hjpg))
    img_jpg_new_resized.save("resized.jpg")

def resize_jpeg():
    wjpeg = int(eW.get())
    hjpeg = int(eH.get())
    imagejpeg = Image.open("image.jpeg")
    img_jpeg_new_resized = imagejpeg.resize((wjpeg, hjpeg))
    img_jpeg_new_resized.save("resized.jpeg")

def exitp():
    window.quit()
    messagebox.showinfo('Made by ZeaCeR#5641', 'Thanks for using this program! Make sure to share!')

# variables
pversion = "V1.0"
pname = "Image Resizer"
pcreator = "ZeaCer#5641"
pline = " - "

# window properties
window.title("Image Resizer V1.0 - by ZeaCeR")
window['background'] = '#333333'
window.iconbitmap("icon.ico")

# entries
eW = Entry(window, width=35, borderwidth=5)
eH = Entry(window, width=35, borderwidth=5)

# labels main
lW = Label(window, text="Width: ", padx=3, fg="#FFFFFF", bg="#333333")
lH = Label(window, text="Height: ", padx=3, fg="#FFFFFF", bg="#333333")

# labels others
l1 = Label(window, text=pname + pline + pversion + pline + "by " + pcreator, fg="#FFFFFF", bg="#333333")
lgap = Label(window, text="                                   ", bg="#333333")
lgaptwo = Label(window, text="                                   ", bg="#333333")
lgapthree = Label(window, text="                                   ", bg="#333333")

# buttons
bConvertpng = Button(window, text="Resize .png", fg="#FFFFFF" ,bg="#FF5733", padx=40, pady=5, command=resize_png)
bConvertpjpg = Button(window, text="Resize .jpg", fg="#FFFFFF" ,bg="#FF5733", padx=40, pady=5, command=resize_jpg)
bConvertpjpeg = Button(window, text="Resize .jpeg", fg="#FFFFFF" ,bg="#FF5733", padx=40, pady=5, command=resize_jpeg)
bExitp = Button(window, text="Exit Program", fg="#FFFFFF" ,bg="red", padx=183, pady=5, command=exitp)

# canvas
canv = Canvas(window, width=440, height=300)

try:
    imgpng = ImageTk.PhotoImage(Image.open("image.png"))
    canv.create_image(10, 10, anchor=NW, image=imgpng)
except FileNotFoundError:
    imgjpg = ImageTk.PhotoImage(Image.open("image.jpg"))
    canv.create_image(10, 10, anchor=NW, image=imgjpg)
except FileNotFoundError:
    imgjpeg = ImageTk.PhotoImage(Image.open("image.jpeg"))
    canv.create_image(10, 10, anchor=NW, image=imgjpeg)

#location
# row 0
l1.grid(row=0, column=0, columnspan=3)
#row 1
canv.grid(row=1, column=0, columnspan=3)
# row 2
lgaptwo.grid(row=2, column=0, columnspan=3)
# row 3
lW.grid(row=3, column=0, sticky=E, columnspan=1)
eW.grid(row=3, column=1, columnspan=2)
# row 4
lH.grid(row=4, column=0, sticky=E, columnspan=1)
eH.grid(row=4, column=1, columnspan=2)
# row 5
lgap.grid(row=5, column=0, columnspan=2)
# row 6
lgapthree.grid(row=6, column=0, columnspan=2)
# row 7
bConvertpng.grid(row=7, column=0, columnspan=1)
bConvertpjpg.grid(row=7, column=1, columnspan=1)
bConvertpjpeg.grid(row=7, column=2, columnspan=1)
# row 8
bExitp.grid(row=8, column=0, columnspan=3)


window.mainloop()


