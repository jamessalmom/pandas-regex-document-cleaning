# Limpeza de CPF/CNPJ

Método pandas + regex para remover caracteres não numéricos de CPF/CNPJ
e classificar o tipo de documento pelo tamanho resultante.

## Uso
```python
import pandas as pd
from limpar_documento import limpar_documento

df = pd.DataFrame({"documento": ["123.456.789-00", "12.345.678/0001-90"]})
df = limpar_documento(df, "documento")
```
