from api.Kiwoom import *
import sys
app = QApplication(sys.argv)
kiwoom = Kiwoom()
kiwoom.get_account_number()
app.exec_()