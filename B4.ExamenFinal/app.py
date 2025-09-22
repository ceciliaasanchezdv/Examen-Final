from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# --Ejercicio 1--
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        edad = int(request.form.get("edad", 0))
        cant_tarros = int(request.form.get("cant_tarros", 0))

        precio_tarros = 9000
        total_tarros = cant_tarros * precio_tarros

        #descuentos por edad
        if edad < 18:
            perc = 0.00
        elif edad <= 30:
            perc = 0.15
        else:
            perc = 0.25

        descuento = total_tarros * perc
        total_pagar = total_tarros - descuento

        resultado = f"""
        Nombre del cliente: {nombre}<br>
        Total sin descuento: ${total_tarros}<br>
        El descuento es: ${float(descuento)}<br>
        El total a pagar es de: ${float(total_pagar)}
        """

    return render_template("ejercicio1.html", resultado=resultado)

# --- Ejercicio 2 ---
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        pw = request.form.get("pw", "")

        if nombre == "juan" and pw == "admin":
            resultado = "Bienvenido Administrador juan"
        elif nombre == "pepe" and pw == "user":
            resultado = "Bienvenido Usuario pepe"
        else:
            resultado = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)