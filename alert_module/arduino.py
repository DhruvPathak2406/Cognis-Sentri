try:
    import serial

    arduino = serial.Serial('COM3', 9600)

    def trigger_hardware():
        arduino.write(b'1')
        print("🔌 Arduino Triggered")

except:
    def trigger_hardware():
        print("⚠️ Arduino not connected (simulation mode)")