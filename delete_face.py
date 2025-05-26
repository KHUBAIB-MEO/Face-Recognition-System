import tkinter as tk
import os
import json
from dialogbox import dialogBox
import subprocess

DATA_DIR = "faces"

def backButtonClicked():
    root.destroy()
    subprocess.Popen(["python", "main_screen.py"])



def delete_face_by_sid(sid):
    found = False
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            json_path = os.path.join(DATA_DIR, file)
            try:
                with open(json_path, "r") as f:
                    data = json.load(f)
            except:
                continue

            if data.get("SID", "").strip() == sid:
                name = os.path.splitext(file)[0]
                image_path = os.path.join(DATA_DIR, f"{name}.jpg")

                if os.path.exists(image_path):
                    os.remove(image_path)

                os.remove(json_path)
                dialogBox(f"Student '{data.get('name')}' deleted successfully.")
                found = True
                break

    if not found:
        dialogBox("Student not found.")

def on_delete_button():
    sid = sid_entry.get().strip()
    if sid == "":
        dialogBox("Please enter a SID.")
    else:
        delete_face_by_sid(sid)

# Tkinter GUI
root = tk.Tk()
root.title("Delete Face by SID")
root.configure(bg="#424242")

window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

title_label = tk.Label(root, text="Delete Student Face", font=("Helvetica", 20, "bold"), bg="#424242", fg="white")
title_label.pack(pady=20)

sid_label = tk.Label(root, text="Enter SID:", font=("Helvetica", 16), bg="#424242", fg="white")
sid_label.pack()

sid_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
sid_entry.pack(pady=10)

delete_btn = tk.Button(root, text="Delete", font=("Helvetica", 14, "bold"), bg="white", fg="#424242", command=lambda: on_delete_button())
delete_btn.pack(pady=20)

back_btn = tk.Button(root, text="Back", font=("Helvetica", 14, "bold"), bg="white", fg="#424242", command=lambda: backButtonClicked())
back_btn.pack(pady=20)

root.mainloop()
