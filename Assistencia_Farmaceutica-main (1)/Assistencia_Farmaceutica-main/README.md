# Assistencia_Farmaceutica

## Componentes
- Alan César Rebouças de Araújo Carvalho
- Carlos Silvano de Oliveira Junior
- Erick Henrique da Silva Paz
- Félix Luiz Garção Filho
- Hanna Vitória de Oliveira Silva
- Mateus Santana Uchoa de Melo
- Matheus Silva Mendes
- Pedro Henrique da Silva Paixão
  
## Descrição
  Este projeto foi desenvolvido por alunos de Ciências e Tecnologia (C&T) e Engenharia de Computação na UFRN para a disciplina de ECT3517 - CIÊNCIAS E TECNOLOGIAS APLICADAS 3.
  
  O projeto tem como objetivo o desenvolvimento de um sistema web para otimizar a gestão e o acompanhamento dos clientes, no que concerne à atenção farmacêutica, com um foco maior a idosos e pessoas com doenças crônicas que necessitam tomar remédios regularmente e eventualmente de um atendimento com o farmacêutico, seja para verificar a aceitação do tratamento ou monitorar parâmetros clínicos, entre outras coisas.
  
  O sistema permitirá o cadastro das informações dos clientes, incluindo histórico clínico, dando ao farmacêutico a permissão de alterar informações para melhor uso. Também será possível atrelar ao cliente um tratamento devido, como a quantidade de doses de um medicamento específico, doses, frequência, etc. O sistema também deverá notificar ao farmacêutico quando um medicamento de qualquer cliente estiver acabando, vencendo, ou em falta no próprio estoque, então, haverá a ferramenta de entrar em contato com o paciente, por meio do whatsapp. O farmacêutico também terá a possibilidade de gerar relatórios e estatísticas a respeito dos tratamentos. O software também será capaz de cadastrar receitas médicas em seu sistema, e poderá também agendar atendimentos farmacêuticos online.

## Como clonar ou baixar

Você pode obter este repositório de três formas:

### Clonar via HTTPS
```bash
git clone https://github.com/Alan-CRA/Assistencia_Farmaceutica.git
```

### Clonar via SSH
```bash
git clone git@github.com:Alan-CRA/Assistencia_Farmaceutica.git
```

### Baixar como ZIP
1. Acesse a página do repositório no GitHub:
   https://github.com/Alan-CRA/Assistencia_Farmaceutica
2. Clique no botão **Code** (verde).
3. Selecione **Download ZIP**.
4. Extraia o arquivo ZIP para o local desejado em seu computador.

## Rodando localmente
Abra o terminal de comando na pasta que você clonou o repositório e execute os comandos
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows

pip install flask

python main.py
# http://127.0.0.1:8080
```
