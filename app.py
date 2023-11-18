#Writes all flask related codes in here
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')#home route
def home():
    return render_template("index.html")
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)#block to ensure the server only runs if the script is executed directly #debug makes the upadations 
