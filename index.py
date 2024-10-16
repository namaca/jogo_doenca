import tkinter as tk
import random

# Listas de doenças e seus detalhes
doencas_bacteria = [
    ("Peste bubônica", "Vetor: Pulga de rato", "Medida profilática: Controle de roedores", "Vacina: Não", "Transmissão: Picada da pulga de rato infectada"),
    ("Febre maculosa", "Vetor: Carrapato", "Medida profilática: Evitar áreas infestadas por carrapatos", "Vacina: Não", "Transmissão: Picada de carrapato infectado"),
    ("Tuberculose", "Vetor: Não", "Medida profilática: Uso de máscara em locais com pessoas infectadas", "Vacina: Sim (BCG)", "Transmissão: Gotículas respiratórias, como tosse ou espirro"),
    ("Hanseníase", "Vetor: Não", "Medida profilática: Diagnóstico precoce e tratamento", "Vacina: Não", "Transmissão: Contato prolongado com pessoas infectadas"),
    ("Coqueluche", "Vetor: Não", "Medida profilática: Evitar contato com pessoas infectadas", "Vacina: Sim (DTP)", "Transmissão: Gotículas respiratórias, através da tosse"),
    ("Meningite", "Vetor: Não", "Medida profilática: Evitar aglomerações", "Vacina: Sim (para algumas formas)", "Transmissão: Gotículas respiratórias ou contato direto"),
    ("Sífilis", "Vetor: Não", "Medida profilática: Uso de preservativo", "Vacina: Não", "Transmissão: Contato sexual ou de mãe para filho"),
    ("Gonorreia", "Vetor: Não", "Medida profilática: Uso de preservativo", "Vacina: Não", "Transmissão: Contato sexual"),
    ("Cólera", "Vetor: Água e alimentos contaminados", "Medida profilática: Saneamento básico", "Vacina: Sim (oral)", "Transmissão: Ingestão de água ou alimentos contaminados"),
    ("Botulismo", "Vetor: Alimentos contaminados", "Medida profilática: Conservação adequada dos alimentos", "Vacina: Não", "Transmissão: Ingestão de toxinas em alimentos mal conservados"),
    ("Tétano", "Vetor: Não", "Medida profilática: Cuidados com ferimentos", "Vacina: Sim (DTP)", "Transmissão: Entrada de esporos pela pele ferida"),
    ("Leptospirose", "Vetor: Urina de animais infectados", "Medida profilática: Evitar contato com água contaminada", "Vacina: Não", "Transmissão: Contato com água ou solo contaminado com urina")
]

doencas_virus = [
    ("HPV", "Vetor: Não", "Medida profilática: Uso de preservativo", "Vacina: Sim", "Transmissão: Contato sexual"),
    ("AIDS", "Vetor: Não", "Medida profilática: Uso de preservativo", "Vacina: Não", "Transmissão: Contato com fluidos corporais"),
    ("Febre amarela", "Vetor: Mosquito", "Medida profilática: Evitar picadas de mosquito", "Vacina: Sim", "Transmissão: Picada de mosquito infectado"),
    ("Sarampo", "Vetor: Não", "Medida profilática: Evitar contato com pessoas infectadas", "Vacina: Sim (tríplice viral)", "Transmissão: Gotículas respiratórias, tosse ou espirro"),
    ("Rubéola", "Vetor: Não", "Medida profilática: Evitar contato com pessoas infectadas", "Vacina: Sim (tríplice viral)", "Transmissão: Gotículas respiratórias"),
    ("Gripe", "Vetor: Não", "Medida profilática: Higiene das mãos e evitar contato com pessoas infectadas", "Vacina: Sim", "Transmissão: Gotículas respiratórias"),
    ("Dengue", "Vetor: Mosquito Aedes aegypti", "Medida profilática: Controle do mosquito", "Vacina: Sim (parcial)", "Transmissão: Picada do mosquito Aedes aegypti"),
    ("Zika", "Vetor: Mosquito Aedes aegypti", "Medida profilática: Controle do mosquito", "Vacina: Não", "Transmissão: Picada do mosquito Aedes aegypti"),
    ("Chikungunya", "Vetor: Mosquito Aedes aegypti", "Medida profilática: Controle do mosquito", "Vacina: Não", "Transmissão: Picada do mosquito Aedes aegypti"),
    ("Hepatite A", "Vetor: Água e alimentos contaminados", "Medida profilática: Higiene e saneamento", "Vacina: Sim", "Transmissão: Ingestão de água ou alimentos contaminados"),
    ("Hepatite B", "Vetor: Não", "Medida profilática: Uso de preservativo e evitar compartilhamento de seringas", "Vacina: Sim", "Transmissão: Contato com sangue e fluidos corporais"),
    ("Hepatite C", "Vetor: Não", "Medida profilática: Uso de preservativo e evitar compartilhamento de seringas", "Vacina: Não", "Transmissão: Contato com sangue infectado"),
    ("Hepatite D", "Vetor: Não", "Medida profilática: Evitar contato com sangue contaminado", "Vacina: Não (mas pode ser prevenida com vacina da hepatite B)", "Transmissão: Contato com sangue contaminado"),
    ("Hepatite E", "Vetor: Água e alimentos contaminados", "Medida profilática: Higiene e saneamento", "Vacina: Não", "Transmissão: Ingestão de água ou alimentos contaminados")
]
# Unindo todas as doenças
todas_doencas = doencas_bacteria + doencas_virus

# Dicionário para verificar respostas corretas
respostas = {doenca[0]: 'bacteria' for doenca in doencas_bacteria}
respostas.update({doenca[0]: 'virus' for doenca in doencas_virus})

# Função para gerar o resumo de informações sobre a doença
def obter_resumo(doenca_nome):
    for doenca in todas_doencas:
        if doenca[0] == doenca_nome:
            return (f"{doenca[0]}\n\n"
                    f"* {doenca[1]}\n\n"
                    f"* {doenca[2]}\n\n"
                    f"* {doenca[3]}\n\n"
                    f"* {doenca[4]}")  # Adicionando a transmissão

class JogoVirusBacteria:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo Vírus ou Bactéria")
        self.root.configure(bg="#121212")  # Cor de fundo
        self.root.geometry("800x600")  # Tamanho da janela

        self.score = 0
        self.tentativas = 0
        self.doenca_atual = random.choice(todas_doencas)[0]

        # Criação de widgets
        self.label_doenca = tk.Label(
            root, 
            text=f"A doença '{self.doenca_atual}' é causada por:", 
            font=("Arial", 20, "bold"), 
            bg="#121212", 
            fg="white"
        )
        self.label_doenca.pack(pady=20)

        self.btn_virus = tk.Button(
            root, 
            text="Vírus", 
            font=("Arial", 16, "bold"), 
            bg="#007ACC", 
            fg="white", 
            width=12, 
            height=2, 
            borderwidth=0,
            relief="flat",
            activebackground="#005F99",
            command=lambda: self.verificar_resposta('virus')
        )
        self.btn_virus.pack(side=tk.LEFT, padx=20, pady=10)

        self.btn_bacteria = tk.Button(
            root, 
            text="Bactéria", 
            font=("Arial", 16, "bold"), 
            bg="#28A745", 
            fg="white", 
            width=12, 
            height=2, 
            borderwidth=0,
            relief="flat",
            activebackground="#218838",
            command=lambda: self.verificar_resposta('bacteria')
        )
        self.btn_bacteria.pack(side=tk.RIGHT, padx=20, pady=10)

        self.label_placar = tk.Label(
            root, 
            text="Placar: 0 acertos em 0 tentativas", 
            font=("Arial", 18), 
            bg="#121212", 
            fg="white"
        )
        self.label_placar.pack(pady=10)

        self.label_resultado = tk.Label(
            root, 
            text="", 
            font=("Arial", 18, "bold"), 
            bg="#121212", 
            fg="cyan"
        )
        self.label_resultado.pack(pady=10)

        self.label_resumo = tk.Label(
            root, 
            text="", 
            font=("Arial", 14), 
            bg="#121212", 
            fg="white", 
            justify=tk.LEFT,  # Alinha o texto à esquerda
            wraplength=350  # Limite de 200 pixels
        )
        self.label_resumo.pack(pady=10)

        self.btn_proximo = tk.Button(
            root, 
            text="Próximo", 
            font=("Arial", 16, "bold"),  
            fg="white", 
            command=self.proximo,
            borderwidth=0,
            bg="#007ACC",
            relief="flat",
            activebackground="#005F99"
        )
        self.btn_proximo.pack(pady=40)
        self.btn_proximo.pack_forget()  # Esconder inicialmente

        self.root.bind('<space>', lambda event: self.proximo())  # Vincular tecla espaço ao botão próximo

    def verificar_resposta(self, resposta_usuario):
        resposta_correta = respostas[self.doenca_atual]
        self.tentativas += 1

        # Desativar botões enquanto o resumo é exibido
        self.btn_virus.config(state=tk.DISABLED)
        self.btn_bacteria.config(state=tk.DISABLED)

        if resposta_usuario == resposta_correta:
            self.score += 1
            self.label_resultado.config(text="Correto!", fg="green")
        else:
            self.label_resultado.config(text="Incorreto!", fg="red")

        # Exibir resumo da doença
        resumo = obter_resumo(self.doenca_atual)
        self.label_resumo.config(text=resumo)

        # Atualiza placar
        self.label_placar.config(text=f"Placar: {self.score} acertos em {self.tentativas} tentativas")

        # Exibir botão "Próximo"
        self.btn_proximo.pack(pady=10)

    def proximo(self):
        # Resetar para a próxima doença
        self.doenca_atual = random.choice(todas_doencas)[0]
        self.label_doenca.config(text=f"A doença '{self.doenca_atual}' é causada por:")
        self.label_resultado.config(text="")
        self.label_resumo.config(text="")

        # Reabilitar botões
        self.btn_virus.config(state=tk.NORMAL)
        self.btn_bacteria.config(state=tk.NORMAL)
        self.btn_proximo.pack_forget()  # Esconder botão "Próximo"

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoVirusBacteria(root)
    root.mainloop()
