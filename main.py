from cProfile import label
from tempfile import TemporaryDirectory
from tkinter import *
import tkinter


#   Cores:
cor1 = "#0a0a0a"  # black
cor2 = "#fafcff"  # white
cor3 = "#21c25c"  # green
cor4 = "#eb463b"  # red
cor5 = "#dedcdc"  # gray 
cor6 = "#3080f0"  # blue 


#   Criando uma janela
janela = Tk()
janela.title('')
janela.geometry('300x180')
janela.configure(bg=cor1)

#   Bloquear o aumento ou diminuição da janela
janela.resizable(width=False, height=False)

#   Definindo variaveis globais
global tempo
global rodar
global contador
global limitador

limitador = 59

#   Funções do cronômetro
tempo = '00:00:00'
rodar = False
contador = -5


def iniciar():
    global tempo
    global contador
    global limitador
    if rodar:
        # Antes do cronometro começar, o programa irá começar uma contagem de 5~0 para começar o cronômetro
        if contador <= -1:
            inicio = 'Começando em ' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
            
        #   Rodando o cronômetro
        else:
            label_tempo['font'] = 'Times 50 bold'
            temporario = str(tempo)
            h, m, s = map(int, temporario.split(':'))
            h = int(h)
            m = int(m)
            s = int(contador)
            
            if (s >= limitador):
                contador = 0
                m += 1
            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)
            
            #   Atualizando os valores atuais
            temporario = str(h[-2:]) + ':' + str(m[-2:]) + ':' + str(s[-2:])
            label_tempo['text'] = temporario
            tempo = temporario
            
        label_tempo.after(300, iniciar)
        contador += 1

def start():
    global rodar
    rodar = True
    iniciar()

#   Criando labels: Cronômetro
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor3)

#   Posicionamento para dentro da janela
label_app.place(x=20, y=5)
label_tempo.place(x=20, y=30)

#   Criando botões: Iniciar, Pausa, Reiniciar
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=12, y=130)

botao_pausar = Button(janela, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=113, y=130)

botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=211, y=130)


janela.mainloop()