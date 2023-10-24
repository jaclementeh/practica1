from extract_data import extract_data
from analize_data import analize_data
from transform_data import transform_data
from metrics import metrics



if __name__ == '__main__':

    df1, df2, df3 = extract_data()

    analize_data(df1, df2, df3)

    transformed_data = transform_data(df1, df2, df3)

    metrics(transformed_data)

# decribe con to_string
# drop with field value
# logs with dataframe (xlsx?)
