#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
    Serial.begin(9600);
    Wire.begin();
    mpu.initialize();
}

void loop() {
    if (mpu.testConnection()) {
        int16_t ax, ay, az, gx, gy, gz;
        mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

        // Send data over Serial
        Serial.print("Accelerometer: ");
        Serial.print(ax); Serial.print(", ");
        Serial.print(ay); Serial.print(", ");
        Serial.println(az);

        Serial.print("Gyroscope: ");
        Serial.print(gx); Serial.print(", ");
        Serial.print(gy); Serial.print(", ");
        Serial.println(gz);

        delay(500);  // Adjust the delay as needed
    }
}
