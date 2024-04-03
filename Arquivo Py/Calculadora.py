from tkinter import *
from math import *

janela = Tk()
janela.title('A Calculadora')
janela.geometry('800x800')

# Label1
meulabel = Label(janela, text='Calculadora:', font=('Arial', 43), fg="black", bg="lightgray")
meulabel.pack()

# Label2
meulabel2 = Label(janela, text='Número 1:', font=('Arial', 20), fg="black", bg="lightgray")
meulabel2.pack()

# Número1
entrada_de_texto = StringVar()
número = Entry(janela, textvariable=entrada_de_texto, bg='lightblue', font=("Arial", 12))
número.pack()

# Label3
meulabel3 = Label(janela, text='Operação desejada:', font=('Arial', 20), fg="black", bg="lightgray")
meulabel3.pack()

# Radios
operacao_var = StringVar()
radio1 = Radiobutton(text='+', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao1", width='4', variable=operacao_var)
radio1.pack()
radio2 = Radiobutton(text='-', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao2", width='4', variable=operacao_var)
radio2.pack()
radio3 = Radiobutton(text='X', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao3", width='4', variable=operacao_var)
radio3.pack()
radio4 = Radiobutton(text='/', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao4", width='4', variable=operacao_var)
radio4.pack()
radio5 = Radiobutton(text='^', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao5", width='4', variable=operacao_var)
radio5.pack()
radio6 = Radiobutton(text='%', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao6", width='4', variable=operacao_var)
radio6.pack()
radio7 = Radiobutton(text='√', font=('Arial', 20), fg='blue', bg="lightgray", value="opcao7", width='4', variable=operacao_var)
radio7.pack()

# Label3
meulabel4 = Label(janela, text='Número 2:', font=('Arial', 20), fg="black", bg="lightgray")
meulabel4.pack()

# Número2
entrada_de_texto2 = StringVar()
número2 = Entry(janela, textvariable=entrada_de_texto2, bg='lightblue', font=("Arial", 12))

def on_radio_select(*args):
    operacao = operacao_var.get()
    if operacao == 'opcao7':
        meulabel4.pack_forget()
        número2.pack_forget()
    else:
        meulabel4.pack()
        número2.pack()

# Associando a função on_radio_select ao rastreamento da variável operacao_var
operacao_var.trace_add("write", on_radio_select)

# Chama manualmente a função on_radio_select uma vez para garantir que o número2 seja removido corretamente
on_radio_select()

número2.pack()

# Botão
def botao():
    num1 = float(entrada_de_texto.get().replace(',','.'))
    num2 = float(entrada_de_texto2.get().replace(',','.'))
    operacao = operacao_var.get()
    if operacao == 'opcao1':
        resultado = num1 + num2
        labelzao.config(text=f'O resultado da sua soma é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
    elif operacao == 'opcao2':
        resultado = num1 - num2
        labelzao.config(text=f'O resultado da sua subtração é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
    elif operacao == 'opcao3':
        resultado = num1 * num2
        labelzao.config(text=f'O resultado da sua multiplicação é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
    elif operacao == 'opcao4':
        if num2 != 0:
            resultado = num1 / num2
            labelzao.config(text=f'O resultado da sua divisão é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
        else:
            resultado = "Erro: Divisão por zero"
            labelzao.config(text=resultado, font=('Arial', 25), fg='navyblue')
    elif operacao == 'opcao5':
        resultado = num1 ** num2
        labelzao.config(text=f'O resultado da sua potenciação é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
    elif operacao == 'opcao6':
        resultado = (num1 * num2) / 100
        labelzao.config(text=f'O resultado da sua porcentagem é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
    elif operacao == 'opcao7':
        resultado = sqrt(num1)
        labelzao.config(text=f'O resultado da sua raiz quadrada é: {resultado:.2f}.', font=('Arial', 25), fg='navyblue')
        
botaozao = Button(janela, text="Resultado!", font=('Arial', 30), fg='white', bg='navyblue', command=botao)
labelzao = Label(text='')
botaozao.pack()
labelzao.pack()

janela.mainloop()
