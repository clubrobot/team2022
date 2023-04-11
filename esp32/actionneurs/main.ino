#include <Arduino.h>
#include <SerialTalks.h>
#include <AX12.h>
#include "instructions.h"

AX12 ax;

void setup()
{
    //Starting SerialTalks
    Serial.begin(SERIALTALKS_BAUDRATE);
    talks.begin(Serial);

    talks.bind(RESET_OPCODE, RESET);

    talks.bind(PING_AX_OPCODE, PING_AX);

    talks.bind(SET_ID_OPCODE, SET_ID);
    talks.bind(SET_BD_OPCODE, SET_BD);

    talks.bind(MOVE_OPCODE, MOVE);
    talks.bind(MOVE_SPEED_OPCODE, MOVE_SPEED);
    talks.bind(TURN_OPCODE, TURN);

    talks.bind(SET_ENDLESS_MODE_OPCODE, SET_ENDLESS_MODE);

    talks.bind(SET_TEMP_LIMIT_OPCODE, SET_TEMP_LIMIT);
    talks.bind(SET_ANGLE_LIMIT_OPCODE, SET_ANGLE_LIMIT);
    talks.bind(SET_VOLTAGE_LIMIT_OPCODE, SET_VOLTAGE_LIMIT);
    talks.bind(SET_MAX_TORQUE_OPCODE, SET_MAX_TORQUE);

    talks.bind(READ_POSITION_OPCODE, READ_POSITION);
    talks.bind(READ_SPEED_OPCODE, READ_SPEED);
    talks.bind(READ_TORQUE_OPCODE, READ_TORQUE);

    //Baud, rx, tx, control
    AX12::SerialBegin(1000000, 5);
   
    ax.attach(254);
    ax.setEndlessMode(true);
}
void loop(){ 
    //talks.execute();
     
    for(int i=0;i<254;i++){
    Serial.println(i);
    ax.attach(i);
    Serial.print("   ");
    Serial.println(ax.ping());
    delay(200);
 }
}