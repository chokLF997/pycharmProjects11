import pytest
import requests


class Test:
    def test_login(self):
        url = "http://121.41.14.39:9097/api/loginS"
        data = {
            "username": "20154084",
            "password": "e10adc3949ba59abbe56e057f20f883e"
        }
        header = {
            "Content-Type": "application/json"
        }
        re = requests.post(url=url, data=data, headers=header)
        print(re.text)


if __name__ == '__main__':
    pytest.main()
#     # os.system("allure generate report -o ./allurereport --clean")
#     # ['-s', '-v', '--alluredir=report']
