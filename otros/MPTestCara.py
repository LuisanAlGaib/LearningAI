
import cv2
import mediapipe as mp

print(cv2.__version__)

width=640
height=480
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

detectionFace = mp.solutions.face_detection.FaceDetection()
drawFace = mp.solutions.drawing_utils
while True:
    ret, frame= capture.read()
    
    
    if ret==True:
        frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = detectionFace.process(frameRGB)
        print(results.detections)
        
        
        if results.detections != None:
            for face in results.detections:
                drawFace.draw_detection(frame,face)
                box = face.location_data.relative_bounding_box
                topLeft = (int(box.xmin*width),int(box.ymin*height))
                bottomRight = (int((box.xmin+box.width)*width),int((box.ymin+box.height)*height))
                cv2.rectangle(frame, topLeft,bottomRight,(255,255,255),3)
    
        cv2.imshow('Original', frame)
        
        key = cv2.waitKey(5)

        if key == ord('q'): 
            break
    else:
        print('error')
        break
capture.release()
cv2.destroyAllWindows()