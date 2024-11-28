from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from Modelo import WeatherModel  # Asegúrate de que el archivo se llame Modelo.py

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar Flask usando las variables de entorno
app.config['DEBUG'] = os.getenv('FLASK_DEBUG') == 'True'

# Instanciar el modelo del clima
weather_model = WeatherModel()

# Ruta principal ("/")
@app.route("/")
def home():
    """Retorna un mensaje de bienvenida"""
    return jsonify({
        "mensaje": "¡Bienvenido a la API de clima!",
        "status": "success"
    })

# Ruta para saludar a una persona ("/saludo/<nombre>")
@app.route("/saludo/<nombre>")
def saludo(nombre):
    """Retorna un saludo personalizado"""
    return jsonify({
        "mensaje": f"¡Hola, {nombre}! Bienvenido.",
        "status": "success"
    })

# Ruta para obtener el clima de una ciudad ("/clima/<ciudad>")
@app.route("/clima/<ciudad>")
def clima(ciudad):
    """Retorna los datos del clima de una ciudad"""
    weather_data = weather_model.get_weather(ciudad)
    if weather_data:
        return jsonify({
            "mensaje": "Datos del clima obtenidos.",
            "status": "success",
            "data": weather_data
        })
    else:
        return jsonify({
            "mensaje": "No se pudo obtener datos del clima.",
            "status": "error"
        }), 404

# Manejar errores 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "mensaje": "Ruta no encontrada.",
        "status": "error"
    }), 404

# Manejar errores 500
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "mensaje": "Error en el servidor.",
        "status": "error"
    }), 500

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()
