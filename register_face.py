import tkinter as tk
import os
import cv2 # type: ignore
from deepface import DeepFace # type: ignore
import json
import numpy as np
from dialogbox import dialogBox
import subprocess


DATA_DIR = "faces"
os.makedirs(DATA_DIR, exist_ok=True)

def backButtonClicked():
    root.destroy()
    subprocess.Popen(["python", "main_screen.py"])

def onEnterFaceButton(entries):
    root = tk.Tk()
    name = entries["Student Name"].get().strip()
    age = entries["Age"].get().strip()
    semester = entries["Semester"].get().strip()
    university = entries["University"].get().strip()
    program = entries["Program"].get().strip()
    sid = entries["SID"].get().strip()



    file_image_path = os.path.join(DATA_DIR, f"{name}.jpg")
    file_info_path = os.path.join(DATA_DIR, f"{name}.json")

    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            dialogBox("Failed to access camera")
            continue

        cv2.imshow("Register - Press 's' to save", frame)
        key = cv2.waitKey(1)

        if key & 0xFF == ord('s'):
            temp_capture_path = "temp_capture.jpg"
            cv2.imwrite(temp_capture_path, frame)

            already_registered = False
            for file in os.listdir(DATA_DIR):
                if file.endswith(".jpg"):
                    existing_face_path = os.path.join(DATA_DIR, file)
                    try:
                        result = DeepFace.verify(img1_path=temp_capture_path, img2_path=existing_face_path, enforce_detection=True)
                        if result["verified"]:
                            dialogBox(f"Face already registered as '{os.path.splitext(file)[0]}'. Registration aborted.")
                            already_registered = True
                            break
                    except Exception as e:
                        pass

            if already_registered:
                os.remove(temp_capture_path)
                break

            cv2.imwrite(file_image_path, frame)
            dialogBox(f"Face of '{name}' saved.")

            user_info = {
                "name": name,
                "age": age,
                "semester": semester,
                "university": university,
                "program": program,
                "SID": sid
            }
            with open(file_info_path, "w") as f:
                json.dump(user_info, f)


            # Remove temp capture image
            os.remove(temp_capture_path)
            break

        elif key & 0xFF == ord('q'):
            dialogBox("Registration cancelled.")
            break

    cam.release()
    cv2.destroyAllWindows()

#--------------------------------GUI------------------------------#

root = tk.Tk()
root.title("Register Face")
root.configure(bg="#424242")

# CENTER SCREEN
window_width = 800
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# STUDENT INFORMATION
form_frame = tk.Frame(root, bg="#424242")
form_frame.place(relx=0.5, rely=0.5, anchor="center")

fields = [
    ("Student Name", 0),
    ("SID", 1),
    ("Age", 2),
    ("University", 3),
    ("Program", 4),
    ("Semester", 5)
]

entries = {}

for label_text, row in fields:
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 20, "bold "), bg="#424242", fg="white")
    label.grid(column=0, row=row, padx=10, pady=10, sticky="e")

    entry = tk.Entry(form_frame, width=40, font=("Helvetica", 15, "bold "))
    entry.grid(column=1, row=row, padx=10, pady=10, ipady=5)
    entry.insert(0, "   ")


    entries[label_text] = entry 

enter_btn = tk.Button(form_frame,text="Enter Face",font=("Helvetica", 16, "bold"), bg="white", fg="#424242", width=20, command=lambda: onEnterFaceButton(entries= entries))
enter_btn.grid(column=0, row=len(fields), columnspan=2, pady=30)

back_btn = tk.Button(form_frame, text="Back", font=("Helvetica", 16, "bold"), bg="white", fg="#424242", width=20, command=lambda: backButtonClicked())
back_btn.grid(column=0, row=len(fields)+1, columnspan=2, pady=10)


root.mainloop()