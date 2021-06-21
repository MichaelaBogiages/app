from flask import Flask, render_template, request, redirect, url_for      
from db_connection import insert_user
from read_files import parseExcel
import os
from os.path import join, dirname, realpath
import pandas 
from werkzeug.utils import secure_filename
import xlrd
import openpyxl


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/",methods=['POST'])
def addUserHome():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    dob = request.form['dob']
    insert_user(firstName, lastName, dob)
    return render_template("home.html")
  

app.config["DEBUG"] = True


UPLOAD_FOLDER = r'C:\Users\'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index", methods=['POST'])
def uploadFiles():
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
           uploaded_file.save(file_path)
           parseExcel(file_path)
      return redirect(url_for('index'))


    
if __name__ == "__main__":
    app.run(debug=True)


 

