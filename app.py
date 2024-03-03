from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        post = Post(content=content)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
