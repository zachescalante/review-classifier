import os
import json
import pickle
import numpy as np
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
import tensorflow as tf
from keras.models import load_model
from keras_preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences

model = load_model(os.path.join(os.getcwd(), 'app/lstm_amzn_rvw.h5'))

with open('app/tokenizer.json', 'rb') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

global graph
graph = tf.get_default_graph()

class TextFormatting(FlaskForm):

    def __init__(self):
        self.MAX_SEQUENCE_LENGTH = 500
        self.tokenizer = tokenizer
        self.labels = [1, 2, 3, 4, 5]
        self.messages = {5: 
                {
                    1: "Keep making customers happy and your board will be also!",
                    2: "Wake up. Brush teeth. Eat Excellence.",
                    3: "The name's Class - World Class."
                    },
                4:
                {
                    1: "Solid product. Happy customer.",
                    2: "Who gives a 4-star review? Just make it a 5 already!",
                    3: "Seems we lost a star somewhere along the way."
                    },
                3:
                {
                    1: "C's get degrees!",
                    2: "When was the last time you heard the term 'milquetoast'?",
                    3: "Mediocrity by any other name would still stink."
                    },
                2:
                {
                    1: "I got a D once too (this is a half-truth).",
                    2: "Let's just blame this on a hangry reviewer.",
                    3: "Looks like my Uber rating."
                    },
                1:
                {
                    1: "Terrible. Awful. No good. Very bad.",
                    2: "Perhaps the package didnt't have the product in it?",
                    3: "Market Share? I think we had that back in '88."
                    }         
                }

        def textAnalytics(self, text):
            return text.upper()

    def predict(self, text):
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=self.MAX_SEQUENCE_LENGTH)
        with graph.as_default():
            pred = model.predict(padded)
        return pred, self.labels[np.argmax(pred)] 
