import tkinter as tk
from dialogbox import dialogBox
import subprocess
import cv2 # type: ignore
from deepface import DeepFace # type: ignore
import os



#------------------------------Login Admin Function(with username and password)--------------------------------#
def loginAdmin(entries):
    userName = entries["Username"].get().strip()
    password = entries["Password"].get().strip()
    while True:
        if userName == "KHUBAIB":
            if password == "15045":
                root.destroy()
                subprocess.Popen(["python", "main_screen.py"])
                break
            else:
                dialogBox("Wrong password")
                break
        else:
            dialogBox("Wrong Username")
            break



#------------------------------Admin Face Login Function--------------------------------#
def onEnterFaceButton():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        dialogBox("Camera not accessible.")
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            dialogBox("Failed to access camera")
            break

        try:
            faces = DeepFace.extract_faces(frame, enforce_detection=False)
        except:
            faces = []

        for face_info in faces:
            facial_area = face_info["facial_area"]
            xmin, ymin = facial_area["x"], facial_area["y"]
            width, height = facial_area["w"], facial_area["h"]
            xmax, ymax = xmin + width, ymin + height

            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        cv2.imshow("Press 's' to take picture, 'q' to quit", frame)
        key = cv2.waitKey(1)

        if key & 0xFF == ord('s'):
            temp_admin_path = "temp_admin_capture.jpg"
            cv2.imwrite(temp_admin_path, frame)

            try:
                result = DeepFace.verify(
                    img1_path=temp_admin_path,
                    img2_path=r"C:\Users\jawad\OneDrive\Desktop\AI PROJECT NEW\admininfo\KHUBAIB NAEEM.jpg",
                    enforce_detection=True
                )
                if result["verified"]:
                    os.remove(temp_admin_path)
                    root.destroy()
                    subprocess.Popen(["python", "main_screen.py"])
                    break
                else:
                    dialogBox("Wrong Person")
                    os.remove(temp_admin_path)
            except Exception as e:
                dialogBox(f"Face verification failed: {str(e)}")
                os.remove(temp_admin_path)

        elif key & 0xFF == ord('q'):
            dialogBox("Verification cancelled.")
            break

    cam.release()
    cv2.destroyAllWindows()

#------------------------------Exit Program Function--------------------------------#
def exitButtonClicked():
    root.destroy()





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


form_frame = tk.Frame(root, bg="#424242")
form_frame.place(relx=0.5, rely=0.5, anchor="center")

fields = [
    ("Username", 0),
    ("Password", 1)
]

entries = {}

for label_text, row in fields:
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 20, "bold "), bg="#424242", fg="white")
    label.grid(column=0, row=row, padx=10, pady=10, sticky="e")

    entry = tk.Entry(form_frame, width=40, font=("Helvetica", 15, "bold "))
    entry.grid(column=1, row=row, padx=10, pady=10, ipady=5)
    entry.insert(0, "   ")

    entries[label_text] = entry


login_btn = tk.Button(form_frame, text="LOGIN", font=("Helvetica", 16, "bold"), bg="white", fg="#424242", width=20, command=lambda: loginAdmin(entries=entries))
login_btn.grid(column=0, row=len(fields), columnspan=2, pady=10) 

enter_btn = tk.Button(form_frame,text="Face Login",font=("Helvetica", 16, "bold"), bg="white", fg="#424242", width=20, command=lambda: onEnterFaceButton())
enter_btn.grid(column=0, row=len(fields)+1, columnspan=2, pady=30)

exit_btn = tk.Button(form_frame, text="Exit", font=("Helvetica", 16, "bold"), bg="white", fg="#424242", width=20, command=lambda: exitButtonClicked())
exit_btn.grid(column=0, row=len(fields)+2, columnspan=2, pady=10) 

root.mainloop()