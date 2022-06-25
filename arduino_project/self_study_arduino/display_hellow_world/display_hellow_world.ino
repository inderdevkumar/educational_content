static const int heartbeat = 6;

void setup() {
  Serial.begin(9600);
  pinMode( heartbeat, OUTPUT );
  Serial.println("Lets begin");
  digitalWrite( heartbeat, HIGH);
  Serial.println("Hello");
  digitalWrite( heartbeat, LOW);
  delay(1000)
  }

void loop() {
  // put your main code here, to run repeatedly:
}
