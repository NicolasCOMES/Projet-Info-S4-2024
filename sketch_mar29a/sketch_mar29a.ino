#include <MKRWAN.h>

LoRaModem modem;

//#include "arduino_secrets.h"

String appEui = " a8610a3435317a0f";
String appKey = "10101010101010101010101010101010";

void setup() {
  Serial.begin(115200);
  while (!Serial);

  if (!modem.begin(EU868)) {
    Serial.println("Failed to start module");
    while (1) {}
  };
  Serial.print("Your module version is: ");
  Serial.println(modem.version());
  Serial.print("Your device EUI is: ");
  Serial.println(modem.deviceEUI());

int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) {
    Serial.println("Something went wrong; are you indoor? Move near a window and retry");
   while (1) {}
  } 
  
  pinMode(LED_BUILTIN, OUTPUT);
  modem.minPollInterval(60);
  
}
void loop() {
  int x = random(-200, 200);
  int y = random(-200, 200);

  String message = "Marguerite:" + String(x) + ":" + String(y);
  sendMessage(message);

  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000); 
  digitalWrite(LED_BUILTIN, LOW);
  delay(10000);
}

void sendMessage(String message) {
  modem.beginPacket();
  modem.print(message);
  modem.endPacket();
  Serial.println("Message envoyé : " + message);
}
