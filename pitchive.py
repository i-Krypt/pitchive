from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f7e5863a2ac81ff4b4a4eea178454687'


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
@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)