from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)
year = datetime.now().year
AGE_API = 'https://api.agify.io/'
GENDER_API = 'https://api.genderize.io'


@app.route('/')
def index_function():
    return render_template('index.html', yyyy=year)


@app.route('/analyse/<name>')
def name_analysis_function(name):
    params = {'name': name}
    age_res = requests.get(AGE_API, params=params)
    age_res.raise_for_status()
    gender_res = requests.get(GENDER_API, params=params)
    gender_res.raise_for_status()

    age = age_res.json()['age']
    gender = gender_res.json()['gender']

    return render_template('name_analysis.html', age=age, name=name, gender=gender)


@app.route('/blog/<test_val>')
def blog_function(test_val):
    res = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    res.raise_for_status()
    print(test_val)
    blog_posts = res.json()
    return render_template('blog.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(debug=True)
