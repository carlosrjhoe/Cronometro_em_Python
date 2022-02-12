from cProfile import label
from tkinter import *
import tkinter


"""Cores:"""
cor1 = "#0a0a0a"  # black
cor2 = "#fafcff"  # white
cor3 = "#21c25c"  # green
cor4 = "#eb463b"  # red
cor5 = "#dedcdc"  # gray 
cor6 = "#3080f0"  # blue 


'''Criando uma janela'''
janela = Tk()
janela.title('')
janela.geometry('300x180')
janela.configure(bg=cor1)

'''Bloquear o aumento ou diminuição da janela'''
janela.resizable(width=False, height=False)

'''Criando labels: Cronômetro'''
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_tempo = Label(janela, text='00:00:00', font=('Times 50 bold'), bg=cor1, fg=cor6)

'''Posicionamento para dentro da janela'''
label_app.place(x=20, y=5)
label_tempo.place(x=20, y=30)

'''Criando botões: Iniciar, Pausa,'''
botao_iniciar = Button(janela, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=12, y=130)

botao_pausar = Button(janela, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=113, y=130)

botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=211, y=130)



janela.mainloop()