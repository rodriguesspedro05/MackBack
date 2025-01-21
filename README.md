# **MackBank - Projeto de Algoritmos e Programação I (UPM)**


Segundo Projeto da matéria de Algoritmos e Programação I - Universidade Presbiteriana Mackenzie.

---

# Projeto Conta Corrente Bancária

## Descrição

Este projeto apresenta a implementação de um sistema de gerenciamento de conta corrente bancária, desenvolvido para consolidar habilidades de programação em Python. A solução busca replicar de forma simples, mas funcional, operações fundamentais de um banco real, como cadastro de clientes, transações financeiras, e consultas de informações. Com foco em validações robustas, segurança e experiência do usuário, o sistema permite interações fluídas por meio de um menu intuitivo. 
Além de reforçar conceitos como estruturas de decisão, repetição, funções e manipulação de listas, o projeto também prepara o desenvolvedor para lidar com problemas reais de lógica e organização de dados, tornando-se uma base sólida para desafios futuros na área.


## Funcionalidades Implementadas

1. **Cadastro da Conta**
   - Realiza o cadastro inicial da conta, incluindo:
     - Nome, telefone e email.
     - Saldo inicial e limite de crédito.
     - Criação de uma senha de 6 caracteres.
   - Validações realizadas:
     - Nome, telefone e email não podem estar em branco.
     - Saldo inicial deve ser maior ou igual a R$0.
     - Limite de crédito deve ser maior ou igual a R$0.
     - A senha deve ter exatamente 6 caracteres e ser confirmada corretamente.
   - Após o cadastro, o número da conta é associado pelo usuário.
   - Esta ação é executada uma única vez.

2. **Depósito**
   - Adiciona dinheiro na conta, atualizando o saldo e o histórico de operações.
   - Validações realizadas:
     - A conta deve estar cadastrada e desbloqueada.
     - O número da conta deve ser fornecido corretamente.
     - O valor do depósito deve ser maior que zero.

3. **Saque**
   - Retira dinheiro da conta mediante autenticação por senha.
   - Validações realizadas:
     - A conta deve estar cadastrada e desbloqueada.
     - O número da conta e a senha devem ser fornecidos corretamente.
     - O valor do saque deve ser maior que zero.
     - O saque é permitido se houver saldo suficiente ou limite de crédito disponível.
     - São permitidas até 3 tentativas de senha antes do bloqueio da conta.

4. **Consulta de Saldo**
   - Exibe o saldo da conta e o limite de crédito.
   - Validações realizadas:
     - A conta deve estar cadastrada e desbloqueada.
     - O número da conta e a senha devem ser fornecidos corretamente.

5. **Consulta de Extrato**
   - Mostra o histórico de operações e o saldo da conta.
   - Validações realizadas:
     - A conta deve estar cadastrada e desbloqueada.
     - O número da conta e a senha devem ser fornecidos corretamente.
   - Detalhes exibidos:
     - Tipo de operação (depósito ou saque) e valor.
     - Mensagem de alerta caso o saldo esteja negativo.

6. **Cancelamento de Conta**
   - Permite o cancelamento de uma conta cadastrada.
   - Validações realizadas:
     - A conta deve estar cadastrada e desbloqueada.
     - O número da conta e a senha devem ser fornecidos corretamente.
   - Ao cancelar:
     - Todos os dados da conta são apagados.
     - O saldo e o limite de crédito são zerados.

7. **Menu Interativo**
   - O programa apresenta um menu com opções para acessar as funcionalidades mencionadas.
   - A opção de finalizar encerra a execução do programa.

## Proposta

O objetivo principal deste projeto é criar uma simulação prática de um ambiente bancário, possibilitando que os usuários realizem operações comuns de forma eficiente e segura. Por meio de funcionalidades essenciais como depósitos, saques e consultas de saldo, o programa proporciona um entendimento detalhado sobre como implementar soluções dinâmicas e adaptáveis para necessidades do mundo real.  
Ao incorporar boas práticas de programação, como validações consistentes e estruturação modular, o projeto visa não apenas o desenvolvimento técnico, mas também a aplicação de conceitos fundamentais de lógica computacional, contribuindo para a formação de profissionais competentes e preparados para desafios na área de tecnologia.

## Desenvolvedor

Este programa foi desenvolvido por:
- **Pedro Henrique de Almeida Rodrigues**
