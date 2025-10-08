#include <SoftwareSerial.h>
#include <Servo.h>
Servo drive;
SoftwareSerial BT(3,4);
void setup() {
  BT.begin(9600);
  drive.attach(8);
}

void loop() {
  while(BT.available()>0){
    char deta=BT.read();
    if(deta=='1'){
      drive.write(0);
      BT.println("成功");
    }if(deta=='2'){
      drive.write(45);
      BT.println("成功");
    }if(deta=='3'){
      drive.write(90);
       BT.println("成功");
    }if(deta=='4'){
      drive.write(180);
       BT.println("成功");
    }else{
      BT.println("失败");
      BT.println(deta);
    }
  }
}
