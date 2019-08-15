# Basic python libraries
import os
import json
import pickle
import numpy as np
from random import randint
# App import packages
from app import app
from app.graphs import GraphFunction
from app.forms import LoginForm, TextInput, Prediction
from app.functions import TextFormatting
# keras deep learning packages
from keras.models import load_model
from keras_preprocessing.text import tokenizer_from_json
# Flask packages
from flask import render_template, flash, redirect, url_for, request

# @app.route('/')
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for user {}, remeber_me={}'.format(form.username.data, form.remember_me.data))
#        return redirect(url_for('index'))
#    return render_template('login.html', title='Sign In', form=form)

@app.route('/', methods=['GET', 'POST'])
def textInput():
    text = TextInput()
    output = TextFormatting()
    probs = Prediction()
    if text.validate_on_submit():
        formatted_text = output.predict(text.body.data)
        flash(output.messages[formatted_text[1]][randint(1,3)])
        # probs.message = output.messages[formatted_text[1]][randint(1,3)]
        probs.values = formatted_text[0][0].tolist()
        probs.index = np.argsort(np.argsort(formatted_text[0][0])).tolist()
        render_template('base.html', text=text, probs=probs)
        # return redirect(url_for('textInput'))
    else:
        print(text.errors)
    return render_template('text.html', title='Amazon Review', text=text, probs=probs)
