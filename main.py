def on_ir_callbackuserv2(message):
    global IR, Direction2
    IR = message
    if message == MbitIR.IR_KeyValue(MbitIR.enIRButton.UP):
        Direction2 = 1
    elif message == MbitIR.IR_KeyValue(MbitIR.enIRButton.DOWN):
        Direction2 = 2
    elif message == MbitIR.IR_KeyValue(MbitIR.enIRButton.LEFT):
        Direction2 = 3
    elif message == MbitIR.IR_KeyValue(MbitIR.enIRButton.RIGHT):
        Direction2 = 4
    else:
        if not (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.UP)) or (not (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.DOWN)) or (not (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.LEFT)) or not (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.RIGHT)))):
            Direction2 = 0
MbitIR.IR_callbackUserV2(on_ir_callbackuserv2)

Direction2 = 0
IR = 0
Mbit_IR.init(Pins.P8)

def on_forever():
    if Direction2 == 1:
        basic.show_number(1)
    elif Direction2 == 2:
        basic.show_number(2)
    elif Direction2 == 3:
        basic.show_number(3)
    elif Direction2 == 4:
        basic.show_number(4)
    else:
        if Direction2 == 0:
            basic.show_number(0)
basic.forever(on_forever)
