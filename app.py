from flask import Flask, render_template
from select_story import select_story

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/meditate")
def meditate():  # put application's code here
    return render_template("meditate.html")

@app.route("/nature")
def nature():  # put application's code here
    return render_template("nature.html")

@app.route("/create")
def create():  # put application's code here
    return render_template("create.html")

@app.route("/cook")
def cook():  # put application's code here
    return render_template("cook.html")

@app.route("/read")
def read():  # put application's code here
    selected_story_title, selected_story = select_story()
    return render_template("read.html", title=selected_story_title, story=selected_story)

@app.route("/random")
def random_choice():  # put application's code here
    return render_template("random.html")

if __name__ == '__main__':
    app.run(debug=True)
