
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("Ishazah", "ujang1975")
if ESP8266_IoT.wifi_state(True):
    basic.show_icon(IconNames.HAPPY)
else:
    basic.show_icon(IconNames.SAD)
blynk_token = "IMzCU65Ppg0IIns6U7wt3ZNNedyM6_mj"
#define BLYNK_TEMPLATE_ID "TMPLynDyvGj5"
#define BLYNK_DEVICE_NAME "ESP8226"
#define BLYNK_AUTH_TOKEN "IMzCU65Ppg0IIns6U7wt3ZNNedyM6_mj"