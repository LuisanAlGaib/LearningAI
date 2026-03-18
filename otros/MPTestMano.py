
import cv2
import mediapipe as mp

print(cv2.__version__)

width=640
height=480
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

handsTracking = mp.solutions.hands.Hands(static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

drawMarks = mp.solutions.drawing_utils
while True:
    ret, frame= capture.read()
    
    
    if ret==True:
        frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = handsTracking.process(frameRGB)
        print(results)
        handsMarks=[]
        
        if results.multi_hand_landmarks != None:
            for hands in results.multi_hand_landmarks:
                handMarks = []
                drawMarks.draw_landmarks(frame,hands, mp.solutions.hands.HAND_CONNECTIONS)
                for marks in hands.landmark:
                    handMarks.append((int(marks.x*width),int(marks.y*height)))
                print(' ')
                #print(handMarks)
                cv2.circle(frame, handMarks[20], 10, (0,0,0), -1)
                handsMarks.append(handMarks)
                print(handsMarks)
                print(' ')
    
        cv2.imshow('Original', frame)
        
        key = cv2.waitKey(5)

        if key == ord('q'): 
            break
    else:
        print('error')
        break
capture.release()
cv2.destroyAllWindows()