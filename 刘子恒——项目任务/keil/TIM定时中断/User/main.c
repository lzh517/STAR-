#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "LED.h"
#include "KEY_Init.h"
#include "OLED.h"
#include "Encode.h"
int main(void){
	OLED_Init ();
	Encode_Init();
    while(1){
		OLED_ShowNum (1,1,Counter_Number_Get (),4);
	}
}

