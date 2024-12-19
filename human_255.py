import cv2
import numpy as np
import math
from tkinter import Tk, Label
from tkinter.ttk import Button, Combobox, LabelFrame
from PIL import Image, ImageTk
import os

def process_image():

    p = int(combo_p.get())

    filepath = os.path.join(os.getcwd(), "human.jpg") 
    if not os.path.exists(filepath):
        label_message.config(text="image is not find or error in opening", foreground="red")
        return

    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if image is None:
        label_message.config(text="error in read", foreground="red")
        return

    width, height = image.shape
    arr=int(math.sqrt(p))
    fi=int((arr-1)/2)
    en=fi+1
    kernel = np.full((arr, arr), 1 / p)

    result = np.zeros((width, height), dtype=np.uint8)

    for i in range(fi, width - fi):
        for j in range(fi, height - fi):
            small_image = image[i - fi:i + en , j - fi:j + en]
            output = np.multiply(small_image, kernel)
            out = np.sum(output)
            result[i, j] = out

    result_image = Image.fromarray(result)
    result_image_tk = ImageTk.PhotoImage(result_image)

    label_image.config(image=result_image_tk)
    label_image.image = result_image_tk
    label_message.config(text="ok", foreground="green")


root = Tk()
root.title("filter image")

frame_controls = LabelFrame(root, text="option")
frame_controls.pack(pady=10, padx=10, fill="x")

Label(frame_controls, text="enter p").grid(row=0, column=0, padx=5, pady=5)
combo_p = Combobox(frame_controls, values=[9, 25, 49, 225], state="readonly")
combo_p.grid(row=0, column=1, padx=5, pady=5)
combo_p.set(9) 

button_process = Button(frame_controls, text="process image", command=process_image)
button_process.grid(row=0, column=2, padx=5, pady=5)

label_message = Label(root, text="")
label_message.pack(pady=5)

label_image = Label(root)
label_image.pack(pady=10)

root.mainloop()

