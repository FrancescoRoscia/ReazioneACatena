from kivy.app import App
from kivy.uix.button import Button

# 1) TROVARE PAROLE 
# 2) INTERFACCIA GRAFICA (Parola da indovinare, Stop, Giusta, Sbagliata, Punteggio, Timer, Numero Passo)
# 3) GESTIONE PUNTEGGIO (3 passi, sbagli -1, giusta +1, passo 0)
# 4) GESTIONE TEMPO

# 5) RADDOPPIO (Tasto visibile solo quando possibile)(Bonus)
# 6) PUNTEGGIO CONTINUATIVO (somma punteggio di più turni) 

class MyApp(App):
    def build(self):
        return Button(text="Ciao da Kivy!")
        
if __name__ == "__main__":
    MyApp().run()

