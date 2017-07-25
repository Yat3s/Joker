from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {
    "code": 1000,
    "message": "OK",
    "dataValue": [
        {
            "skuName": "法国进口 巴黎水Perrier气泡矿泉水 原味 玻璃瓶装1箱 330MLx24瓶",
            "skuNum": 1,
            "stockNum": 10,
            "color": "黄色",
            "weight": "2.5kg",
            "purchaseTime": "2017/07/26 0:20",
            "timeOutTime": "2017/07/26 0:23"
        },
        {
            "skuName": "【京东超市】三只松鼠 蜜饯果干 休闲零食 红宝石蔓越莓干108g/袋",
            "skuNum": 1,
            "stockNum": 10,
            "color": "白色",
            "weight": "2.5kg",
            "purchaseTime": "2017/07/26 0:20",
            "timeOutTime": "2017/07/26 0:23"
        },
        {
            "skuName": "法国进口 巴黎水Perrier气泡矿泉水 原味 玻璃瓶装1箱 330MLx24瓶",
            "skuNum": 1,
            "stockNum": 10,
            "color": "黄色",
            "weight": "2.5kg",
            "purchaseTime": "2017/07/26 0:20",
            "timeOutTime": "2017/07/26 0:23"
        },
        {
            "skuName": "法国进口 巴黎水Perrier气泡矿泉水 原味 玻璃瓶装1箱 330MLx24瓶",
            "skuNum": 1,
            "stockNum": 10,
            "color": "黄色",
            "weight": "2.5kg",
            "purchaseTime": "2017/07/26 0:20",
            "timeOutTime": "2017/07/26 0:23"
        }
    ]
}

api.add_resource(HelloWorld, '/v1/autopay/payments/record')
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = '80')
