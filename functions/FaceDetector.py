import os
import cv2 
import mediapipe as mp 
import time 
import face_recognition
import threading


class FaceDetector():
    def __init__(self, minDetectConf=0.5, faces_dir='faces'):
        self.minDetectConf = minDetectConf
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectConf)

        # Load multiple pictures and learn how to recognize them.
        self.known_face_encodings = []
        self.known_face_names = []
        for filename in os.listdir(faces_dir):
            if filename.endswith(".png") or filename.endswith(".jpg"): 
                image_path = os.path.join(faces_dir, filename)
                image = face_recognition.load_image_file(image_path)
                face_encoding = face_recognition.face_encodings(image)[0]
                self.known_face_encodings.append(face_encoding)
                # Use the filename without extension as the face name
                face_name = os.path.splitext(filename)[0]
                self.known_face_names.append(face_name)

        # Initialize threading
        self.face_locations = []
        self.face_encodings = []
        self.face_thread = None
        self.face_detected = False
        self.last_scan_time = time.time()
        
    def thread_stop(self):
        if self.face_thread is not None:
            self.face_thread.join()
            self.face_thread = None

    def find_faces(self, img):
        # Find all the faces and face encodings in the current frame of video
        self.face_locations = face_recognition.face_locations(img)
        self.face_encodings = face_recognition.face_encodings(img, self.face_locations)

    def findFaces(self, img, freq_scan=10, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        results = self.results
        bboxs = []
        if results.detections:
            for id, detection in enumerate(results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw: 
                    img = self.fancyDraw(img, bbox)    
                    cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 210, 0), 2)

                if not self.face_detected or time.time() - self.last_scan_time >= freq_scan:
                    self.last_scan_time = time.time()
                    # Wait for the previous face recognition thread to finish
                    if self.face_thread is not None:
                        self.face_thread.join()

                    # Start the face recognition thread for the next frame
                    self.face_thread = threading.Thread(target=self.find_faces, args=(imgRGB,))
                    self.face_thread.start()

                    face_found = False
                    for (top, right, bottom, left), face_encoding in zip(self.face_locations, self.face_encodings):
                        # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                        name = "Unknown"

                        # If a match was found in known_face_encodings, just use the first one.
                        if True in matches:
                            first_match_index = matches.index(True)
                            name = self.known_face_names[first_match_index]
                            face_found = True

                        # Draw a box around the face
                        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

                        # Draw a label with a name below the face
                        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                    self.face_detected = face_found
                else:
                    if len(results.detections) == 0:
                        self.face_detected = False
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=6, rt=1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        cv2.rectangle(img, bbox, (0, 255, 0), rt)
        cv2.line(img, (x, y), (x+l, y), (0, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (0, 0, 255), t)
        cv2.line(img, (x1, y), (x1-l, y), (0, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y+l), (0, 0, 255), t)
        return img