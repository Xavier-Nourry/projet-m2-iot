// Imports des bibliothèques
#include <TheThingsNetwork.h>
#include <Servo.h>
#include <TimeLib.h>

// Définition des constantes
#define loraSerial Serial1
#define debugSerial Serial
#define freqPlan TTN_FP_EU868
const char *DEV_ADDR = "260B9F2A";
const char *NWK_SKEY = "C927B91EDAFD2FFC7EB2DAB162F90BA1";
const char *APP_SKEY = "815DC9CB8FCE1223203EE74DCDFC97E7";

const int ENGINE_PIN = 12;
const int SWITCH_PIN = 4;
const int BUTTON_PIN = 8;
const int LEDS_PIN = 7;
const int NB_ROT = 7;
const int ROT_ANGLE = (int)(155 / (float) 8);
const int TIME_DISTRIB = 2500; // milliseconds
const int TIME_TO_WAIT = 5; // seconds
const char* MSG_TO_SEND = "Emergency";


// Définition des variables
TheThingsNetwork ttn(loraSerial, debugSerial, freqPlan);
int actual_angle;
int rot_cpt;
time_t start_time;
time_t current_time;
Servo engine;

// Fait clignoter une led avec la fréquence en millisecondes souhaitée
void wink_led(int LEDS_PIN, int freq){
  digitalWrite(LEDS_PIN, HIGH);
  delay(freq);
  digitalWrite(LEDS_PIN, LOW);
  delay(freq);
}

// Lance un appel d'urgence via LORA (lié à une application IP)
void emergency_call(){
  debugSerial.print("Sending msg...");
  ttn.sendBytes(MSG_TO_SEND, sizeof(MSG_TO_SEND));
  debugSerial.print("Message sent");    
}

void setup() {
  // put your setup code here, to run once:
  loraSerial.begin(57600);
  debugSerial.begin(9600);
  ttn.personalize(DEV_ADDR, NWK_SKEY, APP_SKEY);
  ttn.showStatus();
  actual_angle = 155;
  rot_cpt = 0;
  engine.attach(ENGINE_PIN);
  pinMode(ENGINE_PIN, OUTPUT);
  pinMode(SWITCH_PIN, INPUT);  
  pinMode(LEDS_PIN, OUTPUT);
  digitalWrite(LEDS_PIN, LOW);
  engine.write(actual_angle);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(SWITCH_PIN) == HIGH){
    if(rot_cpt >= NB_ROT){
      actual_angle = 155;
      rot_cpt = 0;
    } else{
        actual_angle -= ROT_ANGLE;
        rot_cpt++;
      }
    
    engine.write(actual_angle);
    current_time = now();
    start_time = current_time;
    while(digitalRead(BUTTON_PIN) != LOW){ // TODO : voir si nécessaire de faire des actions en parallèle
      current_time = now();
      wink_led(LEDS_PIN, 250);
      if(current_time >= start_time + TIME_TO_WAIT){
        start_time = now();
        emergency_call();
      }
    }
    delay(TIME_DISTRIB);
  }
}