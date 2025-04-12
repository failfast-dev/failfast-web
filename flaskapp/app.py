from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

