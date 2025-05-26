import tkinter as tk
import subprocess
from search_face import searchFace


def registerFaceButtonClick():
    global root
    root.destroy()
    subprocess.Popen(["python", "register_face.py"])

def searchFaceButtonClick():
    searchFace()

def deleteFaceButtonClick():
    global root
    root.destroy()
    subprocess.Popen(["python", "delete_face.py"])

def logoutProgramButtonClicked():
    global root
    root.destroy()
    subprocess.Popen(["python", "admin_login_screen.py"])

    
def mainContent():
    global root
    root = tk.Tk()
    root.title("Main Screen")
    root.configure(bg="#424242")
    root.title("Main Screen")
    root.configure(bg="#424242")

    window_width = 800
    window_height = 800

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    regiterFaceButton  = tk.Button(root, text= "REGISTER FACE", command=registerFaceButtonClick, width=15, font=("Helvetica", 20, "bold underline"), bg="white", fg="#424242")
    regiterFaceButton.pack(pady = 20)
    regiterFaceButton.place(relx=0.5, rely=0.3, anchor="center")

    searchFaceButton = tk.Button(root, text= "SEARCH FACE", command=searchFaceButtonClick, width=15, font=("Helvetica", 20, "bold underline"), bg="white", fg="#424242")
    searchFaceButton.pack(pady = 20)
    searchFaceButton.place(relx=0.5, rely=0.4, anchor="center")

    DeleteFaceButton = tk.Button(root, text= "DELETE FACE", command=deleteFaceButtonClick, width=15, font=("Helvetica", 20, "bold underline"), bg="white", fg="#424242")
    DeleteFaceButton.pack(pady = 20)
    DeleteFaceButton.place(relx=0.5, rely=0.5, anchor="center")

    logoutButton = tk.Button(root, text= "Logout", command=logoutProgramButtonClicked, width=15, font=("Helvetica", 20, "bold underline"), bg="white", fg="#424242")
    logoutButton.pack(pady = 20)
    logoutButton.place(relx=0.5, rely=0.6, anchor="center")

    root.mainloop()


if __name__ == "__main__":
    mainContent()