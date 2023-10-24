import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")

file_handler = logging.FileHandler('../outputfiles/metrics.log', 'w', 'utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def metrics(transformed_data):


    mean_price_quantity = round((transformed_data['total_price_quantity'].mean()), 2)
    logger.debug('Mostramos precio medio por litro: \n {}'.format(mean_price_quantity))

    mean_price_by_item_name = round(transformed_data.groupby(['item_name'], as_index=False)['total_price_quantity'].mean().
                                    rename(columns={'item_name':'Producto','total_price_quantity' : 'Mean_price_quantity'})
                                    ,2)
    logger.debug('Mostramos precio medio por litro agrupado por tipo de carburante: \n {}'.format(mean_price_by_item_name))







