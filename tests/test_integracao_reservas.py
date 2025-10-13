import pytest
from hotel.cliente import Cliente
from hotel.quarto import Quarto
from hotel.reserva import Reserva

# Teste 1: Cliente reserva um quarto disponível
def test_reserva_quarto_disponivel():
    cliente = Cliente("João", "joao@example.com")
    quarto = Quarto(101, "Luxo")
    reserva = Reserva(cliente, quarto, "2025-10-10", "2025-10-12")

    reserva.confirmar()  # Confirmando a reserva

    assert quarto.ocupado is True  # Verificando se o quarto está ocupado
    assert reserva.ativa is True  # Verificando se a reserva está ativa

# Teste 2: Cliente tenta reservar um quarto já ocupado
def test_reserva_quarto_ocupado():
    cliente1 = Cliente("João", "joao@example.com")
    cliente2 = Cliente("Maria", "maria@example.com")
    quarto = Quarto(101, "Luxo")
    
    reserva1 = Reserva(cliente1, quarto, "2025-10-10", "2025-10-12")
    reserva1.confirmar()  # Confirmando a primeira reserva
    
    reserva2 = Reserva(cliente2, quarto, "2025-10-12", "2025-10-14")
    
    with pytest.raises(Exception):  # Esperando uma exceção
        reserva2.confirmar()

# Teste 3: Cliente cancela a reserva
def test_cancelamento_reserva():
    cliente = Cliente("João", "joao@example.com")
    quarto = Quarto(101, "Luxo")
    reserva = Reserva(cliente, quarto, "2025-10-10", "2025-10-12")
    
    reserva.confirmar()  # Confirmando a reserva
    reserva.cancelar()  # Cancelando a reserva
    
    assert quarto.ocupado is False  # Verificando se o quarto está livre
    assert reserva.ativa is False  # Verificando se a reserva está inativa

# Teste 4: Cliente tenta reservar um quarto sobrepondo datas com outra reserva
def test_reserva_quarto_com_datas_sobrepostas():
    cliente1 = Cliente("João", "joao@example.com")
    cliente2 = Cliente("Maria", "maria@example.com")
    quarto = Quarto(101, "Luxo")
    
    reserva1 = Reserva(cliente1, quarto, "2025-10-10", "2025-10-12")
    reserva1.confirmar()  # Confirmando a primeira reserva
    
    reserva2 = Reserva(cliente2, quarto, "2025-10-11", "2025-10-13")
    
    with pytest.raises(Exception):  # Esperando uma exceção devido à sobreposição de datas
        reserva2.confirmar()

