from flask import Flask, request, jsonify

app = Flask(__name__)


usuarios = []

#/info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "aplicacion": "Gestión de Usuarios",
        "version": "1.0",
        "autor": "Luis Serrano"
    })

#/crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json
    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Se requiere nombre y correo"}), 400

    nuevo_usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario
    }), 201

#/usuarios
@app.route("/usuarios", methods=["GET"])
def usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)
