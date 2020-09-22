def on_gesture_shake():
    global steps
    steps += 1
    led.stop_animation()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0

def on_forever():
    basic.show_number(steps)
basic.forever(on_forever)
