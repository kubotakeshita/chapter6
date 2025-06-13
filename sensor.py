import BME280
import time

BME280.setup()
BME280.get_calib_param()

for i in range(10):
        pres = BME280.readPres()
        temp = BME280.readTemp()
        humi = BME280.readHumi()

        print("pressure : %7.2f hPa" % pres)
        print("temperature : %-6.2f C" % temp)
        print("humidity : %6.2f %%" % humi)
        time.sleep(3.0)
