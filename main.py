from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
kiwoom = Kiwoom()

fids = get_fid("체결시간")
codes = '005930;007700;000660;'
kiwoom.set_real_reg("1000", codes, fids, "0")

app.exec_()
