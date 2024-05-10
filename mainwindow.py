from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton, QHeaderView, QDialog
from PySide2.QtCore import Qt, QTimer, QDate
from PySide2.QtGui import QIcon, QColor
from db.paciente import Paciente
from ui_mainwindow import Ui_login
from ui_secondwindow import Ui_MainWindow
from ui_deletewindow import Ui_DeleteWindow
from db.sesion import Sesion
from db.user import User
from db.rol import Rol
from db.cita import Cita
from db.sintoma import Sintoma
from db.signo import Signo
from db.enfermedad import Enfermedad


STYLE_MSJ_EXITOSO = """
    QFrame{
        background-color: #22c55e;
        border-radius: 5px;
    }
"""
STYLE_MSJ_ERROR = """QFrame{
        background-color: #ef4444;
        border-radius: 5px;
    }
"""

ICONO_EDITAR = QIcon('./img/edit.svg')
ICONO_ELIMINAR = QIcon('./img/trash.svg')
ICONO_CHECK = QIcon('./img/check.svg')
ICONO_ERROR = QIcon('./img/x_circle.svg')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)

        #Autenticar Usuario
        self.ui.btnIniciarSesion.clicked.connect(self.autenticar)

    def autenticar(self):
        nickname = self.ui.inpUsuario.text()
        password = self.ui.inpPass.text()
        usuario = Sesion.login(nickname, password)
        if(usuario != None):
            self.secondWindow = SecondWindow(usuario=usuario)
            self.secondWindow.show()
            self.hide()


class SecondWindow(QMainWindow):
    def __init__(self, usuario:User):
        super(SecondWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

            #Configuracion Usuario
        self.usuarioAutenticado = usuario
        if self.usuarioAutenticado.rol_id == 2:
            self.ui.btnUsuarios.hide()
            self.ui.btnAnalasis.hide()
            self.ui.cardUsuarios.hide()
        elif self.usuarioAutenticado.rol_id == 3:
            self.ui.btnUsuarios.hide()            
            self.ui.cardUsuarios.hide()
            #Configuracion Usuario
        self.estadoMenu = True
        self.paginaInicio(event=None)

        #Subventana Eliminar
        self.confirmacion = False
        self.deleteWindow = QDialog(self)
        self.deleteWindow_UI = Ui_DeleteWindow()
        self.deleteWindow_UI.setupUi(self.deleteWindow)
        self.deleteWindow.setWindowFlag(Qt.FramelessWindowHint)
        self.deleteWindow_UI.btnEliminarCancelar.clicked.connect(lambda: self.deleteWindow.close())
        self.deleteWindow_UI.btnEliminarAceptar.clicked.connect(self.confirmacionEliminar)

        

        #Cerrar Sesión
        self.ui.btnSalir.mousePressEvent = self.cerrarSesion

        #Menu
        self.ui.btnMenu.clicked.connect(self.toogleMenu)

        #Paginas
            #Inicio
        self.ui.btnInicio.mousePressEvent = self.paginaInicio
        self.ui.cardUsuarios.mousePressEvent = self.paginaUsuarios
        self.ui.cardPacientes.mousePressEvent = self.paginaPacientes
        self.ui.cardCitas.mousePressEvent = self.paginaCitas

            #Usuarios
        self.ui.btnUsuarios.mousePressEvent = self.paginaUsuarios
                #Agregar Usuarios
        self.ui.btnAgregarUsuario.clicked.connect(self.agregarUsuariosGet)
        self.ui.btnRegresarAUsuarios.clicked.connect(self.paginaUsuarios)
        self.ui.lblRegresarAgUsuarios.mousePressEvent = self.paginaUsuarios
        self.ui.btnRegistroSubmit.clicked.connect(self.agregarUsuarioPost)
                #Editar Usuarios
        self.ui.btnRegresarAUsuarios2.clicked.connect(self.paginaUsuarios)
        self.ui.lblRegresarAgUsuarios2.mousePressEvent = self.paginaUsuarios
        self.ui.btnEditarSubmit.clicked.connect(self.editarUsuarioPost)
                #Buscar Usuarios
        self.ui.inpUsuariosBusqueda.textChanged.connect(self.busquedaUsuarios)

            #Pacientes
        self.ui.btnPacientes.mousePressEvent = self.paginaPacientes
                #Agregar Pacientes
        self.ui.btnAgregarPaciente.clicked.connect(self.agregarPacienteGet)
        self.ui.btnRegresarAPacientes.clicked.connect(self.paginaPacientes)
        self.ui.lblRegresarAPacientes.mousePressEvent = self.paginaPacientes
        self.ui.btnRegistroPacienteSubmit.clicked.connect(self.agregarPacientePost)
                #Editar Pacientes
        self.ui.btnRegresarAgPacientes.clicked.connect(self.paginaPacientes)
        self.ui.lblRegresarAgPacientes.mousePressEvent = self.paginaPacientes
        self.ui.btnEditarPacienteSubmit.clicked.connect(self.editarPacientePost)
                #Buscar Pacientes
        self.ui.inpBusquedaPacientes.textChanged.connect(self.busquedaPacientes)

            #Citas
        self.ui.btnCitas.mousePressEvent = self.paginaCitas
                #Agregar Citas
        self.ui.btnAgregarCita.clicked.connect(self.agregarCitaGet)
        self.ui.lblRegresarACitas.mousePressEvent = self.paginaCitas
        self.ui.btnRegresarACitas.clicked.connect(self.paginaCitas)
        self.ui.btnRegistroCitaSubmit.clicked.connect(self.agregarCitaPost)
                #Editar Citas
        self.ui.btnRegresarAgCitas.clicked.connect(self.paginaCitas)
        self.ui.lblRegresarAgCitas.mousePressEvent = self.paginaCitas
        self.ui.btnEditarCitaSubmit.clicked.connect(self.editarCitaPost)
                #Busqueda Citas
        self.ui.inpBusquedaCitas.textChanged.connect(self.busquedaCitas)
            
            #* Analisis
        self.ui.btnAnalisis.mousePressEvent = self.paginaAnalisis
                # Agregar Analisis
        self.ui.btnAgregarAnalisis.clicked.connect(self.agregarAnalisisGet)
        self.ui.btnRegresarAAnalisis.clicked.connect(self.paginaAnalisis)
        self.ui.lblRegresarAAnalisis.mousePressEvent = self.paginaAnalisis
        self.ui.btnDiagnosticoSubmit.clicked.connect(self.agregarAnalisisPost)

            # Enfermedades
        self.ui.btnEnfermedades.mousePressEvent = self.paginaEnfermedades
                #Agregar Enfermedad
        self.ui.btnAgregarEnfermedad.clicked.connect(self.agregarEnfermedadGet)
        self.ui.btnRegresarAEnfermedades.clicked.connect(self.paginaEnfermedades)
        self.ui.lblRegresarAEnfermedades.mousePressEvent = self.paginaEnfermedades
        self.ui.btnRegistroEnfermedadSubmit.clicked.connect(self.agregarEnfermedadPost)
                #Editar Enfermedad
        self.ui.btnRegresarAgEnfermedades.clicked.connect(self.paginaEnfermedades)
        self.ui.lblRegresarAgEnfermedades.mousePressEvent = self.paginaEnfermedades
        self.ui.btnEditarEnfermedadSubmit.clicked.connect(self.editarEnfermedadPost)


            # Signos
        self.ui.btnSignos.mousePressEvent = self.paginaSignos
                #Agregar Signo
        self.ui.btnAgregarSigno.clicked.connect(self.agregarSignoGet)
        self.ui.btnRegistroSignoSubmit.clicked.connect(self.agregarSignoPost)
        self.ui.btnRegresarASignos.clicked.connect(self.paginaSignos)
        self.ui.lblRegresarASignos.mousePressEvent = self.paginaSignos
                #Editar Signo
        self.ui.btnRegresarAgSignos.clicked.connect(self.paginaSignos)
        self.ui.lblRegresarAgSignos.mousePressEvent = self.paginaSignos
        self.ui.btnEditarSignoSubmit.clicked.connect(self.editarSignoPost)

            # Sintomas
        self.ui.btnSintomas.mousePressEvent = self.paginaSintomas
                #Agregar Sintoma
        self.ui.btnAgregarSintoma.clicked.connect(self.agregarSintomaGet)
        self.ui.btnRegistroSintomaSubmit.clicked.connect(self.agregarSintomaPost)
        self.ui.btnRegresarASintomas.clicked.connect(self.paginaSintomas)
        self.ui.lblRegresarASintomas.mousePressEvent = self.paginaSintomas
                #Editar Sintoma
        self.ui.btnRegresarAgSintomas.clicked.connect(self.paginaSintomas)
        self.ui.lblRegresarAgSintomas.mousePressEvent = self.paginaSintomas
        self.ui.btnEditarSintomaSubmit.clicked.connect(self.editarSintomaPost)
        
    
    def confirmacionEliminar(self):
        self.confirmacion = True
        self.deleteWindow.close()

    def frameIconoMensaje(self, lblFrame, lblIcono, lblMensaje, lblStyle=STYLE_MSJ_EXITOSO, icoStyle=ICONO_CHECK, error=False, mensaje=None):
        lblFrame.setStyleSheet(lblStyle)
        lblMensaje.setText(("Registro completado exitosamente", "Complete todos los campos")[error])
        lblIcono.setIcon(icoStyle)
        if mensaje != None: lblMensaje.setText(mensaje)

    def cerrarSesion(self, event):
        if event.button() == Qt.LeftButton:
            self.mainWindow = MainWindow()
            self.mainWindow.show()
            self.hide()

    def toogleMenu(self):
        if self.estadoMenu:
            self.ui.lblLogo.hide()
            self.ui.lblUsuarios.hide()
            self.ui.lblPacientes.hide()
            self.ui.lblCitas.hide()
            self.ui.lblAnalisis.hide()
            self.ui.lblSalir.hide()
            self.estadoMenu = False
        else:
            self.ui.lblLogo.show()
            self.ui.lblUsuarios.show()
            self.ui.lblPacientes.show()
            self.ui.lblCitas.show()
            self.ui.lblAnalisis.show()
            self.ui.lblSalir.show()
            self.estadoMenu = True
    
    #Pagina Inicio
    def paginaInicio(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagInicio)
        self.ui.lblBienvenenida.setText(f"Bienvenido {self.usuarioAutenticado.nickname}")
        self.contadorTablas()

    def contadorTablas(self):
        self.ui.lblContadorUsuarios.setText(str(User.count()))
        self.ui.lblContadorPacientes.setText(str(Paciente.count()))
        self.ui.lblContadorCitas.setText(str(Cita.count()))
        
    #Pagina Inicio

    #Pagina Usuarios
    def paginaUsuarios(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagUsuarios)
        self.configurarTabla(self.ui.tblUsuarios)
        self.obtenerUsuarios(usuarios=User.all())
        self.ui.inpUsuariosBusqueda.setFocus()

    def configurarTabla(self, tabla):
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def obtenerUsuarios(self, usuarios):
        self.ui.tblUsuarios.clearContents()
        self.ui.tblUsuarios.setRowCount(len(usuarios))
        i = 0
        for usuario in usuarios:
            btnEditar = QPushButton(ICONO_EDITAR, "", self)
            btnEditar.setProperty("id", usuario[0])
            btnEditar.clicked.connect(self.editarUsuariosGet)
            btnEditar.setCursor(Qt.PointingHandCursor)
            btnEditar.setStyleSheet("""
                    QPushButton{
                        background-color: #86efac;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #4ade80;
                        border: none;
                    }
                """)
            btnEliminar = QPushButton(ICONO_ELIMINAR, "", self)
            btnEliminar.setProperty("id", usuario[0])
            btnEliminar.clicked.connect(self.eliminarUsuarioGet)
            btnEliminar.setCursor(Qt.PointingHandCursor)
            btnEliminar.setStyleSheet("""
                    QPushButton{
                        background-color: #fca5a5;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #f87171;
                    }
                """)
            
            
            self.ui.tblUsuarios.setItem(i, 0, QTableWidgetItem(str(usuario[0])))
            self.ui.tblUsuarios.setItem(i, 1, QTableWidgetItem(usuario[1]))
            self.ui.tblUsuarios.setItem(i, 2, QTableWidgetItem(usuario[2]))
            self.ui.tblUsuarios.setCellWidget(i, 3, btnEditar)
            self.ui.tblUsuarios.setCellWidget(i, 4, btnEliminar)
            i = i+1

    def agregarUsuariosGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAgregarUsuario)
        self.obtenerUsuarioRoles(self.ui.inpRegistroRol)
        self.ui.lblRegistroUsuario.hide()
        self.ui.inpRegistroNick.setFocus()
        self.ui.inpRegistroNick.setText('')
        self.ui.inpRegistroPass.setText('')

    def obtenerUsuarioRoles(self, comboBox, rol_id=0):
        roles = Rol.all()
        comboBox.clear()
        for rol in roles:
            comboBox.addItem(rol[1], str(rol[0]))

        if rol_id != 0: comboBox.setCurrentIndex(comboBox.findData(rol_id))

    def agregarUsuarioPost(self):
        self.ui.lblRegistroUsuario.show()
        nickname = self.ui.inpRegistroNick.text()
        password = self.ui.inpRegistroPass.text()
        rol_id = str(self.ui.inpRegistroRol.currentData())
        if nickname != '' and password != '':            
            User.create(nickname, password, rol_id)

            self.frameIconoMensaje(self.ui.lblRegistroUsuario, self.ui.lblIconoRegistroUsuario, self.ui.lblMsjRegistroUsuario)

            QTimer.singleShot(2000, lambda: self.paginaUsuarios(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblRegistroUsuario, self.ui.lblIconoRegistroUsuario, self.ui.lblMsjRegistroUsuario, STYLE_MSJ_ERROR, ICONO_ERROR, True)

    def editarUsuariosGet(self):
        usuarioEditar = User.where(str(self.sender().property("id")))
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEditarUsuario)
        self.obtenerUsuarioRoles(comboBox=self.ui.inpEditarRol, rol_id=usuarioEditar.rol_id)
        self.ui.lblEditarUsuarioActual.setText(str(usuarioEditar.id))
        self.ui.inpEditarNick.setText(usuarioEditar.nickname)
        self.ui.inpEditarPass.setText(usuarioEditar.password)
        self.ui.lblEditarUsuario.hide()

    def editarUsuarioPost(self):
        self.ui.lblEditarUsuario.show()
        nickname = self.ui.inpEditarNick.text()
        password = self.ui.inpEditarPass.text()
        rol_id = self.ui.inpEditarRol.currentData()
        id = self.ui.lblEditarUsuarioActual.text()
        if nickname != '' and password != '':
            User.update(id, nickname, password, rol_id)
            self.frameIconoMensaje(self.ui.lblEditarUsuario, self.ui.lblIconoEditarUsuario, self.ui.lblMsjEditarUsuario, mensaje='Usuario actualizado correctamente')
            QTimer.singleShot(2000, lambda: self.paginaUsuarios(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblEditarUsuario, self.ui.lblIconoEditarUsuario, self.ui.lblMsjEditarUsuario, STYLE_MSJ_ERROR, ICONO_ERROR, True)
    
    def eliminarUsuarioGet(self):
        self.deleteWindow_UI.lblEliminarRegistroID.setText(str(self.sender().property("id")))
        self.deleteWindow.finished.connect(self.eliminarUsuarioPost)
        self.deleteWindow.exec_()
    
    def eliminarUsuarioPost(self):
        if self.confirmacion == True:
            id = self.deleteWindow_UI.lblEliminarRegistroID.text()
            User.delete(id)
            self.obtenerUsuarios(User.all())
            self.confirmacion = False
        self.deleteWindow.finished.disconnect(self.eliminarUsuarioPost)
        
    def busquedaUsuarios(self):
        palabra = self.ui.inpUsuariosBusqueda.text()
        self.obtenerUsuarios(usuarios=User.whereAll(palabra))
    #>Pagina Usuarios

    #Pagina Pacientes
    def paginaPacientes(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagPacientes)
        self.configurarTabla(self.ui.tblPacientes)
        self.obtenerPacientes(pacientes=Paciente.all())
        self.ui.inpBusquedaPacientes.setFocus()

    def obtenerPacientes(self, pacientes):
        self.ui.tblPacientes.clearContents()
        self.ui.tblPacientes.setRowCount(len(pacientes))
        i = 0
        for paciente in pacientes:
            btnEditar = QPushButton(QIcon('./img/edit.svg'), "", self)
            btnEditar.setProperty("id", paciente[0])
            btnEditar.clicked.connect(self.editarPacienteGet)
            btnEditar.setCursor(Qt.PointingHandCursor)
            btnEditar.setStyleSheet("""
                    QPushButton{
                        background-color: #86efac;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #4ade80;
                        border: none;
                    }
                """)
            btnEliminar = QPushButton(QIcon('./img/trash.svg'), "", self)
            btnEliminar.setProperty("id", paciente[0])
            btnEliminar.clicked.connect(self.eliminarPacienteGet)
            btnEliminar.setCursor(Qt.PointingHandCursor)
            btnEliminar.setStyleSheet("""
                    QPushButton{
                        background-color: #fca5a5;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #f87171;
                    }
                """)
            
            
            self.ui.tblPacientes.setItem(i, 0, QTableWidgetItem(str(paciente[0])))
            self.ui.tblPacientes.setItem(i, 1, QTableWidgetItem(paciente[1]))
            self.ui.tblPacientes.setItem(i, 2, QTableWidgetItem(paciente[2]))
            self.ui.tblPacientes.setItem(i, 3, QTableWidgetItem(str(paciente[3])))
            self.ui.tblPacientes.setCellWidget(i, 4, btnEditar)
            self.ui.tblPacientes.setCellWidget(i, 5, btnEliminar)
            i = i+1
    
    def agregarPacienteGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAgregarPaciente)
        self.ui.lblRegistroPaciente.hide()
        self.ui.inpRegistroNombre.setFocus()
        self.ui.inpRegistroNombre.setText('')
        self.ui.inpRegistroApellidos.setText('')
        self.ui.inpRegistroEdad.setValue(0)

    def agregarPacientePost(self):
        self.ui.lblRegistroPaciente.show()
        nombre = self.ui.inpRegistroNombre.text()
        apellidos = self.ui.inpRegistroApellidos.text()
        edad = self.ui.inpRegistroEdad.value()
        if nombre != '' and apellidos != '' and edad > 0:
            if Paciente.create(nombre, apellidos, edad):
                self.frameIconoMensaje(self.ui.lblRegistroPaciente, self.ui.lblIconoRegistroPaciente, self.ui.lblMsjRegistroPaciente)
            QTimer.singleShot(2000, lambda: self.paginaPacientes(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblRegistroPaciente, self.ui.lblIconoRegistroPaciente, self.ui.lblMsjRegistroPaciente, STYLE_MSJ_ERROR, ICONO_ERROR, True, ("Edad debe ser mayor a 0", None)[bool(edad)])

    def editarPacienteGet(self):
        paciente = Paciente.where(str(self.sender().property("id")))
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEditarPaciente)
        self.ui.lblEditarPaciente.hide()
        self.ui.lblEditarPacienteActual.setText(str(paciente.id))
        self.ui.inpEditarNombre.setText(paciente.nombre)
        self.ui.inpEditarApellidos.setText(paciente.apellidos)
        self.ui.inpEditarEdad.setValue(int(paciente.edad))
        
    def editarPacientePost(self):
        self.ui.lblEditarPaciente.show()
        id = self.ui.lblEditarPacienteActual.text()
        nombre = self.ui.inpEditarNombre.text()
        apellidos = self.ui.inpEditarApellidos.text()
        edad = self.ui.inpEditarEdad.value()
        if nombre != '' and apellidos != '' and edad > 0:
            if Paciente.update(id, nombre, apellidos, edad):
                self.frameIconoMensaje(self.ui.lblEditarPaciente, self.ui.lblIconoEditarPaciente, self.ui.lblMsjEditarPaciente, mensaje="Paciente actualizado correctamente")
            QTimer.singleShot(2000, lambda: self.paginaPacientes(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblEditarPaciente, self.ui.lblIconoEditarPaciente, self.ui.lblMsjEditarPaciente, STYLE_MSJ_ERROR, ICONO_ERROR, True, ("Edad debe ser mayor a 0", None)[bool(edad)])

    def eliminarPacienteGet(self):
        self.deleteWindow_UI.lblEliminarRegistroID.setText(str(self.sender().property("id")))
        self.deleteWindow.finished.connect(self.eliminarPacientePost)
        self.deleteWindow.exec_()

    def eliminarPacientePost(self):
        if self.confirmacion == True:
            id = self.deleteWindow_UI.lblEliminarRegistroID.text()
            Paciente.delete(id)
            self.obtenerPacientes(Paciente.all())
            self.confirmacion = False
        self.deleteWindow.finished.disconnect(self.eliminarPacientePost)

    def busquedaPacientes(self):
        palabra = self.ui.inpBusquedaPacientes.text()
        self.obtenerPacientes(Paciente.whereAll(palabra))
    #>Pacientes

    #Citas
    def paginaCitas(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagCitas)
        self.configurarTabla(self.ui.tblCitas)
        self.ui.inpBusquedaCitas.setFocus()
        self.obtenerCitas(Cita.all())

    def obtenerCitas(self, citas):
        self.ui.tblCitas.clearContents()
        self.ui.tblCitas.setRowCount(len(citas))
        fechaActual = QDate.currentDate()
        i = 0
        for cita in citas:
            btnEditar = QPushButton(ICONO_EDITAR, "", self)
            btnEditar.setProperty("id", cita[0])
            btnEditar.clicked.connect(self.editarCitaGet)
            btnEditar.setCursor(Qt.PointingHandCursor)
            btnEditar.setStyleSheet("""
                    QPushButton{
                        background-color: #86efac;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #4ade80;
                        border: none;
                    }
                """)
            btnEliminar = QPushButton(ICONO_ELIMINAR, "", self)
            btnEliminar.setProperty("id", cita[0])
            btnEliminar.clicked.connect(self.eliminarCitaGet)
            btnEliminar.setCursor(Qt.PointingHandCursor)
            btnEliminar.setStyleSheet("""
                    QPushButton{
                        background-color: #fca5a5;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #f87171;
                    }
                """)
            
            
            fechaCita = QDate.fromString(str(cita[3]), "yyyy-MM-dd")
            fechaColor = "#fff"
            fechaFondo = ""
            if fechaActual < fechaCita:
                fechaFondo = "#16a34a"
            else:
                fechaFondo = "#f59e0b"
            
            citaFecha = QTableWidgetItem(str(cita[3]))
            citaFecha.setBackgroundColor(QColor(fechaFondo))
            citaFecha.setTextColor(QColor(fechaColor))
            
            self.ui.tblCitas.setItem(i, 0, QTableWidgetItem(str(cita[0])))
            self.ui.tblCitas.setItem(i, 1, QTableWidgetItem(cita[1]))
            self.ui.tblCitas.setItem(i, 2, QTableWidgetItem(cita[2]))
            self.ui.tblCitas.setItem(i, 3, citaFecha)
            self.ui.tblCitas.setCellWidget(i, 4, btnEditar)
            self.ui.tblCitas.setCellWidget(i, 5, btnEliminar)
            i = i+1
        
    def agregarCitaGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAgregarCita)
        self.ui.lblRegistroCita.hide()
        self.obtenerMedicosCmbx(self.ui.inpRegistroMedicoCita)
        self.obtenerPacientesCmbx(self.ui.inpRegistroPacienteCita)
        self.ui.inpRegistroFechaCita.setMinimumDate(QDate.currentDate())

    def obtenerPacientesCmbx(self, comboBox, paciente_id=0):
        pacientes = Paciente.all()
        comboBox.clear()
        for paciente in pacientes:
            comboBox.addItem(paciente[1], str(paciente[0]))

        if paciente_id != 0: comboBox.setCurrentIndex(comboBox.findData(paciente_id))

    def obtenerMedicosCmbx(self, comboBox, rol_id=0):
        medicos = User.getByRol('3')
        comboBox.clear()
        for medico in medicos:
            comboBox.addItem(medico[1], str(medico[0]))

        if rol_id != 0: comboBox.setCurrentIndex(comboBox.findData(rol_id))

    def agregarCitaPost(self):
        self.ui.lblRegistroCita.show()
        fechaCalendar = self.ui.inpRegistroFechaCita.selectedDate()
        fechaCita = str(fechaCalendar.year()) + "-" + str(fechaCalendar.month()) + "-" + str(fechaCalendar.day())
        paciente_id = self.ui.inpRegistroPacienteCita.currentData()
        medico_id = self.ui.inpRegistroMedicoCita.currentData()
        if paciente_id != 0 and medico_id != 0:
            if Cita.create(paciente_id, medico_id, fechaCita):
                self.frameIconoMensaje(self.ui.lblRegistroCita, self.ui.lblIconoRegistroCita, self.ui.lblMsjRegistroCita)
            QTimer.singleShot(2000, lambda: self.paginaCitas(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblRegistroCita, self.ui.lblIconoRegistroCita, self.ui.lblMsjRegistroCita, STYLE_MSJ_ERROR, ICONO_ERROR, True)

    def editarCitaGet(self):
        cita = Cita.where(str(self.sender().property("id")))
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEditarCita)
        self.ui.lblEditarCita.hide()
        self.ui.lblEditarCitaActual.setText(str(cita.id))
        self.obtenerPacientesCmbx(self.ui.inpEditarPacienteCita, cita.paciente_id)
        self.obtenerMedicosCmbx(self.ui.inpEditarMedicoCita, cita.medico_id)
        self.ui.inpEditarFechaCita.setSelectedDate(QDate.fromString(str(cita.fecha), "yyyy-MM-dd"))
        self.ui.inpEditarFechaCita.setMinimumDate(QDate.currentDate())

    def editarCitaPost(self):
        self.ui.lblEditarCita.show()
        id = self.ui.lblEditarCitaActual.text()
        paciente_id = self.ui.inpEditarPacienteCita.currentData()
        medico_id = self.ui.inpEditarMedicoCita.currentData()
        fechaCalendar = self.ui.inpEditarFechaCita.selectedDate()
        fechaCita = str(fechaCalendar.year()) + "-" + str(fechaCalendar.month()) + "-" + str(fechaCalendar.day())
        if paciente_id != 0 and medico_id != 0 and id != 0:
            if Cita.update(id, paciente_id, medico_id, fechaCita):
                self.frameIconoMensaje(self.ui.lblEditarCita, self.ui.lblIconoEditarCita, self.ui.lblMsjEditarCita, mensaje="Cita actualizada correctamente")
            QTimer.singleShot(2000, lambda: self.paginaCitas(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblEditarCita, self.ui.lblIconoEditarCita, self.ui.lblMsjEditarCita, STYLE_MSJ_ERROR, ICONO_ERROR, True)

    def eliminarCitaGet(self):
        self.deleteWindow_UI.lblEliminarRegistroID.setText(str(self.sender().property("id")))
        self.deleteWindow.finished.connect(self.eliminarCitaPost)
        self.deleteWindow.exec_()

    def eliminarCitaPost(self):
        if self.confirmacion == True:
            id = self.deleteWindow_UI.lblEliminarRegistroID.text()
            Cita.delete(id)
            self.obtenerCitas(Cita.all())
            self.confirmacion = False
        self.deleteWindow.finished.disconnect(self.eliminarCitaPost)

    def busquedaCitas(self):
        palabra = self.ui.inpBusquedaCitas.text()
        self.obtenerCitas(Cita.whereAll(palabra))
    #>Citas

    # * Pagina Analisis
    def paginaAnalisis(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAnalisis)
        self.configurarTabla(self.ui.tblAnalisis)

    def agregarAnalisisGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagDiagnostico)
        self.ui.lblRegistroAnalisis.hide()
        self.ui.inpAgregarAnalisisSigno.setText('')
        self.ui.inpAgregarAnalisisSintoma.setText('')

    def agregarAnalisisPost(self):
        signo = self.ui.inpAgregarAnalisisSigno.text()
        sintoma = self.ui.inpAgregarAnalisisSintoma.text()
        print(signo, sintoma)
        if sintoma != '' and signo != '':
            self.frameIconoMensaje(self.ui.lblRegistroAnalisis, self.ui.lblIconoRegistroAnalisis, self.ui.lblMsjRegistroAnalisis)
            QTimer.singleShot(2000, lambda: self.paginaAnalisis(event=None))
        else:
             self.frameIconoMensaje(self.ui.lblRegistroAnalisis, self.ui.lblIconoRegistroAnalisis, self.ui.lblMsjRegistroAnalisis, STYLE_MSJ_ERROR, ICONO_ERROR, True)



    # Pagina Enfermedades
    def paginaEnfermedades(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEnfermedades)
        self.configurarTabla(self.ui.tblEnfermedades)
        self.obtenerEnfermedad(Enfermedad.all())

    def obtenerEnfermedad(self, enfermedad):
        self.ui.tblEnfermedades.clearContents()
        self.ui.tblEnfermedades.setRowCount(len(enfermedad))
        i = 0
        for enfermedad in enfermedad:
            btnEditar = QPushButton(ICONO_EDITAR, "", self)
            btnEditar.setProperty("id", enfermedad[0])
            btnEditar.clicked.connect(self.editarEnfermedadGet)
            btnEditar.setCursor(Qt.PointingHandCursor)
            btnEditar.setStyleSheet("""
                    QPushButton{
                        background-color: #86efac;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #4ade80;
                        border: none;
                    }
                """)
            btnEliminar = QPushButton(ICONO_ELIMINAR, "", self)
            btnEliminar.setProperty("id", enfermedad[0])
            btnEliminar.clicked.connect(self.eliminarEnfermedadGet)
            btnEliminar.setCursor(Qt.PointingHandCursor)
            btnEliminar.setStyleSheet("""
                    QPushButton{
                        background-color: #fca5a5;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #f87171;
                    }
                """)
            
            
            self.ui.tblEnfermedades.setItem(i, 0, QTableWidgetItem(str(enfermedad[0])))
            self.ui.tblEnfermedades.setItem(i, 1, QTableWidgetItem(enfermedad[1]))
            self.ui.tblEnfermedades.setItem(i, 2, QTableWidgetItem(enfermedad[2]))
            self.ui.tblEnfermedades.setItem(i, 3, QTableWidgetItem(enfermedad[3]))
            self.ui.tblEnfermedades.setCellWidget(i, 4, btnEditar)
            self.ui.tblEnfermedades.setCellWidget(i, 5, btnEliminar)
            i = i+1

    def agregarEnfermedadGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAgregarEnfermedad)
        self.ui.lblRegistroEnfermedad.hide()
        self.ui.inpRegistroEnfermedad.setText('')
        self.ui.inpRegistroESigno.setText('')
        self.ui.inpRegistroESintoma.setText('')

    def agregarEnfermedadPost(self):
        enfermedad = self.ui.inpRegistroEnfermedad.text()
        signo = self.ui.inpRegistroESigno.text()
        sintoma = self.ui.inpRegistroESintoma.text()
        print(enfermedad, signo, sintoma)
        if enfermedad != '' and sintoma != '' and signo != '':
            if Enfermedad.create(enfermedad, signo, sintoma):
                self.frameIconoMensaje(self.ui.lblRegistroEnfermedad, self.ui.lblIconoRegistroEnfermedad, self.ui.lblMsjRegistroEnfermedad)
            QTimer.singleShot(2000, lambda: self.paginaEnfermedades(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblRegistroEnfermedad, self.ui.lblIconoRegistroEnfermedad, self.ui.lblMsjRegistroEnfermedad, STYLE_MSJ_ERROR, ICONO_ERROR, True)
    
    def editarEnfermedadGet(self):
        enfermedad = Enfermedad.where(str(self.sender().property("id")))
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEditarEnfermedad)
        self.ui.lblEditarEnfermedad.hide()
        self.ui.lblEditarEnfermedadActual.setText(str(enfermedad.id))
        self.ui.inpEditarEnfermedad.setText(enfermedad.enfermedad)
        self.ui.inpEditarESigno.setText(enfermedad.signo)
        self.ui.inpEditarESintoma.setText(enfermedad.sintoma)

    def editarEnfermedadPost(self):
        self.ui.lblEditarEnfermedad.show()
        id = self.ui.lblEditarEnfermedadActual.text()
        enfermedad = self.ui.inpEditarEnfermedad.text()
        signo = self.ui.inpEditarESigno.text()
        sintoma = self.ui.inpEditarESintoma.text()
        if enfermedad != '' and signo != '' and sintoma != '':
            if Enfermedad.update(id, enfermedad, signo, sintoma):
                self.frameIconoMensaje(self.ui.lblEditarEnfermedad, self.ui.lblIconoEditarEnfermedad, self.ui.lblMsjEditarEnfermedad, mensaje="Enfermedad actualizada correctamente")
            QTimer.singleShot(2000, lambda: self.paginaEnfermedades(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblEditarEnfermedad, self.ui.lblIconoEditarEnfermedad, self.ui.lblMsjEditarEnfermedad, STYLE_MSJ_ERROR, ICONO_ERROR, True)

    def eliminarEnfermedadGet(self):
        self.deleteWindow_UI.lblEliminarRegistroID.setText(str(self.sender().property("id")))
        self.deleteWindow.finished.connect(self.eliminarEnfermedadPost)
        self.deleteWindow.exec_()

    def eliminarEnfermedadPost(self):
        if self.confirmacion == True:
            id = self.deleteWindow_UI.lblEliminarRegistroID.text()
            Enfermedad.delete(id)
            self.obtenerEnfermedad(Enfermedad.all())
            self.confirmacion = False
        self.deleteWindow.finished.disconnect(self.eliminarEnfermedadPost)
    #>Enfermedades

    # Pagina Signos
    def paginaSignos(self, event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagSignos)
        self.configurarTabla(self.ui.tblSignos)
        self.obtenerSignos(Signo.all())

    def obtenerSignos(self, signos):
        self.ui.tblSignos.clearContents()
        self.ui.tblSignos.setRowCount(len(signos))
        i = 0
        for signo in signos:
            btnEditar = QPushButton(ICONO_EDITAR, "", self)
            btnEditar.setProperty("id", signo[0])
            btnEditar.clicked.connect(self.editarSignoGet)
            btnEditar.setCursor(Qt.PointingHandCursor)
            btnEditar.setStyleSheet("""
                    QPushButton{
                        background-color: #86efac;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #4ade80;
                        border: none;
                    }
                """)
            btnEliminar = QPushButton(ICONO_ELIMINAR, "", self)
            btnEliminar.setProperty("id", signo[0])
            btnEliminar.clicked.connect(self.eliminarSignoGet)
            btnEliminar.setCursor(Qt.PointingHandCursor)
            btnEliminar.setStyleSheet("""
                    QPushButton{
                        background-color: #fca5a5;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #f87171;
                    }
                """)
            self.ui.tblSignos.setItem(i, 0, QTableWidgetItem(str(signo[0])))
            self.ui.tblSignos.setItem(i, 1, QTableWidgetItem(signo[1]))
            self.ui.tblSignos.setCellWidget(i, 2, btnEditar)
            self.ui.tblSignos.setCellWidget(i, 3, btnEliminar)
            i = i+1

    def agregarSignoGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAgregarSigno)
        self.ui.lblRegistroSigno.hide()

    def agregarSignoPost(self):
        signo = self.ui.inpRegistroSigno.text()
        print(signo)
        self.ui.lblRegistroSigno.show()
        if signo !="":   
            if Signo.create(signo):
                self.frameIconoMensaje(self.ui.lblRegistroSintoma, self.ui.lblIconoRegistroSintoma, self.ui.lblMsjRegistroSintoma)
            QTimer.singleShot(2000, lambda: self.paginaSignos(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblRegistroSigno, self.ui.lblIconoRegistroSigno, self.ui.lblMsjRegistroSigno, STYLE_MSJ_ERROR, ICONO_ERROR, True)
            print('error')
            
    def editarSignoGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEditarSigno)
        self.ui.lblEditarSigno.hide()
        signo = Signo.where(str(self.sender().property("id")))
        self.ui.lblEditarSignoActual.setText(str(signo.id))
        self.ui.inpEditarSigno.setText(signo.signo)
    
    def editarSignoPost(self):
        self.ui.lblEditarSigno.show()
        signo = self.ui.inpEditarSigno.text()
        id = self.ui.lblEditarSignoActual.text()
        if signo != '' and id != 0:
            if Signo.update(id, signo):
                self.frameIconoMensaje(self.ui.lblEditarSigno, self.ui.lblIconoEditarSigno, self.ui.lblMsjEditarSigno, mensaje="Signo actualizado correctamente")
            QTimer.singleShot(2000, lambda: self.paginaSignos(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblEditarSigno, self.ui.lblIconoEditarSigno, self.ui.lblMsjEditarSigno, STYLE_MSJ_ERROR, ICONO_ERROR, True)
    
    def eliminarSignoGet(self):
        self.deleteWindow_UI.lblEliminarRegistroID.setText(str(self.sender().property("id")))
        self.deleteWindow.finished.connect(self.eliminarSignoPost)
        self.deleteWindow.exec_()

    def eliminarSignoPost(self):
        if self.confirmacion == True:
            id = self.deleteWindow_UI.lblEliminarRegistroID.text()
            Signo.delete(id)
            self.obtenerSignos(Signo.all())
            self.confirmacion = False
        self.deleteWindow.finished.disconnect(self.eliminarSignoPost)
    #>Signos
    
    # Pagina Sintomas
    def paginaSintomas(self,event):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagSintomas)
        self.configurarTabla(self.ui.tblSintomas)
        self.obtenerSintomas(Sintoma.all())
         
    def obtenerSintomas(self, sintomas):
        self.ui.tblSintomas.clearContents()
        self.ui.tblSintomas.setRowCount(len(sintomas))
        i = 0
        for sintoma in sintomas:
            btnEditar = QPushButton(ICONO_EDITAR, "", self)
            btnEditar.setProperty("id", sintoma[0])
            btnEditar.clicked.connect(self.editarSintomaGet)
            btnEditar.setCursor(Qt.PointingHandCursor)
            btnEditar.setStyleSheet("""
                    QPushButton{
                        background-color: #86efac;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #4ade80;
                        border: none;
                    }
                """)
            btnEliminar = QPushButton(ICONO_ELIMINAR, "", self)
            btnEliminar.setProperty("id", sintoma[0])
            btnEliminar.clicked.connect(self.eliminarSintomaGet)
            btnEliminar.setCursor(Qt.PointingHandCursor)
            btnEliminar.setStyleSheet("""
                    QPushButton{
                        background-color: #fca5a5;
                        border: none;
                    }
                    QPushButton::hover{
                        background-color: #f87171;
                    }
                """)
            self.ui.tblSintomas.setItem(i, 0, QTableWidgetItem(str(sintoma[0])))
            self.ui.tblSintomas.setItem(i, 1, QTableWidgetItem(sintoma[1]))
            self.ui.tblSintomas.setCellWidget(i, 2, btnEditar)
            self.ui.tblSintomas.setCellWidget(i, 3, btnEliminar)
            i = i+1


    def agregarSintomaGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagAgregarSintoma)
        self.ui.lblRegistroSintoma.hide()

    def agregarSintomaPost(self):
        sintoma = self.ui.inpRegistroSintoma.text()
        self.ui.lblRegistroSintoma.show()
        if sintoma!="":
            if Sintoma.create(sintoma):
                self.frameIconoMensaje(self.ui.lblRegistroSintoma, self.ui.lblIconoRegistroSintoma, self.ui.lblMsjRegistroSintoma)
            QTimer.singleShot(2000, lambda: self.paginaSintomas(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblRegistroSintoma, self.ui.lblIconoRegistroSintoma, self.ui.lblMsjRegistroSintoma, STYLE_MSJ_ERROR, ICONO_ERROR, True)
            print('error')

    def editarSintomaGet(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pagEditarSintoma)
        self.ui.lblEditarSintoma.hide()
        sintoma = Sintoma.where(str(self.sender().property("id")))
        self.ui.lblEditarSintomaActual.setText(str(sintoma.id))
        self.ui.inpEditarSintoma.setText(sintoma.sintoma)

    def editarSintomaPost(self):
        self.ui.lblEditarSintoma.show()
        sintoma = self.ui.inpEditarSintoma.text()
        id = self.ui.lblEditarSintomaActual.text()
        if sintoma != '' and id != 0:
            if Sintoma.update(id, sintoma):
                self.frameIconoMensaje(self.ui.lblEditarSintoma, self.ui.lblIconoEditarSintoma, self.ui.lblMsjEditarSintoma, mensaje="Sintoma actualizado correctamente")
            QTimer.singleShot(2000, lambda: self.paginaSintomas(event=None))
        else:
            self.frameIconoMensaje(self.ui.lblEditarSintoma, self.ui.lblIconoEditarSintoma, self.ui.lblMsjEditarSintoma, STYLE_MSJ_ERROR, ICONO_ERROR, True)
    
    def eliminarSintomaGet(self):
        self.deleteWindow_UI.lblEliminarRegistroID.setText(str(self.sender().property("id")))
        self.deleteWindow.finished.connect(self.eliminarSintomaPost)
        self.deleteWindow.exec_()

    def eliminarSintomaPost(self):
        if self.confirmacion == True:
            id = self.deleteWindow_UI.lblEliminarRegistroID.text()
            Sintoma.delete(id)
            self.obtenerSintomas(Sintoma.all())
            self.confirmacion = False
        self.deleteWindow.finished.disconnect(self.eliminarSintomaPost)

    #>Sintomas
