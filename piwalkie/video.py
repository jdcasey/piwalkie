from tempfile import NamedTemporaryFile
import threading
import cv2
import imageio
import imutils
from pygifsicle import optimize

MUTEX = threading.Lock()

##############################################
# v4l2-ctl --list-devices
##############################################
#
# TODO: Make this configuration!
##############################################
DEVICE = 4
ROTATE = 90


def capture_gif(cfg):
    MUTEX.acquire()
    tf = NamedTemporaryFile('w+b', prefix='cam.', suffix='.gif', delete=False)
    cam = cv2.VideoCapture(DEVICE)

    with imageio.get_writer(tf.name, mode='I') as iw:
        for idx in range(60):
            ret_val, image = cam.read()

            if ROTATE > 0:
                image = imutils.rotate(image, ROTATE)

            if idx > 40:
                iw.append_data(image)

    optimize(tf.name)

    del cam
    MUTEX.release()
    return tf.name


def capture_png(cfg):
    MUTEX.acquire()
    cam = cv2.VideoCapture(DEVICE)
    ret_val, image = cam.read()

    if ROTATE > 0:
        image = imutils.rotate(image, ROTATE)

    tf = NamedTemporaryFile('w+b', prefix='cam.', suffix='.png', delete=False)
    cv2.imwrite(tf.name, image)

    del cam
    MUTEX.release()
    return tf.name


