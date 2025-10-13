#  Atividade Prática: Testes de Integração com Pytest — Sistema de Reservas de Hotel

##  Objetivo
Desenvolver um sistema simples de **reservas de hotel** com três módulos principais:
- `Cliente`
- `Quarto`
- `Reserva`

E criar **testes de integração** com **Pytest** para verificar o funcionamento conjunto entre esses módulos.

---

##  Contexto
Você trabalha como QA em uma empresa que desenvolve sistemas para hotéis e pousadas.  
Seu objetivo é validar o comportamento de um sistema de reservas, garantindo que:
1. Os clientes consigam reservar quartos disponíveis.  
2. Não ocorram reservas duplicadas no mesmo período.  
3. O cancelamento de reservas libere o quarto corretamente.

---

##  Estrutura sugerida do projeto

```
hotel/
│
├── hotel/
│   ├── __init__.py
│   ├── cliente.py
│   ├── quarto.py
│   ├── reserva.py
│
└── tests/
    ├── __init__.py
    ├── test_integracao_reservas.py
```

---

##  Requisitos do sistema

### Módulo `cliente.py`
- Classe `Cliente` com atributos:
  - `nome`
  - `email`
  - `reservas` (lista de reservas feitas)
- Método `adicionar_reserva(reserva)` para vincular reservas ao cliente.

### Módulo `quarto.py`
- Classe `Quarto` com atributos:
  - `numero`
  - `tipo` (ex: "Standard", "Luxo")
  - `ocupado` (booleano)
- Métodos:
  - `ocupar()` → marca o quarto como ocupado.  
  - `liberar()` → marca o quarto como livre.

### Módulo `reserva.py`
- Classe `Reserva` com atributos:
  - `cliente`
  - `quarto`
  - `data_inicio`
  - `data_fim`
  - `ativa` (booleano)
- Métodos:
  - `confirmar()` → ativa a reserva e ocupa o quarto.  
  - `cancelar()` → desativa a reserva e libera o quarto.

---

##  Testes de Integração (arquivo `test_integracao_reservas.py`)

Crie pelo menos **2 testes de integração**, como por exemplo:

- ✅ **Teste 1:** Cliente reserva um quarto disponível.  
  Verifique se o quarto passa para `ocupado=True` e a reserva é marcada como `ativa=True`.

- ✅ **Teste 2:** Cliente tenta reservar um quarto já ocupado.  
  Verifique se o sistema impede a operação (por exceção ou mensagem).

- ✅ **Teste 3 (opcional):** Cliente cancela a reserva.  
  Verifique se o quarto volta para `ocupado=False` e a reserva para `ativa=False`.

---

##  Instruções

### 1. Criar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 2. Instalar o Pytest
```bash
pip install pytest
```

### 3. Executar os testes
```bash
pytest -v
```

---

##  Dicas
- Utilize exceções (`raise Exception("Mensagem")`) para tratar erros de reserva.  
- Simule conflitos de datas ou ocupação com variáveis booleanas.  
- Garanta que as classes se comuniquem corretamente.

---

##  Entrega
- Enviar um arquivo `.zip` com o projeto completo (`hotel/` e `tests/`).  
- Certifique-se de que todos os testes passam com `pytest`.  
- Inclua comentários explicando cada parte do código.

---

**Desafio bônus :**  
Adicione um recurso de **verificação de disponibilidade por data** no quarto e teste se o sistema bloqueia reservas sobrepostas corretamente.
