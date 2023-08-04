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
            death_increase=item["deathIncrease"],
            hospitalized=item["hospitalized"],
            hospitalized_cumulative=item["hospitalizedCumulative"],
            hospitalized_currently=item["hospitalizedCurrently"],
            hospitalized_increase=item["hospitalizedIncrease"],
            in_icu_cumulative=item["inIcuCumulative"],
            in_icu_currently=item["inIcuCurrently"],
            negative=item["negative"],
            negative_increase=item["negativeIncrease"],
            on_ventilator_cumulative=item["onVentilatorCumulative"],
            on_ventilator_currently=item["onVentilatorCurrently"],
            pending=item["pending"],
            pos_neg=item["posNeg"],
            positive=item["positive"],
            positive_increase=item["positiveIncrease"],
            recovered=item["recovered"],
            states=item["states"],
            total=item["total"],
            total_test_results=item["totalTestResults"],
            total_test_results_increase=item["totalTestResultsIncrease"],
        )
    return data


def main():
    data = get_data_from_api()
    # print("Данные успешно сохранены в базе данных!")


def run():
    main()
