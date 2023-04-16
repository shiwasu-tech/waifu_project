import cv2
import subprocess

#fpf means face per frame

face_cascade_path = '~~~~' ##カスケードファイルへのPATH
face_cascade = cv2.CascadeClassifier(face_cascade_path)



#VideoCaptureオブジェクト取得
cap = cv2.VideoCapture(-1) ##個々の数字は-1,0,1とか入れれば行ける。

print("start")

while(True):
    
    fpf = 0

    for i in range(10):
        
        #フレームを取得
        ret, frame = cap.read()
        
        if not ret:
            print("not capture")
            break
            
        #画面サイズを指定
        print(frame.shape)
        frame = cv2.resize(frame, (640, 480))
        frame2= cv2.resize(frame, (640, 480))
        
        #取得したフレームをウインドウ上に表示する
        #cv2.imshow("frame1", frame)
        
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print('got gray image')
        
        faces = face_cascade.detectMultiScale(frame_gray)
        
        
        if len(faces) > 0:
            fpf = fpf + 1
        else:
            print('no human detected')

        
        
        cv2.imshow("frame1", frame)
        
    if fpf > 6:
        print('human detected -> show oppen')
        subprocess.run(["cvlc","-f","--play-and-exit","~~~"]) ###再生動画のPATH
        cv2.waitKey(10000)
        
        
        
    #キーボード入力処理
    key = cv2.waitKey(1)
    if key == 13: #enterキーの場合処理を抜ける
        break
        
#カメラデバイスクローズ
cap.release()

#ウィンドウクローズ
cv2.destroyAllWindows()










































