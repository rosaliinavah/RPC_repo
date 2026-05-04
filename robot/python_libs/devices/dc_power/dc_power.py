"""
DC Power Library
=================

A Robot Framework library for interacting with DC Powers using PyVisa API.
"""
import time
import pyvisa


class dc_power:
    """
    Class acts as an interface for DC Powers.
    """

    def __init__(self, resource_name=None):
        """
        Initialize the DC power class. Optionally provide a resource name.

        *Arguments:*

        resource_name (str): The PyVisa resource name of the DC power.
        """
        self.resource_name = resource_name
        self.rm = pyvisa.ResourceManager()
        self.instrument = None

    def connect(self):
        """
        Connect to the DC power device using the resource name provided during initialization.
        """
        if not self.resource_name:
            raise ValueError("No resource name provided.")

        try:
            self.instrument = self.rm.open_resource(self.resource_name)
            print(f"Opened resources:{self.rm.list_opened_resources()}")
        except pyvisa.VisaIOError as e:
            raise ValueError(
                f"Failed to connect to {self.resource_name}: {e}") from e

    def disconnect(self):
        """
        Disconnect from the device.
        """
        if self.instrument is None:
            raise ValueError("Open connection before disconnect.")

        if self.instrument:
            self.instrument.close()

    def output_on(self):
        """
        Send the command to power on outputs on the device.
        """
        if self.instrument is None:
            raise ValueError("Open connection before Output ON.")

        if self.instrument:
            self.instrument.write('OUTP ON')

    def output_off(self):
        """
        Send the command to power off outputs on the device.
        """
        if self.instrument is None:
            raise ValueError("Open connection before Output OFF.")

        if self.instrument:
            self.instrument.write('OUTP OFF')

    def read_voltage(self):
        """
        Gets the voltage in Volts from the device.
        """
        if self.instrument is None:
            raise ValueError(
                "Open connection before reading values from DC power.")

        if self.instrument:
            ret_val = str(self.instrument.query_ascii_values('MEAS:VOLT?'))

        return ret_val

    def read_current(self):
        """
        Gets the current in Amperes from the device.
        """
        if self.instrument is None:
            raise ValueError(
                "Open connection before reading values from DC power.")

        if self.instrument:
            ret_val = str(self.instrument.query_ascii_values('MEAS:CURR?'))

        return ret_val


if __name__ == "__main__":
    RESOURCE_STR = 'TCPIP::10.200.120.105::inst0::INSTR'
    dc_power_lib = dc_power(resource_name=RESOURCE_STR)
    dc_power_lib.connect()
    time.sleep(1)
    dc_power_lib.output_on()
    time.sleep(2)
    print(dc_power_lib.read_voltage())
    print(dc_power_lib.read_current())
    dc_power_lib.output_off()
    time.sleep(2)
    print(dc_power_lib.read_voltage())
    print(dc_power_lib.read_current())
    time.sleep(1)
    dc_power_lib.disconnect()
    time.sleep(1)
