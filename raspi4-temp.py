from bme280 import bme280
from bme280 import bme280_i2c
from influxdb_client.client.write_api import SYNCHRONOUS
import ambient
import socket
import influxdb_client

def main():

    url="http://localhost:8086"
    token = "cIqwizWxnzr5IAOyesBdrW9t1XubOOge0R43otIENtKV7jY9sd695ZXDK17lWiBbrRrP_j9uuCw18JQFzg7LdA=="
    org = "home"
    bucket = "室温"
    client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)

    # 初期化
    bme280_i2c.set_default_i2c_address(0x76)
    bme280_i2c.set_default_bus(1)
    temp = 0.0
    pre = 0.0
    hum = 0.0

    # キャリブレーション
    bme280.setup()

    # データ取得
    data_all = bme280.read_all()

    # 温度、湿度、気圧の表示
   # print"(%7.2f" % data_all.temperature)
   # print("%7.2f" % data_all.humidity)
   # print("%7.2f" % data_all.pressure)
   # return
    temp = ("%7.2f" % int(data_all.temperature))
    pre = ("%7.2f" % data_all.pressure)
    hum = ("%7.2f" % data_all.humidity)
   # ambi = ambient.Ambient(64210, "623cf410407b8a34")
   # r = ambi.send({"d1": temp, "d2": pre, "d3": hum})
    # データー送る
    #UDP_IP = "127.0.0.1"
    #UDP_PORT = 8092
    #MESSAGE = "2F 気温=({str(temp)})"
    #print ("UDP target IP:" + UDP_IP)
    #print ("UDP target port:" + str(UDP_PORT))
    #print ("message: " + MESSAGE)
    #sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    #sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))

   #ambi = ambient.Ambient(64118, "036b6f7b14a9bc2a") 
   #r = ambi.send({"d1": temp, "d2": pre, "d3": hum})




# url="http://localhost:8086"
# token = "cIqwizWxnzr5IAOyesBdrW9t1XubOOge0R43otIENtKV7jY9sd695ZXDK17lWiBbrRrP_j9uuCw18JQFzg7LdA=="
# org = "home"
# bucket = "室温"

    write_api = client.write_api(write_options=SYNCHRONOUS)
    p = influxdb_client.Point("二階").\
	tag("機器", "rasp4").\
	field("気温", (round(data_all.temperature, 2)))

    w = influxdb_client.Point("二階").\
        tag("機器", "rasp4").\
        field("湿度", (round(data_all.humidity, 2)))

    a = influxdb_client.Point("二階").\
        tag("機器", "rasp4").\
        field("気圧", (round(data_all.pressure, 2)))


    write_api.write(bucket=bucket, org=org, record=p)
    write_api.write(bucket=bucket, org=org, record=w)
    write_api.write(bucket=bucket, org=org, record=a)

if __name__ == "__main__":
    main()
