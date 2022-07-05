import tensorflow as tf
import cv2


def get_prediction(imgName):
    loaded_model = tf.keras.models.load_model('./model.h5')
    image = cv2.imread(imgName)

    image = cv2.resize(image, (150, 150))
    img0 = (image.reshape(1, 150, 150, 3).astype("float32")) / 255  # 归一化
    predict = loaded_model.predict(img0)
    predict = 1 if predict[0][0] > 0.5 else 0
    return predict
