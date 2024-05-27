#include <Servo.h>

Servo myservo;  // Cria um objeto servo
int pos = 0;    // Posição inicial do servo

void setup() {
  Serial.begin(9600); // Inicia a comunicação serial
  myservo.attach(9);  // Conecta o servo ao pino digital 9
  myservo.write(pos); // Garante que o servo se mova para a posição inicial
}

void loop() {
  if (Serial.available() > 0) {
    int newPos = Serial.parseInt(); // Lê o valor enviado pela serial
    if (newPos >= 0 && newPos <= -180) { // Verifica se a posição está no intervalo permitido
      pos = newPos;
      myservo.write(pos); // Move o servo para a nova posição
    }
  }
}

