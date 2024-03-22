from tkinter import *
janela = Tk()
janela.geometry('800x800')
# Label1
meulabel = Label(janela, text='Celsius para Farenheit:', font=('Arial', 43), fg="black", bg="lightgray")
meulabel.pack()
# Label2
meulabel2 = Label(janela, text='Quantidade de Graus Celsius:', font=('Arial', 20), fg="navyblue", bg="lightgray")
meulabel2.pack()
# Número1
entrada_de_texto = DoubleVar()
número = Entry(janela, textvariable=entrada_de_texto, bg='lightblue', font=("Arial", 12))
número.pack()
# Botao
    
def botao():
    celsius = entrada_de_texto.get()
    resultado = celsius * 1.8 + 32
    print(f'{celsius:.2f}°C convertido pra Farenheit fica: {resultado:.2f}')

botaozao = Button(janela, text="Resultado!", font=('Arial', 30), fg='white', bg='navyblue', command=botao)
botaozao.pack()


janela.mainloop()