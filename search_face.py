from deepface import DeepFace  # type: ignore
import cv2  # type: ignore
import os
import sys
import json
import contextlib
from dialogbox import dialogBox

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

@contextlib.contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def searchFace():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            dialogBox("Failed to access camera")
            continue

        with suppress_stdout():
            try:
                faces = DeepFace.extract_faces(frame, enforce_detection=False)
            except:
                faces = []

        for face_info in faces:
            facial_area = face_info["facial_area"]
            xmin, ymin = facial_area["x"], facial_area["y"]
            width, height = facial_area["w"], facial_area["h"]
            xmax, ymax = xmin + width, ymin + height

            cropped_face = frame[ymin:ymax, xmin:xmax]

            with suppress_stdout():
                try:
                    result = DeepFace.find(img_path=cropped_face, db_path="./faces", enforce_detection=False, model_name="ArcFace")
                except:
                    result = []

            if len(result) > 0 and len(result[0]['identity']) > 0:
                identity_path = result[0]['identity'][0]
                filename = os.path.basename(identity_path)
                name_without_ext = os.path.splitext(filename)[0]

                color = (0, 255, 0)
                json_path = os.path.join("faces", name_without_ext + ".json")

                info_lines = [f"Name: {name_without_ext}"]
                if os.path.exists(json_path):
                    with open(json_path, "r") as f:
                        data = json.load(f)
                    info_lines = [
                        f"Name: {data.get('name', '').strip()}",
                        f"Age: {data.get('age', '').strip()}",
                        f"Semester: {data.get('semester', '').strip()}",
                        f"University: {data.get('university', '').strip()}",
                        f"Program: {data.get('program', '').strip()}"
                    ]
            else:
                color = (0, 0, 255)
                info_lines = ["No Match"]

            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 1)
            for i, text in enumerate(info_lines):
                y_offset = ymin - 10 + (i * 20)
                cv2.putText(frame, text, (xmin, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        cv2.imshow("Search Face", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    searchFace()