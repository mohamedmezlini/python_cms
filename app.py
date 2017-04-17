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
    def __init__(self, name, id, pwd, permission, active=True):
        self.name = name
        self.id = id
        self.pwd = pwd
        self.permission = permission
        self.active = active

    def is_active(self):
        return self.active
    def get_permission(self):
        return self.permission
    def get_name(self):
        return self.name


class Anonymous(AnonymousUser):
    name = u"Anonymous"

USERS = {}
permission=False

app.config.from_object(__name__)

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

def _id():
    nb=[x[u"id"] for x in pymongo.MongoClient().site.users.find()]
    g_id=0;
    for x in nb :
        idd=int(x) 
        if idd>g_id:
            g_id=idd
    return g_id

@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))


login_manager.setup_app(app)

def update(oldpassword,newpassword,login):
    if exist_id(login, oldpassword):

        if pymongo.MongoClient().site.users.update({"id": exist_id(login,oldpassword)},{"$set":{"password": newpassword}}) :
            return True

    return False


def exist_email(email):
    d=[p[u'email'] for p in pymongo.MongoClient().site.users.find() if email==p[u'email']]
    if len(d)!=0:
        return False
    else :
        return True



def users_login_mail():
    users={}
    i=1
    for user in pymongo.MongoClient().site.users.find():

        users["user"+str(i)]={"login":user["login"],"email":user["email"]}
        print users
        i=i+1
    return users


def exist_login(login):
    d=[p[u'login'] for p in pymongo.MongoClient().site.users.find() if login==p[u'login']]
    if len(d)!=0:
        return False
    else :
        return True

def exist_id(login, password):
    d=[p for p in pymongo.MongoClient().site.users.find() if login==p[u'login'] and password== p[u'password']]
    if len(d)!=0:
        print d
        return d[0][u'id']
    else :
        return False


@app.route("/login", methods=["GET", "POST"])
def login():
    x=[xx for xx in pymongo.MongoClient().site.users.find()]

    p=0
    for user in x:
    
        p=p+1
        USERS[p]=User(user["login"], int(user["id"]), user["password"] , permission=user["permission"])

    USER_logs = dict((u.name, u)  for u in USERS.itervalues())
    USER_pwd = dict((u.pwd, u) for u in USERS.itervalues())
    if request.method == "POST" and "login" in request.form and "pwd" in request.form:
        username = request.form["login"]
        password = request.form["pwd"]       
        if username in USER_logs and password in USER_pwd:
            if login_user(USER_logs[username]) == login_user(USER_pwd[password]):
                session.pop('username', None)
                session.modified=True
                session["username"]=username
                session["permission"]=pymongo.MongoClient().site.users.find({"login":username})[0]["permission"]
                resp= make_response(redirect(request.args.get("next") or "/main" ))
                resp.set_cookie('username', username)
                return resp
    flash(u"Invalid username or password")
    return render_template("log.html")


@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("/main"))
    return render_template("reauth.html")



@app.route("/delete_users", methods=["GET", "POST"])
@login_required
def delete():

    if request.method == "POST":
        if pymongo.MongoClient().site.users.rmove({"login":request.form["login"]}):
            return render_template("supprimer.html",liste=users_login_mail() , message="delete user Success")
        else :
            return render_template("supprimer.html",liste=users_login_mail() , message="delete user not Success")
    return render_template("delete.html",liste=users_login_mail() , message="")





@app.route("/update_users", methods=["POST"])
@login_required
def update_users():
    print request.data
    if request.method == "POST" and "login" in request.data and "password" in request.data and "email" in request.data:
        req=request.data.replace("{","")
        req=req.replace("}","")
        req=req.replace("\"","")
        req=req.split(",")
        login=req[0].split(":")[1]
        print login
        password= req[1].split(":")[1]
        print password
        email= req[2].split(":")[1]
        print email
        permission= req[3].split(":")[1]
        
        if permission=="true":
            permission=True
        else:
            permission=True
        print permission

        new_user={"login":login, "id" :_id()+1, "password":password, "email":email ,"permission":permission}
        if exist_login(login):
            if exist_email(email):
                if pymongo.MongoClient().site.users.save(new_user):
                    return "Success --add user--"    
            else:
                return "email already used"
        else :
            return "login already used"    
    return "failed"

    

@app.route("/update_user", methods=["POST"])
@login_required
def update_user():
    print request.data
    if request.method == "POST" and "login" in request.data and "old_password" in request.data and "new_password" in request.data:
        req=request.data.replace("{","")
        req=req.replace("}","")
        req=req.replace("\"","")
        req=req.split(",")
        login=req[0].split(":")[1]
        print login
        old_password= req[1].split(":")[1]
        print old_password
        new_password= req[2].split(":")[1]
        print new_password
        if update(old_password,new_password,login):
            return "Success --update user--"
    return "failed"


@app.route("/logout")
@login_required
def logout():
    session.pop('username', None)
    session.modified=True
    logout_user()
    flash(u"Please log in to access this page.")
    return redirect(url_for("index"))

#*******************************************************************************************************
@app.route("/")
def index():
    
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"panda"})]
    site=site[0]

    return render_template("user.html",site=site, ang='', controll='')

@app.route("/get-site")
def get_site():
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"panda"})]
    site=site[0]
    return jsonify(site)

@app.route("/main")
@login_required
def back_office():
    
    return render_template("main.html",permission=session["permission"])
    
@app.route("/account")
@login_required
def update_password():
    return render_template("update_password.html")
@app.route("/create")
@login_required
def create_user():
    return render_template("create_user.html")


@app.route("/style")
@login_required
def style():
  
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"panda"})]
    site=site[0]
    return render_template("style.html",site=site, ang='ng-click=demo()', controll='ng-controller=change_style')
@app.route("/layout")
@login_required
def layout():
    # la recherche dans la base de donn_ee de site dont son _id est panda
    site=[x for x in pymongo.MongoClient().site.site.find({"_id":"panda"})]#liste de site 
    site=site[0]# site[0] est un dictionnaire (json de site)
    return render_template("layout.html",site=site, ang='ng-click=demo()', controll='ng-controller=change_layout')
        

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template("log.html")


@app.route('/test')
def test():
    return render_template("test.html")



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
@login_required
def save_style():

    os.remove("/home/benzina/exmple/static/stylesheets/screen.css");
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








