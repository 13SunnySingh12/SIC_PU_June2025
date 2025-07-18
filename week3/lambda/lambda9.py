import tkinter as tk

root = tk.Tk()
root.title("Lambda Button Example")

# Button that prints a custom message
tk.Button(root, text="Say Hello", command=lambda: print("Hello from lambda!")).pack()

root.mainloop()
