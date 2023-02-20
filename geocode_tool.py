import sys
from PyQt6 import QtWidgets, uic

from geocode_ui import Ui_Dialog


class Geocode(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Geocode, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = Geocode()
window.show()
app.exec()