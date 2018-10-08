from cv2 import cv2
import glob


def video2img():
    vc = cv2.VideoCapture('./1.avi')
    c = 0
    rval = vc.isOpened()

    while rval:
        c = c + 1
        rval, frame = vc.read()
        if rval:
            cv2.imwrite('img/'+str(c) + '.jpg', frame)
            cv2.waitKey(1)
        else:
            break
    vc.release()


def img2video():
    fps = 20
    img = cv2.imread('./1.jpg') # 先读一张图片确定视频的宽高
    height, width, _ = img.shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    videoWriter = cv2.VideoWriter(
        'savedVideo.avi', fourcc, fps, (width, height))
    imgs = glob.glob('./*.jpg')
    for imgname in imgs:
        frame = cv2.imread(imgname)
        videoWriter.write(frame)
    videoWriter.release()
