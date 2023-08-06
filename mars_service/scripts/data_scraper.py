import requests
import psycopg2
import datetime
from covid_data.models import CovidData


# Функция для получения данных из API
def get_data_from_api():
    url = "https://api.covidtracking.com/v1/us/daily.json"  # Замените на URL вашего открытого API
    response = requests.get(url)
    data = response.json()

    def parse_datetime(datetime_str):
        datetime_str = datetime_str.replace("T24:00:00Z", "T00:00:00Z")
        datetime_object = datetime.datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
        return datetime_object
    for item in data:
        CovidData.objects.create(
            date=parse_datetime(item["dateChecked"]),
            death=item["death"],
            hospitalized=item["hospitalized"],
            positive=item["positive"],
        )
    return data


def main():
    data = get_data_from_api()
    # print("Данные успешно сохранены в базе данных!")


def run():
    main()
