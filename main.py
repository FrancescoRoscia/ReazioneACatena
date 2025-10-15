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
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)  # disposizione verticale

        buttonRst = Button(text = "Reset", size_hint=(0.33, None), pos_hint={'center_x': 0.5})

        labelParola = Label(text="Parola Da Indovinare", font_size=28)
        labelTempo = Label(text="Tempo Rimasto")
        labelPunteggio = Label(text="Punteggio")
        labelPasso = Label(text="N. Passo Rimasti")

        buttonWrong = Button(text = "", background_normal="wrong.png", size_hint=(None, None), size=(140, 140))
        buttonSS = Button(text="Inizia") #button start stop
        buttonRight = Button(text = "", background_normal="right.png", size_hint=(None, None), size=(140, 140))

        # azione quando premo il bottone
        buttonSS.bind(on_press=self.on_button_press)

        #riga punteggio + passo
        layoutPuntPas = BoxLayout(orientation='horizontal', spacing=20)
        layoutPuntPas.add_widget(labelPunteggio)
        layoutPuntPas.add_widget(labelPasso)

        #riga bottoni finali
        layoutButtons = BoxLayout(orientation='horizontal', spacing=20)
        layoutButtons.add_widget(buttonWrong)
        layoutButtons.add_widget(buttonSS)
        layoutButtons.add_widget(buttonRight)

        layout.add_widget(buttonRst)
        layout.add_widget(labelParola)
        layout.add_widget(labelTempo)
        layout.add_widget(layoutPuntPas)
        layout.add_widget(layoutButtons)

        return layout
    

    def on_button_press(self, instance):
        print("Hai premuto il bottone!")
        
if __name__ == "__main__":
    MyApp().run()

