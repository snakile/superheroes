import requests
import urllib.parse


class CharacterFetcher:
    def __init__(self):
        self.base_url = 'https://comicvine.gamespot.com/api/'
        self.base_params = {'api_key': '969a888c5b1043890fb27bbf267ace9d4d7e0fd8', 'format': 'json'}

    def _fetch(self, api, params):
        url = urllib.parse.urljoin(self.base_url, api)
        params = {**self.base_params, **params}
        response = requests.get(url=url, params=params, headers={'User-agent': 'foo'})
        results = response.json()['results']
        return results

    def _fetch_characters_api(self, params):
        default_params = {'field_list': 'id'}
        params = {**params, **default_params}
        return self._fetch('characters', params)

    def _fetch_single_character_api(self, params, character_id):
        character_field_list = ['name', 'gender', 'origin', 'powers']
        default_params = {'field_list': ','.join(character_field_list)}
        params = {**params, **default_params}
        return self._fetch('character/{}'.format(character_id), params)

    def get_male_characters(self, n=100):
        params = {'filter': 'gender:1', 'limit': str(n)}
        results = self._fetch_characters_api(params)
        return (result['id'] for result in results)

    def get_character(self, character_id):
        id_prefix = '4005'
        character_id = '-'.join([id_prefix, character_id])
        return self._fetch_single_character_api({}, character_id)


def main():
    fetcher = CharacterFetcher()
    male_characters = fetcher.get_male_characters(10)
    print(list(male_characters))
    character_json = fetcher.get_character('1264')
    print(character_json['name'])
    print(character_json['gender'])
    print(character_json['origin']['name'])
    print(character_json['powers'])


if __name__ == '__main__':
    main()
