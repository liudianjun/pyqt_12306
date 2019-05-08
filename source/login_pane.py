from PyQt5.Qt import *
from source.ui.login_windows import Ui_Form
from source.api.api_login import Api_Login
from source.api.YDMHTTP import YDMHttp


class Login_pane(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(Form=self)
        self.refresh_code()

    def login_check(self):

        # print('登录')
        yzm_point = self.yzm.get_point()
        result_code = Api_Login.check_yzm(yzm_point)
        # 判断是否校验验证码
        if len(result_code) == 0:
            print('点击验证码')
            return None

        if result_code == '4':
            print('验证码校验成功')
            self.yzm.clear_points()
            print(self.username_text.text(), self.password_text.text(), yzm_point)
            Api_Login.check_login(self.username_text.text(), self.password_text.text(), yzm_point)
            result_code = Api_Login.author_cli()
            if result_code == 0:
                # 获取登录信息
                Api_Login.get_user_base_info()
                # 查票
                train = Api_Login.query_tickets()
                # 验证登录状态
                Api_Login.check_user()
                # 订票
                Api_Login.book_ticket(train[-1])
                # 获取token
                token,key_check_isChange = Api_Login.get_token()
                # 获取联系人
                Api_Login.getPassenger_info(token)

                # 检查订单信息
                Api_Login.check_order_info(token)

                # 获取订单队列
                Api_Login.get_queue_count(train[-1], token)

                # 下订单
                Api_Login.confirmSingleForQueue(token, key_check_isChange, train[-1])

        else:
            print('验证码错误')
            self.refresh_code()
            self.yzm.clear_points()


    def refresh_code(self):
        yzm = Api_Login.get_yzm()
        self.yzm_url = yzm
        print(yzm)
        pixmap = QPixmap(yzm)
        self.yzm.setPixmap(pixmap)
        self.yzm.clear_points()

    def dm_auto(self):
        print('打码')
        dm = YDMHttp()
        print(dm.get_yzm_position(self.yzm_url))

    def auto_enable_login_btn(self):
        if len(self.username_text.text()) == 0 or len(self.password_text.text()) == 0:
            self.login_btn.setEnabled(False)
        else:
            self.login_btn.setEnabled(True)

if __name__ == '__main__':
    import sys
    window = QApplication(sys.argv)

    login = Login_pane()
    login.show()

    sys.exit(window.exec_())