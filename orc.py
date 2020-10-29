import requests
import json
import base64
import time

#获取access_token
def get_access_token():
    client_id = 'API Key'
    client_secret = 'Secret Key'
     #client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id, client_secret)
    response = requests.get(host).text
    data = json.loads(response)
    access_token = data['access_token']
    return access_token
    #获取返回信息

#获取识别结果
def get_info(access_token):

    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    # 二进制方式打开图片文件
    f = open('图片位置', 'rb')
    img = base64.b64encode(f.read())#base64编码
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # if response:
    #     print(response.json())
    data_1 = response.json()
    return data_1

# 获取excel
def get_excel(requests_id, access_token):
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    pargams = {
        'request_id': requests_id,
        'result_type': 'excel'
    }
    url = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
    url_all = url + "?access_token=" + access_token
    res = requests.post(url_all, headers=headers, params=pargams)#访问链接获取excel下载页
    info_1 = res.json()['result']['ret_msg']
    excel_url=res.json()['result']['result_data']
    excel_1=requests.get(excel_url).content
    #识别输出文件
    with open('test.xls','wb+') as f:
        f.write(excel_1)
    print(info_1)


def main():
    print('正在处理中请稍后')
    access_token = get_access_token()
    data_1 = get_info(access_token)
    try:
        requests_id = data_1['result'][0]['request_id']
        if requests_id != '':
            print('识别完成')
    except:
        print('识别错误')
    print('正在获取excel')
    time.sleep(10)#延时十秒让图片转excel完毕，excel量多的话，转化会慢，可以延时长一点
    get_excel(requests_id, access_token)

main()

