import xbee
from machine import (I2C)
from BNO080.i2c import BNO08X_I2C
from BNO080.BNO080 import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_MAGNETOMETER,
    BNO_REPORT_ROTATION_VECTOR,
)

# BOSS 64 bit DIR
TARGET_64BIT_ADDR = b'\00\x13\xA2\x00\x41\xB8\xF1\x2B'

i2c_obj = I2C(1, freq=400000)
bno = BNO08X_I2C(i2c_obj, debug=False, xbee_dir=TARGET_64BIT_ADDR)


bno.enable_feature(BNO_REPORT_ACCELEROMETER)
bno.enable_feature(BNO_REPORT_GYROSCOPE)
bno.enable_feature(BNO_REPORT_MAGNETOMETER)
bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)

bno.enable_report_transmission(BNO_REPORT_ACCELEROMETER)
bno.enable_report_transmission(BNO_REPORT_GYROSCOPE)
bno.enable_report_transmission(BNO_REPORT_MAGNETOMETER)
bno.enable_report_transmission(BNO_REPORT_ROTATION_VECTOR)

while True:
    bno._process_available_packets()