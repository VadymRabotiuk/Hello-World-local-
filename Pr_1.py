from flask import Flask
app= Flask(__name__)
@app.route("/")
def startF():
    return None
@app.route("/hello")
def Hello():
    return "World"
if __name__=="__main__":
    app.run(debug=False)