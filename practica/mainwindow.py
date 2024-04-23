from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from libreria.libreria import Libreria
from libreria.libro import Libro

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.libreria = Libreria()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAgregarFinal.clicked.connect(self.click_agregar)
        self.ui.btnAgregarInicio.clicked.connect(self.click_agregar_inicio)
        self.ui.btnMostrar.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot()
    def action_abrir_archivo(self):
        print('Abrir archivo')

    @Slot()
    def action_guardar_archivo(self):
        # print('Guardar archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )

        print(ubicacion)

    @Slot()
    def click_mostrar(self):
        # self.libreria.mostrar()
        self.ui.txtMostrar.clear()
        self.ui.txtMostrar.insertPlainText(str(self.libreria))
        
    @Slot()
    def click_agregar(self):
        titulo = self.ui.inpTitulo.text()
        autor = self.ui.inpAutor.text()
        publicado = self.ui.inpPublicado.text()
        editorial = self.ui.inpEditorial.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_final(libro)

    @Slot()
    def click_agregar_inicio(self):
        titulo = self.ui.inpTitulo.text()
        autor = self.ui.inpAutor.text()
        publicado = self.ui.inpPublicado.text()
        editorial = self.ui.inpEditorial.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_inicio(libro)