import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter
import logging
logging.basicConfig(level=logging.DEBUG, filename="./data/converter.log")
logger = logging.getLogger()


class CurrencyConv(QtWidgets.QMainWindow):

    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setWindowTitle('Currency Converter')
        self.setWindowIcon(QIcon('data\icon_converter.png'))

        self.ui.input_currency.setPlaceholderText('Какая валюта у меня есть?')
        self.ui.input_amount.setPlaceholderText('Сколько нужно перевести?')
        self.ui.output_currency.setPlaceholderText('В какую валюту?')
        self.ui.output_amount.setPlaceholderText('Я получу:')
        self.ui.pushButton.clicked.connect(self.converter)


    def converter(self):
        try:
            c = CurrencyConverter() # TODO variable
            input_currency = self.ui.input_currency.text()
            output_currency = self.ui.output_currency.text()
            input_amount = self.ui.input_amount.text() # TODO maybe float?

            output_amount = round(c.convert(input_amount, input_currency, output_currency), 2)
            # output_amount = round(c.convert(input_amount, '%s' % input_currency, '%s' % output_currency), 2)
            self.ui.output_amount.setText(str(output_amount))
        except Exception as e:
            logger.error(f'error: {e}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = CurrencyConv()
    application.show()


    sys.exit(app.exec())


# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QIcon
# from ui import Ui_MainWindow
# from currency_converter import CurrencyConverter
#
#
# class CurrencyConv(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(CurrencyConv, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.init_UI()
#
#     def init_UI(self):
#         self.setWindowTitle('Конвертер валют')
#         self.setWindowIcon(QIcon('exchanging.png'))
#         self.ui.input_currency.setPlaceholderText('Из валюты:')
#         self.ui.input_amount.setPlaceholderText('У меня есть:')
#         self.ui.output_currency.setPlaceholderText('В валюту:')
#         self.ui.output_amount.setPlaceholderText('Я получу:')
#         self.ui.pushButton.clicked.connect(self.converter)
#
#     def converter(self):
#         c = CurrencyConverter()
#         input_currency = self.ui.input_currency.text()
#         output_currency = self.ui.output_currency.text()
#         input_amount = int(self.ui.input_amount.text())
#         output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
#         self.ui.output_amount.setText(str(output_amount))
#
#
# app = QtWidgets.QApplication([])
# application = CurrencyConv()
# application.show()
#
# sys.exit(app.exec())