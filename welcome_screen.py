import tkinter as tk
import subprocess

def goToAdminScreen():
    root.destroy()
    subprocess.Popen(["python", "admin_login_screen.py"])

root = tk.Tk()
root.title("Welcome Screen")
root.configure(bg="#424242")

window_width = 800
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label = tk.Label(root, text="Welcome to Face Recognition system", font=("Helvetica", 20, "bold underline"), bg="#424242", fg="white")
label.pack(expand=True)

root.after(1000, goToAdminScreen)
root.mainloop()