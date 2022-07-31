ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("Ishazah", "ujang1975")
if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Happy)
} else {
    basic.showIcon(IconNames.Sad)
}

let blynk_token = "IMzCU65Ppg0IIns6U7wt3ZNNedyM6_mj"
