from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *
import sys



class MyWebBrowser(QMainWindow):
    
    def __init__(self, *args, **kwargs):

        super(MyWebBrowser, self).__init__(*args, **kwargs)

        #Brwoser

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/webhp?hl=de&sa=X&ved=0ahUKEwjZwv6Y3I74AhUpM-wKHYieDRYQPAgI"))

        self.setCentralWidget(self.browser)
        self.showMaximized()

    #Navigationsleiste

        #Zurück
        navbar = QToolBar()
        navbar.setMinimumHeight(15)
        self.addToolBar(navbar)

        zrck_btn = QAction("<", self)
        zrck_btn.triggered.connect(self.browser.back)

        navbar.addAction(zrck_btn)

        #Vorwärts
        vorwärts_btn = QAction(">", self)
        vorwärts_btn.triggered.connect(self.browser.forward)

        navbar.addAction(vorwärts_btn)

        #Refresh
        refresh_btn = QAction("Refresh", self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        #url leiste
        self.url_leiste = QLineEdit()
        self.url_leiste.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_leiste)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.url_leiste.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_leiste.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Loster Browser")
window = MyWebBrowser()
app.exec_()

