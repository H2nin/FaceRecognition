import cv2
import face_recognition
import tkinter as tk
from tkinter import filedialog, messagebox

# Load known face (Rory)
rory_image = face_recognition.load_image_file("images/rory.jpg")
rory_encoding = face_recognition.face_encodings(rory_image)[0]

# Known face database
known_face_encodings = [rory_encoding]
known_face_names = ["Rory"]

def recognize_face():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        return

    # Load selected image
    unknown_image = face_recognition.load_image_file(file_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    if len(unknown_encodings) == 0:
        messagebox.showerror("Error", "No face found in the image!")
        return

    unknown_encoding = unknown_encodings[0]

    # Compare with known face
    results = face_recognition.compare_faces(known_face_encodings, unknown_encoding)
    name = "Unknown"

    if True in results:
        name = known_face_names[0]

    # Show result
    messagebox.showinfo("Result", f"Detected Face: {name}")

# GUI
root = tk.Tk()
root.title("Face Recognition App")
root.geometry("300x200")

label = tk.Label(root, text="Face Recognition Using OpenCV", font=("Arial", 12))
label.pack(pady=20)

choose_button = tk.Button(root, text="Choose Image", command=recognize_face, width=20, height=2)
choose_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, width=20, height=2)
exit_button.pack(pady=10)

root.mainloop()