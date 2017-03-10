import sklearn
import numpy as num
import pandas as pa
import os


output_fileName="imports-85.data.csv"
output_path=os.path.join(r'C:\Users\Praveen Kn\Downloads',output_fileName)
data_csv=pa.read_csv(output_path)
data_csv.columns=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
                  "body-style","drive-wheels","engine-location","wheel-base","length","width",
                  "height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system",
                  "bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
data_frame=pa.DataFrame(data_csv)
print(data_frame.head())
