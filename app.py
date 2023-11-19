#Writes all flask related codes in here
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
cv=pickle.load("models/cv.pkl")

@app.route('/', methods=['GET', 'POST'])
def home():
    text = ""
    if request.method == 'POST':
        text = request.form.get('email-content')
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)#block to ensure the server only runs if the script is executed directly #debug makes the upadations 
