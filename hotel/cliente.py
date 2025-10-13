"""
Módulo cliente

Contém a classe Cliente, que representa um cliente do hotel e
mantém as reservas associadas a esse cliente.
"""
class Cliente:
        """Representa um cliente com suas reservas.

        Atributos:
        - nome (str): nome completo do cliente
        - email (str): email de contato do cliente
        - reservas (list): lista em memória de objetos Reserva vinculados
        """

        def __init__(self, nome, email):
                """Inicializa o cliente com nome e email e cria a lista de reservas.

                Parâmetros:
                - nome (str): nome do cliente
                - email (str): email do cliente
                """
                # Dados básicos de identificação do cliente
                self.nome = nome
                self.email = email

                # Lista que armazenará objetos Reserva associados a este cliente.
                # armazenada como array em formato de lista.
                self.reservas = []

        def adicionar_reserva(self, reserva):
                """Adiciona uma reserva à lista `reservas` do cliente.

                Este método não realiza validações complexas — assume-se que a
                reserva passada já foi validada/confirmada pela lógica de Reserva.
                Apenas vincula a reserva ao cliente para consulta posterior.

                Parâmetros:
                - reserva: instância de `Reserva` a ser vinculada
                """
                # Uso do append preserva a referência ao objeto Reserva.
                self.reservas.append(reserva)

        

