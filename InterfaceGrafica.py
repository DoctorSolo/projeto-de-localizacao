from tkinter    import *
from Local      import Local

# Vou implementar os valores atravez de uma interface grafica
class InterfaceGrafica:
    def __init__(self) -> None:
        pass


    # Devo ter certeza que o valor inserido seja um numero
    def validade_numero(self, P):
        # Caso user comece digitando um numero negativo a validação vai aceitar
        if P == "" or P == "-":
            return True
        try:
            # Tenta converter o valor de entrada, caso se aplica a float a validação aceita
            float(P)
            return True
        # Caso o valor de entrada seja um caractere qualquer então o valor não sera digitado
        except ValueError:
            return False


    def Interface(self):
        janela = Tk()   # Crio aqui a janenela
        janela.title("Buscar Localização")

        # Atributo para a validade da entrada, se numero ou letra
        validade = (janela.register(self.validade_numero), '%P')

        # Para entrada da latitude
        titulo = Label(janela, text="Digite em baixo o valor das cordenada", pady=10)
        titulo.grid(column=0,row=0)

        txt_latitude = Label(janela, text="Informe aqui o valor da latitude: ")
        txt_latitude.grid(column=0, row=1)

        entrada_latitude = Entry(janela, validate="key", validatecommand=validade)
        entrada_latitude.grid(column=1,row=1, pady=10, padx=30)

        # Para entrada da longitude
        txt_longitude = Label(janela, text="Informe aqui o valor da longitude: ")
        txt_longitude.grid(column=0, row=2)

        entrada_longitude = Entry(janela, validate="key", validatecommand=validade)
        entrada_longitude.grid(column=1,row=2, pady=10)

        # Resultado
        result = ''
        saida = Label(janela, text='')
        saida.grid(column=3, row=1)
        
        
        # Resultado no mapa
        def resultado_mapa(local_img='imagens/nao_encontrado.png'):
            img = PhotoImage(file=local_img)
            mapa = Label(janela, image=img, padx=20, pady=20)
            mapa.image = img
            mapa.grid(column=3,row=5)

        
        resultado_mapa()
        

        # Para o botão
        def insere_valor():
            lat     = float(entrada_latitude.get())
            long    = float(entrada_longitude.get())
            local0 = Local(lat, long)
            resultado_mapa(local0.mapa())
            saida["text"] = local0.pesquisa()


        enter = Button(janela, text="ENTER", command=insere_valor)
        enter.grid(column=0, row=4)

        janela.mainloop()   #Fim da janela