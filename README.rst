Introduction
============

Helper library for the Hillcrest Laboratories BNO08x IMUs
and xbee i2c capable devices


* Based upon "adafruit_BNO080" for CPython by Bryan Siepert
* Author(s): Bryan Siepert
* Port to Micropython by Niko Rodriguez


Dependencies
=============
This driver depends on:

* `Digi XBee MicroPython PyCharm IDE Plugin <https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/digi-xbee-pycharm-ide-plug-in>`_

Known issues
=============
When debugging, string containing packets can overflow


Usage Example
=============

.. code-block:: python3

    from utime import sleep
    from machine import I2C
    from i2c import BNO08X_I2C
    from BNO080 import (
        BNO_REPORT_ACCELEROMETER,
        BNO_REPORT_GYROSCOPE,
        BNO_REPORT_MAGNETOMETER,
        BNO_REPORT_ROTATION_VECTOR,
    )

    i2c_obj = I2C(1, freq=400000)
    #bno = BNO08X_I2C(i2c_obj, debug=True)
    bno = BNO08X_I2C(i2c_obj)


    bno.enable_feature(BNO_REPORT_ACCELEROMETER)
    bno.enable_feature(BNO_REPORT_GYROSCOPE)
    bno.enable_feature(BNO_REPORT_MAGNETOMETER)
    bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)

    while True:
        
        sleep(1)
        print("Acceleration:")
        accel_x, accel_y, accel_z = bno.acceleration  # pylint:disable=no-member
        print("X: %0.6f  Y: %0.6f Z: %0.6f  m/s^2" % (accel_x, accel_y, accel_z))
        print("")

        print("Gyro:")
        gyro_x, gyro_y, gyro_z = bno.gyro  # pylint:disable=no-member
        print("X: %0.6f  Y: %0.6f Z: %0.6f rads/s" % (gyro_x, gyro_y, gyro_z))
        print("")

        print("Magnetometer:")
        mag_x, mag_y, mag_z = bno.magnetic  # pylint:disable=no-member
        print("X: %0.6f  Y: %0.6f Z: %0.6f uT" % (mag_x, mag_y, mag_z))
        print("")
        
        sleep(1)
        #print("Rotation Vector Quaternion:")
        quat_i, quat_j, quat_k, quat_real = bno.quaternion  # pylint:disable=no-member
        print(
            "%0.2f,%0.2f,%0.2f,%0.2f" % (quat_real,quat_i, quat_j, quat_k)
        )