import cv2
#Load the trained data 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image
#img = cv2.imread('test_face.jpg')

#webcam real time detection
webcam = cv2.VideoCapture(0)

#convert to grayscale
#grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#loop cuz loop is cool and fixes shit
while True:

    #make that dumbas read the frame
    successful_frame_read, frame = webcam.read()
       
    #convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #detect faces
    face_coords = trained_face_data.detectMultiScale(grayscaled_img)
    
    #draw da square
    for  (x, y, w, h) in face_coords:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (240, 210, 101), 2)
    
    cv2.imshow('cool face detection lol', frame)
    key = cv2.waitKey(1)
    
    #stop that shit if q is presed
    if key==81 or key==113:
        break
        cv2.destroyAllWindows()
