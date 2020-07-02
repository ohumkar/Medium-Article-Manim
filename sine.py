from manimlib.imports import *
import numpy as np
import math


class SineWave(Scene):
    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x : 1 / (1 + np.exp(-(x)*dx)),
            x_min=-10,x_max=10
        )

    def construct(self):
        sine_function=self.get_sine_wave()
        d_theta=ValueTracker(0)
        def update_wave(func):
            func.become(
                self.get_sine_wave(dx=d_theta.get_value())
            )
            return func
        sine_function.add_updater(update_wave)
        self.play(ShowCreation(sine_function), runtime = 2)
        self.play(d_theta.increment_value,10,rate_func=linear)
        self.wait()