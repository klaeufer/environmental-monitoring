void setup() {
  Serial.begin(9600);
}

void loop() {
  unsigned short rawValue = analogRead(A0);
  unsigned char* rawValueInByteArray = convertShortToByteArray(rawValue);
  Serial.write(rawValueInByteArray, 2);
  delay(1000);
}

unsigned char* convertShortToByteArray(unsigned short value) {
  unsigned char* bytes = (unsigned char *) malloc(sizeof(char) * 2);
  bytes[0] = value & 0xFF;
  bytes[1] = (value >> 8) & 0xFF;
  return bytes;
}
