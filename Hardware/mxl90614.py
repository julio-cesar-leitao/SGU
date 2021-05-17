import smbus
from time import sleep

class MXL90614():
    # Based on the following source-code
    # github.com/sightsdev/PyMLX90614/blob/master/mlx90614.py
    #
    # More details on MLX90614 datasheet on section 8.4 (SMBus)

    BUS = 1         # /dev/i2c-1 is bus=1
    ADDRESS = 0x5a    # MXL90614 slave address is 0x5a

    ############# MLX90614 ADDRESS #################
    Tamb = 0x06
    Tobj1 = 0x07
    Tobj2 = 0x08

    comm_retries = 5
    comm_sleep_amount = 0.1

    def __init__(self):
        self.bus = smbus.SMBus(self.BUS)
        self.t_amb = 0
        self.t_obj1 = 0
        self.t_obj2 = 0

    def read(self):
        err = None
        for i in range(self.comm_retries):
            try:
                self.t_amb = self.bus.read_word_data(self.ADDRESS, self.Tamb)
                self.t_obj1 = self.bus.read_word_data(self.ADDRESS, self.Tobj1)
                self.t_obj2 = self.bus.read_word_data(self.ADDRESS, self.Tobj2)
            except IOError as e:
                err = e
                sleep(self.comm_sleep_amount)
        #raise err

    def celsius(self, data):
        return (data * 0.02) - 273.15


if __name__ == "__main__":
    sensor = MXL90614()
    sensor.read()
    temp = sensor.celsius(sensor.t_obj1)
    print(temp)


