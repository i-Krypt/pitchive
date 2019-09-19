from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f7e5863a2ac81ff4b4a4eea178454687'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    pitch = db.relationship('Pitch', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Pitch(db.Model):
    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Pitch('{self.title}', '{self.date_posted}')"


#dummy data
posts = [
    {
         'author': 'Jeff',
         'title': 'Pitch 1',
         'content': 'brr kang kang buyaka buyaka are frtiom whad up frigo from the frost frsnkeinstrein bla ha ndi hu ha na mayengs  na o nano vroom',
         'date_posted': 'August 15th, 2019'       
    },
    {
        'author': 'Sam',
         'title': 'Pitch 2',
         'content': 'clappers to the front',
         'date_posted': 'September 20th, 2019' 
    }

]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


# RegistrationForm route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# LoginForm route   
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and  form.password.data == 'password':
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)