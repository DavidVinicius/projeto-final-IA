from flask import Flask, render_template, request, jsonify
from io import BytesIO
import re, time, base64
from PIL import Image, ImageFile
import os

import numpy as np
from sklearn.externals import joblib


app = Flask(__name__)
model = joblib.load('model/model_KERAS_MNIST.pkl')

# Setting this up here does not do anything
app.config.update({'TEMPLATES_AUTO_RELOAD': True})
# Neither does this:
app.templates_auto_reload = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():    
    s   = request.json.get("img")        
    img = getI420FromBase64(s)            
    print(img)
    return jsonify(1)


def getI420FromBase64(codec):
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    threshold = 100
    img = Image.open(image_data)       
    im  = img.convert("L")    
    im  = im.resize((50, 50), Image.ANTIALIAS)
    im.save('temp.png', "PNG")
    t  = list(map(lambda x: int(x), list(im.getdata())))
    t  = np.divide(t, 255)
    return np.array(t)

def recognize(index):
    if index == 1:
        return "Retângulo"
    elif index == 0:
        return "Elipse"
    return "Não reconhecido"
