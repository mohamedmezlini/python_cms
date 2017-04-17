import bson
import json 
import pymongo 
import os
import sys
from flask import Flask, request, render_template, url_for, redirect, send_file,flash, session, abort, make_response,url_for,jsonify
from werkzeug import secure_filename
app = Flask(__name__)
app.secret_key = 'aa100100'
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)


class User(UserMixin):
    def __init__(self, name, id, pwd, active=True):
        self.name = name
        self.id = id
        self.pwd = pwd
        self.active = active

    def is_active(self):
        return self.active

class Anonymous(AnonymousUser):
    name = u"Anonymous"

#***********************code ajoutee***************

#**************************************




USERS = {}

app.config.from_object(__name__)

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))


login_manager.setup_app(app)



@app.route("/login", methods=["GET", "POST"])
def login():
    
    x=[xx for xx in pymongo.MongoClient().site.users.find()]

    p=0
    for user in x:
    
        p=p+1
        USERS[p]=User(user["login"], int(user["id"]), user["pwd"])

    USER_logs = dict((u.name, u)  for u in USERS.itervalues())
    USER_pwd = dict((u.pwd, u) for u in USERS.itervalues())
    if request.method == "POST" and "login" in request.form and "pwd" in request.form:
        username = request.form["login"]
        password = request.form["pwd"]       
        if username in USER_logs:
            if login_user(USER_logs[username]) and login_user(USER_pwd[password]):
                return redirect(request.args.get("next") or url_for("index"))
    flash(u"Invalid username or password.")
    return render_template("log.html")
print USERS

@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(u"Please log in to access this page.")
    return redirect(url_for("index"))

#*******************************************************************************************************
@app.route("/")
def index():
    # la recherche dans la base de donn_ee de site dont son _id est essai
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"essai"})]#liste de site 
    site=site[0]# site[0] est un dictionnaire (json de site)

    return render_template("user.html",site=site, ang='', controll='')

@app.route("/main")
def index():
    # la recherche dans la base de donn_ee de site dont son _id est essai
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"essai"})]#liste de site 
    site=site[0]# site[0] est un dictionnaire (json de site)

    return render_template("user.html",site=site, ang='', controll='')


@app.route("/style")
@fresh_login_required
def administrateur():
    # la recherche dans la base de donn_ee de site dont son _id est essai
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"essai"})]#liste de site 
    site=site[0]# site[0] est un dictionnaire (json de site)
    return render_template("style.html",site=site, ang='ng-click=demo()', controll='ng-controller=change_style')
    

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template("log.html")


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/admin/verification', methods=['POST'])
def verification():

    if (request.form['login']=='mido' and request.form['pwd']=='aa100100'):
        session['login'] = request.form['login']
        session['logged'] = True
        return redirect("/modif")
    else:
        
        return redirect("/admin")    


@app.route('/modif', methods=['GET'])
def modifications():
    if session.has_key('logged'):
        liste= os.listdir('/home/benzina/exmple/templates/')
        return make_response(open('./templates/modification.html').read())
    else:
        abort(404)
        return redirect("/admin")



@app.route('/liste', methods=['GET'])
def liste():
    if session.has_key('logged'):

        liste= os.listdir('/home/benzina/exmple/templates/')
        print liste
        return render_template('liste.html', listes=liste)
    else:
        abort(404)
        return redirect("/admin")



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



@app.route('/save', methods=['POST'])
def save():
    
    with open("/home/benzina/exmple/static/sass/screen.scss", "rU") as myfile:
        liste = request.data
        for line in myfile:
            if liste.find(line) != -1 :
                print liste
                liste = liste.replace(line,"")
    with open("/home/benzina/exmple/static/sass/screen.scss", "a") as myfile:
        myfile.write(liste)
    
    return "Success"
    


if __name__ == '__main__':
    app.debug=True
    app.run()
