from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
import yaml, os, socket

""" Importing profile.py path """
#from Core.profile import temporaryfiles, *
#profile = open(profile_path)
profile = open('/home/d-slave1/d1_SuperDismis/Dismis_Home_Automation/SystemService/APIs/profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()
host_ip= profile_data['host_ip']
login_id_path=profile_data['login_id_path']

directory = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#print(directory)
template_dir = os.path.join(directory, 'SystemService/credentialsFlask/templates/')
static_dir = os.path.join(directory, 'SystemService/credentialsFlask/static/')
app = Flask(__name__, template_folder=template_dir, static_url_path=static_dir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + login_id_path
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/citizenshipInfo",methods=["GET", "POST"])
def citizenshipInfo_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('citizenship_QR.html')
    return render_template("login.html")

@app.route("/login/backupCodePersonalMail",methods=["GET", "POST"])
def backupCodePersonalMail_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('backupcodePersonalMail_QR.html')
    return render_template("login.html")


@app.route("/login/folderlockpassInfo",methods=["GET", "POST"])
def folderlockpasswd_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('folderlockpasswd_QR.html')
    return render_template("login.html")

@app.route("/login/internetAccInfo",methods=["GET", "POST"])
def internetAcc_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('internetAcc_QR.html')
    return render_template("login.html")


@app.route("/login/otherGmailInfo",methods=["GET", "POST"])
def otherGmail_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('otherGmail_QR.html')
    return render_template("login.html")

@app.route("/login/passwd-GInfo",methods=["GET", "POST"])
def passwd_G_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('passwd-G_QR.html')
    return render_template("login.html")


@app.route("/login/payeerInfo",methods=["GET", "POST"])
def payeer_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('payeer_QR.html')
    return render_template("login.html")

@app.route("/login/payoneerInfo",methods=["GET", "POST"])
def payoneer_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('payoneer_QR.html')
    return render_template("login.html")

@app.route("/login/personalGmailInfo",methods=["GET", "POST"])
def personalGmail_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('personalGmail_QR.html')
    return render_template("login.html")

@app.route("/login/twillioInfo",methods=["GET", "POST"])
def twillio_site():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return render_template('twillio_QR.html')
    return render_template("login.html")


""" running credentialsFlask """
try:
    db.create_all()
    print(' ')
    print(' ')
    print('--- Flask Is Running!! ---')
    app.run(debug=True,host='192.168.1.106')
except OSError:
    print('--- Requested Address Already Assign!! ---')
    print(' ')
    print(' ')
except socket.gaierror:
    pass
 