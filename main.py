import json

class CountriesIterator():

    def __init__(self, file):
        self.file = file
        self.site_link = 'https://en.wikipedia.org/wiki/'
        self.start = -1

    def get_country_names(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            countries_list = json.load(file)
            result = []

            for country in countries_list:
                result.append(country['name']['official'])

            return result

    def write_countries_in_file(self, country_name):
        link = self.site_link + country_name

        with open('result.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{country_name} - {link} \n')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.get_country_names()):
            raise StopIteration

        self.write_countries_in_file(self.get_country_names()[self.start])
        return


if __name__ == '__main__':
    country_iter = CountriesIterator('countries.json')

    for i in country_iter:
        print('done')
