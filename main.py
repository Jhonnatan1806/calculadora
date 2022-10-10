from vistas.calculadora_ui import *
from PyQt5.QtWidgets import QMessageBox
from modulos.binario import Binario
from modulos.complemento1 import Complemento1
from modulos.complemento2 import Complemento2
from modulos.fraccionario import Fraccionario
from modulos.octal import Octal
from modulos.hexadecimal import Hexadecimal
from modulos.IEEE754x32 import IEEE754x32
from modulos.IEEE754x64 import IEEE754x64

from PyQt5.QtWidgets import QPlainTextEdit
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.__init_cmp()
    
    def __init_cmp(self):
        self.text_edit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.text_res.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.copiar.clicked.connect(self.__copiar)
        self.boton.clicked.connect(self.__accion)

    def __copiar(self):
        msg = QMessageBox()
        if self.text_res.toPlainText()!='':
            command = 'echo|set /p=' + self.text_res.toPlainText() + '| clip'
            os.system(command)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Exito")
            msg.setText("Copiado con exito")
        else:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("No hay datos por copiar")
        x = msg.exec_()


    def __accion(self):
        index = self.combo_box.currentIndex()
        # Validamos si es un numero valido
        if index >= 0 and index < 3:
            es_valido =  self.__validar('bin',self.text_edit.toPlainText())
        elif index >= 3 and index < 6:
            es_valido =  self.__validar('bin_frac',self.text_edit.toPlainText())
        elif index >= 6 and index < 8:
            es_valido =  self.__validar('bin',self.text_edit.toPlainText())
        elif index >= 8 and index < 11:
            es_valido =  self.__validar('dec',self.text_edit.toPlainText())
        elif index >= 11 and index < 14:
            es_valido =  self.__validar('dec_frac',self.text_edit.toPlainText())
        elif index >= 14 and index < 16:
            es_valido =  self.__validar('dec',self.text_edit.toPlainText())
        elif index >= 16 and index < 18:
            es_valido =  self.__validar('oct',self.text_edit.toPlainText())
        else:
            es_valido =  self.__validar('hex',self.text_edit.toPlainText())
        # Si es un numero valido realizamos conversion
        if es_valido:
            self.text_res.setPlainText(self.__calcular(index,self.text_edit.toPlainText()))
        # mensaje de error
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Dato invalido")
            x = msg.exec_()

    # Validamos si es un numero valido dependiendo al tipo de numero a convertir
    def __validar(self, tipo, palabra):
        # Verificamos si es binario
        if tipo == 'bin':
            try:
                int(palabra, 2)
                return True
            except ValueError:
                return False
        elif tipo == 'bin_frac':
            p = set(palabra)
            if p == {'0','1','.'} or p == {'0','.'} or p == {'1','.'}:
                return True
            else:
                try:
                    int(palabra, 2)
                    return True
                except ValueError:
                    return False
        # Verificamos si es entero
        elif tipo == 'dec':
            try:
                int(palabra)
                return True
            except ValueError:
                return False
        # Verificamos si es fraccion
        elif tipo == 'dec_frac':
            try:
                float(palabra)
                return True
            except ValueError:
                return False
        # Verificamos si es octal
        elif tipo == 'oct':
            try:
                int(palabra, 8)
                return True
            except ValueError:
                return False
        # Verificamos si es hexadecimal
        else:
            try:
                int(palabra, 16)
                return True
            except ValueError:
                return False
        return False
    
    def __calcular(self,opcion,palabra):
        if opcion == 0:
            palabra = str(Binario().bin_dec(palabra))
        elif opcion == 1:
            palabra = str(Complemento1().bin_dec(palabra))
        elif opcion == 2:
            palabra = str(Complemento2().bin_dec(palabra))
        elif opcion == 3:
            palabra = str(IEEE754x32().bin_dec(palabra))
        elif opcion == 4:
            palabra = str(IEEE754x64().bin_dec(palabra))
        elif opcion == 5:
            palabra = str(Fraccionario().bin_dec(palabra,4))
        elif opcion == 6:
            numero = Binario().bin_dec(palabra)
            palabra = str(Octal().dec_oct(numero))
        elif opcion == 7:
            numero = Binario().bin_dec(palabra)
            palabra = str(Hexadecimal().dec_hex(numero))
        elif opcion == 8:
            numero = int(palabra)
            palabra = str(Binario().dec_bin(numero))
        elif opcion == 9:
            numero = int(palabra)
            palabra = str(Complemento1().dec_bin(numero))
        elif opcion == 10:
            numero = int(palabra)
            palabra = str(Complemento2().dec_bin(numero))
        elif opcion == 11:
            numero = float(palabra)
            palabra = str(IEEE754x32().dec_bin(numero))
        elif opcion == 12:
            numero = float(palabra)
            palabra = str(IEEE754x64().dec_bin(numero))
        elif opcion == 13:
            numero = float(palabra)
            palabra = str(Fraccionario().dec_bin(numero,8))
        elif opcion == 14:
            numero = int(palabra)
            palabra = str(Octal().dec_oct(numero))
        elif opcion == 15:
            numero = int(palabra)
            palabra = str(Hexadecimal().dec_hex(numero))
        elif opcion == 16:
            decimal = Octal().oct_dec(palabra)
            palabra = str(Binario().dec_bin(decimal))
        elif opcion == 17:
            palabra = str(Octal().oct_dec(palabra))
        elif opcion == 18:
            decimal = Hexadecimal().hex_dec(palabra)
            palabra = str(Binario().dec_bin(decimal))
        elif opcion == 19:
            palabra = str(Hexadecimal().hex_dec(palabra))
        else:
            palabra = ''
        return palabra
         
def main():    
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setMinimumSize(350,450)
    window.setMaximumSize(350,450)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()