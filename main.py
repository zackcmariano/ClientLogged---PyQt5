from PyQt5 import uic,QtWidgets
from PyQt5 import QtGui

def TelaFatura():
    tela.frame_9.close()

def TelaPlanos():
    tela.frame_9.show()

def TelaAmigos():
    tela.close()
    telaamigos.show()

def VoltarPLanos():
    telaamigos.close()
    tela.show()

def FecharTela():
    tela.close()


#Chamar Telas UI
app=QtWidgets.QApplication([])
tela=uic.loadUi("ScreenLogg.ui")
telaamigos=uic.loadUi("ScreenFriends.ui")

#Endereçar Buttons
tela.pushButton_18.clicked.connect(TelaFatura)
tela.pushButton_8.clicked.connect(TelaPlanos)
tela.pushButton_19.clicked.connect(TelaAmigos)
telaamigos.pushButton_11.clicked.connect(VoltarPLanos)
tela.pushButton_16.clicked.connect(FecharTela)

#Add as Imagens das Telas
icon=QtGui.QPixmap([])
telaamigos.label.setPixmap(QtGui.QPixmap('friends.png'))
tela.label_2.setPixmap(QtGui.QPixmap('logoinnova.png'))
tela.label_8.setPixmap(QtGui.QPixmap('logoinnova.png'))
telaamigos.label_2.setPixmap(QtGui.QPixmap('logoinnova.png'))

tela.show()
app.exec()