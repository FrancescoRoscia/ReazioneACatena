from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

# 1) TROVARE PAROLE (controllate fino a riga 100) (quelle separate da spazio le ho aggiunte io)
# 5) RADDOPPIO (Tasto visibile solo quando possibile)(MAX 2 volte a partita)

class MyApp(App):

    def build(self):
        self.punteggio = 0 #mettendo self.variabile si crea un attributo dell'oggetto (come in Java)
        self.nPasso = 3
        self.timer = 60
        self.timer_running = False 
        self.timerName = None
        self.canChange = False #variabile booleana se il punteggio può cambiare
        self.canPass = False #variabile booleana se si può utilizzare il passo


        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)  # disposizione verticale

        buttonRst = Button(text = "Reset", size_hint=(0.33, None), pos_hint={'center_x': 0.5})
        buttonRst.bind(on_press=self.resetGame)

        labelParola = Label(text="Parola Da Indovinare", font_size=28)
        self.labelTempo = Label(text=f"Tempo: {self.timer}", font_size=30)
        self.labelPunteggio = Label(text=str(self.punteggio), font_size = 30)
        self.labelPasso = Label(text=str(self.nPasso), font_size = 30)

        buttonWrong = Button(text = "", background_normal="wrong.png", size_hint=(None, None), size=(140, 140))
        self.buttonSS = Button(text="Inizia") #bottone start stop
        buttonPasso = Button(text="Passo") 
        buttonRight = Button(text = "", background_normal="right.png", size_hint=(None, None), size=(140, 140))

        # azione quando premo il bottone
        buttonRight.bind(on_press=self.addPoint)
        buttonWrong.bind(on_press=self.removePoint)
        buttonPasso.bind(on_press=self.passaParola)
        self.buttonSS.bind(on_press=self.toggleTimer)

        #riga punteggio + passo
        layoutPuntPas = BoxLayout(orientation='horizontal', spacing=20)
        layoutPuntPas.add_widget(self.labelPunteggio)
        layoutPuntPas.add_widget(self.labelPasso)

        #riga bottoni finali
        layoutButtons = BoxLayout(orientation='horizontal', spacing=20)
        layoutButtons.add_widget(buttonWrong)
        layoutButtons.add_widget(self.buttonSS)
        layoutButtons.add_widget(buttonPasso)
        layoutButtons.add_widget(buttonRight)

        layout.add_widget(buttonRst)
        layout.add_widget(labelParola)
        layout.add_widget(self.labelTempo)
        layout.add_widget(layoutPuntPas)
        layout.add_widget(layoutButtons)

        return layout
    

    def addPoint(self, instance):
        if(self.canChange == True):
            self.punteggio += 1
            self.labelPunteggio.text = str(self.punteggio)
            self.canChange = False
            self.stopTimer() 

    def removePoint(self, instance):
        if(self.punteggio >= 1 and self.canChange == True):
            self.punteggio -= 1
            self.labelPunteggio.text = str(self.punteggio)
        
        self.canChange = False
        self.stopTimer()

    def passaParola(self, instance):
        if(self.nPasso >= 1 and self.canPass == True):
            self.nPasso -= 1
            self.labelPasso.text = str(self.nPasso)
            self.canChange = False
            self.canPass = False
            self.stopTimer()
    
    def toggleTimer(self, instance):
        if(self.timer_running == False):
            # Avvia o riprende il timer
            self.buttonSS.text = "Ferma"
            self.timer_running = True
            self.canChange = True
            self.canPass = True
            if self.timerName is None:
                self.timerName = Clock.schedule_interval(self.updateTimer, 1) # creo un'istanza di timer
            else:
                Clock.schedule_interval(self.updateTimer, 1) # non creo nuove istanze ma modifico quella gia esistente
        else: 
            # Ferma temporaneamente
            self.stopTimer()
 

    def stopTimer(self):
        self.buttonSS.text = "Riprendi"
        self.timer_running = False
        self.canPass = False
        Clock.unschedule(self.updateTimer)

    def updateTimer(self, second):
        if self.timer > 0:
            self.timer -= 1
            self.labelTempo.text = f"Tempo: {self.timer}"
        else:
            Clock.unschedule(self.updateTimer)
            self.timerName = None
            self.labelTempo.text = "Tempo scaduto!"
            self.timer_running = False
            
    
    def resetGame(self, instance):
        self.punteggio = 0
        self.nPasso = 3
        self.timer = 60
        self.timer_running = False
        self.timerName = None
        self.labelPunteggio.text = str(self.punteggio)
        self.labelPasso.text = str(self.nPasso)
        self.labelTempo.text = f"Tempo: {self.timer}"
        self.buttonSS.text = "Inizia"
        Clock.unschedule(self.toggleTimer)
        
if __name__ == "__main__":
    MyApp().run()

