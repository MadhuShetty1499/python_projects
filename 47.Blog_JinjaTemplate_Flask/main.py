from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.before_request
def before_request():
    response = requests.get("https://api.npoint.io/653a1986a31832bd8dae")
    all_posts = response.json()
    request.posts = all_posts

@app.route('/')
def home():
    return render_template("index.html", posts=request.posts)


@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=request.posts, num=num)



if __name__ == "__main__":
    app.run(debug=True)
