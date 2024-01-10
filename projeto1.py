import customtkinter as ctk
import pandas as pd

app = ctk.CTk()
app.geometry("400x150")
app.title("começo")

dados = pd.read_csv('dados.csv')

#usuário
usuario1 = ctk.CTkLabel(app, text='Usuário:  ', width=50)
usuario1.grid(row=0, column=0, padx=0, pady=0)

usuário = ctk.CTkEntry(app, width=300)
usuário.grid(row=0, column=1, padx=0, pady=1)

#senha
senha1 = ctk.CTkLabel(app, text='Senha:  ', width=50)
senha1.grid(row=1, column=0, padx=0, pady=0)

senha = ctk.CTkEntry(app, width=300)
senha.grid(row=1, column=1, padx=0, pady=1)
senha.configure(show="*")

def botaos():
    dados = pd.DataFrame({'Usuário': [usuário.get()], 'senha': [senha.get()]})
    dados.to_csv('dados.csv', index=False)

botao_salvar = ctk.CTkButton(app, text="Salvar", width=50, command=botaos)
botao_salvar.place(x=5, y=145, anchor="sw")

app.mainloop()
