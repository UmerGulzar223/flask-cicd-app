from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.context_processor
def inject_version():
    return dict(build_version="v1.0.2")  # manually or dynamically updated


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)