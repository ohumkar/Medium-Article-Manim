from manimlib.imports import*
import numpy as np
import math


class Neuron(GraphScene) :
    CONFIG = {
        'x_min' : -15,
        'x_max' : 15,
        "x_tick_frequency" : 5,
        'y_min' : 0,
        'y_max' : 1,
        "y_tick_frequency" : 0.5,
        'y_axis_height' : 4,
        'graph_origin' : 1.2 * DOWN,
        'function_color' : YELLOW,
        'axes_color' : BLUE
        }



    def construct(self) :
        #Get Objects
        self.setup_axes()
        sigmoid = self.get_graph(lambda x : 1 / (1 + np.exp(-x)), self.function_color)
        tower_one = self.get_graph(lambda x : 1 / (1 + np.exp(-1000*(x -5))))
        graph_label = self.get_graph_label(sigmoid, label = r"\frac{1}{1+e^{-(wx+b)}}", color = WHITE)
        #label = TexMobject(r"\frac{1}{1+e^{-(wx+b)}}")


        # f(x) = x**2
        #fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        w_value = ValueTracker(1)
        b_value = ValueTracker(0)
        #fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        w_tex = DecimalNumber(w_value.get_value()).add_updater(lambda v: v.set_value(w_value.get_value()))
        b_tex = DecimalNumber(b_value.get_value()).add_updater(lambda v: v.set_value(b_value.get_value()))
        #fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        w_label = TexMobject("w =", color = ORANGE)
        b_label = TexMobject("b =", color = ORANGE)
        #fx_label = TexMobject("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(w_tex,b_tex,w_label,b_label).scale(1)
        #VGroup(w_tex, b_tex).arrange_submobjects(0.5*DOWN,buff=1)
        VGroup(b_tex, w_tex).arrange_submobjects(5*LEFT,buff= 0.5)
        # Align labels and numbers
        w_label.next_to(w_tex,LEFT, buff=0.2,aligned_edge=w_label.get_bottom())
        b_label.next_to(b_tex,LEFT, buff=0.2,aligned_edge=b_label.get_bottom())

        

        def increase_w(curve, dt) :
            alpha = interpolate(1, 10 , dt)
            sigmoid_new = self.get_graph(lambda x : 1 / (1 + np.exp(-alpha * x)))
            sigmoid.become(sigmoid_new)
        def label_w_up(number, dt, l = 1, u = 10) :
            alpha = interpolate(1,10, dt)
            number.set_value(alpha)

        def decrease_w(curve, dt) :
            alpha = interpolate(10, -10 , dt)
            sigmoid_new = self.get_graph(lambda x : 1 / (1 + np.exp(-alpha * x)))
            sigmoid.become(sigmoid_new)
        def label_w_down(number, dt) :
            alpha = interpolate(10,-10, dt)
            number.set_value(alpha)
                    
        def increase_b(curve, dt) :
            alpha = interpolate(0, 10 , dt)
            sigmoid_new = self.get_graph(lambda x : 1 / (1 + np.exp(-(x) + alpha)))
            sigmoid.become(sigmoid_new)
        def label_b_up(number, dt) :
            alpha = interpolate(0,10, dt)
            number.set_value(alpha)

        def decrease_b(curve, dt) :
            alpha = interpolate(10, -10 , dt)
            sigmoid_new = self.get_graph(lambda x : 1 / (1 + np.exp(-(x) + alpha)))
            sigmoid.become(sigmoid_new)
        def label_b_down(number, dt) :
            alpha = interpolate(10,-10, dt)
            number.set_value(alpha)

        #Animate
        self.play(ShowCreation(sigmoid), Write(graph_label.move_to(3.5*RIGHT+1*UP)), runtime = 2)
        self.wait(1)
        self.add(group.move_to(2.5*DOWN))
        #self.wait(3)
        self.play(UpdateFromAlphaFunc(sigmoid, increase_w), UpdateFromAlphaFunc(w_value, label_w_up))
        #self.play(x_value.set_value,10, rate_func=linear,run_time=1.5)
        self.wait(1)
        self.play(UpdateFromAlphaFunc(sigmoid, decrease_w),UpdateFromAlphaFunc(w_value, label_w_down), rate_func= lambda t: t, runtime = 3.5)
        self.wait(2)
        #self.play(w_tex.set_value(1))
        self.play(UpdateFromAlphaFunc(sigmoid, increase_b), UpdateFromAlphaFunc(b_value, label_b_up))
        self.wait(1)
        self.play(UpdateFromAlphaFunc(sigmoid, decrease_b), UpdateFromAlphaFunc(b_value, label_b_down), rate_func= lambda t: t, runtime = 3.5)
        self.wait(2)
        self.play(FadeOut(group), FadeOut(sigmoid), FadeOut(graph_label), FadeOut(self.axes))
        # self.play(Transform(sigmoid, tower_one))
        # self.wait(2)
        
        #self.play(UpdateFromAlphaFunc(sigmoid, update_w),rate_func=lambda t: 1-smooth(t))
        self.wait(1)

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = -15
        end_label_x = 15
        step_x = 5
        #   For y
        init_label_y = 0
        end_label_y = 1
        step_y = 1
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT

        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class Track(GraphScene) :
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        x_value = ValueTracker(1)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = TexMobject("x = ")
        fx_label = TexMobject("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(0.5)
        VGroup(x_tex, fx_tex).arrange_submobjects(0.5*DOWN,buff=1.5)
        # Align labels and numbers
        x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())


        
        self.add(group.move_to(ORIGIN))
        self.wait(3)
        # self.play(
        #     (x_value.set_value,10,
        #     rate_func=linear,
        #     run_time=1.5
        #     ))
        # self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=1.5
            )
        self.wait(3)

class New(GraphScene) :
    CONFIG = {
        'x_min' : -15,
        'x_max' : 15,
        "x_tick_frequency" : 5,
        'y_min' : 0,
        'y_max' : 1,
        'y_axis_height' : 4,
        'graph_origin' : 1.5 * DOWN,
        'function_color' : WHITE,
        'axes_color' : BLUE
        }

    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x : 1 / (1 + np.exp(-(x)*dx)),
            x_min=-10,x_max=10
        )

    def construct(self) :
        #Get Objects
        self.setup_axes()
        sine_function=self.get_sine_wave()
        #graph_label = self.get_graph_label(sine_function, label = "1/1 + e^{-x}")
        d_theta=ValueTracker(0)
                
        def update_wave(func):
            func.become(
                self.get_sine_wave(dx=d_theta.get_value())
            )
            return func

        sine_function.add_updater(update_wave)
        self.play(ShowCreation(sine_function), runtime = 2)
        self.wait(1)
        self.play(d_theta.increment_value,10,rate_func=linear)
        self.wait(1)


    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = -15
        end_label_x = 15
        step_x = 5
        #   For y
        init_label_y = 0
        end_label_y = 1
        step_y = 1
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT

        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

    