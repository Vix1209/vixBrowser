import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

url = 'https://google.com' #input('Enter Address: ') 

class MainWindow (QMainWindow):
    def __init__ (self):  # a constructor
        super (MainWindow, self). __init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url)) #the default address the borswer will go to on launch
        self.setCentralWidget(self.browser)
        
        self.showMaximized() ##browser will be fullscreen 


        #navbar
        navbar = QToolBar() # this specifies the presence of a navbar at the top pf the browser
        self.addToolBar (navbar) 
        
        #back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        #forward Button
        fwrd_btn = QAction('Forward', self)
        fwrd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwrd_btn)
        
        # reload
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        #home
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home) # the specific loacation to navigate to needs to be indicated which is a function => navigate_home
        navbar.addAction(home_btn)
        
        # url bar 
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url_on_searchbar)
        navbar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_urls_on_searchbar) # this makes sre the search bar always commensorates the particular webpage is currently loaded on the browser
        
    def navigate_home (self):
        self.browser.setUrl(QUrl(url)) # the location is set to be url indicated as the default url location of te browser
    
        
    def navigate_to_url_on_searchbar (self):
        bar_url = self.url_bar.text()
        self.browser.setUrl(QUrl(bar_url))
        
    def update_urls_on_searchbar(self, q):
        self.url_bar.setText(q.toString())
        

app = QApplication(sys.argv)
QApplication.setApplicationName(' Vix Browser ') #the name that shows at the top of the browser
window = MainWindow()
app.exec_()

