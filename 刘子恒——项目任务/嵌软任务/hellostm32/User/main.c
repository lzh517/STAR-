#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "LED.h"
#include "KEY_Init.h"
#include "OLED.h"
int main(void){
	OLED_Init();
	OLED_ShowString  (1,1,"Hello");
	while(1){
	
	}
}
