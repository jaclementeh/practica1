
def metrics(transformed_data):


    mean_price_quantity = round((transformed_data['total_price_quantity'].mean()), 2)
    print('Mostramos precio medio por litro: \n', mean_price_quantity)

    mean_price_by_item_name = round(transformed_data.groupby(['item_name'], as_index=False)['total_price_quantity'].mean().
                                    rename(columns={'item_name':'Producto','total_price_quantity' : 'Mean_price_quantity'})
                                    ,2)
    print('Mostramos precio medio por litro agrupado por tipo de carburante: \n', mean_price_by_item_name)







