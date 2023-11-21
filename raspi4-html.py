from bme280 import bme280
from bme280 import bme280_i2c
import ambient

def main():
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
   # print("%7.2f" % data_all.temperature)
   # print("%7.2f" % data_all.humidity)
   # print("%7.2f" % data_all.pressure)
   # return
    temp = ("%-6.2f" % data_all.temperature)
    pre = ("%7.2f" % data_all.pressure)
    hum = ("%6.2f" % data_all.humidity)
    ambi = ambient.Ambient()
    r = ambi.send({"d1": temp, "d2": pre, "d3": hum})
    # データー送る

   #ambi = ambient.Ambient(64118, "036b6f7b14a9bc2a") 
   #r = ambi.send({"d1": temp, "d2": pre, "d3": hum})
if __name__ == "__main__":
    main()
