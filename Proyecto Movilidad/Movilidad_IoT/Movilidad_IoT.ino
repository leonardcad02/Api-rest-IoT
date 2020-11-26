//librerias
#include "ESP8266WiFi.h"
#include <aREST.h>
#include <DHT.h>



// Define Temperature and Humidity
#define DHTPIN  D6
#define DHTTYPE DHT11
#define MQ A0
DHT dht (DHTPIN,DHTTYPE );



//Define Apirest
aREST rest = aREST();

//Variables API

float humidity, temperature, mq;



//Wifi

const char* ssid = "Fla Garcia";
const char* password = "1049633057j";

//Port
#define LISTEN_PORT 80

//create instance of server
WiFiServer server (LISTEN_PORT);



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();


  //init variables API
  rest.variable("temperature", &temperature);
  rest.variable ("humidity", &humidity);
  rest.variable ("Polution",&mq);

  
  //Name ID 
  rest.set_id("1");
  rest.set_name("sensor_node");

  //conect to wifi
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
    }
  Serial.print("");
  Serial.println("Wifi connected");

  //Start server
  server.begin();
  Serial.println("Server started!");

  //IP
  Serial.println(WiFi.localIP());  
}

void loop() {
  // put your main code here, to run repeatedly:
  //wait 1 segundo 
  delay(1000);
    
  //read of sensors 
  mq = analogRead(MQ); //MQ135
  humidity = dht.readHumidity(); // RH % 0-100
  temperature = dht.readTemperature(); // 0 - 100°C
  Serial.println(humidity);
  Serial.println(temperature);
  
 
  //REST Calls
  WiFiClient client = server.available();
//
//  if(!client){
//    return;
//    }
//  while (!client.available()){
//    delay(1);
//    }  
  rest.handle(client);  
  delay(2000);
}
