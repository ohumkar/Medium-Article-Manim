from manimlib.imports import*
import numpy as numpy
import math

class Lines(GraphScene) :

    CONFIG = {
        'x_min' : -1,
        'x_max' : 8,
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        'y_min' : -1,
        'y_max' : 8,
        'y_axis_height' : 6,
        'x_axis_width' : 8,
        'graph_origin' : 3*DOWN + 3.3*LEFT,
        'function_color' : WHITE,
        'axes_color' : BLUE
        }

    def construct(self) :
        self.setup_axes()
        line_one = self.get_graph(lambda x: -2*x + 3, x_min = -1, x_max = 2, color = RED)
        label_one = TexMobject(r"-2x + 3", color = RED)

        line_two = self.get_graph(lambda x: -0.7*x + 5,  x_min = -1, x_max = 8, color = YELLOW)
        label_two = TexMobject( r"-0.7x + 5", color = YELLOW)

        line_three = self.get_graph(lambda x: 0.5*x - 0.7,  x_min = -1, x_max = 8, color = GREEN)
        label_three = TexMobject(r"0.5x - 0.7", color = GREEN)

        group_one = VGroup(label_one, label_two, label_three).scale(0.8)
        group_one.arrange_submobjects(0.4*DOWN, buff = 0.7, aligned_edge = label_one.get_left())
        group_one.move_to(3*RIGHT+1.5*UP)


        max_one = self.get_graph(lambda x: max(0, -2*x + 3), x_min = -1, x_max = 8, color = RED)
        lm_one = TexMobject(r"\max \left ( 0 ,-2x + 3\right )", color = RED)

        max_two = self.get_graph(lambda x: max(0, -0.7*x + 5),  x_min = -1, x_max = 8, color = YELLOW)
        lm_two = TexMobject(r"\max \left ( 0 ,-0.7x + 5\right )", color = YELLOW)

        max_three = self.get_graph(lambda x: max(0, 0.5*x - 0.7),  x_min = -1, x_max = 8, color = GREEN)
        lm_three = TexMobject(r"\max \left ( 0 ,0.5x - 0.7\right )", color = GREEN)

        group_two = VGroup(lm_one, lm_two, lm_three).scale(0.8)
        group_two.arrange_submobjects(0.4*DOWN, buff = 0.7, aligned_edge = lm_one.get_left())
        group_two.move_to(2.5*RIGHT+1.5*UP)
        

        note_one =  TexMobject("Output\,\,from\,\,3\,\,Hidden\,\,Neurons").scale(0.8)
        note_one.move_to(3.3*UP)

        note_two =  TexMobject("Output\,\,after\,\,passing\,\,through\,\,ReLu\,\,activation\,\,function").scale(0.8)
        note_two.move_to(3.5*UP)

        note_three =  TexMobject("Addition\,\,of\,\,the\,\,activations").scale(0.8)
        

        #Animate
        self.play(Write(note_one),
                ShowCreation(line_one), ShowCreation(line_two), ShowCreation(line_three),Write(group_one))       
        self.wait(4)

        self.play(ReplacementTransform(note_one,note_two), ReplacementTransform(group_one,group_two),
                Transform(line_one, max_one), Transform(line_two, max_two), Transform(line_three, max_three))
        self.wait(4)

        self.play(FadeOut(note_two), FadeOut(group_two),FadeOut(self.axes),FadeOut(line_one), FadeOut(line_two), FadeOut(line_three),
                    FadeOut(label_one), FadeOut(label_two), FadeOut(label_three))
        self.wait(1)
        self.play(Write(note_three))
        self.wait(1)
        self.play(FadeOut(note_three))
        self.wait(1)
    
       
    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = 0
        end_label_x = 8
        step_x = 2
        #   For y
        init_label_y = 0
        end_label_y = 8
        step_y = 2
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

class Final(GraphScene) :
    CONFIG = {
        'x_min' : -1,
        'x_max' : 11,
        "x_tick_frequency" : 2,
        "y_tick_frequency" : 2,
        'y_min' : -1,
        'y_max' : 11,
        #'y_axis_height' : 4,
        'graph_origin' : 2.5*DOWN + 3.5*LEFT,
        'function_color' : WHITE,
        'axes_color' : BLUE
        }

    def construct(self) :
        self.setup_axes()
        result = self.get_graph(lambda x: max(0, -2*x + 3) + max(0, -0.7*x + 5) + max(0, 0.5*x - 0.7),
                                x_min = -1, x_max = 11, color = GOLD)
        label = TexMobject(r"\max \left ( 0 ,-2x + 3\right ) \\+  \,\,\max \left ( 0 ,-0.7x + 5\right )\\ \,\,+ \,\,\max \left ( 0 ,0.5x - 0.7\right )", color = GOLD)
        label.scale(0.7)
        label.move_to(2*UP+1*RIGHT)
        self.play(ShowCreation(result), Write(label), runtime = 2)
        self.wait(2.5)
        #self.setup_axes()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = -1
        end_label_x = 11
        step_x = 2
        #   For y
        init_label_y = -1
        end_label_y = 11
        step_y = 2
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