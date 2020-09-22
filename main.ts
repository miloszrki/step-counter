input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
    led.stopAnimation()
})
let steps = 0
basic.forever(function on_forever() {
    basic.showNumber(steps)
})
