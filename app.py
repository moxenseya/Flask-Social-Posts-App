from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post,get_posts

#create the app
app = Flask(__name__)


#create the routes/endpoints

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name,post)

    posts = get_posts()

    return render_template('index.html', posts=posts)



#If this is the file that is being run, then execute this file as an app.
if __name__ == '__main__':
    app.run(debug=True)
