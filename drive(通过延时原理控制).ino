#define mydrive 2
int delayTime[]={500,833,1000,1500,2000,2500};
int periodTime=20000; 
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
    delay(1000);
  for(int i=0;i<6;i++){
    digitalWrite(mydrive,HIGH);
    delayMicroseconds(delayTime[i]);
    digitalWrite(mydrive,LOW);
    delayMicroseconds(periodTime-delayTime[i]);
    delay(1000);
  }

}
