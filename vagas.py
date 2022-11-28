from tkinter import * 
import tkinter as tk
from tkinter import ttk 
from functions import Funcs


class Application(Funcs):

    def __init__(self) -> None:
        self.root = root
        # mostra janela criada
        self.display()
        # janelas
        self.frame_form()
        # buttons
        self.create_button()
        # input, entry, combox
        self.input_text()
        # treeview
        self.mostra_lista_display()
        # mostrar datas na treeview do banco de dados
        self.datas_to_treeview()
        
    
    def display(self) -> None:
        self.root.title('Cadastro de vaga de garagem')
        self.root.configure(background='#0075b3')
        self.root.geometry('710x410')
        self.root.resizable(False, False)
        
    def frame_form(self) -> None:
        self.frame_window = Frame(self.root, bg = '#fff', highlightbackground="#0075b3")
        self.frame_window.place(relx = 0.01, rely = 0.03, relwidth = 0.37, relheight = 0.94)

    def create_button(self) -> None:
        # salvar
        self.btn_save = Button(self.frame_window, text='Save', bd=0, bg="#0075b3",
        highlightthickness=1,highlightbackground="#fff", cursor="hand1",
        command=self.insert_dml)

        self.btn_save.place(relx=0.14, rely=0.81, relwidth=0.25, relheight=0.1)

        # limpar
        self.btn_clear = Button(self.frame_window, text='Clear', bd=0,
        highlightthickness=1,highlightbackground="#fff", cursor="hand1",
        command= self.clear_form)
        self.btn_clear.place(relx=0.58, rely=0.81, relwidth=0.25, relheight=0.1)

        #search
        self.btn_search = Button(self.root, text='Search', bd=0, bg='#fff',fg='#0075b3',
        highlightthickness=1,highlightbackground="#0075b3", cursor="hand1")

        self.btn_search.place(relx=0.81, rely=0.04, relwidth=0.1, relheight=0.09)

        # atualizar
        self.btn_edit = Button(self.root, text='Update', bd=0, bg='#fff',fg='#0075b3',
        highlightthickness=1,highlightbackground="#0075b3", cursor="hand1")
        self.btn_edit.bind("<Button-1>", self.edit_dml)
        
        self.btn_edit.place(relx=0.55, rely=0.84, relwidth=0.1, relheight=0.09)

        # delete
        self.btn_delete = Button(self.root, text='Delete', bd=0, bg='#fff',fg='#0075b3',
        highlightthickness=1,highlightbackground="#0075b3", cursor="hand1",
        command=self.delete_dml)
        
        self.btn_delete.place(relx=0.77, rely=0.84, relwidth=0.1, relheight=0.09)


    def input_text(self) -> None:
        # criacao label placa do carro
        self.lb_placa = Label(self.frame_window, text="Placa", bg = "#fff", 
        fg="#0075b3")
        self.lb_placa.place(relx=0.04, rely=0.065)

        self.placa_entry = Entry(self.frame_window, bg = "#f2f2f2", bd=0, fg="#000",
        width=4,highlightthickness=1, highlightcolor="#252426", 
        highlightbackground="#fff", insertbackground='#252426')
        # posicionamento
        self.placa_entry.place(relx=0.33, rely=0.05, relwidth=0.6, relheight=0.08)

        #  criacao label morador
        self.lb_morador = Label(self.frame_window, text="Morador", bg = "#fff", 
        fg="#0075b3")
        self.lb_morador.place(relx=0.04, rely=0.2)
        # input morador
        self.morador_entry = Entry(self.frame_window, bg = "#f2f2f2", bd=0, fg="#000",
        width=4,highlightthickness=1, highlightcolor="#252426", 
        highlightbackground="#fff", insertbackground='#252426')
        self.morador_entry.place(relx=0.33, rely=0.18, relwidth=0.6, relheight=0.08)

        # apto
        listApto = ['-',101,102,103,201,202,203,301,302,303,401,402,403,501,502,503]
        self.lb_apto = Label(self.frame_window, text="Apto", bg = "#fff", 
        fg="#0075b3")
        self.lb_apto.place(relx=0.05, rely=0.34)
        # input apto
        self.apto_cb = ttk.Combobox(self.frame_window, value=listApto, 
        width = 4,foreground='#0075b3', background='#fff')
        self.apto_cb.set('-')
        self.apto_cb.place(relx=0.33, rely=0.32, relwidth=0.21, relheight=0.058)

         #  criacao label telefone
        self.lb_telefone = Label(self.frame_window, text="Telefone", bg = "#fff", 
        fg="#0075b3")
        self.lb_telefone.place(relx=0.05, rely=0.48)
        # input telefone
        self.telefone_entry = Entry(self.frame_window, bg = "#f2f2f2", bd=0, fg="#000", width=4,
        highlightthickness=1, highlightcolor="#252426", 
        highlightbackground="#fff", insertbackground='#252426')
        self.telefone_entry.place(relx=0.33, rely=0.48, relwidth=0.6, relheight=0.08)

        # input pesquisa
        self.search_entry = Entry(self.root, bg = "#f2f2f2", bd=0, fg="#000",relief=SOLID, width=4,
        highlightthickness=1, highlightcolor="#0075b3", highlightbackground="#fff",
        insertbackground='#0075b3')
        self.search_entry.place(relx=0.48, rely=0.04, relwidth=0.29, relheight=0.10)


    def mostra_lista_display(self) -> None:
        self.trv = ttk.Treeview(self.root, height=3,
        column=('col1','col2','col3','col4','col5', 'col6'))
        # personalizar treeview
        ttk.Style().configure(self.trv, background = "black", foreground="white", fieldbackground="red")
        # nome das colunas
        self.trv.heading('#0', text='')
        self.trv.heading('#1', text='ID')
        self.trv.heading('#2', text='Apto')
        self.trv.heading('#3', text='Morador')
        self.trv.heading('#4', text='Placa')
        self.trv.heading('#5', text='Telefone')
        # tamanho das colunas
        self.trv.column('#0', width=0, stretch=NO)
        self.trv.column('#1', width=30, minwidth=15, anchor=CENTER)
        self.trv.column('#2', width=60, minwidth=15, anchor=CENTER)
        self.trv.column('#3', width=125, minwidth=25, anchor=CENTER)
        self.trv.column('#4', width=80, minwidth=25, anchor=W)
        self.trv.column('#5', width=125, minwidth=25, anchor=W)
        # posicao treeview
        self.trv.place(relx=0.39, rely=0.2, relwidth=0.58, relheight=0.6)
        # barra de rolagem
        self.scroolbar_trv = Scrollbar(self.root, orient='vertical')
        self.trv.configure(yscroll=self.scroolbar_trv.set)
        # posicao barra de rolagem
        self.scroolbar_trv.place(relx=0.97, rely=0.2, relwidth=0.014, relheight=0.6)
        # evento de deplo click, auxilia no update
        self.trv.bind("<ButtonRelease-1>", self.edit_in_treeview)

    # retornar treeview
    def element_trv(self):
        return self.trv
            

if __name__ == "__main__":
    root = Tk()
    Application()
    root.mainloop()