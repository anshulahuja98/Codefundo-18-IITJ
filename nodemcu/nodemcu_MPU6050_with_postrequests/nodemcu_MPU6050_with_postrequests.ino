#include <Wire.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
const uint8_t MPU6050SlaveAddress = 0x68;
const uint8_t scl = D6;
const uint8_t sda = D7;
const uint16_t AccelScaleFactor = 16384;
const uint16_t GyroScaleFactor = 131;
const uint8_t MPU6050_REGISTER_SMPLRT_DIV   =  0x19;
const uint8_t MPU6050_REGISTER_USER_CTRL    =  0x6A;
const uint8_t MPU6050_REGISTER_PWR_MGMT_1   =  0x6B;
const uint8_t MPU6050_REGISTER_PWR_MGMT_2   =  0x6C;
const uint8_t MPU6050_REGISTER_CONFIG       =  0x1A;
const uint8_t MPU6050_REGISTER_GYRO_CONFIG  =  0x1B;
const uint8_t MPU6050_REGISTER_ACCEL_CONFIG =  0x1C;
const uint8_t MPU6050_REGISTER_FIFO_EN      =  0x23;
const uint8_t MPU6050_REGISTER_INT_ENABLE   =  0x38;
const uint8_t MPU6050_REGISTER_ACCEL_XOUT_H =  0x3B;
const uint8_t MPU6050_REGISTER_SIGNAL_PATH_RESET  = 0x68;

int16_t AccelX, AccelY, AccelZ, Temperature, GyroX, GyroY, GyroZ;

void setup() {
  Serial.begin(115200);
  WiFi.begin("aksh", "akshchordia");
   while (WiFi.status() != WL_CONNECTED) {
 delay(500);
 Serial.println("Waiting for connection");
  Wire.begin(sda, scl);
   MPU6050_Init();
}}

void loop() {
    HTTPClient http;
    http.begin("http://192.168.43.75:8090/post");
    http.addHeader("Content-Type", "text/plain");
    String final = " ";
    double Ax, Ay, Az, T, Gx, Gy, Gz;
    Read_RawValue(MPU6050SlaveAddress, MPU6050_REGISTER_ACCEL_XOUT_H);
    Ax = (double)AccelX/AccelScaleFactor;
    Ay = (double)AccelY/AccelScaleFactor;
    Az = (double)AccelZ/AccelScaleFactor;
    T = (double)Temperature/340+36.53;
    Gx = (double)GyroX/GyroScaleFactor;
    Gy = (double)GyroY/GyroScaleFactor;
    Gz = (double)GyroZ/GyroScaleFactor;

    Serial.print("Ax: "); Serial.print(Ax);
    Serial.print(" Ay: "); Serial.print(Ay);
    Serial.print(" Az: "); Serial.print(Az);
    Serial.print(" T: "); Serial.print(T);
    Serial.print(" Gx: "); Serial.print(Gx);
    Serial.print(" Gy: "); Serial.print(Gy);
    Serial.print(" Gz: "); Serial.println(Gz);
    final = Ax+Ay+Az+T+Gx+Gy+Gz;
    Serial.println(final);
    int httpCode = http.POST("Message from nodemcu"); 
    String payload = http.getString();
    http.end();
    delay(100);
}



void I2C_Write(uint8_t deviceAddress, uint8_t regAddress, uint8_t data){
  Wire.beginTransmission(deviceAddress);
  Wire.write(regAddress);
  Wire.write(data);
  Wire.endTransmission();
}

void Read_RawValue(uint8_t deviceAddress, uint8_t regAddress){
  Wire.beginTransmission(deviceAddress);
  Wire.write(regAddress);
  Wire.endTransmission();
  Wire.requestFrom(deviceAddress, (uint8_t)14);
  AccelX = (((int16_t)Wire.read()<<8) | Wire.read());
  AccelY = (((int16_t)Wire.read()<<8) | Wire.read());
  AccelZ = (((int16_t)Wire.read()<<8) | Wire.read());
  Temperature = (((int16_t)Wire.read()<<8) | Wire.read());
  GyroX = (((int16_t)Wire.read()<<8) | Wire.read());
  GyroY = (((int16_t)Wire.read()<<8) | Wire.read());
  GyroZ = (((int16_t)Wire.read()<<8) | Wire.read());


}

void MPU6050_Init() {
  delay(150);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_SMPLRT_DIV, 0x07);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_PWR_MGMT_1, 0x01);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_PWR_MGMT_2, 0x00);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_CONFIG, 0x00);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_GYRO_CONFIG, 0x00);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_ACCEL_CONFIG, 0x00);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_FIFO_EN, 0x00);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_INT_ENABLE, 0x01);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_SIGNAL_PATH_RESET, 0x00);
  I2C_Write(MPU6050SlaveAddress, MPU6050_REGISTER_USER_CTRL, 0x00);
}
