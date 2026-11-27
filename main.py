from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculo', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        valor_tarro = 9000
        total_sin_descuento = cantidad * valor_tarro

        if 18 <= edad <= 30:
            porcentaje = 0.15
        elif edad > 30:
            porcentaje = 0.25
        else:
            porcentaje = 0.0

        descuento = total_sin_descuento * porcentaje
        total = total_sin_descuento - descuento

        return render_template(
            'calculo.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total=total
        )

    return render_template('calculo.html')


@app.route('/sesion', methods=['GET', 'POST'])
def sesion():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'miguel' and contrasena == 'admin':
            mensaje = f'Bienvenido Administrador {usuario}'
        elif usuario == 'gustavo' and contrasena == 'user':
            mensaje = f'Bienvenido Usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('sesion.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)