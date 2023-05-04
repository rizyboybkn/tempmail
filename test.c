#include<stdio.h>

HIGH = 10;
LOW = 10;
int hundreds =10;

void loop(){
    long int x = pulseIn(13,HIGH,200000);
    int ones,tens = (x/10000);
    hundreds = (x/100000);
    tens = (x-(hundreds*10000))/1000;
    ones = (x-(hundreds*10000))-(tens*1000)/100;

    int a = hundreds%2;
    int b = (hundreds/2)%2; 
    int c = (hundreds/4)%2; 
    int d = (hundreds/8)%2; 

    digitalWrite(6,HIGH);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    digitalWrite(2,a);
    digitalWrite(3,b);
    digitalWrite(4,c);
    digitalWrite(5,d);

}