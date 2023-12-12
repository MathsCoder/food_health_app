import os
from fastai.learner import load_learner
from flask import current_app

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def classify_image(image):
    """
    Classify an image using the fastai model.
    :param image:
    :return: string
    """
    learn = load_learner(f"{BASEDIR}/food_classifier_object.pkl")
    current_app.logger.info("Running image classifier")
    labels = learn.predict(image)[0]
    if labels:
        return labels[0].capitalize()
    else:
        return "Could not identify"
