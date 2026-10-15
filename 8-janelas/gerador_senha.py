# Importando a biblioteca e nomeando de tk
import tkinter as tk
import random
import string

ALTURA = "450"
LARGURA = "400"

#===================================
#7. FUNÇÕES DO SISTEMA (A Lógica)
#===================================

def gerar_senha():
    try:
        tamanho = int(entry_tamanho_senha.get())
        # Verificando se a quantidade de caracteres definida é maior do que 4
        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: Mínimo de 4 caracteres!",
                fg="#ff5555"
            )
            return

        caracteres = ""
        if var_maiusculo.get():
            caracteres += string.ascii_uppercase
        if var_minusculo.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
           caracteres += string.digits
        if var_simbolos.get():
          caracteres += string.punctuation

          if not caracteres:
              lbl_resultado.config(
                  text="Erro: Selecione ao menos uma opção",
                  fg="#ff5555"
              )
              return
          
        senha = "".join(random.choice(caracteres) for i in range(tamanho))

        lbl_resultado.config(
            text= f"Senha: {senha}",
            fg="#50fa7b"
        )
        
    except ValueError:
        lbl_resultado.config(
            text="Erro: Digite um número válido!",
            fg="#ff5555"
            )

def copiar_senha():
    texto_resultado = lbl_resultado.cget("text")

    if "Senha: " in texto_resultado:
        senha_pura = texto_resultado.replace("Senha: ","")

        janela.clipboard_clear()
        janela.clipboard_append(senha_pura)
    else:
        lbl_status_copia.config(
            text = "Gere uma senha primeiro!",
            fg = "#ff5555"
        )


#===================================
#1. Configuração da janela principal
#===================================
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#171733")

#2.Título principal do aplicativo
titulo = tk.Label(
    text="Gerador de Senhas",
    font=("Ravie Regular",16,"bold"),
    bg="#171733",
    fg="#1b8e77"
)
titulo.pack(pady=20)

#3. Label Tamanho Senha
lbl_tamanho_senha = tk.Label(
    text="Tamanho da Senha",
    font=("Terminal",11),
    bg="#171733",
    fg="#ffffff"
)
lbl_tamanho_senha.pack(pady=12)

#4. Entrada do tamanho da senha
entry_tamanho_senha = tk.Entry(
    janela,
    font=("Arial",12),
    width=10,
    justify="center"
)
entry_tamanho_senha.pack(pady=5)

var_maiusculo = tk.BooleanVar(value=True)
var_minusculo = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=False)
var_simbolos = tk.BooleanVar(value=False)

#5.2 Criando a caixinha de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text="Maiúscula (A-Z)",
    variable=var_maiusculo,
    bg="#171733",
    fg="#ffffff",
    selectcolor="#171733",
    activebackground="#171733",
    activeforeground="#ffffff"
)
chk_maiuscula.pack(anchor="w", padx=60,pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text="Minúscula (a-z)",
    variable=var_minusculo,
    bg="#171733",
    fg="#ffffff",
    selectcolor="#171733",
    activebackground="#171733",
    activeforeground="#ffffff"
)
chk_minuscula.pack(anchor="w", padx=60,pady=2)

chk_numero = tk.Checkbutton(
    janela,
    text="Números (0-9)",
    variable=var_numeros,
    bg="#171733",
    fg="#ffffff",
    selectcolor="#171733",
    activebackground="#171733",
    activeforeground="#ffffff"
)
chk_numero.pack(anchor="w", padx=60,pady=2)

chk_simbolo = tk.Checkbutton(
    janela,
    text="Caracteres Especiais (*#@?!)",
    variable=var_simbolos,
    bg="#171733",
    fg="#ffffff",
    selectcolor="#171733",
    activebackground="#171733",
    activeforeground="#ffffff"
)
chk_simbolo.pack(anchor="w", padx=60,pady=2)

#6. Criar botão gerador de senha
btn_gerar = tk.Button(
    janela,
    text="Gerar senha Segura",
    command=gerar_senha,
    bg="#1b8e77",
    fg="#171733",
    padx=10,
    pady=5
)
btn_gerar.pack(pady=15)

# Label que apresenta o resultado no programa
lbl_resultado = tk.Label(
    janela,
    text="A senha aparecerá aqui",
    font=("Terminal",11,"bold"),
    bg="#171733",
    fg="#f8f8f2" 
)
lbl_resultado.pack(pady=5)

btn_copiar = tk.Button(
    janela,
    text="Copiar",
    command=copiar_senha,
    font=("terminal",10,"bold"),
    bg="#525257",
    fg="#bceff4",
    padx=10,
    pady=3
)
btn_copiar.pack(pady=5)

lbl_status_copia = tk.Label(
    janela,
    text="",
    font=("Arial",9),
    bg="#171733",
    fg="#50fa7b"
)
lbl_status_copia.pack(pady=2)

janela.mainloop()