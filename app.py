from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Load questions from the JSON file
    try:
        with open('questions.json', 'r') as f:
            data = json.load(f)
    except:
        data = [] # Agar file nahi mili to empty list
        
    return render_template('quiz.html', questions=data)

if __name__ == '__main__':
    app.run(debug=True)
