# 1- DEFINIÇÃO DA CLASSE (A "fôrma" ou "molde")
class Aluno:
# 2- O MÉTODO CONSTRUTOR (INICIALIZAÇÃO DE OBJETOS)
    def __init__(self, nome_completo, matricula, curso_atual):
        # O self é uma referência para o próprio objeto que está sendo criado. Ele permite acessar os atributos e métodos da instância atual da classe.
        # 3- ATRIBUTOS (CARACTERÍSTICAS)
        self.nome_completo = nome_completo
        self.matricula = matricula
        self.curso_atual = curso_atual
        self.presencas = 0
    # 4- MÉTODOS (COMPORTAMENTOS)
    def registrar_presenca(self):
        self.presencas += 1
        print(f"Presença registrada para {self.nome_completo}. Total de presenças: {self.presencas}")

    def exibir_perfil(self):
            print("\n" + "="*30)
            print("DADOS DO ALUNO")
            print("="*30)
            print(f"Nome: {self.nome_completo}")
            print(f"Matrícula: {self.matricula}")
            print(f"Curso Atual: {self.curso_atual}")
            print(f"Total de Presenças: {self.presencas}")

if __name__ == "__main__":
    # 5- CRIAÇÃO DE OBJETOS/INSTÂNCIAS DA CLASSE
    aluno1 = Aluno("Juliana Ferreira", "EFG2026-02-01", "Análise e Desenvolvimento de Sistemas")
    aluno2 = Aluno("Lara Lorrany", "EFG2026-02-02", "Desenvolvimento Web e Mobile")

    # 6- USO DOS MÉTODOS
    print("Registrando presenças...")
    aluno1.registrar_presenca()
    aluno2.registrar_presenca()

    # 7- Exibindo os perfis dos alunos
    aluno1.exibir_perfil()
    aluno2.exibir_perfil()