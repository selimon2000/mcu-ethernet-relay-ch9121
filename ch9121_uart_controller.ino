// TRANSCEIVER CODE //////////////////////////////////////////////////////////////////////////////////////
#include <DHT11.h>

#define DHT11_PIN 2

#define CFG_PIN 1
#define RST_PIN 4
#define TX_PIN 41
#define RX_PIN 42

#define LED_PIN 6

DHT11 dht11(DHT11_PIN);


void setup() {
  dht11.setDelay(1500); // Set this to the desired delay. Default is 500ms.

  // Initialise configuration pins
  pinMode(CFG_PIN, OUTPUT);
  pinMode(RST_PIN, OUTPUT);
  digitalWrite(CFG_PIN, HIGH);  // HIGH = Normal mode, LOW = Config mode
  digitalWrite(RST_PIN, HIGH);  // HIGH = Normal operation
  
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);  // HIGH = Normal operation

  Serial.begin(9600, SERIAL_8N1, RX_PIN, TX_PIN);

  // Wait for serial port to connect (optional, but good practice)
  while (!Serial);
  delay(1000);
}


void loop() {
    int temperature = 0;
    int humidity = 0;
    int result = dht11.readTemperatureHumidity(temperature, humidity);
    if (result == 0) {
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.print(" °C\tHumidity: ");
        Serial.print(humidity);
        Serial.println(" %");
    }

  if (Serial.available() > 0) {
    String command = Serial.readString();
    if (command == "L0-ON\n") {
      digitalWrite(LED_PIN, LOW);
    }
    else if (command == "L0-OFF\n")  {
      digitalWrite(LED_PIN, HIGH);
    }
  }  
}