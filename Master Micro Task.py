import sys
import pytest
from PySide2 import QtWidgets, QtGui
import matplotlib.pyplot as plt


class FunctionPlotter(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")

        # Create a text box for the user to enter the function.
        self.function_textbox = QtWidgets.QLineEdit()

        # Create a label for the min value of x.
        self.min_label = QtWidgets.QLabel("Min x:")

        # Create a text box for the user to enter the min value of x.
        self.min_textbox = QtWidgets.QLineEdit()

        # Create a label for the max value of x.
        self.max_label = QtWidgets.QLabel("Max x:")

        # Create a text box for the user to enter the max value of x.
        self.max_textbox = QtWidgets.QLineEdit()

        # Create a button to plot the function.
        self.plot_button = QtWidgets.QPushButton("Plot")

        # Create a layout to arrange the widgets.
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.function_textbox)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_textbox)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_textbox)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

        # Connect the plot button to the plot function.
        self.plot_button.clicked.connect(self.plot)

    def plot(self):
        # Get the function from the user.
        function_string = self.function_textbox.text()

        # Get the min and max values of x from the user.
        min_x = float(self.min_textbox.text())
        max_x = float(self.max_textbox.text())

        # Evaluate the function at a range of x values.
        x_values = np.linspace(min_x, max_x, 100)
        y_values = eval(function_string)

        # Plot the function.
        plt.plot(x_values, y_values)
        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    app.exec_()
