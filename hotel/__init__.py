"""
Pacote `hotel`.

Este arquivo expõe as classes centrais do pacote para permitir importações
como `from hotel import Cliente, Quarto, Reserva` nos testes e exemplos.

Corrige importações para os nomes de módulos presentes neste pacote.
"""

# Exportações públicas do pacote
from .reserva import Reserva
from .quarto import Quarto
from .cliente import Cliente
