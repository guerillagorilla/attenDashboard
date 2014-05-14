from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    page_list = ['Eins', 'Zwei']
    return render_template('base.html', pages=page_list)


if __name__ == "__main__":
    app.run(port=8000)
