#include <SoftwareSerial.h>
#include <Servo.h>
int deta;
String beforeDeta="";
Servo drive;
SoftwareSerial BT(3,4);
void setup() {
  BT.begin(9600);
  drive.attach(8);
  beforeDeta.reserve(200);

}

void loop() {
  while(BT.available()>0){
    char singleDeta=(char)BT.read();
    if(singleDeta=='\n'){
      deta=beforeDeta.toInt();
      drive.write(deta);
      beforeDeta="";
      BT.print("成功发送");
      delay(100);

    }else{
      beforeDeta+=singleDeta;
    }
  }
}
