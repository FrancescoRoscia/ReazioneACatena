from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# 1) TROVARE PAROLE 
# 2) INTERFACCIA GRAFICA (Parola da indovinare, Stop, Giusta, Sbagliata, Punteggio, Timer, Numero Passo, Reset)
# 3) GESTIONE PUNTEGGIO (3 passi, sbagli -1, giusta +1, passo 0)
# 4) GESTIONE TEMPO

# 5) RADDOPPIO (Tasto visibile solo quando possibile)(Bonus)
# 6) PUNTEGGIO CONTINUATIVO (somma punteggio di più turni) 

class MyApp(App):

    def build(self):
        self.punteggio = 0 #mettendo self.variabile si crea un attributo dell'oggetto (come in Java)
        self.nPasso = 3

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)  # disposizione verticale

        buttonRst = Button(text = "Reset", size_hint=(0.33, None), pos_hint={'center_x': 0.5})

        labelParola = Label(text="Parola Da Indovinare", font_size=28)
        labelTempo = Label(text="Tempo Rimasto")
        self.labelPunteggio = Label(text=str(self.punteggio), font_size = 30)
        self.labelPasso = Label(text=str(self.nPasso), font_size = 30)

        buttonWrong = Button(text = "", background_normal="wrong.png", size_hint=(None, None), size=(140, 140))
        buttonSS = Button(text="Inizia") #bottone start stop
        buttonPasso = Button(text="Passo") 
        buttonRight = Button(text = "", background_normal="right.png", size_hint=(None, None), size=(140, 140))

        # azione quando premo il bottone
        buttonRight.bind(on_press=self.addPoint)
        buttonWrong.bind(on_press=self.removePoint)
        buttonPasso.bind(on_press=self.passaParola)

        #riga punteggio + passo
        layoutPuntPas = BoxLayout(orientation='horizontal', spacing=20)
        layoutPuntPas.add_widget(self.labelPunteggio)
        layoutPuntPas.add_widget(self.labelPasso)

        #riga bottoni finali
        layoutButtons = BoxLayout(orientation='horizontal', spacing=20)
        layoutButtons.add_widget(buttonWrong)
        layoutButtons.add_widget(buttonSS)
        layoutButtons.add_widget(buttonPasso)
        layoutButtons.add_widget(buttonRight)

        layout.add_widget(buttonRst)
        layout.add_widget(labelParola)
        layout.add_widget(labelTempo)
        layout.add_widget(layoutPuntPas)
        layout.add_widget(layoutButtons)

        return layout
    

    def addPoint(self, instance):
        self.punteggio += 1
        self.labelPunteggio.text = str(self.punteggio)

    def removePoint(self, instance):
        if(self.punteggio >= 1):
            self.punteggio -= 1
            self.labelPunteggio.text = str(self.punteggio)

    def passaParola(self, instance):
        if(self.nPasso >= 1):
            self.nPasso -= 1
            self.labelPasso.text = str(self.nPasso)
        
if __name__ == "__main__":
    MyApp().run()

