from manimlib.imports import *
import math
import numpy as np


class Omkar(GraphScene) :

    CONFIG = {
            'x_min' : -5,
            'x_max' : 5,
            'y_min' : -1,
            'y_max' : 5,
            'graph_origin' : 2 * DOWN,
            'function_color' : WHITE,
            'axes_color' : BLUE
            }

    def construct(self) :
        #Make objects
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "sinx + |x - {2}|")

        func_graph_2 = self.get_graph(self.func_to_graph_2, self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "cosx + |x^{5} - {2}|")
        
        
        vert_line = self.get_vertical_line_to_graph(1, func_graph, color = YELLOW)
        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x, y, color = YELLOW)
        point = Dot(self.coords_to_point(1, self.func_to_graph(1)))
        
        #Animate
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)

    def func_to_graph(self, x):
        return (np.sin(x) + abs(x - 2))

    def func_to_graph_2(self, x):
        return (np.cos(x) + abs(x**5 - 2))


class Rects(GraphScene) :

    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
        'axes_color' : BLUE
    }
    '''
    CONFIG = {
            'x_min' : -1,
            'x_max' : 10,
            'y_min' : -1,
            'y_max' : 5,
            'graph_origin' : 2 * DOWN,
            'function_color' : WHITE,
            'axes_color' : BLUE
            }
        '''

    def construct(self) :
        self.setup_axes(animate =True)
        func_graph = self.get_graph(lambda t : 0.1 * (t + 3-5) * (t - 3-5) * (t-5) + 5, x_min = 0.5, x_max = 9.5, color = YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "0.1(x + 2)(x - 2)(x-5) + 5", color = YELLOW)
        graph_lab.scale(0.8)
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.show_rects()
    
    def show_rects(self) :
        rect_list = self.get_riemann_rectangles_list(
            self.get_graph(lambda t : 0.1 * (t + 3-5) * (t - 3-5) * (t-5) + 5, x_min = 0, x_max = 8),
            n_iterations = 4,
            max_dx = 1.0,
            x_min = 1,
            x_max = 8
        )
        flat_graph = self.get_graph(lambda t : 0)
        rects = self.get_riemann_rectangles(
            flat_graph, x_min = -3, x_max = 3, dx = 1.0
        )

        for new_rects in rect_list :
            new_rects.set_fill(opacity = 0.8)
            rects.align_submobjects(new_rects)
            for alt_rect in rects[::2] :
                alt_rect.set_fill(opacity = 0)
            self.play(Transform(
                rects, new_rects,
                run_time =2,
                lag_ratio = 0.5
            ))
        self.wait()
    