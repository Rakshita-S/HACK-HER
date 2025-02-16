from flask import Flask, render_template, url_for
from routes import routes
from database import init_db


from flask_cors import CORS

app = Flask(__name__, template_folder="./Template")
CORS(app)

init_db(app)

@app.route('/')
def home():
    return render_template('main.html')

app.register_blueprint(routes)


if __name__ == '__main__':
    app.run(debug=True)