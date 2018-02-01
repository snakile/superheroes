import requests


class Fetcher:
    def __init__(self):
        self.url = 'https://comicvine.gamespot.com/api/characters'
        self.base_params = {'api_key': '969a888c5b1043890fb27bbf267ace9d4d7e0fd8', 'format': 'json'}

    def fetch(self, params):
        params = {**self.base_params, **params}
        response = requests.get(url=self.url, params=params, headers={'User-agent': 'foo'})
        data = response.json()
        return data


def main():
    params = {'field_list': 'gender,name,powers,origin,id',
              'limit': '2'}
    data = Fetcher().fetch(params)
    print(data['results'][0]['name'])


if __name__ == '__main__':
    main()
