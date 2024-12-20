# Projeto de Amortização pelo Sistema SAC (Flask)

Este é um projeto Flask que calcula a amortização de um financiamento utilizando o sistema SAC (Sistema de Amortização Constante). O projeto foi criado para facilitar o entendimento de como funciona o cálculo das parcelas e juros em um financiamento. O app permite que o usuário insira o saldo devedor, o número de meses e a taxa de juros, e exibe os cálculos do valor das prestações, amortização e juros totais.

O projeto foi desenvolvido para um trabalho escolar e está disponível na plataforma Vercel para acesso remoto.

## Funcionalidades

- Cálculo da amortização constante (SAC) para um financiamento.
- Exibição das parcelas mensais, total de juros pagos e o valor total do montante.
- Interface simples e amigável para facilitar o entendimento do sistema SAC.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **HTML/CSS**: Para estruturação e estilização da página.
- **Python**: Linguagem de programação usada no backend para os cálculos de amortização e juros.

## Como Rodar o Projeto Localmente

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/SEU_USUARIO/PROJETO_SAC.git
```

### 2. Criar um Ambiente Virtual

Se você não tiver um ambiente virtual configurado, crie um com o seguinte comando:

```bash
python3 -m venv venv
```

### 3. Ativar o Ambiente Virtual

- **No Windows:**

```bash
venv\Scripts\activate
```

- **No Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Instalar as Dependências

Instale as dependências do projeto com o seguinte comando:

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não estiver presente, você pode instalar o Flask manualmente com:

```bash
pip install Flask
```

### 5. Rodar o Servidor Flask

Após a instalação das dependências, execute o seguinte comando para rodar o servidor Flask:

```bash
python app.py
```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

### 6. Acessar o Projeto

Abra o navegador e acesse `http://127.0.0.1:5000/` para interagir com o aplicativo.

## Como Usar o Projeto

1. Ao abrir a aplicação, você verá um formulário para inserir os seguintes dados:
   - **Saldo Devedor**: O valor total da dívida.
   - **Número de Meses**: O número de meses para o financiamento.
   - **Taxa de Juros**: A taxa de juros anual aplicada.

2. Preencha os campos e clique no botão para calcular.

3. O sistema irá exibir:
   - O valor da amortização mensal constante.
   - O total de juros pagos ao longo do financiamento.
   - O valor total das prestações.
   - O montante total a ser pago.

## Deploy na Vercel

O projeto foi deployado na plataforma Vercel, e você pode acessá-lo online no seguinte link:

[**Link para o Deploy**](https://seu-usuario.vercel.app)

## Estrutura do Projeto

```
projeto-sac/
│
├── app.py              # Arquivo principal do Flask.
├── requirements.txt    # Arquivo com as dependências do projeto.
├── templates/
│   └── amortizacao.html  # Template HTML para exibição da interface.
├── static/
│   └── css/
│       └── style.css   # Arquivo CSS para estilização da página.
└── venv/               # Ambiente virtual (pode ser ignorado no repositório).
```

## Contribuições

Se você deseja contribuir para este projeto, fique à vontade para criar um **fork**, fazer suas alterações e enviar um **pull request**.

## Licença

Este projeto é de código aberto e pode ser utilizado e modificado de acordo com os termos da licença [MIT](LICENSE).
