from flask import render_template, url_for, flash, redirect, request
from pitchive import app, db, bcrypt
from pitchive.forms import RegistrationForm, LoginForm, PitchForm
from pitchive.models import User, Pitch
from flask_login import login_user, current_user, logout_user, login_required



#dummy data
# posts = [
#     {
#          'author': 'Jeff',
#          'title': 'Pitch 1',
#          'content': 'brr kang kang buyaka buyaka are frtiom whad up frigo from the frost frsnkeinstrein bla ha ndi hu ha na mayengs  na o nano vroom',
#          'date_posted': 'August 15th, 2019'       
#     },
#     {
#         'author': 'Sam',
#          'title': 'Pitch 2',
#          'content': 'clappers to the front',
#          'date_posted': 'September 20th, 2019' 
#     }

# ]

@app.route('/')
def home():
    pitches = Pitch.query.all()
    return render_template('home.html', pitches=pitches)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/comments")
def comments():
    return render_template('comments.html', title='Comments')

# RegistrationForm route
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# LoginForm route   
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/pitch/new", methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_pitch.html', title='New Pitch', form=form)



