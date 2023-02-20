import sys
from PyQt6 import QtWidgets, uic

from dialog3 import Ui_Dialog


class dialog3(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(dialog3, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = dialog3()
window.show()
app.exec()