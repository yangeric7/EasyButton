// Open a serial connection and flash LED when input is received

int buttonPin = 4;
int buttonState = 0;

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(buttonPin,INPUT);
  Serial.write('1'); 
}

void loop(){ 
  buttonState = digitalRead(buttonPin);
  if(buttonState == LOW){
    Serial.write('9');
  }
  /*
  if(Serial.available() > 0){      // if data present, blink
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(500); 
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(500);
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(500); 
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(2000);
    Serial.write('0');
  } */
} 
