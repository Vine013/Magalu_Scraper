# Projeto de Automação de Extração de Dados - Magazine Luiza

Este projeto foi desenvolvido para automatizar a busca, extração e análise de produtos do site Magazine Luiza. Ele realiza uma pesquisa por notebooks, organiza os produtos conforme o número de avaliações, e gera um relatório em Excel que é enviado por e-mail automaticamente.

## Índice
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Execução](#instalação-e-execução)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Exemplo de Uso](#exemplo-de-uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

Este projeto utiliza o **Selenium WebDriver** para acessar o site da Magazine Luiza e realizar uma busca automatizada por notebooks. Em seguida, coleta os dados principais dos produtos encontrados, organiza-os em um relatório categorizado (produtos com mais e menos avaliações) e envia o relatório final por e-mail.

## Funcionalidades

1. **Abertura do site Magazine Luiza**: A automação tenta acessar o site até três vezes para garantir que ele seja carregado corretamente.
2. **Busca automatizada**: Realiza uma busca por "notebooks" e aguarda o carregamento dos produtos.
3. **Extração de dados**: Coleta nome, URL e número de avaliações dos notebooks listados.
4. **Análise de dados**: Filtra e categoriza produtos com base no número de avaliações, organizando em duas categorias: melhores (100+ avaliações) e piores (menos de 100 avaliações).
5. **Geração de relatório em Excel**: Cria um arquivo Excel com duas abas (Melhores e Piores), utilizando a biblioteca `pandas`.
6. **Envio de e-mail com relatório**: Envia o relatório em anexo para um destinatário configurado, utilizando o servidor SMTP do Gmail.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Selenium**: Automação de navegação e extração de dados.
- **Pandas**: Manipulação e geração de relatórios em Excel.
- **smtplib**: Envio de e-mail com o relatório anexado.

## Instalação e Execução

### Pré-requisitos

- Python 3.x
- Chrome WebDriver instalado e configurado no PATH do sistema.
- Conta de e-mail configurada para envio de relatórios via SMTP (recomendado Gmail com permissões adequadas para uso de SMTP).

---

## Autor

Desenvolvido por [Vinicius Santiago](https://www.linkedin.com/in/vinicius-santiago01/)

---

Se gostou deste projeto, não esqueça de dar uma ⭐️!

