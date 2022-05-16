def on_button_pressed_a():
    radio.send_string("A")
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_right():
    radio.send_string("Høyre")
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_ab():
    radio.send_string("A+B")
    basic.show_string("AB")
    bitbot.bb_bias(BBRobotDirection.LEFT, 10)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "A":
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        bitbot.led_rotate()
        bitbot.go(BBDirection.FORWARD, 35)
    elif receivedString == "B":
        for index in range(11):
            bitbot.led_rotate()
        bitbot.go(BBDirection.REVERSE, 35)
    elif receivedString == "Høyre":
        bitbot.rotate(BBRobotDirection.RIGHT, 20)
    elif receivedString == "Venstre":
        bitbot.rotate(BBRobotDirection.LEFT, 20)
    else:
        bitbot.stop(BBStopMode.BRAKE)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("B")
    basic.show_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_left():
    radio.send_string("Venstre")
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

radio.set_group(1)
bitbot.led_rainbow()
bitbot.select_model(BBModel.XL)