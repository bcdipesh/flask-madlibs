from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html', questions=story.prompts)


@app.route("/generate-story")
def generate_story():
    generated_story = story.generate(request.args)

    return render_template('generate-story.html', generated_story=generated_story)
