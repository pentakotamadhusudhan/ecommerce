import requests
import json


def FCMF_token(body, title, token):
    serverToken = 'AAAAdpCt0RM:APA91bF1EzO_FeQqhh_mTrotjbTGbqiqJdc_gsJOhRzdVV_HtqH' \
                  '-vCGar0hHUQDXVxRpRKtfKxTITfrVTo9v4ucIDQUyQ5HAj_T4EIHyE-jskDquUgp2F077_6P73rvrwxAiLQmCCLEq '
    deviceToken = token

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
    }

    body = {
        'notification': {'title': title,
                         'body': body
                         },
        'to':
            deviceToken,
        'priority': 'high',
        #   'data': dataPayLoad,
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
    print(response.status_code)

    return response.json()
