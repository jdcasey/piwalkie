from tempfile import NamedTemporaryFile
import cv2
import imageio

def capture_gif(cfg):
    tf = NamedTemporaryFile('w+b', prefix='cam.', suffix='.gif', delete=False)
    cam = cv2.VideoCapture(0)

    with imageio.get_writer(tf.name, mode='I') as iw:
        for idx in range(20):
            ret_val, image = cam.read()
            iw.append_data(image)

    del(cam)
    return tf.name

def capture_png(cfg):
    cam = cv2.VideoCapture(0)
    ret_val, image = cam.read()

    tf = NamedTemporaryFile('w+b', prefix='cam.', suffix='.png', delete=False)
    cv2.imwrite(tf.name, image)

    del(cam)
    return tf.name


