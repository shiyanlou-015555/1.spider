import requests
#申请的key
ak='f30c9d52b003c2b3ac089e2672e18baf'

#传入地址，返回对应地址的经纬度信息
def address(address):
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    contest=contest['geocodes'][0]['location']
    return contest


if __name__ == '__main__':
    print(address("兰州西站"))