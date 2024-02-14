
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Array of button names
button_names = ['Page1', 'Page2', 'Page3']

@app.route('/')
def index():
    return render_template('index.html', button_names=button_names)

@app.route('/<button_name>')
def button(button_name):
    return render_template(f'{button_name}.html')

if __name__ == '__main__':
    app.run(debug=True)
