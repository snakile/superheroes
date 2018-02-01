import requests


class CharacterFetcher:
    def __init__(self):
        self.url = 'https://comicvine.gamespot.com/api/characters'
        self.base_params = {'api_key': '969a888c5b1043890fb27bbf267ace9d4d7e0fd8', 'format': 'json', 'field_list': 'id'}

    def _fetch(self, params):
        params = {**self.base_params, **params}
        response = requests.get(url=self.url, params=params, headers={'User-agent': 'foo'})
        results = response.json()['results']
        return results

    def fetch_male_characters(self, n=100):
        params = {'filter': 'gender:1', 'limit': str(n)}
        results = self._fetch(params)
        return (result['id'] for result in results)


def main():
    fetcher = CharacterFetcher()
    male_characters = fetcher.fetch_male_characters(10)
    print(list(male_characters))


if __name__ == '__main__':
    main()
