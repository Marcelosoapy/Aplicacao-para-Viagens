import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


# criacao da janela

janela = tk.Tk()
janela.title("Meu organizador de Tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

frame_em_edicao = None

# funcao de adicionar tarefa
def adicionar_tarefa():
    global frame_em_edicao # global pra que seja alterado quando for preciso

    tarefa = entrada_tarefa.get().strip() # get para pegar o valor dentro ao campo
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None: # se frame_em_edicao for nao, atualize a tarefa 
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:   # senao adicione a tarefa e a delete
            adicionar_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)

    else:   # senao apresenta mensagem de erro
        messagebox.showwarning("Entrada Invalida","Por favor, Insira uma tarefa")

# adicionando as definicoes da variavel adicionar_item_tarefa

def adicionar_item_tarefa(entrada):
    frame_tarefa = tk.Frame(canvas_interior, bg="white, bd=1, relief=tk.SOLID")

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Garamond", 16),bg="white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg="white", relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5) 

    botao_deletar = tk.Button(frame_tarefa, image=icon_deletar, command=lambda f=frame_tarefa: deletar_tarefa(f), bg="white", relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)

    



    icon_editar = PhotoImage(file="editar.png".subsample(3, 3))
    icon_deletar = PhotoImage(file="lixeira.png".subsample(3, 3))


# fonte para a escrita na front-page com tamanho e destaque
font_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(janela, text="Meu Roteiro Diário", font=font_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20) # bg = background

# frame para customizacao 
frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(pady=10)


# entrada para caixa
entrada_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

# button de entrada
botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)
adicionar_tarefa = tk.Button(frame_em_edicao)

# criar um frame para a lista de tarefas com sistema de rolagem
frame_listar_tarefas = tk.Frame(janela, bg="white")
frame_listar_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_listar_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_listar_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# configurando canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))



janela.mainloop()