#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.scrolledtext as tksc

def test_my_button():
    user_pass = ent_password.get()
    lbl_display.config(text=user_pass)
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("400x200")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root, bg='azure2')
frame_login.grid(row=0, column=0, sticky="news")

frame_auth = tk.Frame(root, bg='plum4')
frame_auth.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:', bg='azure2')
lbl_username.pack(pady=5)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text="Password:", font="Arial", bg='azure2')
lbl_password.pack(padx=5)

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)

# Add this code before the code that creates your "Login" button
bt_image = tk.PhotoImage(file="button.gif") 
bt_image = bt_image.subsample(10,10) 

btn_login = tk.Button(frame_login, text="Login", image=bt_image, command=test_my_button, bg='azure2')
btn_login.pack(padx=175, pady=20)

lbl_display = tk.Label(frame_auth, text="Password:", font="Arial", bg='azure2')
lbl_display.pack(padx=5)

frame_login.tkraise()
test_textbox = tksc.ScrolledText(frame_auth)
test_textbox.configure(bg="mediumpurple3",font=("comic sans", 12), height=10, width=50)
test_textbox.pack()

root.mainloop()