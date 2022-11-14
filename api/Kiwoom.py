from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._make_kiwoom_instance()
        self._set_signal_slots()
        self._comm_connect()

        self.account_number = self.get_account_number()

    def _make_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        """API로 보내는 요청들을 받아올 slot을 등록하는 함수"""
        # 로그인 응답의 결과를 _on_login_connect을 통해 받도록 설정
        self.OnEventConnect.connect(self._login_slot)

    def _login_slot(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("not connected")

        self.login_event_loop.exit()

    def _comm_connect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def get_account_number(self, tag="ACCNO"):
        account_list = self.dynamicCall("GetLoginInfo(QString)", tag)  # tag로 전달한 요청에 대한 응답을 받아옴
        account_number = account_list.split(';')[0]
        print(account_number, account_list)
        return account_number
