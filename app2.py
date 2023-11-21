from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message='Hello, World!')

@app.route('/about')
def about():
    return render_template('index.html', message='This is the about page.')

@app.route('/contact')
def contact():
    return render_template('index.html', message='Contact us at: contact@example.com')

if __name__ == '__main__':
    app.run(debug=True)
