MbitIR.IR_callbackUserV2(function (message) {
    IR = message
    if (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Up)) {
        Direction2 = 1
    } else if (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Down)) {
        Direction2 = 2
    } else if (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Left)) {
        Direction2 = 3
    } else if (message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Right)) {
        Direction2 = 4
    } else {
        if (!(message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Up)) || (!(message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Down)) || (!(message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Left)) || !(message == MbitIR.IR_KeyValue(MbitIR.enIRButton.Right))))) {
            Direction2 = 0
        }
    }
})
let Direction2 = 0
let IR = 0
Mbit_IR.init(Pins.P8)
basic.forever(function () {
    if (Direction2 == 1) {
        basic.showNumber(1)
    } else if (Direction2 == 2) {
        basic.showNumber(2)
    } else if (Direction2 == 3) {
        basic.showNumber(3)
    } else if (Direction2 == 4) {
        basic.showNumber(4)
    } else {
        if (Direction2 == 0) {
            basic.showNumber(0)
        }
    }
})
