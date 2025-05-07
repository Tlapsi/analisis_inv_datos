import pandas as pd

def clean ():

    df=pd.read_csv('productos_raw.csv')
    #print(df.head())
    df=df.loc[:,['Nombre', 'Precio', 'Stock']]
    df=df.dropna(subset=['Nombre', 'Precio','Stock'])
    df=df.reset_index(drop=True)

    return df
def add_columns (df_clean):

    #print(df)
    df_clean["Precio_IVA"] = df_clean['Precio'] * 1.16
    df_clean["Disponibilidad"] = df_clean["Stock"].apply(lambda x: "Sí" if x > 0 else "No")
    df_add_columns = df_clean

    return df_add_columns

def filters (df_add_columns):

    filtro=df_add_columns[(df_add_columns["Stock"] > 0) & (df_add_columns["Precio"] > 15000)]
    filtro.to_csv('productos_filtrados.csv', index=False, encoding="utf-8-sig")
    print("csv productos_filtrados creado exitosamente")

def group (df_add_columns):
    resumen = df_add_columns.groupby("Nombre").agg({
        "Precio": "mean",
        "Stock": "sum",
        "Precio_IVA": "max"
    })
    #print(resumen)
    resumen.to_csv('resumen_productos.csv',  encoding="utf-8-sig")
    print("csv resumen_productos creado exitosamente")

def main ():
    df_clean = clean()
    df_add_columns = add_columns(df_clean)
    filters(df_add_columns)
    group(df_add_columns)

if __name__ == '__main__':
    main()