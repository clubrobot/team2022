#include <Arduino.h>
#include "instructions.h"

extern AX12 ax;
/*
All the instructions are with ax.attach this is for swaping between 
differents ax12 that have differents ID
*/

void RESET(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.reset();
}

void PING_AX(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    output.write<int>(ax.ping());
}

void SET_ID(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setID(input.read<byte>());
}

void SET_BD(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setID(input.read<long>());
}

void MOVE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.move(input.read<float>());
}

void MOVE_SPEED(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.moveSpeed(input.read<float>(), input.read<float>());
}

void TURN(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.turn((int) input.read<float>());
}

void SET_ENDLESS_MODE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setEndlessMode(input.read<bool>());
}

void SET_TEMP_LIMIT(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setTempLimit(input.read<byte>());
}

void SET_ANGLE_LIMIT(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setAngleLimit(input.read<float>(), input.read<float>());
}

void SET_VOLTAGE_LIMIT(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setVoltageLimit(input.read<byte>(), input.read<byte>());
}

void SET_MAX_TORQUE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setMaxTorque(input.read<int>());
}

void SET_MAX_TORQUE_RAM(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setMaxTorqueRAM(input.read<int>());
}

void SET_SRL(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setSRL(input.read<byte>());
}

void SET_RDT(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setRDT(input.read<byte>());
}

void SET_LED_ALARM(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setLEDAlarm(input.read<byte>());
}

void SET_SUTDOWN_ALARM(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setShutdownAlarm(input.read<byte>());
}

void SET_CMARGIN(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setCMargin(input.read<byte>(), input.read<byte>());
}

void SET_CSLOPE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setCSlope(input.read<byte>(), input.read<byte>());
}

void SET_PUNCH(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    ax.setPunch(input.read<int>());
}

void READ_TEMPERATURE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    output.write<int>(ax.readTemperature());
}

void READ_VOLTAGE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    output.write<float>(ax.readVoltage());
}

void READ_POSITION(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    output.write<float>(ax.readPosition());
}

void READ_SPEED(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    output.write<float>(ax.readSpeed());
}

void READ_TORQUE(SerialTalks &inst, Deserializer &input, Serializer &output){
    ax.attach(input.read<byte>());
    output.write<int>(ax.readTorque());
}