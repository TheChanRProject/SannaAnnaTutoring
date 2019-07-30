import math
from IPython.display import display, Markdown
display(Markdown("# $60^{\circ} = x \sqrt{3} $"))
display(Markdown("# $30^{\circ} = x $"))
display(Markdown("# $90^{\circ} = 2x $"))
# 30 - 60 - 90 Right  Triangles

display(Markdown("# $A = \\frac{1}{2}bh$"))
class Special_Triangle_One():
    def __init__(self, x: float, side: str):
        if side.lower() == "thirty":
            self.thirty = x
            self.sixty = self.thirty * math.sqrt(3)
            self.ninety = 2*x
        elif side.lower() == "sixty":
            self.thirty = (x * math.sqrt(3)) / 3
            self.sixty = x
            self.ninety = (2 * x * math.sqrt(3)) / 3
        else:
            self.thirty = x / 2
            self.sixty = self.thirty * math.sqrt(3)
            self.ninety = x

    def triangle_area(self, b, h):
        return 0.5 * b * h

    def triangle_perimeter(self):
        return self.thirty + self.sixty + self.ninety

trial_one = Special_Triangle_One(x=4, side="sixty")
trial_one.thirty
trial_one.ninety
trial_one.triangle_area(trial_one.thirty, trial_one.sixty)

display(Markdown("# $45^{\circ} = x$"))
display(Markdown("# $90^{\circ} = x \\sqrt{2}$"))

class Special_Triangle_Two():
    def __init__(self, x: float, side: str):
        if side.lower() in ["fourty_five", "fourty five", "fourtyfive", "fourty-five"]:
            self.fourty_five = x
            self.ninety = self.fourty_five * math.sqrt(2)
        else:
            self.fourty_five = (x * math.sqrt(2)) / 2
            self.ninety = x
    def area(self, b, h):
        return 0.5*b*h
    def triangle_perimeter(self):
        return 2*self.fourty_five + self.ninety

trial_one = Special_Triangle_Two(x=2, side="ninety")
trial_one.fourty_five
trial_one.area(trial_one.ninety, 3)

def equilateral_triangle_area(s):
    return 0.25 * s**2 * math.sqrt(3)
    
