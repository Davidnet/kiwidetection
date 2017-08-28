import os
import cv2
import time
import argparse

from utils import FPS, WebcamVideoStream
CWD_PATH = os.getcwd()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', dest='output_name', type=str,
                        default="output_recorded.avi", help='name of output file.')
    args = parser.parse_args()


    video_capture = WebcamVideoStream(src=0,
                                      width=480,
                                      height=360).start()
    fps = FPS().start()

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(args.output_name,fourcc, 20.0, (352, 288))
    while True:  # fps._numFrames < 120
        frame = video_capture.read()

        t = time.time()
        print('video output activates')
        cv2.imshow('Video', frame)
        out.write(frame)
        fps.update()

        print('[INFO] elapsed time: {:.2f}'.format(time.time() - t))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    fps.stop()
    print('[INFO] elapsed time (total): {:.2f}'.format(fps.elapsed()))
    print('[INFO] approx. FPS: {:.2f}'.format(fps.fps()))

    video_capture.stop()
    out.release()

    cv2.destroyAllWindows()
