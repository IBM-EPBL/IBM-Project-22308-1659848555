//
int moisture_data = 0;
void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(12, OUTPUT);  
  pinMode(7, INPUT);
  pinMode(6, OUTPUT);
}
void loop()
{
  moisture_data = analogRead(A0);

  Serial.println(moisture_data);

  if (moisture_data < 21) {

    digitalWrite(12, HIGH);

  } else {

    digitalWrite(12, LOW);
  }
if (digitalRead(7) == HIGH) {
    tone(6, 523, 1000); // play tone 60 (C5 = 523 Hz)
  } else {
    digitalWrite(5, LOW);
    noTone(6);
  }
  delay(10); // Delay a little bit to improve simulation performance


}