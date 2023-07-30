from manim import *
from customConfig import *

class Main(Scene): 
    def construct(self):
        backGrid = NumberPlane(**BCKPLANECONFIG)
        frontGrid = NumberPlane(**FRTPLANECONFIG)

        #A2 = PolarPlane(**POLARPLANECONFIG).add_coordinates()
       
        func2 = FunctionGraph(
            lambda x: np.sin(2*x),
            color=RED,
            x_range=[-10, 10]
        )      
        vector1 = Vector([1,0])
        vector2 = Vector([0,1])

        vector2bis = Vector([-1,1])

        self.play(
            Create(backGrid),
            Create(frontGrid),
            Create(vector1),
            Create(vector2)
        )  
        self.wait(1)
        self.play(
            ApplyPointwiseFunction(nonlinearMap, frontGrid),
        ) 
        self.wait(5)

class Linear(LinearTransformationScene):
            def __init__(self):
                LinearTransformationScene.__init__(
                    self,
                    background_plane_kwargs=BCKPLANECONFIG,
                    foreground_plane_kwargs=FRTPLANECONFIG,
                )
            def construct(self):
                matrix = [[1, 1], [1, 2]]

                self.apply_nonlinear_transformation(nonlinearMap)
                self.wait()

class Complex(Scene):
    def construct(self):
        self.plane = ComplexPlane(**PLANECONFIG)
        self.plane.prepare_for_nonlinear_transform()
        
        graph = ParametricFunction(
            lambda t: [t, t/(t-1), 0], 
            t_range=[-20, 20], 
            discontinuities= [1],
            dt= 0.05,
            color=PURPLE_C)               
        
        functionBox = self.createFunctionBox("z - \\frac{1}{z}")
        self.play(
            AnimationGroup(*[
                Create(self.plane),
                #Create(graph),
                Create(functionBox)
            ], lag_ratio = 2, run_time=4),
        )    
        self.wait(1)
        self.play(
            ApplyComplexFunction(self.transform, self.plane)
        )
        self.wait(4)

    def createFunctionBox(self, functionName):
        funcTag = MathTex(r"f : z \longrightarrow " + functionName).move_to(DR * 3 + RIGHT * 2)
        box = Rectangle(
            height=2, width=4, fill_color="#2B2C2C", 
            fill_opacity=1, stroke_color="#2B2C2C"
        ).move_to(DR * 3 + RIGHT * 2.1)
        group = VGroup().add(box, funcTag)
        group.set_z_index(3)
        return group

    def transform(self, z):
        if abs(z) < 0.05:
            return z
        return (1)/(z)

class VectorField(Scene):
    def construct(self):
        func = lambda pos: -5*pos[1]/np.exp(pos[0]**2 + pos[1]**2) * RIGHT + 5*pos[0]/np.exp(pos[0]**2 + pos[1]**2) * UP
        vector_field = ArrowVectorField(func)
        axes = Axes(**AXISCONFIG)

        dot = Dot().move_to([1, 0, 0])

        self.play(
            Create(vector_field),
            Create(axes),
            Create(dot),
        )
        self.wait(3)
        
        vector_field.nudge(dot, 1, 500)
        self.wait(3)
        dot.add_updater(vector_field.get_nudge_updater())
        self.wait()





