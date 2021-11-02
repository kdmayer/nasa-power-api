import yaml
from pathlib import Path
import pandas as pd
from src.power_api import PowerAPI

def main():

    # ------- Read configuration -------

    config_file = 'config.yaml'

    with open(config_file, 'rb') as f:

        conf = yaml.load(f, Loader=yaml.FullLoader)

    latitude = conf.get('lat', 0)
    longitude = conf.get('lon', 0)
    start_date = conf.get('start_date', 0)
    end_date = conf.get('end_date', 0)
    output_dir = conf.get('output_dir', 0)

    output_dir = Path(output_dir) / f"{longitude};{latitude}.csv"

    nasa_weather = PowerAPI(start=pd.Timestamp(str(start_date)), end=pd.Timestamp(str(end_date)), long=longitude, lat=latitude)

    weather_df = nasa_weather.get_weather()

    weather_df.to_csv(output_dir, sep=";")

if __name__ == '__main__':

    main()


