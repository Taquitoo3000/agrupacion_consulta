import pandas as pd

def concatenar_valores_unicos(series):
    "Concatena valores únicos no nulos"
    valores_unicos = series.dropna().unique()
    if len(valores_unicos) == 0:
        return None
    elif len(valores_unicos) == 1:
        return str(valores_unicos[0])
    else:
        return ', '.join(map(str, valores_unicos))
    
def concatenar_valores(series):
    "Concatena valores no nulos"
    valores = series.dropna()
    if len(valores) == 0:
        return None
    elif len(valores) == 1:
        return str(valores.iloc[0])
    else:
        return ', '.join(map(str, valores))

df = pd.read_excel('quejas.xlsx')

df_agrupado = df.groupby('Expediente').agg({
    'FechaInicio': 'first',
    'Nombre': concatenar_valores_unicos,
    'Quejoso/Agraviado': concatenar_valores_unicos,
    'Sexo': concatenar_valores_unicos,
    'EdadNumero': concatenar_valores_unicos,
    'Dependencia': 'first',
    'Autoridad': concatenar_valores_unicos,
    'LugarProcedencia': concatenar_valores_unicos,
    'Motivo': concatenar_valores_unicos,
    'Conclusión': 'first',
    'F_Conclusion': 'first'
}).reset_index()

print(f"Expedientes únicos procesados: {len(df_agrupado)}")

df_agrupado.to_excel('quejas_consolidadas.xlsx', index=False)