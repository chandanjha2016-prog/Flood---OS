
// ESP32 + Ultrasonic + Rain sensor
void setup() {
  Serial.begin(9600);
}
void loop() {
  int waterLevel = analogRead(A0); // replace with real sensor logic
  int rain = analogRead(A1);
  Serial.print("Water:"); Serial.print(waterLevel);
  Serial.print(" Rain:"); Serial.println(rain);
  delay(5000);
}
