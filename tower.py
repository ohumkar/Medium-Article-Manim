from manimlib.imports import*
import numpy as np
import math


class Add(GraphScene) :
    CONFIG = {
        'x_min' : -4,
        'x_max' : 4,
        'y_min' : -3,
        'y_max' : 3,
        'y_axis_height' : 6,
        'graph_origin' : 0.1*UP  ,
        'axes_color' : BLUE
        }



    def construct(self) :
        #Get Objects
        self.setup_axes()
        centre = -1
        sig_one = self.get_graph(lambda x : 1 / (1 + np.exp(-10000*(x-(centre)))), color = RED)
        sig_two = self.get_graph(lambda x : -1 / (1 + np.exp(-10000*(x-(centre + 2)))), color = YELLOW)
        tower = self.get_graph(lambda x : 1 / (1 + np.exp(-10000*(x-(centre)))) -1 / (1 + np.exp(-10000*(x-(centre+2)))), color = GREEN)

        label_one = self.get_graph_label(sig_one, label = r"\frac{1}{1+e^{-(wx+b)}}", color = RED)
        label_two = self.get_graph_label(sig_one, label = r"-\frac{1}{1+e^{-(wx+b+db)}}", color = YELLOW)
        result = self.get_graph_label(sig_one, label = r"\frac{1}{1+e^{-(wx+b)}} - \frac{1}{1+e^{-(wx+b+db)}}", color = GREEN).scale(0.8)


        '''
        By taking a linear combination of two sigmoids we can a tower function
        The resulting function can also Scaled and Shifted as required

        sig = r"\frac{1}{1+e^{-(wx+b)}}"

        

        '''


        def height_one(curve, dt) :
            alpha = interpolate(1, 2.5 , dt)
            tower_new = self.get_graph(lambda x : alpha * (1 / (1 + np.exp(-10000*(x-(centre)))) -1 / (1 + np.exp(-10000*(x-(centre+2))))))
            tower.become(tower_new)
        def height_two(curve, dt) :
            alpha = interpolate(1, -2.5 , dt)
            tower_new = self.get_graph(lambda x : alpha * (1 / (1 + np.exp(-10000*(x-(centre)))) -1 / (1 + np.exp(-10000*(x-(centre+2))))))
            tower.become(tower_new)
                    
        def pos_one(curve, dt) :
            alpha = interpolate(-1, 2 , dt)
            tower_new = self.get_graph(lambda x : 1 / (1 + np.exp(-10000*(x-(alpha)))) -1 / (1 + np.exp(-10000*(x-(alpha+2)))))
            tower.become(tower_new)
        def pos_two(curve, dt) :
            alpha = interpolate(-1, -4 , dt)
            tower_new = self.get_graph(lambda x : 1 / (1 + np.exp(-10000*(x-(alpha)))) -1 / (1 + np.exp(-10000*(x-(alpha+2)))))
            tower.become(tower_new)

    
        
        #graph_label = self.get_graph_label(sigmoid, label = "1/1 + e^{-x}")


        #Animate
        self.play(ShowCreation(sig_one), Write(label_one.move_to(3*LEFT+2*UP)))
        self.wait(1)
        self.play(ShowCreation(sig_two),Write(label_two.move_to(3*RIGHT+2*DOWN)))
        self.wait(1)
        self.play(ReplacementTransform(sig_one, tower), ReplacementTransform(sig_two, tower),
                ReplacementTransform(label_one, result.move_to(3*RIGHT+2.5*UP)), ReplacementTransform(label_two, result.move_to(3*RIGHT+2.5*UP)))
        self.wait(1)
        self.play(FadeOut(result))
        self.play(UpdateFromAlphaFunc(tower, height_one), rate_func = there_and_back, runtime = 1.5)
        self.play(UpdateFromAlphaFunc(tower, height_two), rate_func = there_and_back, runtime = 1.5)
        self.wait(1)
        self.play(UpdateFromAlphaFunc(tower, pos_one), rate_func = there_and_back, runtime = 1.5)
        self.play(UpdateFromAlphaFunc(tower, pos_two), rate_func = there_and_back, runtime = 1.5)
        self.wait(1)
        #self.play(UpdateFromAlphaFunc(sigmoid, update_w),rate_func=lambda t: 1-smooth(t))

    

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = -4
        end_label_x = 4
        step_x = 2
        #   For y
        init_label_y = -1
        end_label_y = 3
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
