String incomingByte ;    
const int alpha = 8;

void setup() {
  Serial.begin(9600);
  pinMode(alpha, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    
    if (incomingByte == "day") {     
      digitalWrite(alpha, HIGH);
    }
    
    else if (incomingByte == "night") {
      digitalWrite(alpha, LOW);
    }       
  }
}
