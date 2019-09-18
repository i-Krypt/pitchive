from flask import Flask, render_template, url_for

app = Flask(__name__)


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
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)