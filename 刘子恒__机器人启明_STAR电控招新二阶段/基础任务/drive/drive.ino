//这是通过延时原理控制占空比实现的（在此并未引用Servo库，以展现我对舵机运行原理的理解，后面的蓝牙嵌软任务我将应用Servo库）
#define mydrive 2
int delayTime[]={500,833,1000,1500,2000,2500};
int periodTime=20000; //规定高电平时长和周期
void setup() {
  // put your setup code here, to run once:
  pinMode(mydrive,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(mydrive,HIGH);
   delayMicroseconds(delayTime[0]);
    digitalWrite(mydrive,LOW);
    delayMicroseconds(periodTime-delayTime[0]);
    delay(1000);//复位
  for(int i=0;i<6;i++){
    digitalWrite(mydrive,HIGH);
    delayMicroseconds(delayTime[i]);
    digitalWrite(mydrive,LOW);
    delayMicroseconds(periodTime-delayTime[i]);
    delay(1000);
  }//旋转到指定角度
  

}
