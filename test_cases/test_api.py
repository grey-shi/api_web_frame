import os.path
import pytest
from common.requests_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml, clear_yaml, read_yaml_testcase
from common.logger import Log

log = Log()


class TestApi(object):

    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase('data\\env_test\\case_yaml\\01-登录_yaml.yaml'))
    def test_get_token(self, caseinfo):
        methods = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        datas = caseinfo["request"]["params"]
        res = RequestUtil().send_all_request(method=methods, url=urls, params=datas)
        if "token" in dict(res.json()).keys():
            write_yaml({"token": res.json()['token']})

    @pytest.mark.user
    @pytest.mark.parametrize("caseinfo", read_yaml_testcase('data\\env_test\\case_yaml\\01-登录_yaml.yaml'))
    def test_logout(self, caseinfo):
        urls = base_url + '/api/user/logout'
        header = {
            'Authorization': read_yaml("token"),
            'Content-Type': 'application/json'
        }
        datas = {
        }
        res = RequestUtil().send_all_request(method="post", url=urls, headers=header, json=datas)
