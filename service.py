from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
import pymysql as MySQLdb
app = Flask(__name__, static_url_path="/templates", static_folder='/home/soumya/PycharmProjects/myproject/templates')

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/index")
def search():
    return "<h1>Soumya Ranjan Rout</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
   message = None
   if request.method == 'POST':
        datafromjs = request.form['mydata']
        result = "return this"
        resp = make_response('{"response": '+result+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        #return render_template('/home/soumya/work-space/web-app/main.html', message='')

if __name__ == "__main__":
    app.run(debug = True)