from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from web3 import Web3, HTTPProvider
import uitility as u
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('root.html')

@app.route('/Explore')
def explore():
    return render_template('explore.html')

@app.route('/Events')
def events():
    return render_template('events.html') 
@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']
        check=u.getUser(email,password,role)[1]
        if(check[0]==True):
            return redirect(url_for('dashboard',uuid=check[2],role=role))
        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        
    return render_template('login.html')



@app.route('/Register')
def signup():
    
    return render_template('register.html')
@app.route('/E-Library')
def library():
    return render_template('library.html')

def profile():
    return render_template('profile.html')
if __name__ == '__main__':
    app.run(debug=True)
