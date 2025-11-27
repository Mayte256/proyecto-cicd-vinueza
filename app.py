# Proyecto CI/CD - Mayte Anahi Anchapanta Vinueza
# Aplicación Flask con IA

from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Respuestas simples de IA
RESPUESTAS_IA = {
    "hola": ["¡Hola! Soy el asistente de Mayte Vinueza", "¡Saludos! ¿En qué puedo ayudarte?"],
    "como estas": ["Estoy funcionando correctamente", "Todo bien, gracias por preguntar"],
    "quien eres": ["Soy una aplicación Flask con IA creada por Mayte Anchapanta Vinueza"],
    "default": ["Interesante pregunta", "Cuéntame más", "No estoy seguro, pero puedo ayudarte con otra cosa"]
}

@app.route('/')
def home():
    return jsonify({
        "mensaje": "Aplicación CI/CD Flask con IA",
        "estudiante": "Mayte Anahi Anchapanta Vinueza",
        "segundo_apellido": "Vinueza",
        "version": "1.0.5",
        "estado": "Funcionando correctamente"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok", "estudiante": "Vinueza"})

@app.route('/ia', methods=['POST'])
def chatbot():
    data = request.get_json()
    mensaje = data.get('mensaje', '').lower()
    
    # Lógica simple de IA
    for key in RESPUESTAS_IA:
        if key in mensaje:
            respuesta = random.choice(RESPUESTAS_IA[key])
            return jsonify({
                "pregunta": mensaje,
                "respuesta": respuesta,
                "estudiante": "Mayte Vinueza"
            })
    
    respuesta = random.choice(RESPUESTAS_IA["default"])
    return jsonify({
        "pregunta": mensaje,
        "respuesta": respuesta,
        "estudiante": "Mayte Vinueza"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
