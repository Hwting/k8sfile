#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
lark
"""
import json
from elastalert.alerts import Alerter, BasicMatchString
from requests.exceptions import RequestException
from elastalert.util import elastalert_logger, EAException
import requests
'''
###################################################################
# lark群机器人推送消息                                               #
#                                                                 #
# 作者: Wang.t                                                     #
# 作者博客:                                                         #
# Github: https://github.com/hwting/elastalert-lark-plugin        #
#                                                                 #
###################################################################
'''


class LarkAlerter( Alerter ):
    required_options = frozenset( ['lark_bot'] )

    def alert(self, matches):
        headers = {
            'content-type': 'application/json',
            'Accept': 'application/json;charset=utf-8',
        }
        body = self.create_alert_body( matches )
        content = {
                'title': self.create_title( matches ),
                'text': body
            }
        webhook_url = 'https://'
        try:
            response = requests.post( webhook_url, data=json.dumps( content ), headers=headers )
            response.raise_for_status()
        except RequestException as e:
            raise EAException( "send message has error: %s" % e )
        elastalert_logger.info( "send msg and response: %s")

    def get_info(self):
        return {'type': "LarkAlerter"}
