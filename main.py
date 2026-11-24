
from flask import Flask, render_template, request

# Crear aplicación Flask
app = Flask(__name__)


# MENU PRINCIPAL
@app.route("/")
def inicio():
    return render_template("index.html")


# EJERCICIO 1: CALCULO DE COMPRAS
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        if not nombre or edad < 0 or cantidad <= 0:
            return render_template(
                "ejercicio1.html",
                error="Ingresa datos válidos."
            )

        precio = 9000
        total = precio * cantidad

        if edad >= 18 and edad <= 30:
            porcentaje = 15
        elif edad > 30:
            porcentaje = 25
        else:
            porcentaje = 0

        descuento = total * porcentaje / 100
        total_pagar = total - descuento

        resultado = {
            "nombre": nombre,
            "total": total,
            "porcentaje": porcentaje,
            "descuento": descuento,
            "total_pagar": total_pagar
        }

        return render_template(
            "resultado_compra.html",
            resultado=resultado
        )

    return render_template("ejercicio1.html")


# EJERCICIO 2: INICIO DE SESION
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    mensaje = None

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido administrador juan"

        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido usuario pepe"

        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


# INICIAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)
