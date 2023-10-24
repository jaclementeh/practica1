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

    logger.debug('Dataframe 1 rows {}'.format(df1.shape[0]))
    logger.debug('Dataframe 1 columns {}'.format(df1.shape[1]))
    logger.debug('Dataframe 2 rows {}'.format(df2.shape[0]))
    logger.debug('Dataframe 2 columns {}'.format(df2.shape[1]))
    logger.debug('Dataframe 3 rows {}'.format(df3.shape[0]))
    logger.debug('Dataframe 3 columns {}'.format(df3.shape[1]))

    logger.debug('DataFrame describe: \n {}'.format(df1.describe()))
    logger.debug('DataFrame describe: \n {}'.format(df2.describe()))
    logger.debug('DataFrame describe: \n {}'.format(df3.describe()))








