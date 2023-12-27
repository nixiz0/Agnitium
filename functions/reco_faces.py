import cv2 
import time 
from tkinter import ttk, simpledialog, messagebox

from functions.FaceDetector import FaceDetector


def start_reco_faces(num_cam, freq_scan=10, showFPS=True):
    cap = cv2.VideoCapture(num_cam)
    if not cap.isOpened():
        messagebox.showerror("Error", "Camera not found")
        return
    pTime = 0
    detector = FaceDetector()
    while True: 
        success, img = cap.read()
        img, bboxs = detector.findFaces(img, freq_scan)
    
        if showFPS:
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'{int(fps)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 210, 0), 3)
            
        cv2.imshow("Faces Recognition (press space to exit)", img)
        if cv2.waitKey(1) == 32:
            detector.thread_stop()
            cap.release()
            cv2.destroyAllWindows()
            break