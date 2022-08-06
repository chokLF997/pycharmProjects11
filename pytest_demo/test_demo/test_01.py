import pytest
import requests

from read_yaml import YamlUtil


class Test:
    @pytest.mark.parametrize('args', YamlUtil('demo.yaml').read_yaml())
    def test_login(self, args):
        url = args['login']['requests']['url']
        data = args['login']['requests']['data']
        r = requests.post(url=url, json=data)
        print(r.json())
        assert args['login']['requests']['valicate']['eq']['code'] == r.json()['code']

    @pytest.mark.parametrize('args', YamlUtil('demo.yaml').read_yaml())
    def test_search(self, args):
        url = args['search']['requests']['url']
        params = {
            "format": "json",
        }
        data = args['search']['requests']['data']
        headers = args['search']['requests']['headers']
        r = requests.post(url=url, params=params, headers=headers, json=data)
        print(r.json())
        assert args['search']['requests']['valicate']['eq']['code'] == r.json()['code']

    @pytest.mark.parametrize('args', YamlUtil('demo.yaml').read_yaml())
    def test_detail(self, args):
        url = args['detail']['requests']['url']
        params = {
            "format": "json",
            "ReportNum": "2019074000914701"
        }
        headers = args['detail']['requests']['headers']
        r = requests.get(url=url, params=params, headers=headers)
        print(r.json())
        assert args['detail']['requests']['valicate']['eq']['code'] == r.json()['code']


if __name__ == '__main__':
    pytest.main()

#     # os.system("allure generate report -o ./allurereport --clean")
#     # ['-s', '-v', '--alluredir=report']
