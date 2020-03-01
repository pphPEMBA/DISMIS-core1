#Create a file called hello.py

from flask import Flask
from flask import Flask, request, render_template
#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
return render_template('index.html')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pemba")
def pemba():
    #return "pemba"
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.106",port=5010) 


