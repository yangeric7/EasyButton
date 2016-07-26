const int buttonPin = 4;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin
const int buttonPin2 = 5;

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int buttonState2 = 0;

void setup() {

  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  pinMode(buttonPin2, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  buttonState2 = digitalRead(buttonPin2);
    //system("python ../hackathon.py");

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  Serial.print(buttonState);
  if (buttonState == LOW) {
    // turn LED on:
    for (int i = 0; i < 10; i++){
      digitalWrite(ledPin, HIGH);
      delay(500);
      digitalWrite(ledPin, LOW);
      delay(500);
    }
  }
  else if (buttonState2 == LOW){
    for (int i = 0; i < 50; i++){
      digitalWrite(ledPin, HIGH);
      delay(100);
      digitalWrite(ledPin, LOW);
      delay(100);
    }
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
