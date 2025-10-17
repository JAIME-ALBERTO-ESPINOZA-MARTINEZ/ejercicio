from flask import Flask, render_template

app = Flask(__name__)

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/vehiculos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/maravillas")
def maravilllas():
    return render_template("maravillas.html")

@app.route("/acerca_de")
def acerca_de():
    return render_template("acerca_de.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
