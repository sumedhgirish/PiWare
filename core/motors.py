import gpiozero as gpio
import time

class StepperMotor(gpio.Device):

    # CONSTANTS

    # direction
    CW = 1      # forward
    CCW = -1    # reverse

    def __init__(self, num_steps, *args, pin_factory=None, **kwargs):
        super().__init__(pin_factory=pin_factory)

        self.pins = list(map(gpio.OutputDevice, args))
        self.num_pins = len(args)

        self.direction = self.CW
        self.num_steps = num_steps
        self.angle_per_step = 360 / self.num_steps
        self.cur_step = 0
        self.step_delay = 60 / self.num_steps / 240     # assumes a speed of 240 rpm, which we should change at some point

        self.step_cycle = kwargs.get("step_cycle", [[i==j for i in range(self.num_pins)] for j in range(self.num_pins)])
        self.cycle_len = len(self.step_cycle)

    def __repr__(self):
        return "StepperMotor(" + \
            f"num_pins={self.num_pins}, " + \
            f"direction={'CW' if self.direction > 0 else 'CCW'}, " + \
            f"angle_moved={self.cur_step * self.angle_per_step}°" + \
            ")"

    def _set_state(self, state):
        for pini, pin in enumerate(self.pins):
            if state[pini]:
                pin.on()
            else:
                pin.off()

            time.sleep(self.step_delay)

    def move_steps(self, nsteps):
        for _ in range(nsteps):
            self._set_state(self.step_cycle[self.cur_step % self.cycle_len])
            self.cur_step += 1
