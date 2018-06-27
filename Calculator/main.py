import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
kivy.require("1.10.0")


# creating the view and GUI for calculator app
class CalcGrid(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                function = calculation.split()
                addsub = []
                idx = 0
                while idx < len(function):
                    i = function[idx]
                    print(i)
                    if i == "+":
                        pass
                    elif i == "-":
                        addsub.append(-1*int(function[idx+1]))
                        idx += 1
                    elif i == "*":
                        i = addsub[-1] * int(function[idx+1])
                        addsub[-1] = i
                        idx += 1
                    elif i == "/":
                        i = addsub[-1] / int(function[idx+1])
                        addsub[-1] = i
                        idx += 1
                    else: addsub.append(int(i))
                    idx += 1
                self.display.text = str(sum(addsub))
                # alternate calculation method, but may be unsecure:
                # self.display.text = str(eval(calculation))
            except:
                self.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalcGrid()

calcApp = CalculatorApp()
calcApp.run()
