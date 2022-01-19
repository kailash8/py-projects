import wikipedia
from flask import Flask, request, render_template

app = Flask(__name__)


# create Home view
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form["search"]

        # Fetch data from wikipedia
        result = wikipedia.summary(search, sentences=10)
        return f"<p>{result}</p>"


if __name__ == '__main__':
    app.run(debug=True)
