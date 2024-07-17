import BNO055
import smbus

class I2C:
    def __init__(self, bus=6):
        print("init")
        self.bus = smbus.SMBus(bus)
        self.deviceAddress = 0x4a
    
    def get_i2c_device(self, address):
        print("getting i2c device at address:",address)
        return self

    def writeList(self, address, data):
        print("writelist",address,data)

    def write8(self, address, value):
        print("write8",address,value)

    def readList(self, address, length):
        print("readlist",self.deviceAddress,address,length)
        data = self.bus.read_i2c_block_data(self.deviceAddress, address, length)
        return data

    def readU8(self, address):
        print("readU8",address)
        # return self.bus.read_byte(address)


# i2c = I2C(bus=6)

# print(i2c)
# sensor = BNO055.BNO055(i2c=i2c)
# sensor.read_gyroscope()

print("start")
bus = smbus.SMBus(6)
# print(bus.read_block_data(0x4a,0))