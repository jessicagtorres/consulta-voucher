# -*- coding: utf-8 -*-
import pyodbc
import Tkinter as tk
import tkMessageBox
from datetime import datetime



def consultar_vale_presente():
    id_vp = id_vp_entry.get()
    try:
        # Configurações de conexão
        nome_servidor = "mrd.cacaudigital.com.br,6275"
        login = "CSVP"
        senha = "csvp*@"
        banco_de_dados = "CSVP"

        # Conectar ao banco de dados
        connection_string = "DRIVER={SQL Server};SERVER=" + nome_servidor + ";DATABASE=" + banco_de_dados + ";UID=" + login + ";PWD=" + senha
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Consulta ao banco de dados
        cursor.execute("SELECT ID_VP, LOJA_VP, DATA_VP, PDV_VP, VALOR_VP, DataVAL_VP, LOJAAUT_VP, CPFAUT_VP FROM VALE_PRESENTES WHERE ID_VP = ?", id_vp)

        # Exibir resultados da consulta
        row = cursor.fetchone()
        if row:
            data_vp_formatada = row.DATA_VP.strftime("%d/%m/%Y %H:%M") if row.DATA_VP else ""
            data_val_vp_formatada = row.DataVAL_VP.strftime("%d/%m/%Y %H:%M") if row.DataVAL_VP else ""

            # Converter valores None para espaços em branco, exceto para o ID do vale
            loja_vp = row.LOJA_VP if row.LOJA_VP is not None else ""
            pdv_vp = row.PDV_VP if row.PDV_VP is not None else ""
            valor_vp = row.VALOR_VP if row.VALOR_VP is not None else ""
            lojaaut_vp = row.LOJAAUT_VP if row.LOJAAUT_VP is not None else ""
            cpfaut_vp = row.CPFAUT_VP if row.CPFAUT_VP is not None else ""

            # Atualizar os labels com os resultados da consulta
            resultados_labels[0].config(text=row.ID_VP)
            resultados_labels[1].config(text=loja_vp)
            resultados_labels[2].config(text=data_vp_formatada)
            resultados_labels[3].config(text=pdv_vp)
            resultados_labels[4].config(text=valor_vp)
            resultados_labels[5].config(text=data_val_vp_formatada)
            resultados_labels[6].config(text=lojaaut_vp)
            resultados_labels[7].config(text=cpfaut_vp)
        else:
            tkMessageBox.showinfo("Informações do Vale Presente", "Nenhum resultado encontrado para o voucher informado.")

    except pyodbc.Error as ex:
        tkMessageBox.showerror("Erro ao conectar ao banco de dados", str(ex))
    finally:
        # Fechar conexão
        if conn:
            conn.close()

def criar_interface():
    root = tk.Tk()
    root.title("Consulta de Vale Presente")
   
    # Campo de entrada para o ID do vale
    global id_vp_entry
    id_vp_entry = tk.Entry(root)
    id_vp_entry.grid(row=0, column=1, padx=5, pady=5)

    # Rótulo para o campo de entrada
    id_vp_label = tk.Label(root, text="Vale Presente:")
    id_vp_label.grid(row=0, column=0, padx=5, pady=5)

    # Botão para consultar o vale presente
    consultar_button = tk.Button(root, text="Consultar", command=consultar_vale_presente)
    consultar_button.grid(row=0, column=2, padx=5, pady=5)

    # Criar rótulos para as colunas
    colunas = ["Vale Presente", "Loja Utilizada", "Data de utilização", "PDV", "Valor do Vale Presente", "Data de Vencimento", "Loja Autorizada", "CPF Vinculado"]
 
    for i, coluna in enumerate(colunas):
        label = tk.Label(root, text=coluna, borderwidth=1, relief="solid", width=20)
        label.grid(row=1, column=i, padx=1, pady=1)

    # Criar labels para exibir os resultados
    global resultados_labels
    resultados_labels = []
    for i in range(8):
        resultado_label = tk.Label(root, text="", borderwidth=1, relief="solid", width=20)
        resultado_label.grid(row=2, column=i, padx=1, pady=1)
        resultados_labels.append(resultado_label)

    root.mainloop()

criar_interface()
