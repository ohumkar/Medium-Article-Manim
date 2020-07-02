from manimlib.imports import *

location = 2

class SingleSurface(ParametricSurface):
    def __init__(self, origin = 1, rang = BLUE_D, axis = 'x', negative = False, **kwargs):
        self.origin = origin
        self.negative = negative
        self.rang = rang
        kwargs = {
        "u_min": -2,
        "u_max": 2,
        "v_min": -2,
        "v_max": 2,
        "checkerboard_colors": [self.rang]
        }
        if axis == 'x' :
            ParametricSurface.__init__(self, self.func_x, **kwargs)
        elif axis == 'y' :
            ParametricSurface.__init__(self, self.func_y, **kwargs)

    def func_x(self, x, y):
        if self.negative :
            return np.array([ x, y, -1/(1+np.exp(-(50*(x-self.origin)))) ] )
        else :
            return np.array([ x, y, 1/(1+np.exp(-(50*(x-self.origin)))) ] )
    
    def func_y(self, x, y):
        if self.negative :
            return np.array([ x, y, -1/(1+np.exp(-(50*(y-self.origin)))) ] )
        else :
            return np.array([ x, y, 1/(1+np.exp(-(50*(y-self.origin)))) ] )

class DoubleSurface(ParametricSurface):
    def __init__(self, rang = BLUE_D, axis = 'x', origin = 2, **kwargs):
        self.origin = origin
        self.axis = axis
        self.rang = rang
        kwargs = {
        "u_min": -2,
        "u_max": 2,
        "v_min": -2,
        "v_max": 2,
        "checkerboard_colors": [self.rang]
        }
        ParametricSurface.__init__(self, self.funcs, **kwargs)

    def funcs(self, x, y):
        if self.axis =='x' :
            return np.array([ x, y, ( (1/(1+np.exp(-(50*(x+self.origin))))) - (1/(1+np.exp(-(50*(x-self.origin))))) ) ] )
        else : 
            return np.array([ x, y, ( (1/(1+np.exp(-(50*(y+self.origin))))) - (1/(1+np.exp(-(50*(y-self.origin))))) ) ] )

class ThreeDSurface(ParametricSurface):
    def __init__(self, rang = BLUE_D, origin = 2, final = False, **kwargs):
        self.final = final
        self.origin = origin
        self.rang = rang
        kwargs = {
        "u_min": -2,
        "u_max": 2,
        "v_min": -2,
        "v_max": 2,
        "checkerboard_colors": [self.rang]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        if self.final : 
            return np.array([ x, y, 2*max(0,( (( (1/(1+np.exp(-(50*(x+self.origin))))) - (1/(1+np.exp(-(50*(x-self.origin))))) ) + ( (1/(1+np.exp(-(50*(y+self.origin))))) - (1/(1+np.exp(-(50*(y-self.origin))))) )) -1) )] )
        else :
            return np.array([ x, y, ( (1/(1+np.exp(-(50*(x+self.origin))))) - (1/(1+np.exp(-(50*(x-self.origin))))) ) + ( (1/(1+np.exp(-(50*(y+self.origin))))) - (1/(1+np.exp(-(50*(y-self.origin))))) )] )
        

class Curve(ThreeDScene) :
    def construct(self) :
        axes = ThreeDAxes()
        #axes.add(axes.get_axis_labels3D())

        sigx_one = SingleSurface(origin = -1,  axis = 'x', rang = YELLOW_E)
        sigx_two = SingleSurface(origin = 1,  axis = 'x', rang = RED_E)
        sigx_two_neg = SingleSurface(origin = 1, axis = 'x', rang = RED_E, negative = True)



        sigy_one = SingleSurface(origin = 2, axis = 'y', rang = YELLOW_E)
        sigy_two = SingleSurface(origin = -2, axis = 'y',rang = RED, negative = True)

        sigx_2d = DoubleSurface(origin = 1, rang = YELLOW_E, axis = 'x')
        sigy_2d = DoubleSurface(origin = 1, rang = RED_E, axis = 'y')

        threed = ThreeDSurface(origin = 1, rang = BLUE_D)
        final = ThreeDSurface(origin = 1, final = True, rang = BLUE_D)

    
        self.set_camera_orientation(phi = 65*DEGREES, theta = -120*DEGREES, distance = 4)
        self.play(ShowCreation(axes))


        #Single tower along x
        self.play(ShowCreation(sigx_one)) #add sig one
        self.wait(1)
        self.play(ShowCreation(sigx_two)) #add sig two
        self.wait(1)
        self.play(ReplacementTransform(sigx_two, sigx_two_neg)) #make negative
        self.wait(1)
        self.play(ReplacementTransform(sigx_two_neg, sigx_2d), ReplacementTransform(sigx_one, sigx_2d)) #convert to XSIGMA
        self.wait(1)

        #self.begin_ambient_camera_rotation(rate=-0.5) 
        
        #Sigmoid tower along y
        #self.play(FadeOut(sigx_2d))
        self.move_camera(phi = 65*DEGREES, theta = -210*DEGREES, distance = 4)
        self.play(ShowCreation(sigy_2d))
        self.wait(1)
        self.move_camera(phi = 45*DEGREES, theta = -120*DEGREES, distance = 4)

        #Three D sigmoid
        self.play(ReplacementTransform(sigy_2d, threed), ReplacementTransform(sigx_2d, threed))
        self.wait(1)
        self.move_camera(phi = 60*DEGREES, theta = -120*DEGREES, distance = 4)
        self.play(ReplacementTransform(threed, final))
        
        #self.wait(1)
        #self.move_camera(phi = 80*DEGREES, theta = 90*DEGREES, distance = 8, runtime = 5)
        self.wait(3)
    