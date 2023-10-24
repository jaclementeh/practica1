import pandas as pd
import logging


def transform_data(df1, df2, df3):

    # Se concatenan los tres dataframes de los tres archivos
    df_concat = pd.concat([df1, df2, df3])
    logging.debug(df_concat)

    # Se resetean los índices con el nuevo dataframe concatenado
    df_reset_index = df_concat.reset_index()
    print(df_reset_index)

    # Se elimina la fila cuyo artículo es Puros
    df_drop_line = df_reset_index.drop(index=0)
    print(df_drop_line)

    # Reducimos las columnas. Se quedan las columnas a trabajar y reseteamos el index
    df_transformed = df_drop_line[["line_number", "item_name", "quantity", "price"]]
    df_transformed = df_transformed.reset_index()
    print('Dataframe df_tranformed reducido con index ordenado: \n', df_transformed)

    # Añadimos columna precio total por cantidad y redondeamos a 2 decimales
    df_transformed['total_price_quantity'] = df_transformed.quantity * df_transformed.price
    df_transformed['total_price_quantity'] = df_transformed['total_price_quantity'].round(2)
    print('Dataframe df_tranformed: \n', df_transformed.to_string())

    return df_transformed







