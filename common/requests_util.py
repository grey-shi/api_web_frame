import requests
from common.logger import Log

log = Log()


class RequestUtil(object):
    sess = requests.session()

    # 统一请求封装
    def send_all_request(self, **kwargs):
        res = RequestUtil.sess.request(**kwargs)
        log.info(res.text)
        return res


