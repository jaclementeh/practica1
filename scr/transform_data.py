import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")

file_handler = logging.FileHandler('../outputfiles/formated_data.log', 'w', 'utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



def transform_data(df1, df2, df3):

    # Se concatenan los tres dataframes de los tres archivos
    df_concat = pd.concat([df1, df2, df3])
    logger.debug('Dataframes concatenated: \n {}'.format(df_concat))

    # Se resetean los índices con el nuevo dataframe concatenado
    df_reset_index = df_concat.reset_index()
    # Se elimina la fila cuyo artículo es Puros
    df_drop_line = df_reset_index.drop(index=0)
    # Reducimos las columnas. Se quedan las columnas a trabajar y reseteamos el index
    df_transformed = df_drop_line[["line_number", "item_name", "quantity", "price"]]
    df_transformed = df_transformed.reset_index()
    logger.debug('Dataframe transformed: \n {}'.format(df_transformed))

    # Añadimos columna precio total por cantidad y redondeamos a 2 decimales
    df_transformed['total_price_quantity'] = df_transformed.quantity * df_transformed.price
    df_transformed['total_price_quantity'] = df_transformed['total_price_quantity'].round(2)
    logger.debug('Final Dataframe df_tranformed: \n {}'.format(df_transformed.to_string()))

    return df_transformed







