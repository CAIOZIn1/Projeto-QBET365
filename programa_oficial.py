from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import sip
import sys
import pymysql
import json
import requests


cu = 0
class MainWindow(object):
    def __init__(self, QBET365):
        self.chamar_janela()

    def chamar_janela(self):
        # janela
        QBET365.resize(592, 590)
        QBET365.setStyleSheet("background-color:black")
        self.janela_principal()

    def janela_principal(self):
        #frame principal
        self.main_frame = QFrame(QBET365)
        self.main_frame.setGeometry(QRect(0, 0, 592, 590))
        self.main_frame.setStyleSheet('background-color:black')
        self.main_frame.show()

        #gif principal
        self.label_gif = QLabel(parent=self.main_frame)
        self.gif = QMovie('imagens/abstract gif.gif')
        self.label_gif.resize(1500, 900)
        self.label_gif.setMovie(self.gif)
        self.label_gif.move(60,-120)
        self.gif.start()
        self.label_gif.show()

        #frame das informações
        self.frame = QFrame(parent=self.main_frame)
        self.frame.setGeometry(QRect(150, 130, 301, 331))
        self.frame.setStyleSheet("background-color:white; border:25px solid; border-radius:15px; border-color:white")
        self.frame.show()

        #imagens
        self.label_imagem_abstract = QLabel(parent=self.main_frame)
        self.label_imagem_abstract.setPixmap(QPixmap('imagens/abstract image-2.jpg'))
        self.label_imagem_abstract.resize(201,150)
        self.label_imagem_abstract.move(-35,500)
        self.label_imagem_abstract.show()

        self.label_imagem_abstract2 = QLabel(parent=self.main_frame)
        self.label_imagem_abstract2.setPixmap(QPixmap('imagens/abstract image-2.jpg'))
        self.label_imagem_abstract2.resize(200, 170)
        self.label_imagem_abstract2.move(470, -50)
        self.label_imagem_abstract2.show()

        self.label_user = QLabel(parent=self.frame)
        self.label_user.setPixmap(QPixmap('imagens/user.jpg'))
        self.label_user.resize(140, 134)
        self.label_user.move(80, 5)
        self.label_user.show()

        #entradas
        self.entrada = QLineEdit(parent=self.frame)
        self.entrada.setStyleSheet('background-color:#EE625E; color:black; border:1px solid; border-radius:15px; font-size: 12pt')
        self.entrada.setPlaceholderText('                  Username:')
        self.entrada.resize(250, 40)
        self.entrada.move(25, 140)
        self.entrada.show()

        self.entrada2 = QLineEdit(parent=self.frame)
        self.entrada2.setStyleSheet('background-color:#EE625E; color:black; border:1px ; border-radius:15px; font-size: 12pt')
        self.entrada2.setPlaceholderText('                  Password:')
        self.entrada2.resize(250, 40)
        self.entrada2.move(25, 200)
        self.entrada2.show()

        #botões
        self.botao_enter = QPushButton('ENTER', parent=self.frame)
        self.botao_enter.setStyleSheet('background-color:#52057B; color:black; border:1px groove; border-radius:15px')
        self.botao_enter.clicked.connect(self.auteticacao_username)
        self.botao_enter.resize(70, 35)
        self.botao_enter.move(120, 270)
        self.botao_enter.show()

        self.botao_create = QPushButton('Create login', parent=self.main_frame)
        self.botao_create.setFont(QFont('Monteserrat', 10))
        self.botao_create.setStyleSheet('background-color:black; color:#56AEFF')
        self.botao_create.clicked.connect(self.move_frame_login)
        self.botao_create.resize(90, 35)
        self.botao_create.move(500, 555)
        self.botao_create.show()

    def auteticacao_username(self):
        self.conexao = pymysql.connect(
                host='localhost',
                user='root',
                passwd=''
            )

        self.cursor = self.conexao.cursor()
        self.cursor.execute('''use QBET365''')

        self.username = self.entrada.text()
        self.password = self.entrada2.text()
        
        try:
            self.cursor.execute(f"select senha from cadastro where nome='{self.username}' ")
            dados = self.cursor.fetchall()
            self.conexao.commit()

            if self.password == dados[0][0]:
                self.animation()
                
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("ERROR")
            self.msg.setText("Incorrect login or password")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.exec_()


    def animation(self):
        effect = QGraphicsOpacityEffect(self.botao_enter)
        self.botao_enter.setGraphicsEffect(effect)
        self.anim_button = QPropertyAnimation(self.botao_enter, b'pos')
        self.anim_button.setEndValue(QPoint(120, 350))
        self.anim_button.setDuration(1000)
        self.anim_2 = QPropertyAnimation(effect, b'opacity')
        self.anim_2.setStartValue(1)
        self.anim_2.setEndValue(0)
        self.anim_2.setDuration(900)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_button)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        self.progressbar = QProgressBar(self.frame)
        self.progressbar.setStyleSheet('''QProgressBar {
        border: 1px solid black;
        border-radius: 3px;
}

    QProgressBar::chunk {background-color:qlineargradient(spread:pad, x1:0.0336364, y1:0.068, x2:0.966, y2:0.0625, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(20, 255, 236, 255))}''')
        self.progressbar.move(95, 275)
        self.progressbar.setTextVisible(False)
        self.progressbar.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.to_fill)
        self.timer.start(25)

    def to_fill(self):
        global cu
        self.progressbar.setValue(cu)
        if cu > 100:
            self.timer.stop()
            self.delete_login()
        cu += 5


    def delete_login(self):
        sip.delete(self.main_frame)
        self.choice_bet()

    def move_frame_login(self):
        #animação
        self.anim_login = QPropertyAnimation(self.main_frame, b"pos")
        self.anim_login.setEndValue(QPoint(600, 0))
        self.anim_login.setEasingCurve(QEasingCurve.OutBounce)
        self.anim_login.setDuration(1200)
        self.anim_login.start()

        #def's
        self.create_login()
        self.move_frame_create()


    def move_frame_create(self):
        #animação
        self.anim = QPropertyAnimation(self.main_frame_create, b"pos")
        self.anim.setEndValue(QPoint(0, 0))
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.setDuration(1200)
        self.anim.start()


    def create_login(self):
        #frame principal
        self.main_frame_create = QFrame(QBET365)
        self.main_frame_create.setGeometry(QRect(-592, 0, 592, 590))
        self.main_frame_create.setStyleSheet('background-color:black')

        self.abstract_images2 = QLabel(parent=self.main_frame_create)
        self.abstract_images2.setPixmap(QPixmap('imagens/earth image.jpg'))
        self.abstract_images2.resize(500,1000)
        self.abstract_images2.move(60, -120)

        self.frame = QFrame(parent=self.main_frame_create)
        self.frame.setGeometry(QRect(150, 110, 301, 420))
        self.frame.setStyleSheet("background-color:white; border:25px solid; border-radius:15px; border-color:white")

        #entradas
        self.entrada_username = QLineEdit(parent=self.frame)
        self.entrada_username.setStyleSheet('background-color:#EE625E; color:black; border:1px solid; border-radius:15px; font-size: 12pt')
        self.entrada_username.setPlaceholderText('                  Username:')
        self.entrada_username.resize(250, 40)
        self.entrada_username.move(25, 115)

        self.entrada_email = QLineEdit(parent=self.frame)
        self.entrada_email.setStyleSheet('background-color:#EE625E; color:black; border:1px solid; border-radius:15px; font-size: 12pt')
        self.entrada_email.setPlaceholderText('                     Email:')
        self.entrada_email.resize(250, 40)
        self.entrada_email.move(25, 175)

        self.entrada_password = QLineEdit(parent=self.frame)
        self.entrada_password.setStyleSheet('background-color:#EE625E; color:black; border:1px solid; border-radius:15px; font-size: 12pt')
        self.entrada_password.setPlaceholderText('                  Password:')
        self.entrada_password.resize(250, 40)
        self.entrada_password.move(25, 235)

        #imagens
        self.label_user = QLabel(parent=self.frame)
        self.label_user.setPixmap(QPixmap('imagens/user.jpg'))
        self.label_user.resize(140,135)
        self.label_user.move(80, -20)

        self.abstract_images = QLabel(parent=self.main_frame_create)
        self.abstract_images.setPixmap(QPixmap('imagens/abstract image-1.jpg'))
        self.abstract_images.resize(200,180)
        self.abstract_images.move(-50, -50)

        self.abstract_images2 = QLabel(parent=self.main_frame_create)
        self.abstract_images2.setPixmap(QPixmap('imagens/abstract image-3.jpg'))
        self.abstract_images2.resize(200,180)
        self.abstract_images2.move(470, 470)

        self.sun_image = QLabel(parent=self.main_frame_create)
        self.sun_image.setPixmap(QPixmap('imagens/sun image.jpg'))
        self.sun_image.resize(200,180)
        self.sun_image.move(500, 0)

        #botões
        self.botao_create = QPushButton('CREATE', parent=self.frame)
        self.botao_create.setStyleSheet('background-color:#52057B; color:black; border:1px groove; border-radius:15px')
        self.botao_create.clicked.connect(self.login_create)
        self.botao_create.resize(70, 35)
        self.botao_create.move(120, 310)

        self.botao_voltar = QPushButton('↩', parent=self.main_frame_create)
        self.botao_voltar.setFont(QFont('montserrat', 20))
        self.botao_voltar.setStyleSheet('background-color:#DA0037; color:white; border:-8px solid; border-radius:22px')
        self.botao_voltar.clicked.connect(self.back_to_login)
        effect = QGraphicsOpacityEffect(self.botao_voltar)
        self.botao_voltar.setGraphicsEffect(effect)
        self.botao_voltar.resize(55,45)
        self.botao_voltar.move(-100, 285)

        self.anim_button = QPropertyAnimation(self.botao_voltar, b'pos')
        self.anim_button.setEndValue(QPoint(45, 285))
        self.anim_button.setDuration(2000)
        self.anim_2 = QPropertyAnimation(effect, b'opacity')
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(3000)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_button)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()

        #shows
        self.main_frame_create.show()
        self.abstract_images2.show()
        self.frame.show()
        self.entrada_username.show()
        self.entrada_email.show()
        self.entrada_password.show()
        self.botao_create.show()
        self.label_user.show()
        self.abstract_images.show()
        self.sun_image.show()
        self.botao_voltar.show()     


    def login_create(self):
        
        try:
            self.conexao = pymysql.connect(
                host='localhost',
                user='root',
                passwd=''
            )

            self.username = self.entrada_username.text()
            self.email = self.entrada_email.text()
            self.password = self.entrada_password.text()

            self.cursor = self.conexao.cursor()
            self.cursor.execute('''use QBET365''')
            self.cursor.execute(f'''insert into cadastro (nome, email, senha) values ('{self.username}', '{self.email}', '{self.password}')''')
            self.conexao.commit()
            
            self.label_correct = QLabel(parent=self.frame)
            self.label_correct.setPixmap(QPixmap('imagens/correct.png'))
            self.label_correct.setStyleSheet('background-color:transparent')
            self.label_correct.resize(100,100)
            self.label_correct.move(200, 280)
            self.label_correct.show()

            if self.username == '':
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Attention")
                self.msg.setText("you didn't put the username in your login")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()
                self.cursor.execute(f'''delete from cadastro where nome='{self.username}' ''')
                self.conexao.commit()

                self.label_error = QLabel(parent=self.frame)
                self.label_error.setPixmap(QPixmap('imagens/error.png'))
                self.label_error.setStyleSheet('background-color:transparent')
                self.label_error.resize(100,100)
                self.label_error.move(200, 280)
                self.label_error.show()

            if self.password == '':
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Attention")
                self.msg.setText("you didn't fill in the password field")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()
                self.cursor.execute(f'''delete from cadastro where nome='{self.username}' ''')
                self.conexao.commit()

                self.label_error = QLabel(parent=self.frame)
                self.label_error.setPixmap(QPixmap('imagens/error.png'))
                self.label_error.setStyleSheet('background-color:transparent')
                self.label_error.resize(100,100)
                self.label_error.move(200, 280)
                self.label_error.show()
            
            if self.email == '':
                self.msg = QMessageBox()
                self.msg.setWindowTitle("ERROR")
                self.msg.setText("The login was created but you did not enter the email")
                self.msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Ignore | QMessageBox.Cancel)
                self.msg.exec_() 

        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Attention")
            self.msg.setText("Email already in use")
            self.msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Ignore | QMessageBox.Cancel)
            self.msg.exec_()


    def back_to_login(self):

        self.anim = QPropertyAnimation(self.main_frame_create, b"pos")
        self.anim.setEndValue(QPoint(-600, 0))
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.setDuration(1200)
        self.anim.start()

        self.anim_login = QPropertyAnimation(self.main_frame, b"pos")
        self.anim_login.setEndValue(QPoint(0, 0))
        self.anim_login.setEasingCurve(QEasingCurve.OutBounce)
        self.anim_login.setDuration(1200)
        self.anim_login.start()


    def choice_bet(self):
        self.main_frame = QFrame(QBET365)
        self.main_frame.setGeometry(QRect(0, 0, 592, 590))
        self.main_frame.setStyleSheet('background-color:black')
        self.main_frame.show()

        self.abstract_image = QLabel(self.main_frame)
        self.abstract_image.setPixmap(QPixmap('imagens/abstract image-4.jpg'))
        self.abstract_image.resize(900, 900)
        self.abstract_image.move(0, 55)
        self.abstract_image.show()

        self.abstract_image1 = QLabel(self.main_frame)
        self.abstract_image1.setPixmap(QPixmap('imagens/abstract image-5.jpg'))
        self.abstract_image1.resize(900, 500)
        self.abstract_image1.move(200, -50)
        self.abstract_image1.show()

        self.frame_choice = QFrame(self.main_frame)
        self.frame_choice.setGeometry(QRect(150, 130, 301, 331))
        self.frame_choice.setStyleSheet(
            'background-color:white; border:25px solid; border-radius:15px; border-color:white')
        self.frame_choice.show()

        self.abstract_image_bet = QLabel(self.frame_choice)
        self.abstract_image_bet.setPixmap(QPixmap('imagens/bet365.png'))
        self.abstract_image_bet.setStyleSheet('background-color:white')
        self.abstract_image_bet.resize(250, 250)
        self.abstract_image_bet.move(50, 10)
        self.abstract_image_bet.show()

        self.botao_next = QPushButton('➔', parent=self.main_frame)
        self.botao_next.setFont(QFont('montserrat', 20))
        self.botao_next.setStyleSheet('background-color:#DA0037; color:white; border:-8px solid; border-radius:17px')
        self.botao_next.resize(50, 40)
        self.botao_next.move(600, 280)
        self.botao_next.show()
        effect = QGraphicsOpacityEffect(self.botao_next)
        self.botao_next.setGraphicsEffect(effect)
        self.anim_button1 = QPropertyAnimation(self.botao_next, b'pos')
        self.anim_button1.setEndValue(QPoint(500, 280))
        self.anim_button1.setDuration(2000)
        self.anim = QPropertyAnimation(effect, b'opacity')
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setDuration(3000)
        self.anim_group1 = QParallelAnimationGroup()
        self.anim_group1.addAnimation(self.anim_button1)
        self.anim_group1.addAnimation(self.anim)
        self.anim_group1.start()

        self.botao_enter_choice = QPushButton('ENTER', parent=self.frame_choice)
        self.botao_enter_choice.setFont(QFont('montserrat', 20))
        self.botao_enter_choice.setStyleSheet(
            'background-color:#252525; color:white; border:-8px solid; border-radius:17px')
        self.botao_enter_choice.clicked.connect(self.choice_sports)
        self.botao_enter_choice.resize(100, 40)
        self.botao_enter_choice.move(105, 250)
        self.botao_enter_choice.show()

    def choice_sports(self):
        sip.delete(self.main_frame)

        self.main_frame = QFrame(QBET365)
        self.main_frame.setGeometry(QRect(0, 0, 592, 590))
        self.main_frame.setStyleSheet('background-color:black')
        self.main_frame.show()

        self.abstract_image = QLabel(self.main_frame)
        self.abstract_image.setPixmap(QPixmap('imagens/abstract image sports.jpg'))
        self.abstract_image.resize(1500, 1000)
        self.abstract_image.move(0, 50)
        self.abstract_image.show()

        self.frame_choice = QFrame(self.main_frame)
        self.frame_choice.setGeometry(QRect(150, 130, 301, 331))
        self.frame_choice.setStyleSheet(
            'background-color:white; border:25px solid; border-radius:15px; border-color:white')
        self.frame_choice.show()

        self.abstract_image = QLabel(self.frame_choice)
        self.abstract_image.setPixmap(QPixmap('imagens/tênis.jpg'))
        self.abstract_image.resize(200, 200)
        self.abstract_image.move(85, 20)
        self.abstract_image.show()

        self.botao_next = QPushButton('➔', parent=self.main_frame)
        self.botao_next.setFont(QFont('montserrat', 20))
        self.botao_next.setStyleSheet('background-color:#DA0037; color:white; border:-8px solid; border-radius:17px')
        self.botao_next.resize(50, 40)
        self.botao_next.move(600, 280)
        self.botao_next.show()
        effect = QGraphicsOpacityEffect(self.botao_next)
        self.botao_next.setGraphicsEffect(effect)
        self.anim_button1 = QPropertyAnimation(self.botao_next, b'pos')
        self.anim_button1.setEndValue(QPoint(500, 280))
        self.anim_button1.setDuration(2000)
        self.anim = QPropertyAnimation(effect, b'opacity')
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setDuration(3000)
        self.anim_group1 = QParallelAnimationGroup()
        self.anim_group1.addAnimation(self.anim_button1)
        self.anim_group1.addAnimation(self.anim)
        self.anim_group1.start()

        self.botao_enter_choice = QPushButton('ENTER', parent=self.frame_choice)
        self.botao_enter_choice.setFont(QFont('montserrat', 20))
        self.botao_enter_choice.setStyleSheet(
            'background-color:#252525; color:white; border:-8px solid; border-radius:17px')
        self.botao_enter_choice.clicked.connect(self.best_BET)
        self.botao_enter_choice.resize(100, 40)
        self.botao_enter_choice.move(105, 250)
        self.botao_enter_choice.show()


    def best_BET(self):
        sip.delete(self.main_frame)

        self.main_frame = QFrame(QBET365)
        self.main_frame.setGeometry(0, 0, 592, 590)
        self.main_frame.setStyleSheet('background-color:black')
        self.main_frame.show()

        self.image_best_bet = QLabel(self.main_frame)
        self.image_best_bet.setPixmap(QPixmap("imagens/abstract image best BET's"))
        self.image_best_bet.resize(590, 500)
        self.image_best_bet.move(0,0)
        self.image_best_bet.show()

        self.image_hash = QLabel(self.main_frame)
        self.image_hash.setPixmap(QPixmap("imagens/abstract image hash"))
        self.image_hash.resize(592,500)
        self.image_hash.move(320,420)
        self.image_hash.show()

        self.frame_bets = QFrame(self.main_frame)
        self.frame_bets.setGeometry(QRect(60, 100, 360, 410))
        self.frame_bets.setStyleSheet('background-color:white; border:25px solid; border-radius:15px; border-color:white')
        self.frame_bets.show()

        self.image_cross = QLabel(self.frame_bets)
        self.image_cross.setPixmap(QPixmap("imagens/cross"))
        self.image_cross.resize(300, 200)
        self.image_cross.move(40, 120)
        self.image_cross.show()

        self.leitor = requests.get('https://betsapi.com/docs/samples/bet365_inplay.json')
        self.leitor = self.leitor.json()

        self.od = self.leitor['results'][0][86]['OD']
        self.nome_od = self.leitor['results'][0][86]['NA']
        self.od_2 = self.leitor['results'][0][85]['OD']
        self.nome_od_2 = self.leitor['results'][0][85]['NA']
        
        self.best_od = QLabel(self.od, self.frame_bets)
        self.best_od.setFont(QFont('Monteserrat', 22))
        self.best_od.resize(150, 100)
        self.best_od.move(115, 115)
        self.best_od.show()

        self.best_od_2 = QLabel(self.od_2, self.frame_bets)
        self.best_od_2.setFont(QFont('Monteserrat', 22))
        self.best_od_2.resize(150, 100)
        self.best_od_2.move(110, 245)
        self.best_od_2.show()

        self.plus =  QPushButton('↗',self.frame_bets)
        self.plus.setFont(QFont('Monteserrat', 22))
        self.plus.setStyleSheet('color:blue')
        self.plus.clicked.connect(self.atleta1)
        self.plus.resize(80,80)
        self.plus.move(222, 126)
        self.plus.show()

        self.plus2 =  QPushButton('↗',self.frame_bets)
        self.plus2.setFont(QFont('Monteserrat', 22))
        self.plus2.setStyleSheet('color:blue')
        self.plus2.clicked.connect(self.atleta2)
        self.plus2.resize(80,80)
        self.plus2.move(222, 256)
        self.plus2.show()

        self.image_crown = QLabel(self.main_frame)
        self.image_crown.setPixmap(QPixmap("imagens/crown"))
        self.image_crown.setStyleSheet('background-color:transparent')
        self.image_crown.resize(100, 90)
        self.image_crown.move(370, 40)
        self.image_crown.show()

        self.best_odd = QLabel('Melhores odds', self.frame_bets)
        self.best_odd.setFont(QFont('Monteserrat', 22))
        self.best_odd.resize(300, 100)
        self.best_odd.move(55, 15)
        self.best_odd.show()

        self.button_historic =  QPushButton(self.main_frame)
        self.button_historic.setStyleSheet('background-image: url(imagens/button historic)')
        self.button_historic.clicked.connect(self.historic)
        self.button_historic.resize(105,105)
        self.button_historic.move(450, 150)
        self.button_historic.show()

        self.button_future =  QPushButton(self.main_frame)
        self.button_future.setStyleSheet('background-image: url(imagens/button future)')
        self.button_future.clicked.connect(self.future)
        self.button_future.resize(105,105)
        self.button_future.move(450, 270)
        self.button_future.show()

        self.button_home =  QPushButton('Home',self.main_frame)
        self.button_home.setFont(QFont('Montserrat', 15))
        self.button_home.setStyleSheet('background-color:black; color:#56AEFF')
        self.button_home.clicked.connect(self.choice_bet)
        self.button_home.resize(70,35)
        self.button_home.move(5, 550)
        self.button_home.show()

        self.button_leave =  QPushButton('Leave',self.main_frame)
        self.button_leave.setFont(QFont('Montserrat', 15))
        self.button_leave.setStyleSheet('background-color:black; color:#56AEFF')
        self.button_leave.clicked.connect(self.janela_principal_delete)
        self.button_leave.resize(70,35)
        self.button_leave.move(80, 550)
        self.button_leave.show()

    def atleta1(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("INFO")
        self.msg.setText(f'Atleta: {self.nome_od}')
        self.msg.setStandardButtons(QMessageBox.Cancel)
        self.msg.exec_() 

    def atleta2(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("INFO")
        self.msg.setText(f'Atleta: {self.nome_od_2}')
        self.msg.setStandardButtons(QMessageBox.Cancel)
        self.msg.exec_() 


    def future(self):
        sip.delete(self.main_frame)

        self.main_frame = QFrame(QBET365)
        self.main_frame.setGeometry(0, 0, 592, 590)
        self.main_frame.setStyleSheet('background-color:black')
        self.main_frame.show()

        self.image_best_bet = QLabel(self.main_frame)
        self.image_best_bet.setPixmap(QPixmap("imagens/abstract image best BET's"))
        self.image_best_bet.resize(590, 500)
        self.image_best_bet.move(0,0)
        self.image_best_bet.show()

        self.image_hash = QLabel(self.main_frame)
        self.image_hash.setPixmap(QPixmap("imagens/abstract image hash"))
        self.image_hash.resize(592,500)
        self.image_hash.move(320,420)
        self.image_hash.show()

        self.frame_bets = QFrame(self.main_frame)
        self.frame_bets.setGeometry(QRect(60, 100, 360, 410))
        self.frame_bets.setStyleSheet('background-color:white; border:25px solid; border-radius:15px; border-color:white')
        self.frame_bets.show()

        self.image_luck= QLabel(self.main_frame)
        self.image_luck.setPixmap(QPixmap("imagens/luck"))
        self.image_luck.setStyleSheet('background-color:transparent')
        self.image_luck.resize(500, 500)
        self.image_luck.move(20, 40)
        self.image_luck.show()

        self.best_odd = QLabel('Jogos futuros', self.frame_bets)
        self.best_odd.setFont(QFont('Monteserrat', 22))
        self.best_odd.resize(300, 100)
        self.best_odd.move(70, 15)
        self.best_odd.show()


        self.button_historic =  QPushButton(self.main_frame)
        self.button_historic.setStyleSheet('background-image: url(imagens/button historic)')
        self.button_historic.clicked.connect(self.historic)
        self.button_historic.resize(105,105)
        self.button_historic.move(450, 150)
        self.button_historic.show()

        self.button_future =  QPushButton(self.main_frame)
        self.button_future.setStyleSheet('background-image: url(imagens/button best bets)')
        self.button_future.clicked.connect(self.best_BET)
        self.button_future.resize(105,105)
        self.button_future.move(450, 270)
        self.button_future.show()

        self.button_home =  QPushButton('Home',self.main_frame)
        self.button_home.setFont(QFont('Montserrat', 15))
        self.button_home.setStyleSheet('background-color:black; color:#56AEFF')
        self.button_home.clicked.connect(self.choice_bet)
        self.button_home.resize(70,35)
        self.button_home.move(5, 550)
        self.button_home.show()

        self.button_leave =  QPushButton('Leave',self.main_frame)
        self.button_leave.setFont(QFont('Montserrat', 15))
        self.button_leave.setStyleSheet('background-color:black; color:#56AEFF')
        self.button_leave.clicked.connect(self.janela_principal_delete)
        self.button_leave.resize(70,35)
        self.button_leave.move(80, 550)
        self.button_leave.show()

    def historic(self):
        sip.delete(self.main_frame)

        self.main_frame = QFrame(QBET365)
        self.main_frame.setGeometry(0, 0, 592, 590)
        self.main_frame.setStyleSheet('background-color:black')
        self.main_frame.show()

        self.image_best_bet = QLabel(self.main_frame)
        self.image_best_bet.setPixmap(QPixmap("imagens/abstract image best BET's"))
        self.image_best_bet.resize(590, 500)
        self.image_best_bet.move(0,0)
        self.image_best_bet.show()

        self.image_hash = QLabel(self.main_frame)
        self.image_hash.setPixmap(QPixmap("imagens/abstract image hash"))
        self.image_hash.resize(592,500)
        self.image_hash.move(320,420)
        self.image_hash.show()

        self.frame_bets = QFrame(self.main_frame)
        self.frame_bets.setGeometry(QRect(60, 100, 360, 410))
        self.frame_bets.setStyleSheet('background-color:white; border:25px solid; border-radius:15px; border-color:white')
        self.frame_bets.show()

        self.image_binoculars = QLabel(self.main_frame)
        self.image_binoculars.setPixmap(QPixmap("imagens/binoculars"))
        self.image_binoculars.setStyleSheet('background-color:transparent')
        self.image_binoculars.resize(500, 500)
        self.image_binoculars.move(30, 55)
        self.image_binoculars.show()

        self.best_odd = QLabel('Histórico', self.frame_bets)
        self.best_odd.setFont(QFont('Monteserrat', 22))
        self.best_odd.resize(300, 100)
        self.best_odd.move(95, 15)
        self.best_odd.show()


        self.button_historic =  QPushButton(self.main_frame)
        self.button_historic.setStyleSheet('background-image: url(imagens/button future)')
        self.button_historic.clicked.connect(self.future)
        self.button_historic.resize(105, 105)
        self.button_historic.move(450, 150)
        self.button_historic.show()

        self.button_future =  QPushButton(self.main_frame)
        self.button_future.setStyleSheet('background-image: url(imagens/button best bets)')
        self.button_future.clicked.connect(self.best_BET)
        self.button_future.resize(105, 105)
        self.button_future.move(450, 270)
        self.button_future.show()

        self.button_home =  QPushButton('Home',self.main_frame)
        self.button_home.setFont(QFont('Montserrat', 15))
        self.button_home.setStyleSheet('background-color:black; color:#56AEFF')
        self.button_home.clicked.connect(self.choice_bet)
        self.button_home.resize(70, 35)
        self.button_home.move(5, 550)
        self.button_home.show()

        self.button_leave =  QPushButton('Leave', self.main_frame)
        self.button_leave.setFont(QFont('Montserrat', 15))
        self.button_leave.setStyleSheet('background-color:black; color:#56AEFF')
        self.button_leave.clicked.connect(self.janela_principal_delete)
        self.button_leave.resize(70, 35)
        self.button_leave.move(80, 550)
        self.button_leave.show()

    def janela_principal_delete(self):
        sip.delete(self.main_frame)
        self.janela_principal()


app = QApplication(sys.argv)
QBET365 = QWidget()
janela = MainWindow(QBET365)
QBET365.show()
sys.exit(app.exec_())