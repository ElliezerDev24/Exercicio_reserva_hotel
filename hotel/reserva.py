"""
Módulo reserva

Define a classe Reserva, que representa uma reserva entre um Cliente e
um Quarto para um intervalo de datas. Este módulo contém comentários
detalhados sobre cada passo da lógica de confirmação e cancelamento.
"""


class Reserva:
    """Representa uma reserva de quarto feita por um cliente.

    Atributos principais:
    - cliente: instância de Cliente que fez a reserva
    - quarto: instância de Quarto a ser ocupada
    - data_inicio: início da reserva (tipo livre — string/datetime)
    - data_fim: fim da reserva (tipo livre — string/datetime)
    - ativa: boolean que indica se a reserva está ativa/confirmada

    Nota: neste exercício não há validação de sobreposição de datas;
    isso é um aprimoramento opcional sugerido no enunciado.
    """

    def __init__(self, cliente, quarto, data_inicio, data_fim):
        """Inicializa a reserva com cliente, quarto e intervalo de datas.

        Parâmetros:
        - cliente: objeto Cliente
        - quarto: objeto Quarto
        - data_inicio: início da reserva (pode ser string ou datetime)
        - data_fim: fim da reserva (pode ser string ou datetime)
        """
        self.cliente = cliente
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim

        # Flag que indica se a reserva está confirmada / ativa
        self.ativa = False

    def confirmar(self):
        """Confirma a reserva.

        Fluxo esperado:
        1. Verificar se o quarto já está ocupado. Se estiver, lançar uma
           exceção para impedir reserva duplicada.
        2. Marcar a reserva como ativa (self.ativa = True).
        3. Marcar o quarto como ocupado chamando `quarto.ocupar()`.
        4. (Bom lugar para vincular a reserva ao cliente: cliente.adicionar_reserva(self))

        Observações:
        - A checagem de `quarto.ocupado` é simples e suficiente para o
          escopo didático. Implementações mais avançadas devem checar
          intervalos de data para detectar sobreposição.
        - A função lança `Exception` com mensagem clara em caso de conflito.
        """
        # Se o quarto já estiver marcado como ocupado, impedimos a confirmação
        if self.quarto.ocupado:
            raise Exception("Quarto já ocupado.")

        # Marca reserva como ativa e atualiza estado do quarto
        self.ativa = True
        self.quarto.ocupar()

        # Vincula a reserva ao cliente para rastreio (opcional, mas útil)
        try:
            # Se o cliente tiver o método adicionar_reserva, use-o.
            self.cliente.adicionar_reserva(self)
        except Exception:
            # Se ocorrer algum erro ao adicionar, não interromper a confirmação
            # mas registrar/propagar conforme política do projeto. Aqui deixamos
            # silencioso por simplicidade.
            pass

    def cancelar(self):
        """Cancela a reserva.

        Fluxo esperado:
        - Marca `ativa` como False.
        - Chama `quarto.liberar()` para tornar o quarto disponível.

        Observação: não removemos a reserva da lista do cliente; se quiser
        que seja removida, implementar lógica adicional em Cliente.
        """
        self.ativa = False
        self.quarto.liberar()
