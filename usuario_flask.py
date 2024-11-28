from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    # Obtener los datos en formato JSON de la solicitud
    datos = request.get_json()

    # Verificar que los datos contienen "nombre" y "edad"
    if not datos or "nombre" not in datos or "edad" not in datos:
        return jsonify({"mensaje": "Faltan datos requeridos ('nombre' y 'edad')"}), 400

    nombre = datos.get("nombre")
    edad = datos.get("edad")

    # Crear una respuesta
    respuesta = {
        "mensaje": f"Usuario {nombre} de {edad} años creado exitosamente."
    }
    return jsonify(respuesta)

if __name__ == "__main__":
    app.run(debug=True)
