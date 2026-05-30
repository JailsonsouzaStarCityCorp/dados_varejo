# Mini Projeto — Análise Exploratória de Dados no Varejo

## Objetivo

Realizar uma Análise Exploratória de Dados (AED) utilizando Python e Pandas sobre uma base real de transações de varejo, identificando problemas de qualidade, realizando tratamentos e gerando insights de negócio.

---

## Tecnologias

- Python 3
- Pandas
- VS Code

---

## Estrutura do Projeto

```
Miniprojeto_Varejo/
│
├── Base_Varejo.csv          ← base de dados original (não incluída no repositório)
├── miniprojeto_varejo.py    ← script principal de análise
├── df_limpo.csv             ← base limpa gerada pelo script
└── README.md                ← este arquivo
```

---

## Dicionário de Dados

| Coluna     | Descrição                                      |
|------------|------------------------------------------------|
| DATA       | Data da transação (dd/mm/aaaa)                 |
| CO_ID      | Código da loja                                 |
| CL_ID      | Código do cliente                              |
| CL_GENERO  | Gênero do cliente (M / F)                      |
| CL_EC      | Estado civil (1=Solteiro, 2=Casado, ...)       |
| CL_FHL     | Número de filhos do cliente                    |
| CL_SEG     | Segmento do cliente (A=Alto, B=Baixo, C=Médio) |
| PR_ID      | Código do produto                              |
| PR_CAT     | Categoria do produto                           |
| PR_NOME    | Nome do produto                                |

---

## Como Executar

1. Coloque o arquivo `Base_Varejo.csv` na mesma pasta do script.
2. Instale as dependências (caso necessário):

```bash
pip install pandas
```

3. Execute o script:

```bash
python miniprojeto_varejo.py
```

4. O arquivo `df_limpo.csv` será gerado automaticamente na mesma pasta.

---

## Etapas do Script

### 1. Carregamento
Leitura da base com separador `;`, selecionando apenas as 10 colunas relevantes (ignorando colunas vazias).

### 2. Identificação de Problemas
- Verificação de valores nulos
- Contagem de registros duplicados
- Identificação de categorias inválidas (`#N/D`)

### 3. Limpeza
- Remoção de duplicados (~96 mil registros)
- Substituição de `#N/D` por `Sem Categoria`
- Conversão da coluna `DATA` para formato datetime

### 4. Estatísticas Descritivas
Análise da coluna `CL_FHL` (número de filhos): média, mediana, moda, desvio padrão, mínimo e máximo.

### 5. Agrupamentos
- Compras por gênero
- Compras por categoria de produto
- Compras por segmento do cliente
- Compras por mês

### 6. Exportação
Geração do arquivo `df_limpo.csv` com a base tratada.

---

## Reflexão sobre ETL e Qualidade dos Dados

O processo ETL (Extract, Transform, Load) é fundamental para garantir que os dados utilizados em análises sejam confiáveis. Neste projeto, a etapa de transformação tratou registros duplicados (quase 12% da base original), categorias inválidas e formatação de datas. Essas ações reduzem erros em análises e dashboards e aumentam a confiança nas conclusões.

---

## Principais Insights

- A base original continha **830.000 registros**; após limpeza ficaram cerca de **733.000**.
- O gênero **Feminino** representa a maior parte das compras.
- A categoria mais consumida é **ALIMENTOS**, seguida de **HIGIENE** e **LIMPEZA**.
- O segmento **B (Baixo)** concentra o maior volume de transações (~72%).
- A maioria dos clientes **não tem filhos** (moda = 0, média ≈ 1,1).
- A base limpa está pronta para análises futuras e dashboards.
