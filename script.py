from flask import Flask, request, send_from_directory
import serial

app = Flask(__name__)
arduino = serial.Serial('COM10', 9600)  # Substitua 'COM10' pela porta serial do seu Arduino
current_position = 0  # Posição inicial do servo

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/servo')
def servo():
    global current_position
    pos = request.args.get('pos')
    if pos:
        try:
            new_position = int(pos)
            if 0 <= new_position <= 180:
                arduino.write((str(new_position) + '\n').encode())
                current_position = new_position
                return f"Posição do servo atualizada para {new_position} graus"
            else:
                return "Posição fora do intervalo permitido (0-180 graus)"
        except ValueError:
            return "Valor inválido para a posição"
    return "Posição inválida"

if __name__ == '__main__':
    app.run(port=5000)