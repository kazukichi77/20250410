import tkinter as tk

def say_hello():
    print("こんにちは!")

#ウインドウの作成
root = tk. Tk()
root.title("タイトル")
root.geometry("400x300")

label = tk.Label(root, text="こんにちは")
label.pack()

button = tk.Button(root, text="クリック", command=say_hello)
button.pack()

root.mainloop()

