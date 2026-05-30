# ==========================================
# MINI PROJETO - ANÁLISE EXPLORATÓRIA VAREJO
# ==========================================

import pandas as pd

# ==========================================
# 1. CARREGAMENTO DOS DADOS
# ==========================================

df = pd.read_csv("Base_Varejo.csv", sep=";", usecols=range(10))

print("=" * 50)
print("INFORMAÇÕES GERAIS DA BASE")
print("=" * 50)

print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de colunas:   {df.shape[1]}")

print("\nColunas disponíveis:")
for col in df.columns:
    print(f"  - {col}")

print("\nTipos de dados:")
print(df.dtypes)

# ==========================================
# 2. IDENTIFICAÇÃO DE PROBLEMAS
# ==========================================

print("\n" + "=" * 50)
print("IDENTIFICAÇÃO DE PROBLEMAS")
print("=" * 50)

print("\nValores nulos por coluna:")
print(df.isnull().sum())

print(f"\nRegistros duplicados: {df.duplicated().sum()}")

# Categorias inválidas (#N/D)
cat_invalidas = (df['PR_CAT'] == '#N/D').sum()
print(f"Categorias inválidas (#N/D): {cat_invalidas}")

# ==========================================
# 3. LIMPEZA DOS DADOS
# ==========================================

print("\n" + "=" * 50)
print("LIMPEZA DOS DADOS")
print("=" * 50)

linhas_antes = len(df)

# Remover duplicados
df = df.drop_duplicates()
print(f"Duplicados removidos: {linhas_antes - len(df)}")

# Substituir categorias inválidas
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'Sem Categoria')
print(f"Categorias '#N/D' substituídas por 'Sem Categoria'.")

# Converter DATA para datetime
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
datas_invalidas = df['DATA'].isnull().sum()
if datas_invalidas > 0:
    df = df.dropna(subset=['DATA'])
    print(f"Datas inválidas removidas: {datas_invalidas}")
else:
    print("Todas as datas convertidas com sucesso.")

print(f"\nRegistros após limpeza: {len(df)}")
print("Limpeza concluída.")

# ==========================================
# 4. ESTATÍSTICAS DESCRITIVAS - FILHOS
# ==========================================

print("\n" + "=" * 50)
print("ESTATÍSTICAS - NÚMERO DE FILHOS (CL_FHL)")
print("=" * 50)

print(f"Média:         {df['CL_FHL'].mean():.2f}")
print(f"Mediana:       {df['CL_FHL'].median():.1f}")
print(f"Desvio padrão: {df['CL_FHL'].std():.2f}")
print(f"Moda:          {df['CL_FHL'].mode()[0]}")
print(f"Máximo:        {df['CL_FHL'].max()}")
print(f"Mínimo:        {df['CL_FHL'].min()}")
print(f"Contagem:      {df['CL_FHL'].count()}")

print("\nDistribuição do número de filhos:")
print(df['CL_FHL'].value_counts().sort_index())

# ==========================================
# 5. AGRUPAMENTOS
# ==========================================

print("\n" + "=" * 50)
print("AGRUPAMENTOS")
print("=" * 50)

print("\nAGRUPAMENTO 1 - COMPRAS POR GÊNERO (CL_GENERO)")
genero_map = {'M': 'Masculino', 'F': 'Feminino'}
compras_genero = (
    df['CL_GENERO']
    .map(genero_map)
    .value_counts()
    .rename("Quantidade de Compras")
)
print(compras_genero)

print("\nAGRUPAMENTO 2 - COMPRAS POR CATEGORIA DE PRODUTO (PR_CAT)")
compras_cat = (
    df.groupby('PR_CAT')
    .size()
    .rename("Quantidade de Compras")
    .sort_values(ascending=False)
)
print(compras_cat)

print("\nAGRUPAMENTO 3 - COMPRAS POR SEGMENTO DO CLIENTE (CL_SEG)")
seg_map = {'A': 'Alto', 'B': 'Baixo', 'C': 'Médio'}
compras_seg = (
    df['CL_SEG']
    .map(seg_map)
    .value_counts()
    .rename("Quantidade de Compras")
)
print(compras_seg)

print("\nAGRUPAMENTO 4 - COMPRAS POR MÊS")
df['MES'] = df['DATA'].dt.to_period('M')
compras_mes = (
    df.groupby('MES')
    .size()
    .rename("Quantidade de Compras")
)
print(compras_mes)

# ==========================================
# 6. EXPORTAÇÃO
# ==========================================

print("\n" + "=" * 50)
print("EXPORTAÇÃO")
print("=" * 50)

df.to_csv("df_limpo.csv", index=False)
print("Arquivo df_limpo.csv gerado com sucesso.")

# ==========================================
# 7. CONCLUSÕES
# ==========================================

print("\n" + "=" * 50)
print("CONCLUSÕES")
print("=" * 50)

print(f"""
1. A base continha {linhas_antes:,} registros; após remoção de duplicados
   ficaram {len(df):,} registros únicos.
2. Foram identificadas e tratadas categorias inválidas ('#N/D').
3. A coluna DATA foi convertida para o formato datetime com sucesso.
4. O número médio de filhos dos clientes é {df['CL_FHL'].mean():.2f},
   com moda igual a {df['CL_FHL'].mode()[0]} (maioria sem filhos).
5. O gênero feminino representa a maior fatia de compras.
6. A categoria mais comprada é ALIMENTOS, seguida de HIGIENE e LIMPEZA.
7. O segmento B (Baixo) concentra o maior volume de transações.
8. A base está limpa e pronta para dashboards e análises futuras.
""")