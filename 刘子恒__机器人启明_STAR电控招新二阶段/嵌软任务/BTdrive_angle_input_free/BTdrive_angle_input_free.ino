//蓝牙app自由输入角度值使舵机转动到相应角度
#include <SoftwareSerial.h>
#include <Servo.h>
int deta;
String beforeDeta="";
Servo drive;
SoftwareSerial BT(3,4);//开始前的定义
void setup() {
  BT.begin(9600);
  drive.attach(8);
  beforeDeta.reserve(200);//为字符串变量预留200字符的空间，防止后面不断添加字符时频繁调用存储

}

void loop() {
  while(BT.available()>0){
    char singleDeta=(char)BT.read();//逐个字符读取
    if(singleDeta=='\n'){
      deta=beforeDeta.toInt();//将字符串变量转化为整形
      drive.write(deta);
      beforeDeta="";
      BT.print("成功发送");
      delay(100);//当读取到换行符时执行命令并将字符串变量清零以便下一次存储

    }else{
      beforeDeta+=singleDeta;//将逐个字符拼成完整的字符串
    }
  }
}
