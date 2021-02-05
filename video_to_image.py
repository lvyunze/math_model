import cv2


def getFrame(videoPath, svPath):
    cap = cv2.VideoCapture(videoPath)
    numFrame = 0
    while True:
        if cap.grab():
            flag, frame = cap.retrieve()
            if not flag:
                continue
            else:
                #cv2.imshow('video', frame)
                numFrame += 1
                newPath = svPath + str(numFrame) + ".jpg"
                cv2.imencode('.jpg', frame)[1].tofile(newPath)
        if cv2.waitKey(10) == 27:
            break


if __name__ == '__main__':
    videoPath='one.mp4'
    savePicturePath='./pic/'
    getFrame(videoPath,savePicturePath)