const int RELAY_PIN = 7;
void setup() {
  // put your setup code here, to run once:
  pinMode(RELAY_PIN,OUTPUT);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(RELAY_PIN,HIGH);
  delay(500);
  digitalWrite(RELAY_PIN,LOW);

}
