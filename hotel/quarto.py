"""
Módulo quarto

Define a classe Quarto, que modela um quarto de hotel com um número,
um tipo (por exemplo 'Standard' ou 'Luxo') e um flag booleano `ocupado`
indicando se o quarto está ocupado.
"""


class Quarto:
    """Representa um quarto de hotel simples.

    Atributos:
    - numero: identificador/numérico do quarto
    - tipo: string descritiva do tipo do quarto
    - ocupado: boolean que indica se o quarto está ocupado

    Métodos:
    - ocupar(): marca o quarto como ocupado
    - liberar(): marca o quarto como livre
    """

    def __init__(self, numero, tipo):
        """Inicializa um quarto com número e tipo.

        Parâmetros:
        - numero: identificador do quarto (int ou str)
        - tipo: descrição do tipo do quarto (str)
        """
        self.numero = numero
        self.tipo = tipo

        # Inicialmente o quarto está livre
        self.ocupado = False

    def ocupar(self):
        """Marca o quarto como ocupado.

        Design choice: não lançamos exceção se `ocupar` for chamado
        quando `ocupado` já é True — a verificação de conflito é feita
        normalmente pela classe Reserva antes de chamar este método.
        """
        self.ocupado = True

    def liberar(self):
        """Marca o quarto como livre (ocupado = False).

        Usado tipicamente por `Reserva.cancelar()` para liberar o quarto.
        """
        self.ocupado = False
