[[_TOC_]]

# Introduction

This README file describes the content and the meaning of the files located in this Python folder.

- [Interfaces](interfaces)
- [Protocols](protocols)
- [Utilities](utilities)

Please see the overall architecture of ATE from main [README](../docs/README.md) file located in docs folder.

# Devices

The content of [devices](devices) folder is meant to act as an interfaces towards different hardware devices.

For example [veristand.py](devices/national_instrument/veristand.py) is a python interface towards National Instrument's [Veristand](https://www.ni.com/en/shop/data-acquisition-and-control/application-software-for-data-acquisition-and-control-category/what-is-veristand.html).

# Interfaces

The content of [interfaces](interfaces) folder is meant to act as an interfaces towards different software.

For example [codesys_rpc_client.py](interfaces/codesys/codesys_rpc_client.py) is a python interface towards Codesys IDE using [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) protocol.

These libraries can be used directly from robot in resource files.
 See more information about Robot and Resources from [here](../robot/README.md).

# Protocols

The content of [protocols](protocols) folder is meant to act as an interfaces towards different communication protocols.

For example canopen.py or modbus.py is a python interface towards these protocols.

These libraries are not meant to be used directly in Robot level.

Usually protocols are needed when communicating certain devices, that's why protocols as a libraries are imported and used by devices libraries.

# Utilities

The content of [utilities](utilities) folder is meant to act as an help libraries for general usage such as mathoperations, file parsers, bit operations etc.

These libraries can be used from other python libraries or utilities can also be used directly from robot in resource files.

See more information about Robot and Resources from [here](../robot/README.md).