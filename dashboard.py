from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:lime;background:#111;font-family:monospace'>Welcome to GODMODE Dashboard 🚀</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
