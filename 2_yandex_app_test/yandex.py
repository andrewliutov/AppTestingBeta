import requests


class Yandex:
    def __init__(self, token_ya):
        self.api_url = 'https://cloud-api.yandex.net'
        self.token_ya = token_ya

    def upload_folder(self):
        headers = {'accept': 'application/json',
                   'authorization': f'OAuth {backup_ul.token_ya}'}
        put = requests.put(self.api_url + '/v1/disk/resources',
                     headers=headers,
                     params={'path': 'Test_folder'})
        return put.status_code


token_ya = 'sample-AQAAAAAdgzd3AADLW1UxrNTnnU5YoDB1vOrnZvo'
backup_ul = Yandex(token_ya)


if __name__ == '__main__':
    backup_ul.upload_folder()
