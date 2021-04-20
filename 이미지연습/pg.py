import pyrebase
import dday
import d_day
from flask import Flask, render_template, request,url_for,session,redirect,send_from_directory

config = {
    "apiKey": "AIzaSyApzWwpFCSxBR-OwZke8jsOJ1s85viymMA",
    "authDomain": "start-3a884.firebaseapp.com",
    "databaseURL": "https://start-3a884-default-rtdb.firebaseio.com",
    "projectId": "start-3a884",
    "storageBucket": "start-3a884.appspot.com",
    "messagingSenderId": "189396804497",
    "appId": "1:189396804497:web:11b0d66e64a548c7c9f030"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')  
app.jinja_env.globals.update(
    zip=zip, 
    enumerate=enumerate, 
) 

@app.route('/')
def index():
 
    key1= request.args.get("keyword1")
    key2= request.args.get("keyword2")
    key3= request.args.get("keyword3")
    if key1=="년도" or key1 is None or key2=="월" or key2 is None or key3=="일" or key3 is None:
        return render_template("index.html")
        
    else:
        key1=int(key1)
        key2=int(key2)
        key3=int(key3)
        data = dday.get_dday_data(key1,key2,key3)
        data1= d_day.get_dayday_data(key1,key2,key3)    
        return render_template("index.html",data=data,data1=data1) 


@app.route('/img', methods=['GET', 'POST'])
def img():
    if request.method == 'POST':
        global user
        user = email[:email.index("@")]
        upload = request.files['upload']
        storage.child(user).child("images/bg.jpg").put(upload)
        return redirect(url_for("s_index"))
    
    return render_template('img.html')

@app.route('/s_index')
def s_index():
    global user
    user = email[:email.index("@")]
    link = storage.child(user).child("images/bg.jpg").get_url(None)
    key1= request.args.get("keyword1")
    key2= request.args.get("keyword2")
    key3= request.args.get("keyword3")
    if key1=="년도" or key1 is None or key2=="월" or key2 is None or key3=="일" or key3 is None:
        return render_template("s_index.html",link=link)
        
    else:
        key1=int(key1)
        key2=int(key2)
        key3=int(key3)
        data = dday.get_dday_data(key1,key2,key3)  
        data1= d_day.get_dayday_data(key1,key2,key3)   
        return render_template("s_index.html",data=data,link=link,data1=data1) 


@app.route('/sitemap.xml')
@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])




@app.route('/login', methods=['GET','POST'])
def login():
    unsuccess1 = "로그인 실패"
    unsuccess2 = "아이디와 비밀번호를 확인해주세요."
    
    
    if request.method == 'POST':
        global email
        email = request.form['name']
        password = request.form['pw']
        try:
            auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for("s_index"))
        except:
            return render_template('login.html', us1=unsuccess1, us2=unsuccess2)
    return render_template('login.html')

@app.route('/join', methods=['GET','POST'])
def join():
    unsuccess3 = "가입 실패"
    unsuccess4 = "아이디와 비밀번호를 확인해주세요."
    
    
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pw']
        try:
            auth.create_user_with_email_and_password(email,password)
            return redirect(url_for("album"))
        except:
            return render_template('join.html', us3=unsuccess3, us4=unsuccess4)
    return render_template('join.html')

@app.route('/album')
def album():
    
    return render_template('album.html')

   




if __name__ == '__main__':
    app.run(debug=True)

