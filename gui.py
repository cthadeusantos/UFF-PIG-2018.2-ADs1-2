#!/usr/bin/env python
# coding: UTF-8
#
## @package GUI Class
#
#  @brief This class generate a GUI to Ranking Class
#  @author Carlos Thadeu Santos - ID: 17113050228
#  @date 31-Oct-2018
#  @version 0.0.1 alpha
#
try:
    # for Python2
    import Tkinter as Tk   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    import tkinter as Tk   ## notice lowercase 't' in tkinter here
from tkinter import ttk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame
from tkinter import Radiobutton
from tkinter import Listbox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog
#from window1 import *
from ranking import *
from ast import literal_eval

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.ranking=[]
        ## Define os três frames existentes na janela principal
        ## A janela principal foi dividida em 3 frames (esquerda, central e direita)
        self.leftframe = Frame(self)
        self.leftframe.grid(row=0,column=0,stick=Tk.NS+Tk.E)
        self.centerframe = Frame(self)
        self.centerframe.grid(row=0,column=1,stick=Tk.NS)
        self.rightframe = Frame(self)
        self.rightframe.grid(row=0,column=2,stick=Tk.NS+Tk.W)
        # Inicializei as instancias aqui porque senão self.botaoSelecionaEntrada\
        # não existe quando da criação dos botoes do frame esquerdo
        # container 1 - contem os objetos para leitura de arquivo
        # container 2 - contem os objetos para entrada de dados manual
        # container 3 - contem os objetos para escolha aleatoria dos rankings
        self.container1 = LabelFrame(self.centerframe, text="Escolha o arquivo", padx=5, pady=5)
        self.container2 = LabelFrame(self.centerframe, text="Entrada de dados", padx=5, pady=5)
        self.container3 = LabelFrame(self.centerframe, text="Escolha aleatória", padx=5, pady=5)

        ###    
        #### Monta frame esquerdo
        #### Frame dos botões
        ###
        lblframe = LabelFrame(self.leftframe, text="Selecione entrada", padx=5, pady=5)
        lblframe.grid(row=0,column=0)
        button1 = Button(lblframe, text="Arquivo", width=20,command= lambda: self.botaoSelecionaEntrada(1))
        button1.grid(row=0,column=0)
        button2 = Button(lblframe, text="Manual",  width=20,command= lambda: self.botaoSelecionaEntrada(2))
        button2.grid(row=1,column=0)
        button3 = Button(lblframe, text="Aleatório",  width=20,command= lambda: self.botaoSelecionaEntrada(3))
        button3.grid(row=2,column=0)
        lblframe = LabelFrame(self.leftframe, text="Calculadora", padx=5, pady=5)
        lblframe.grid(row=3,column=0, pady=20)
        button1 = Button(lblframe, text="Calculadora", width=20,command= lambda: self.Calculadora())
        button1.grid(row=0,column=0)
        button2 = Button(lblframe, text="Reset", width=20,command= lambda: self.resetDisplayResults())
        button2.grid(row=1,column=0)
     
        ###
        ### Monta Frame central
        ###
        ### O Frame central contém 3 "containers" que serão ligados e desligados em tempo
        ### de execução através dos botões existentes no frame esquerdo
        ### 
        ##Entrada através de arquivo
        ##
        self.mySelectionF = Tk.StringVar()
        labelvalue = self.mySelectionF
        self.container1.grid(row=0, column=0)
        buttonFile = Tk.Button(self.container1, text = 'Ler arquivo', width = 10, command=self.askopenfilename)
        buttonFile.grid(row=0,column=0,sticky='N')        
        self.displayRanking1()
        ### Desliga objeto do frame da tela
        self.container1.isgridded = True
        #self.container1.grid_forget()
        
        #
        # Entrada manual
        #
        #### DESISTI DE FAZER ASSIM SE DER TEMPO VOLTO A FAZER SENAO
        #### FAÇO DEPOIS DA ENTRAGA DA AD
        ####
        #self.mySelection = Tk.StringVar()
        #labelvalue = self.mySelection
                #self.container2 = LabelFrame(self.centerframe, text="Entrada de dados", padx=5, pady=5) ## Foi criado la em cima
        #self.container2.grid(row=0, column=0)
                # label com nome do ranking
        #self.label = Label(self.container2, text=labelvalue)
        #self.label.grid(row=0,column=1)
        # campo de entrada
        #entryA = Entry(self.container2,width=6)               #criamos o campo de texto
        #entryA.grid(column=0,row=1,sticky='EW'+'S')
        # Botao
        #button4 = Tk.Button(self.container2, text = '->', width = 10)
        #button4.grid( row=2,column=0,sticky='EW'+'N')
        #Combobox
        #self.comboboxM = ttk.Combobox(self.container2, width= 15, state="readonly", textvariable = self.mySelection)
        #self.comboboxM["values"] = ("Ranking 1", "Ranking 2")
        #self.comboboxM.grid(row=0, column=0)
        #self.comboboxM.bind("<<ComboboxSelected>>", self.callbackFunc)
        #ListBox
                #value=["one", "two", "three", "four", "five", "six", "seven","eight","nine","ten","eleven","twelve"] ### Somente para teste
        #value = []
        #self.listbox = Listbox(self.container2,selectmode=Tk.SINGLE)
        #scrollbar = Tk.Scrollbar(self.container2, orient=Tk.VERTICAL)
        #self.listbox.config( yscrollcommand=scrollbar.set)
        #scrollbar.configure(command=self.listbox.yview)
        #scrollbar.config(command=self.listbox.yview)
        #self.listbox.insert(Tk.END, None)
        #for item in value:
        #    self.listbox.insert(Tk.END, item)
        #self.listbox.grid(row=1, column=1,stick=Tk.W)
        #scrollbar.grid(row=1,column=2,stick=Tk.NS+Tk.W)

        ### Aqui resolvi fazer assim, senão não ia dar tempo para fazer do jeito que eu queria
        ### Caminho mais fácil, senão nao consigo fazer os testes se é que vou conseguir
        self.container2.grid(row=0, column=0)
        self.v1 = Tk.IntVar(value=1)
        #self.v1 = Tk.StringVar(value="1")
        self.v1.set(1)
        self.v2 = Tk.IntVar(value=1)
        #self.v2 = Tk.StringVar(value="1")
        self.v2.set(1)

        self.displayEntradaManual()
        #self.label = Label(self.container2, text="Escolha o tipo de entrada")
        #self.label.grid(row=0,column=0, columnspan=2)
        #self.rb1 = Tk.Radiobutton(self.container2, text="Ranking", variable=self.v1, value=1,state=Tk.ACTIVE,indicatoron=1)
        #self.rb1.grid(row=1,column=0)
        #self.rb2 = Tk.Radiobutton(self.container2, text="Score", variable=self.v1, value=2,state=Tk.ACTIVE,indicatoron=1)
        #self.rb2.grid(row=1,column=1)
        #self.label = Label(self.container2, text="Ranking / Score 1")
        #self.label.grid(row=2,column=0)
        #self.entryM1 = Entry(self.container2,width=30)               #criamos o campo de texto
        #self.entryM1.grid(row=3,column=0,sticky='EW'+'S',columnspan=2)
    
        #self.rb3 = Tk.Radiobutton(self.container2, text="Ranking", variable=self.v2, value=1,state=Tk.ACTIVE,indicatoron=1)
        #self.rb3.grid(row=4,column=0)
        #self.rb4 = Tk.Radiobutton(self.container2, text="Score", variable=self.v2, value=2,state=Tk.ACTIVE,indicatoron=1)
        #self.rb4.grid(row=4,column=1)
        #self.label = Label(self.container2, text="Ranking / Score 2")
        #self.label.grid(row=5,column=0)
        #self.entryM2 = Entry(self.container2,width=30)               #criamos o campo de texto
        #self.entryM2.grid(row=6,column=0,sticky='EW'+'S',columnspan=2)
        self.container2.isgridded = False
        self.container2.grid_forget()

        ##entrada aleatoria
        #self.container3 = LabelFrame(self.centerframe, text="Entrada de dados", padx=5, pady=5)
        self.mySelectionA = Tk.StringVar()
        self.container3.grid(row=0, column=0)
        self.container3A = LabelFrame(self.container3, text="Define tamanho", padx=5, pady=5)
        self.container3A.grid(row=0, column=0)
        # label com nome do ranking
        self.label = Label(self.container3A, text='Selecione o tamanho dos rankings')
        self.label.grid(row=0,column=0, sticky="S")
        self.entryB = Entry(self.container3A,width=6)               #criamos o campo de texto
        self.entryB.grid(row=1, column=0,sticky='EW'+'S')
        button5 = Tk.Button(self.container3A, text = 'Gerar', width = 10, command=self.gerarRankingAleatorio)
        button5.grid( row=2,column=0,sticky='EW'+'N')
        
        self.displayRanking()
        #self.container3B = LabelFrame(self.container3,text="Visualiza RANKINGs", padx=5, pady=5)
        #self.container3B.grid(row=0, column=1)
        self.container3.isgridded = False
        self.container3.grid_forget()
        ####self.container3B = LabelFrame(self.container3, text="Visualiza RANKINGs", padx=5, pady=5)
        ####self.container3B.grid(row=0, column=1)
        ####self.comboboxA = ttk.Combobox(self.container3B, width= 15, state="readonly", textvariable = self.mySelectionA)
        ####self.comboboxA["values"] = ("Ranking 1", "Ranking 2")
        ####self.comboboxA.grid(row=0, column=1)
        ####self.comboboxA.bind("<<ComboboxSelected>>", self.callbackRandom)
        #value=["one", "two", "three", "four", "five", "six", "seven","eight","nine","ten","eleven","twelve"] ### Somente para teste
        ####value = []
        ####self.listbox = Listbox(self.container3B,selectmode=Tk.SINGLE)
        ####scrollbar = Tk.Scrollbar(self.container3B, orient=Tk.VERTICAL)
        ####self.listbox.config( yscrollcommand=scrollbar.set)
        ####scrollbar.configure(command=self.listbox.yview)
        ####scrollbar.config(command=self.listbox.yview)
        ####self.listbox.insert(Tk.END, None)
        ####for item in value:
        ####    self.listbox.insert(Tk.END, item)
        ####self.listbox.grid(row=1, column=1,stick=Tk.W)
        ####scrollbar.grid(row=1,column=2,stick=Tk.NS+Tk.W) 
        ####self.container3.isgridded = False
        ####self.container3.grid_forget()

        ###    
        #### Monta frame direito
        ###
        self.lblframe = LabelFrame(self.rightframe, text="RESULTADOS", padx=5, pady=5)
        self.lblframe.grid(row=0,column=0)
        self.label = Label(self.lblframe, text="Kemeny = ")
        self.label.grid(row=0,column=0, sticky=Tk.W)
        result = str(0)
        self.labelkemeny = Label(self.lblframe, text=result)
        self.labelkemeny.grid(row=0,column=1)
        self.label = Label(self.lblframe, text="Footrule = ")
        self.label.grid(row=1,column=0,sticky=Tk.W)
        self.labelfootrule = Label(self.lblframe, text=result)
        self.labelfootrule.grid(row=1,column=1)
        self.label = Label(self.lblframe, text="*** Inversões ***")
        self.label.grid(row=2,column=0)
        self.label = Label(self.lblframe, text="Inversões Ranking 1 = ")
        self.label.grid(row=3,column=0,sticky=Tk.W)
        self.label = Label(self.lblframe, text="Inversões Ranking 2 = ")
        self.label.grid(row=4,column=0,sticky=Tk.W)
        self.labelinv1 = Label(self.lblframe, text=result)
        self.labelinv1.grid(row=3,column=1)
        self.labelinv2 = Label(self.lblframe, text=result)
        self.labelinv2.grid(row=4,column=1)
        self.bye = Button(self.rightframe, text="Bye Bye", command=self.quit)
        self.bye.grid(row=5,column=0)
        self.pack()

    # Monta radiobutton no frame central container 2
    def displayEntradaManual(self):
        """@ Show RadioButton on container2 in Application Class
           @example self.displayEntradaManual()
        """
        self.label = Label(self.container2, text="Escolha o tipo de entrada")
        self.label.grid(row=0,column=0, columnspan=2)
        self.rb1 = Tk.Radiobutton(self.container2, text="Ranking", variable=self.v1, value=1,state=Tk.ACTIVE,indicatoron=1)
        self.rb1.grid(row=1,column=0)
        self.rb2 = Tk.Radiobutton(self.container2, text="Score", variable=self.v1, value=2,state=Tk.ACTIVE,indicatoron=1)
        self.rb2.grid(row=1,column=1)
        self.label = Label(self.container2, text="Ranking / Score 1")
        self.label.grid(row=2,column=0)
        self.entryM1 = Entry(self.container2,width=30)               #criamos o campo de texto
        self.entryM1.grid(row=3,column=0,sticky='EW'+'S',columnspan=2)
    
        self.rb3 = Tk.Radiobutton(self.container2, text="Ranking", variable=self.v2, value=1,state=Tk.ACTIVE,indicatoron=1)
        self.rb3.grid(row=4,column=0)
        self.rb4 = Tk.Radiobutton(self.container2, text="Score", variable=self.v2, value=2,state=Tk.ACTIVE,indicatoron=1)
        self.rb4.grid(row=4,column=1)
        self.label = Label(self.container2, text="Ranking / Score 2")
        self.label.grid(row=5,column=0)
        self.entryM2 = Entry(self.container2,width=30)               #criamos o campo de texto
        self.entryM2.grid(row=6,column=0,sticky='EW'+'S',columnspan=2)
        self.label = Label(self.container2, text="Formato da entrada(ranking): 5 4 3 2 1")
        self.label.grid(row=7,column=0,sticky='W')
        self.label = Label(self.container2, text="Formato da entrada(score): 0.65 0.32 0.62 0.23 0.34")  
        self.label.grid(row=8,column=0,sticky='W')
        self.container2.isgridded = False
        self.container2.grid_forget()

    # Reset nos valores do frame direito
    def resetDisplayResults(self):
        """@ Reset values kemeny, footrule and Inversions and clean labels
           @example self.resetDisplayResults()
        """
        del self.ranking[:]
        result = str(0)
        self.labelkemeny = Label(self.lblframe, text=result)
        self.labelkemeny.grid(row=0,column=1)
        self.labelfootrule = Label(self.lblframe, text=result)
        self.labelfootrule.grid(row=1,column=1)
        self.labelinv1 = Label(self.lblframe, text=result)
        self.labelinv1.grid(row=3,column=1)
        self.labelinv2 = Label(self.lblframe, text=result)
        self.labelinv2.grid(row=4,column=1)
        if self.buttonClick == 1:
            self.displayRanking1()
        if self.buttonClick == 2:
            self.entryM1.delete(0, 'end')               #limpamos o campo de texto
            self.entryM1.grid(row=3,column=0,sticky='EW'+'S',columnspan=2)
            self.entryM2.delete(0, 'end')               #limpamos o campo de texto
            self.entryM2.grid(row=6,column=0,sticky='EW'+'S',columnspan=2)
        if self.buttonClick == 3:
            self.displayRanking()
        messagebox.showinfo("Mensagem", "Kemeny, footrule e inversões zeradas!")

    # Metodo que retorna um evento de selecao
    def displayRanking(self):
        """@ Show combobox on screen
           @example self.displayRanking()
        """
        self.container3B = LabelFrame(self.container3, text="Visualiza RANKINGs", padx=5, pady=5)
        self.container3B.grid(row=0, column=1)
        self.comboboxA = ttk.Combobox(self.container3B, width= 15, state="readonly", textvariable = self.mySelectionA)
        self.comboboxA["values"] = ("Ranking 1", "Ranking 2")
        self.comboboxA.grid(row=0, column=1)
        self.comboboxA.bind("<<ComboboxSelected>>", self.callbackRandom)
        #value=["one", "two", "three", "four", "five", "six", "seven","eight","nine","ten","eleven","twelve"] ### Somente para teste
        self.displayRankingListbox()
        #####value = []
        #####self.listbox = Listbox(self.container3B,selectmode=Tk.SINGLE)
        #####scrollbar = Tk.Scrollbar(self, orient=Tk.VERTICAL)
        #####self.listbox.config( yscrollcommand=scrollbar.set)
        #####scrollbar.configure(command=self.listbox.yview)
        #####scrollbar.config(command=self.listbox.yview)
        #####self.listbox.insert(Tk.END, None)
        #####for item in value:
        #####    self.listbox.insert(Tk.END, item)
        #####self.listbox.grid(row=1, column=1,stick=Tk.W)
        #####scrollbar.grid(row=1,column=2,stick=Tk.NS+Tk.W) 
        #self.container3B = LabelFrame(self.container3B,text="Visualiza RANKINGs", padx=5, pady=5)
        #self.container3B.grid(row=0, column=1)
    def displayRankingListbox(self, value=[]):
        """@note show Ranking on display
           @param[in] a list
           @example self.displayRankingListbox([1 2 3 4 5])
        """
        self.value = value
        self.listbox = Listbox(self.container3B,selectmode=Tk.SINGLE)
        scrollbar = Tk.Scrollbar(self.container3B, orient=Tk.VERTICAL)
        self.listbox.config( yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox.yview)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.insert(Tk.END, None)
        for item in value:
            self.listbox.insert(Tk.END, item)
        self.listbox.grid(row=1, column=1,stick=Tk.W)
        scrollbar.grid(row=1,column=2,stick=Tk.NS+Tk.W)
    ## Segui o Caminho mais fácil
    ## Dupliquei displayRanking e alterei o container apenas
    ## Não é o correto, mas não está errado, se sobrar tempo faço da forma correta
    def displayRanking1(self):
        """@ Show combobox on screen
           @example self.displayRanking1()
        """
        self.container1B = LabelFrame(self.container1, text="Visualiza RANKINGs", padx=5, pady=5)
        self.container1B.grid(row=0, column=1)
        self.comboboxF = ttk.Combobox(self.container1B, width= 15, state="readonly", textvariable = self.mySelectionF)
        self.comboboxF["values"] = ("Ranking 1", "Ranking 2")
        self.comboboxF.grid(row=0, column=1)
        self.comboboxF.bind("<<ComboboxSelected>>", self.callbackRandom)
        #value=["one", "two", "three", "four", "five", "six", "seven","eight","nine","ten","eleven","twelve"] ### Somente para teste
        self.displayRankingListbox1()
        '''
        value = []
        self.listbox = Listbox(self.container3B,selectmode=Tk.SINGLE)
        scrollbar = Tk.Scrollbar(self, orient=Tk.VERTICAL)
        self.listbox.config( yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox.yview)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.insert(Tk.END, None)
        for item in value:
            self.listbox.insert(Tk.END, item)
        self.listbox.grid(row=1, column=1,stick=Tk.W)
        scrollbar.grid(row=1,column=2,stick=Tk.NS+Tk.W) '''
        #self.container3B = LabelFrame(self.container3B,text="Visualiza RANKINGs", padx=5, pady=5)
        #self.container3B.grid(row=0, column=1)
    def displayRankingListbox1(self, value=[]):
        """@note show Ranking on display
           @param[in] a list
           @example self.displayRankingListbox([1 2 3 4 5])
        """
        self.value = value
        self.listbox = Listbox(self.container1B,selectmode=Tk.SINGLE)
        scrollbar = Tk.Scrollbar(self.container1B, orient=Tk.VERTICAL)
        self.listbox.config( yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox.yview)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.insert(Tk.END, None)
        for item in value:
            self.listbox.insert(Tk.END, item)
        self.listbox.grid(row=1, column=1,stick=Tk.W)
        scrollbar.grid(row=1,column=2,stick=Tk.NS+Tk.W)
    #
    # Gera dois rankings Aleatórios a partir de um inteiro
    # os rankings sao colocados em um vetor self.ranking
    def gerarRankingAleatorio(self):
        """@note Build a random Ranking and show on display
           @example self.gerarRankingAleatorio()
        """
        self.resetDisplayResults()
        try:
            value = int(self.entryB.get())
        except ValueError:
            messagebox.showinfo("ERRO!", "Informar o tamanho do ranking a ser gerado!")
            return
        #choice = self.mySelectionA.get()  ### Não precisei a selecao acontece em displayrankinglistbox
        #index = self.comboboxA.current()  ### nao precisei a selecao acontece em displayrankinglistbox
        if value < 1:
            messagebox.showinfo("Title", "Valor inválido ( "+value+" )")
        else:
            del self.ranking[:]
            for _ in range(2): self.ranking.append(Ranking(value))
            messagebox.showinfo("Title", "Rankings 1 e 2 gerados")
            self.comboboxA.current(0)
            self.displayRankingListbox(getattr(self.ranking[0],'ranking'))
            #self.resetDisplayResults()
    
    #def callbackFunc(self, event):
    #    select = self.mySelection.get()
    #    self.labelvalue = select
    #    self.label = Label(self.container2, text=self.labelvalue)
    #    self.label.grid(row=0,column=1)
    #    print(select)      

    def callbackRandom(self, event):
        """@note auxiliary method to gerarRankingAleatorio
           @example self.callbackRandom()
        """        
        #select = self.mySelection.get()
        try:
            #_ = self.ranking[0]
            #_ = getattr(self.ranking[0],"ranking")
            index = self.comboboxA.current()
            array = getattr(self.ranking[index],'ranking')
            self.listbox.delete(0,Tk.END)
            self.listbox.insert(Tk.END, None)
            for item in array:
                self.listbox.insert(Tk.END, item)
            self.listbox.grid(row=1, column=1,stick=Tk.W)
        except IndexError:
            messagebox.showinfo("ERRO!", "Não existem Rankings gerados!")
            return

    def askopenfilename(self):
        """@note Open ranking file
           @example self.askopenfilename()
        """   
        filepath = askopenfilename()
        if filepath:
            #self.container1.filepaths.append(filepath)
            with open(filepath,"r+") as f:
                del self.ranking[:]
                for line in f:
                    value = line.replace("\n","").replace("\r","") # do something with the line
                    try:
                        value = literal_eval(value)
                    except SyntaxError:
                        messagebox.showinfo("ERRO!", "Arquivo incompatível!")
                        return   
                    else:
                        if type(value) is int:
                            del self.ranking[:]
                            for _ in range(2): self.ranking.append(Ranking(value))
                            messagebox.showinfo("Title", "Rankings 1 e 2 gerados")
                        elif type(value) is list:
                            self.ranking.append(Ranking(value))
                        elif type(value) is tuple:
                            self.ranking.append(Ranking(value))                                            
            #for line in inputfile.readline():
            ##    line = line.replace("\n", "").replace("\r", "")
             #   print(line)

             #   #value = literal_eval(line)
             #   #print(type(value))
            self.comboboxF.current(0)
            self.displayRankingListbox1(getattr(self.ranking[0],'ranking'))
            f.close()

    def botaoSelecionaEntrada(self, value):
        """@note Build a rank from tuple.
           @param[in] integer
           @example self.botaoSelecionaEntrada(1)
        """              
        self.buttonClick = value
        print ("Called"+str(self.value))
        self.container1.isgridded = False
        self.container1.grid_forget()
        self.container2.isgridded = False
        self.container2.grid_forget()
        self.container3.isgridded = False
        self.container3.grid_forget()
        if self.buttonClick == 1:
            self.container1.isgridded=True
            self.container1.grid(row=0,column=0)
        if self.buttonClick == 2:
            # Ativa radiobutton do ranking / score (nao esta ativando)
            self.v1.set(1)
            self.v2.set(1)
            # Liga container 2
            self.displayEntradaManual()
            self.container2.isgridded=True
            self.container2.grid(row=0,column=0)
        if self.buttonClick == 3:
            self.container3.isgridded=True
            self.container3.grid(row=0,column=0)
    def checkType(self, lista):
        """@note Verify there are only digits from list
           @param[in] list
           @return Boolean
           @example self.checkType([1, 3, 4, 2])
        """
        for x in lista:
            if type(x) is str:
                return False
        return True

    def Calculadora(self):
        """@note Method to activate auxiliaries methods to show results
           @example self.Calculadora()
        """
        try:
            if self.buttonClick == 1:
                #value1 = self.entryM1.get().split()
                #value2 = self.entryM2.get().split()
                #print("Valor 1", value1, "Valor 2",value2)
                #del self.ranking[:]
                # Adiciona a entrada 1 ao vetor self.ranking
                #if int(self.v1.get()) == 1:
                #    self.ranking.append(Ranking(value1))
                #else:
                #    self.ranking.append(Ranking(tuple(value1)))
                # Adiciona a entrada 2 ao vetor self.ranking
                #if int(self.v2.get()) == 1:
                #    self.ranking.append(Ranking(value2))
                #else:
                #    self.ranking.append(Ranking(tuple(value2)))
                try:
                    #_ = self.ranking[0]
                    _ = getattr(self.ranking[0],"ranking")
                except IndexError:
                    messagebox.showinfo("ERRO!", "Não existem Rankings gerados!")
                    return
                self.showKemeny()
                self.showFootrule()
                self.showInvert()
                print(getattr(self.ranking[0],'ranking'))             
                print(getattr(self.ranking[1],'ranking')) 
            if self.buttonClick == 2:
                value1 = self.entryM1.get().split()
                value2 = self.entryM2.get().split()
                print("Valor 1", value1, "Valor 2",value2)
                if self.checkType(value1) and self.checkType(value2) or\
                not (len(value1)) or any(d is None for d in value1) or value1 is None or\
                not (len(value2)) or any(d is None for d in value2) or value2 is None or\
                len(value1) != len(set(value1)) or len(value2) != len(set(value2)) or\
                len(set(value1)) != len(set(value2)):
                    messagebox.showinfo("ERRO!", "Erro na entrada de dados - Ranking inválido!")
                else:
                    del self.ranking[:]
                    # Adiciona a entrada 1 ao vetor self.ranking
                    if int(self.v1.get()) == 1:
                        self.ranking.append(Ranking(tuple(value1)))
                    else:
                        self.ranking.append(Ranking(value1))
                    # Adiciona a entrada 2 ao vetor self.ranking
                    if int(self.v2.get()) == 1:
                        self.ranking.append(Ranking(tuple(value2)))
                    else:
                        self.ranking.append(Ranking(value2))
                    self.showKemeny()
                    self.showFootrule()
                    self.showInvert()
                    #print(getattr(self.ranking[0],'ranking'))             
                    #print(getattr(self.ranking[1],'ranking'))        
            if self.buttonClick == 3:
                try:
                    _ = getattr(self.ranking[0],"ranking")
                except (IndexError,AttributeError):
                    messagebox.showinfo("Title", "Não existem Rankings gerados!")
                else:
                #    print(len(getattr(self.ranking,"ranking")))
                    self.showKemeny()
                    self.showFootrule()
                    self.showInvert()
        except AttributeError:
            messagebox.showinfo("ERRO!", "Não existem valores a ser calculados!")
            return

    def showKemeny(self):
        """@note Calculate Kemeny distance from Ranking Class than show on screen
           @example self.showKemeny()
        """        
        value1 = Ranking(getattr(self.ranking[0],'ranking'))
        value2 = Ranking(getattr(self.ranking[1],'ranking'))
        print(value1, value2)
        result = value1.kDist(value2)
        self.labelkemeny = Label(self.lblframe, text=result)
        self.labelkemeny.grid(row=0,column=1)
    def showFootrule(self):
        """@note Calculate Footrule distance from Ranking Class than show on screen
           @example self.showFootrule()
        """        
        value1 = Ranking(getattr(self.ranking[0],'ranking'))
        value2 = Ranking(getattr(self.ranking[1],'ranking'))
        print(value1, value2)
        result = value1.fDist(value2)
        self.labelfootrule = Label(self.lblframe, text=result)
        self.labelfootrule.grid(row=1,column=1) 
    def showInvert(self):
        """@note Calculate inversions from Ranking Class than show on screen
           @example self.showInvert()
        """        
        value1 = Ranking(getattr(self.ranking[0],'ranking'))
        value2 = Ranking(getattr(self.ranking[1],'ranking'))
        print(value1, value2)
        result = value1.invCount()
        self.labelinv1 = Label(self.lblframe, text=result)
        self.labelinv1.grid(row=3,column=1)
        result = value2.invCount()
        self.labelinv2 = Label(self.lblframe, text=result)
        self.labelinv2.grid(row=4,column=1) 
#if __name__ == '__main__':
#    app = Application()
#    app.master.title("PIG AD2 - 2018.2 - Carlos Thadeu Santos")
#    app.master.geometry("1024x300")
#    app.mainloop()
