import tkinter as tk

window = tk.Tk()

window.geometry("1280x720")

T1 = tk.Text(window)
#T1.place(x=0, y=300, height=20, width=250)
#T1.insert("0.0", "Champion you want to pick")



frame = tk.Frame(master=window, width=1280, height=720, bg="blue")
frame.pack()

T1.tag_configure("center", justify='center')
T1.tag_add("center", "1.0", "end")
T1.pack(side="top")

label1 = tk.Label(master=frame, text="League of legend auto-picker by Memetelve", size='20')
#label1.tag_configure("center", justify='center')
#label1.tag_add("center", "1.0", "end")
label1.pack()

button = tk.Button(
    window, justify='center',
    text="Start!",
    width=26,
    height=5,
    bg="blue",
    fg="yellow",
)














window.mainloop()