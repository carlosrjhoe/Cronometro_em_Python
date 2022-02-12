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
janela.geometry('303x280')
janela.configure(bg=cor1)

#   Imagem da janela
logo = PhotoImage(file='imagens/Kyojuro Rengoku_Image Gallery.png')
logo = logo.subsample(1, 1)
figura = Label(image=logo)

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

#   Função Iniciar
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
            
        #   Aqui estou colocando o tempo para percorrer menos de 1s, para diminuir o tempo de execução de amostra da aplicação.
        label_tempo.after(300, iniciar)
        contador += 1

#   Função Pausar
def start():
    global rodar
    rodar = True
    iniciar()

#   Função Reiniciar
def reiniciar():
    global contador
    global tempo
    
    #   Reiniciando o tempo do contador
    contador = 0
    
    #   Reiniciando o tempo
    tempo = '00:00:00'
    label_tempo['text'] = tempo
    
def pausar():
    global rodar
    rodar = False
    
#   Criando labels: Cronômetro
figura.grid()
label_app = Label(janela, text='Cronômetro', font=('Arial 10'))
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bd=0, highlightthickness=0)

#   Posicionamento para dentro da janela
label_app.place(x=20, y=5)
label_tempo.place(x=25, y=140)

#   Criando botões: Iniciar, Pausa, Reiniciar
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge', bd=0, highlightthickness=0)
botao_iniciar.place(x=12, y=230)

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge', bd=0, highlightthickness=0)
botao_pausar.place(x=113, y=230)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivi 8 bold'), relief='raised', overrelief='ridge', bd=0, highlightthickness=0)
botao_reiniciar.place(x=211, y=230)


janela.mainloop()