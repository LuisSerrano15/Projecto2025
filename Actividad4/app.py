from flask import Flask, render_template

app = Flask(__name__)

# Datos simulados
usuarios = [
    {"nombre": "Ana", "correo": "ana@example.com"},
    {"nombre": "Luis", "correo": "luis@example.com"}
]

productos = [
    {"nombre": "Laptop", "precio": 1200.00, "disponible": True},
    {"nombre": "Mouse", "precio": 25.50, "disponible": False}
]

# Rutas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usuarios")
def mostrar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/productos")
def mostrar_productos():
    return render_template("productos.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)

