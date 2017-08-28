import cv2
import urllib.request
import numpy as np

stream = urllib.request.urlopen('http://1.tcp.ngrok.io:21650/stream/video.mjpeg')
stream_bytes = bytes()


while True:
    stream_bytes += stream.read(1024)
    a = stream_bytes.find(b'\xff\xd8')
    b = stream_bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = stream_bytes[a:b+2]
        stream_bytes = stream_bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('i', i)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
            exit(0)
