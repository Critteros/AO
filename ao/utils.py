from keras.utils import load_img, img_to_array
import pickle
import numpy as np


class ImageRecognizer:
    class_names = ("Coast", "Desert", "Forest", "Glacier", "Mountain")

    def __init__(self, model_path):
        self.model = pickle.load(open(model_path, "rb"))

    def recognize(self, img_path):
        img = load_img(
            img_path,
            color_mode="rgb",
            target_size=(256, 256),
            interpolation="nearest",
            keep_aspect_ratio=True,
        )
        img_array = img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        pred = self.model.predict(img_batch)[0]
        pred_score = np.round(max(pred), 2)
        pred_class = self.class_names[np.argmax(pred)]
        return pred_class, pred_score
