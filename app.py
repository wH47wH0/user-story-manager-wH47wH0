from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)


@app.before_request
def before_request():
    init_db()


@app.teardown_request
def teardown_request(exception):
    db.close()


@app.route('/')
def home():
    return render_template('list.html', user_stories=UserStoryManager.select())


@app.route('/story/')
def add_story():
    return render_template('story.html')


@app.route('/create/', methods=['POST'])
def create_story():
    UserStoryManager.create(
        story_title=request.form['story_title'],
        user_story=request.form['user_story'],
        acceptance_criteria=request.form['acceptance_criteria'],
        business_value=request.form['business_value'],
        estimation=request.form['estimation'],
        status=request.form['status']
    )
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
