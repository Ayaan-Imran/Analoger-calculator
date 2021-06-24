from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ColorProperty
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# MUST CHANGE THE COLOR PROB WHEN THE SURPRISE BUTTON IS CLICKED
# Set the size of the window
Window.size = (300, 500)


# Create main layout
class Everything(GridLayout):
    equation = StringProperty("")
    decimal_point_added = False
    operators = ["+", "-", "*", "/"]

    special_button_mode = "display"

    number_pad_fg_color = ColorProperty([144/255, 224/255, 239/255, 1])
    operators_bg_color = ColorProperty([111/225, 200/255, 249/255, 1])
    surprise_button_fg_color = ColorProperty([0, 0, 1, 1])
    surprise_button_bg_color = ColorProperty([160/255, 196/255, 1, 1])
    equal_to_bg_color = ColorProperty([155/255, 246/255, 255/255, 1])
    text_input_color = ColorProperty([0, 180/255, 216/255, 1])

    equal_to_button_pressed = False

    def add_to_equation(self, adding_object):
        # Check if the adding object is a decimal point
        if adding_object == ".":
            # Check if the equal to button was pressed:
            if self.equal_to_button_pressed == True:
                self.clear_screen()
                self.equal_to_button_pressed = False

            # Check if decimal point is added
            if self.decimal_point_added == False:
                self.decimal_point_added = True # Tell the calc that the . is added
                self.equation += adding_object # Add the . point

        # Check if the adding object is an operator. Doing this because we don't want double operator. E.g. 9**********88//////
        elif adding_object in self.operators:
            try:
                self.equal_to_button_pressed = False # Tell the calculator that the equal to button is no longer valid because some other button is being pressed
                if self.equation[-1] in self.operators:
                    pass
                else:
                    self.equation += adding_object
                    self.decimal_point_added = False  # Tells a new number has started

            except IndexError:
                pass

        # Check if new number has started
        elif (adding_object == "(") or (adding_object == ")"):
            # Check if the equal to button was pressed:
            if self.equal_to_button_pressed == True:
                self.clear_screen()
                self.equal_to_button_pressed = False

            # Check is the brackets are closed or not
            if adding_object == ")":
                self.decimal_point_added = True
                self.equation += adding_object
            else:
                self.decimal_point_added = False  # Tells a new number has started
                self.equation += adding_object

        else:
            # Check if the equal to button was pressed:
            if self.equal_to_button_pressed == True:
                self.clear_screen()
                self.equal_to_button_pressed = False

            self.equation += adding_object # Add the object

    def clear_screen(self):
        self.equation = ""
        self.decimal_point_added = False

    def del_last_object(self):
        self.equation = self.equation[:-1]

    def happy_birthday_wish(self, widget):
        if self.special_button_mode == "display":
            self.saved_text_input_fg_color = self.text_input_color # Saves the current color
            self.text_input_color = get_color_from_hex("#ffba08") # Change the color of the screen

            self.saved_equation = self.equation # Save the current equation
            self.equation = "HAPPY BIRTHDAY!" # Say happy birthday

            self.special_button_mode = "remove"
            widget.text = "<"

        else:
            self.equation = self.saved_equation
            self.text_input_color = self.saved_text_input_fg_color

            self.special_button_mode = "display"
            widget.text = ""

    def equal_to(self):
        # Check if there is zero division error
        try:
            # Check if there is any number or operators in the equation
            if len(self.equation) != 0:
                if self.equation.count("(") != self.equation.count(")"):
                    self.equation = "WRONG INSERTION OF BRACKETS!\n\nHit C to clear\n"

                elif self.equation[-1] in self.operators:
                    self.equation = "OPERATOR AT THE END!\n\nHit C to clear\n"

                else:
                    self.equation = str(eval(self.equation))

            # Check if the equation has decimal point
            if "." in self.equation:
                # Check if the numbers after the decimal point is a 0
                if self.equation.split(".")[1] == "0":
                    self.decimal_point_added = False
                    self.equation = self.equation.split(".")[0] # Remove the parts after the .0

                else:
                    self.decimal_point_added = True

            # Let the calculator know that the = is pressed
            self.equal_to_button_pressed = True

        except ZeroDivisionError:
            self.equation = "ZERO DIVISION ERROR\n\nHit C to clear this error\n"

        except SyntaxError:
            self.equation = "SOME KIND OF ERROR OCCURRED\n\nHit C to clear this error\n"

        except TypeError:
            self.equation = "SOME KIND OF ERROR OCCURRED\nPossibly no operator between brackets\n\nHit C to clear\n"


    def change_color_theme_to_blue(self):
        self.number_pad_fg_color = [144 / 255, 224 / 255, 239 / 255, 1]
        self.operators_bg_color = [111 / 225, 200 / 255, 249 / 255, 1]
        self.surprise_button_fg_color = [0, 0, 1, 1]
        self.surprise_button_bg_color = [160/255, 196/255, 1]
        self.equal_to_bg_color = [155/255, 246/255, 255/255, 1]
        self.text_input_color = [0, 180/255, 216/255, 1]

    def change_color_theme_to_green(self):
        self.number_pad_fg_color = [128/255, 185/255, 24/255, 1]
        self.operators_bg_color = [85/255, 166/255, 48/255, 1]
        self.surprise_button_fg_color = [0, 1, 0, 1]
        self.surprise_button_bg_color = [43/255, 147/255, 72/255, 1]
        self.equal_to_bg_color = [170/255, 204/255, 0, 1]
        self.text_input_color = [212/255, 215/255, 0, 1]

    def change_color_theme_to_red(self):
        self.number_pad_fg_color = [255/255, 10/255, 84/255, 1]
        self.operators_bg_color = [255/255, 112/255, 150/255, 1]
        self.surprise_button_fg_color = get_color_from_hex("#e5383b")
        self.surprise_button_bg_color = get_color_from_hex("#9e2a2b")
        self.equal_to_bg_color = get_color_from_hex("#e63946")
        self.text_input_color = [255/255, 10/255, 84/255, 1]

# Create calculator app class
class CalculatorApp(App):
    pass

# Run the app
CalculatorApp().run()