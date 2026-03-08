#include "stm32f10x.h" 
#include "Delay.h"
void KEY_Init(void){
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC,ENABLE);
	GPIO_InitTypeDef GPIO_InitStruct;
	GPIO_InitStruct.GPIO_Mode =GPIO_Mode_IPU;
	GPIO_InitStruct.GPIO_Pin =GPIO_Pin_13 ;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_Init(GPIOC,&GPIO_InitStruct);	
}
uint8_t KEY_Reaction(void){
	uint8_t KEY_Number=0;
	if(GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_13)==0){
		Delay_ms(20);
		while(GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_13)==0);
		Delay_ms(20);
		KEY_Number=1;
		
	}else{
	KEY_Number=0;
	}
	return KEY_Number;
	
}