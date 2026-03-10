"""
Limpeza e classificação de CPF/CNPJ com regex.

Remove qualquer caractere não numérico e classifica o documento
pelo tamanho resultante (11 dígitos = CPF, 14 dígitos = CNPJ).
"""
import pandas as pd


def limpar_documento(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """
    Adiciona `coluna_limpo` (somente dígitos) e `coluna_tipo` (CPF/CNPJ/INVALIDO).

    Exemplo:
        df = limpar_documento(df, 'documento')
    """
    limpo = df[coluna].astype(str).str.replace(r'\D', '', regex=True)
    df[f'{coluna}_limpo'] = limpo
    df[f'{coluna}_tipo'] = limpo.str.len().map({11: 'CPF', 14: 'CNPJ'}).fillna('INVALIDO')
    return df


if __name__ == "__main__":
    df = pd.DataFrame({"documento": ["123.456.789-00", "12.345.678/0001-90", "abc"]})
    print(limpar_documento(df, "documento"))
