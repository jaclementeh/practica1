import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")

file_handler = logging.FileHandler('../outputfiles/analize_data.log', 'w', 'utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



def analize_data(df1, df2, df3):

    logger.debug('DataFrame 1 info \n {}'.format(df1.to_string()))
    logger.debug('DataFrame 2 info \n {}'.format(df2.to_string()))
    logger.debug('DataFrame 3 info \n {}'.format(df3.to_string()))

    logger.debug('Dataframe 1 shape (rows / columns) \n {}'.format(df1.shape))
    logger.debug('Dataframe 2 shape (rows / columns) \n {}'.format(df2.shape))
    logger.debug('Dataframe 3 shape (rows / columns) \n {}'.format(df3.shape))

    logger.debug('DataFrame describe: \n {}'.format(df1.describe()))
    logger.debug('DataFrame describe: \n {}'.format(df2.describe()))
    logger.debug('DataFrame describe: \n {}'.format(df3.describe()))








