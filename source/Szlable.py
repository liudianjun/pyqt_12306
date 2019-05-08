from PyQt5.Qt import *

class SzLable(QLabel):

    def mousePressEvent(self, evt):
        # 鼠标点击事件
        super().mousePressEvent(evt)
        print(evt.pos())

        #显示点击的位置

        point = QPushButton(self)
        point.resize(20,20)
        point.move(evt.pos() - QPoint(10,10))
        point.setStyleSheet('background-color:green; border-radius:10px')
        point.show()

        #监听鼠标点击事件，再次点击取消
        point.clicked.connect(lambda _, btn=point:btn.deleteLater())

    def get_point(self):

        res = ','.join(['{},{}'.format(child.x()+10,child.y()-20) for child in self.children() if child.inherits('QPushButton')])
        # print('res')
        # print(type(res), len(res))
        # print(res)
        return res

    def clear_points(self):
        # 清空验证码
        [child.deleteLater() for child in self.children() if child.inherits('QPushButton')]

