from logging import error
from os.path import exists

from bs4 import BeautifulSoup
from requests import get

from scraping.exceptions import DataFromScrapingNotMatches


class DriverDataScraper:
    def __init__(self):
        self.__url = "https://pl.wikipedia.org/wiki/Lista_zwyci%C4%99zc%C3%B3w_Grand_Prix_Formu%C5%82y_1"
        self.__data = self.__get_data_from_site()

    def __get_data_from_site(self):
        page = get(self.__url)
        bs = BeautifulSoup(page.content, "html.parser")
        return bs.find_all("table", class_="sortable", limit=1)

    def __resolve_headers(self):
        for element in self.__data:
            header = element.find_all('tr', class_="")
            list_of_headers = str(
                header[0].get_text(',', strip=True).replace('Źródło', "").replace("Msc.", "Miejsce w Rankingu"))
            return list_of_headers

    def __get_drivers_data_from_web(self):
        list_of_driver_data = []
        for element in self.__data:
            drivers_data = element.find_all('tr', class_="")
            for number in range(1, len(drivers_data)):
                driver_data = str(drivers_data[number].get_text(',', strip=True))
                list_of_driver_data.append(driver_data)
        return list_of_driver_data

    def save_data_to_file_and_check_correctness(self):
        content_of_file = []
        headers = self.__resolve_headers()
        data_of_drivers = self.__get_drivers_data_from_web()
        if exists('/scraping/drivers_data.txt'):
            with open('drivers_data.txt', 'r', encoding='utf-8') as file:
                content_of_file = file.readlines()
                load_data = []
                try:
                    load_data.append(headers + '\n')
                    for data in data_of_drivers:
                        load_data.append(data + '\n')
                    if len(load_data) != len(content_of_file):
                        raise DataFromScrapingNotMatches(len(load_data) - len(content_of_file))
                except DataFromScrapingNotMatches as e:
                    error(e.get_message())
        else:
            content_of_file.append(headers + '\n')
            for data in data_of_drivers:
                content_of_file.append(data + '\n')
            with open('drivers_data.txt', 'w+', encoding='utf-8') as file:
                file.writelines(content_of_file)
        return content_of_file


if __name__ == '__main__':
    scraper = DriverDataScraper()
    print(scraper.save_data_to_file_and_check_correctness())
