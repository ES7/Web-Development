from flask import Flask
app = Flask(__name__)

@app.route("/")
def hw():
  return render_template("home.html")

if __name__ == "__main__":
  aap.run(host="0.0.0.0", debug=True)
  