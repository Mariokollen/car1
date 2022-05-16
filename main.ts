input.onButtonPressed(Button.A, function () {
    radio.sendString("A")
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendString("Høyre")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("A+B")
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "A") {
        music.playTone(262, music.beat(BeatFraction.Whole))
        bitbot.ledRotate()
        bitbot.go(BBDirection.Forward, 35)
    } else if (receivedString == "B") {
        for (let index = 0; index < 11; index++) {
            bitbot.ledRotate()
        }
        bitbot.go(BBDirection.Reverse, 35)
    } else if (receivedString == "Høyre") {
        bitbot.rotate(BBRobotDirection.Right, 60)
    } else if (receivedString == "Venstre") {
        bitbot.rotate(BBRobotDirection.Left, 60)
    } else {
        bitbot.stop(BBStopMode.Brake)
    }
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("B")
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendString("Venstre")
})
radio.setGroup(1)
bitbot.ledRainbow()
bitbot.select_model(BBModel.XL)