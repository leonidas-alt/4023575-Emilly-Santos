from abc import ABC, abstractmethod

# -------------------------
# 1. Interfaces / Abstrações
# -------------------------

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, pedido):
        pass

# -------------------------
# 2. Implementações concretas
# -------------------------

class PagamentoCartaoCredito(Pagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")

class PagamentoBoleto(Pagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")

# Bônus: Pix
class PagamentoPix(Pagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} via Pix...")

class NotificacaoEmail(Notificacao):
    def enviar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")

# Bônus: SMS
class NotificacaoSMS(Notificacao):
    def enviar(self, pedido):
        print(f"Enviando SMS de confirmação para {pedido['cliente_email']}...")

# -------------------------
# 3. Processador de Pedidos
# -------------------------
class ProcessadorDePedidos:
    def __init__(self, pagamento: Pagamento, notificacao: Notificacao):
        # DIP: depende de abstrações, não de implementações concretas
        self.pagamento = pagamento
        self.notificacao = notificacao

    def processar(self, pedido):
        # SRP: Processador só coordena as etapas, não implementa cada lógica
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        
        # Pagamento
        self.pagamento.pagar(pedido)

        # Notificação
        self.notificacao.enviar(pedido)

        # Finalização
        pedido['status'] = 'concluido'
        print("Pedido concluído!")

# -------------------------
# 4. Como o cliente usaria
# -------------------------
if __name__ == "__main__":
    pedido1 = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    # Exemplo 1: Cartão + Email
    processador1 = ProcessadorDePedidos(PagamentoCartaoCredito(), NotificacaoEmail())
    processador1.processar(pedido1)

    print("-"*20)

    # Exemplo 2: Boleto + SMS
    pedido2 = pedido1.copy()
    pedido2['id'] = 456
    processador2 = ProcessadorDePedidos(PagamentoBoleto(), NotificacaoSMS())
    processador2.processar(pedido2)

    print("-"*20)

    # Exemplo 3: Pix + Email (Bônus)
    pedido3 = pedido1.copy()
    pedido3['id'] = 789
    processador3 = ProcessadorDePedidos(PagamentoPix(), NotificacaoEmail())
    processador3.processar(pedido3)
