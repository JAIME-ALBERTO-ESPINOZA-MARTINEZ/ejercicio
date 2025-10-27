from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

correos_registrados = ["test@example.com", "usuario@gmail.com"]
usuarios = {
    "usuario1": "1234",
    "admin": "admin"
}
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/animales')
def animales():
    return render_template("animales.html")

@app.route('/vehiculos')
def vehiculos():
    return render_template("vehiculos.html")

@app.route('/maravillas')
def maravillas():
    return render_template("maravillas.html")

@app.route('/acerca_de')
def acerca_de():
    return render_template("acerca_de.html")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo = request.form.get('correo')
        password = request.form.get('password')

        if correo in correos_registrados:
            return render_template("registro.html", error="El correo ya está registrado.")
        else:
            correos_registrados.append(correo)
            usuarios[nombre.lower()] = password
            return redirect(url_for('index'))
    return render_template("registro.html", error=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if usuario in usuarios and usuarios[usuario] == password:
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Usuario o contraseña incorrectos.")
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


