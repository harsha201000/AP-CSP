#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    user_pass = ent_password.get()
    lbl_display.config(text=user_pass)
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("300x300")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:', font="Courier")
lbl_username.pack(padx=50, pady=10)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(padx=50, pady=10)

lbl_password = tk.Label(frame_login, text="Password:", font="Courier")
lbl_password.pack(padx=50, pady=10)

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(padx=50, pady=10)

btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack(padx=50, pady=10)

lbl_display = tk.Label(frame_auth, text="Password:", font="Arial")
lbl_display.pack(padx=5)

frame_login.tkraise()
root.mainloop()