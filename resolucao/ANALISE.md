
# Sistema de Processamento de Pedidos - Refatoração SOLID

## Descrição do Projeto
Este projeto é uma refatoração de um sistema de processamento de pedidos de e-commerce, aplicando os **princípios SOLID**.  

O código original tinha problemas de acoplamento e dificuldade de manutenção. A refatoração buscou:
- Separar responsabilidades (SRP)  
- Permitir extensão sem alterar código existente (OCP)  
- Garantir substituição segura das classes (LSP)  
- Criar interfaces bem definidas (ISP)  
- Fazer o processador depender de abstrações, não de implementações concretas (DIP)

## Estrutura do Projeto

resolucao/
├── sistema_refatorado.py # Código refatorado aplicando SOLID
└── ANALISE.md # Análise das violações do SOLID e refatoração

# Análise das Violações do SOLID

## 1. Single Responsibility Principle (SRP) violado
- A classe original **processava três coisas diferentes**: processava o pedido, realizava o pagamento e enviava notificação.
- Ela deveria ter **uma única responsabilidade**: coordenar o processo de pedido.
- **Solução:** separar as responsabilidades em **classes distintas** (Processador, Pagamento, Notificação).

---

## 2. Open/Closed Principle (OCP) violado
- Para adicionar um novo tipo de pagamento, seria necessário criar outro `elif` dentro da classe, **quebrando totalmente o princípio de OCP**.
- O OCP diz que o código deve estar **aberto para extensão, mas fechado para modificação**.
- **Solução:** criar abstrações (interfaces) para os tipos de pagamento, de forma que o processador **use apenas a interface**, sem alterar o código existente.

---

## 3. SRP + OCP + DIP violados
- Alterar o método de notificação para SMS ou WhatsApp **exigiria modificar o código do processador**, violando OCP e SRP.
- Além disso, o processador **depende de uma implementação concreta** (e-mail), violando o **Dependency Inversion Principle (DIP)**.
- **Solução:** criar uma interface de notificação (`Notificacao`) e implementar diferentes métodos concretos (Email, SMS, WhatsApp).

---

## 4. SRP + DIP violados
- A atualização do status do pedido poderia ser **responsabilidade do próprio objeto Pedido**, e não do processador.
- Atualmente, o processador faz algo que não é da sua competência direta, violando SRP e DIP.

---

## Conclusão
Após a refatoração:
- Cada classe tem **uma única responsabilidade** (SRP).
- É possível **adicionar novos métodos de pagamento ou notificação** sem alterar o código do processador (OCP).
- O processador **depende de abstrações** em vez de implementações concretas (DIP).
- Qualquer implementação de pagamento ou notificação pode **substituir outra** sem quebrar o código (LSP).
- Interfaces estão **bem segregadas**, evitando dependências desnecessárias (ISP).

Essa refatoração torna o sistema **flexível, escalável e fácil de manter**.

