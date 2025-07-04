from flask import Flask, render_template, request

appy = Flask(__name__)

@appy.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@appy.route('/', methods=['POST'])
def detect_accessibility():
    website_link = request.form['websiteLink']
