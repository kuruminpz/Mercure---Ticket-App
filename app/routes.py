from flask import Blueprint, session, redirect, url_for, render_template
from app.auth import google_login, google_callback

main_blueprint = Blueprint('main',__name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/login')
def login():
    return google_login()


@main_blueprint.route('/login/callback')
def login_callback():
    return google_callback()


@main_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


@main_blueprint.route('/dashboard')
def dashboard():
    if 'userinfo' not in session:
        return redirect(url_for('main.login'))
    
    userinfo = session.get('userinfo')
    return render_template('dashboard.html',userinfo=userinfo)