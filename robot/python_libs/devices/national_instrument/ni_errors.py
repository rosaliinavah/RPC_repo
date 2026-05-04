"""National Instrument returns an error code when it encounters a problem while executing.

Instrument Driver Error Codes:
https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/errors/instrument-driver-error-codes.html

VeriStand Error Codes:
https://www.ni.com/docs/en-US/bundle/veristand/page/veristand-error-codes.html

Networking Error Codes:
https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/errors/networking-error-codes.html

VISA Error Codes:
https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/errors/visa-error-codes.html

NI-DAQmx Driver Error Codes:
https://www.ni.com/docs/en-US/bundle/ni-daqmx-.net-framework-4.5.1-class-library-getting-started/page/netdaqmxerrorcodes.html

General LabVIEW Error Codes:
https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/errors/general-labview-error-codes.html


Use the following dictionary to locate an error code message.

Example:
    error_msg = ni_errors.get_error_message("0x80054450")
"""


class ni_errors:
    """
    Class for National Instruments errors
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    NI_ERRORS = {
        # ---------- Instrument Driver Error Codes ----------
        -1074003967: "Parameter 1 is out of range.",
        -1074003966: "Parameter 2 is out of range.",
        -1074003965: "Parameter 3 is out of range.",
        -1074003964: "Parameter 4 is out of range.",
        -1074003963: "Parameter 5 is out of range.",
        -1074003962: "Parameter 6 is out of range.",
        -1074003961: "Parameter 7 is out of range.",
        -1074003960: "Parameter 8 is out of range.",
        -1074003951: "Identification query failed, Instrument identification failed, \
            This error can occur if you selected the wrong instrument or your instrument did not respond, \
            This error also can occur if you used a model that is not officially supported by this driver, \
            If you are sure that you have selected the correct instrument and it is responding, \
            try disabling ID Query in the instrument driver's initialize VI.",
        -1074003950: "Error interpreting the instrument's response.",
        -1074000001: "Instrument self-test failure, The instrument you are communicating with reported a self-test failure.",
        -1074000000: "Instrument error query failure, The instrument you are communicating with reported an error.",
        -1300: "Instrument-specific error.",
        -1236: "Error interpreting instrument response.",
        -1223: "Instrument identification query failed.",
        -1210: "Parameter out of range, The Set Cursor VI also can return this error.",
        102: "IVI invalid downcast, Driver is different from the specific driver associated with Logical Name.",
        103: "No IVI class session opened, You must call the class driver Initialize VI before you can call a specific driver VI, \
            This error also can occur if the IVI Logical Name control is set to the wrong IVI Class.",
        1073479937: "ID Query not supported.",
        1073479938: "Reset not supported.",
        1073479939: "Self-test not supported.",
        1073479940: "Error Query not supported.",
        # ---------- VERISTAND ERRORS ----------
        -307500: "The FPGA configuration file (.fpgaconfig) is invalid or contains an error.",
        -307501: "The specified operation is unable to acquire the memory necessary to execute. To correct this error, increase the amount of \
            memory in the system or reduce the amount of memory that this operation requires. You can reduce the amount of memory required by the \
            operation by uninstalling unneeded components from the real-time (RT) target or by reducing the number of devices, channels, and/or \
            stimulus generators used.",
        -307502: "An FPGA argument or parameter is invalid. This might be a problem with the FPGA configuration file (.fpgaconfig) or FPGA bitfile. \
            This problem also might be caused by an invalid FPGA target handle.",
        -307503: "An unknown exception occurred while running the NI FPGA device. Verify that NI-RIO and the VeriStand software are installed \
            correctly on the real-time (RT) target.",
        -307504: "An FPGA argument or parameter is outside the expected range. Update the FPGA configuration file (.fpgaconfig).",
        -307505: "The FPGA bitfile has changed since the system definition file was last compiled. Open the system definition file in System \
            Explorer and refresh the FPGA configuration file (.fpgaconfig).",
        -307510: "Framework with the given name already exists.",
        -307511: "EESPort with the given name already exists.",
        -307512: "An unexpected step error has occurred.",
        -307525: "Cannot open selected file. The file was saved in a later version of VeriStand.",
        -307526: "The XML file provided is invalid.",
        -307548: "Legacy Stimulus Profile Editor is not supported anymore.",
        -307549: "Cannot find the wave file that an alarm response is configured to play when the alarm is triggered. Verify that wave files are \
            located at their specified locations.",
        -307550: "You have provided an invalid username or password.",
        -307551: "Internal error. The buffered data system failed to find required information in the transaction's variant data.",
        -307552: "Internal error. An attempt was made to open a 2D waveform read session.",
        -307553: "Unexpected waveform data type. This VI requires the specified waveform nodes to be of a specific data type.",
        -307554: "The specified stream condition is not valid for the data type of the waveform. This error might occur if you try to set the \
            streaming condition to be within a range of values for a waveform whose data type is a complex double (CDB). The in-range streaming \
            condition supports only waveforms whose data type is double (DBL).",
        -307555: "Cannot open a waveform session using an empty array of waveform references. Use the Get Waveform Data Reference VI to generate \
            valid data references with which you can open a waveform session.",
        -307556: "Cannot open waveform session because waveform data references are not valid. Use the Get Waveform Data Reference VI to generate \
            valid data references with which you can open a waveform session.",
        -307557: "Custom device cannot perform requested operation because VeriStand Engine is shutting down.",
        -307559: "The size of an input array does not match the number of waveforms in the streaming session. When you write to a multiple-waveform \
            session, the number of rows in the 2D Data array must match the number of waveforms in the session. When you start a multiple-waveform \
            session, the size of the 1D t0s array must match the number of waveforms in the session.",
        -307561: "Cannot write to waveform. Another waveform write session is already open for this waveform reference, and only one writer can \
            access the waveform reference at a time.",
        -307562: "The waveform session reference cannot be used if it is not open. Use the Open Waveform Session VI to open a waveform session \
            reference.",
        -307600: "The specified VI is broken and cannot run. Open the VI in LabVIEW for more information.",
        -307601: "The XML file is invalid according to the XML schema document (XSD).",
        -307602: "The GUID could not be found. If the requested page is a custom device, contact the creator of the custom device.",
        -307603: "The requested custom device does not have a main page specified. Contact the creator of the custom device to correct this error.",
        -307604: "VeriStand cannot mutate the system definition file to the current version.",
        -307605: "The requested simulation model could not be found. Navigate to the Model Configuration page in System Explorer and choose a \
            different model.",
        -307606: "The file does not contain a valid file format.",
        -307607: "VeriStand could not mutate the system definition file. The system definition file version is different from the official released \
            version of VeriStand.",
        -307608: "The custom device does not provide a valid source distribution for the target specified. Specify a different target or contact \
            the creator of the custom device for further support.",
        -307609: "The formula contains an unused variable declaration.",
        -307610: "The formula contains an invalid function or variable name.",
        -307611: "The associated NI-XNET database path cannot be found. Update either the alias or the database path.",
        -307612: "One or more chassis are unidentified. Open NI MAX and identify the type of the chassis for each controller that is configured in \
            System Explorer.",
        -307613: "You cannot add channels of the type you selected. The DAQ device either contains no channels of this type, or all available \
            channels of this type are already in the system definition.",
        -307614: "The DAQ support files are missing for the channel type selected. Try repairing your installation of VeriStand.",
        -307615: "This DAQ device does not support reference clock synchronization. In System Explorer on the DAQ Device Configuration page, click \
            the PXI Backplane Reference Clock drop-down and select None or Automatic.",
        -307616: "The associated NI-XNET signal has been deleted from the XNET database or it changed so it no longer matches the system \
            definition. If the database no longer contains the signal, delete the signal from the system definition. If the signal changed in the \
            database, reimport the signal.",
        -307617: "The system definition contains aliases that are not linked to any channel. Click on the Error/Warning icon on System Explorer to \
            get a list of aliases that are not linked and either link them to a channel or delete them.",
        -307621: "The request at the specified index does not have the same number of signals as the signal_num parameter. Call the \
            GetNextCompletedRequest method to get a valid index and signal number of a completed request.",
        -307622: "The specified request was not completed. Call the GetNextCompletedRequest method to get a valid index to a completed request.",
        -307623: "The specified request index is not valid. Call the GetNextCompletedRequest method to get a valid index to a completed request",
        -307624: "No proper request was found. Call the GetNextCompletedRequest method after the model executes a step to get the index of a \
            completed request.",
        -307625: "An error occurred while reading the signal values.",
        -307626: "One or more of the specified signals are not scalar. Only scalar signals can be viewed.",
        -307627: "One or more of the specified signal indexes are not valid. Use signal indexes that are in the model.",
        -307628: "There is not enough space on the target to read the signal values. Ensure you are not viewing signal values from paused models.",
        -307629: "A required input or output parameter for this method is null. Use allocated variables for parameters.",
        -307630: "The model refnum is not valid. Use the InitializeLibrary function to return a valid refnum.",
        -307650: "An unexpected error has occurred in the VeriStand API.",
        -307651: "The VeriStand API does not support this function.",
        -307652: "Failed to open a connection to VeriStand.exe.",
        -307653: "The input file parameter is invalid or does not exist. Ensure that this path is correct and that the file has not been removed.",
        -307654: "Cannot perform this request because VeriStand is not running a system definition file. Deploy a system definition file, and \
            try again.",
        -307655: "Invalid request. VeriStand is missing an engine component that is required to process the request.",
        -307656: "Invalid request. VeriStand does not have a system definition file loaded.",
        -307657: "The specified password does not match the current deployed configuration password.",
        -307658: "VeriStand is unable to run the system definition file when a system definition file is already running.",
        -307659: "Invalid password input parameter. The password cannot be an empty string.",
        -307660: "Timeout occurred while deploying a new system definition file.",
        -307661: "VeriStand failed to deploy the system definition file.",
        -307662: "Node is not found in the system.",
        -307663: "Timeout occurred while processing request.",
        -307664: "Channel does not have read access.",
        -307665: "Channel does not have write access.",
        -307666: "The specified channel cannot be faulted.",
        -307667: "The requested operation on this item reference is invalid.",
        -307668: "The specified channel cannot be scaled.",
        -307669: "The license is unavailable, invalid, or VeriStand failed to initialize the licensing component.",
        -307670: "The VeriStand Gateway cannot process the requested operation. The VeriStand Gateway currently is busy performing another \
            operation.",
        -307671: "The execution host is running a different system definition file than the file specified. You must deploy the system definition \
            file in order to connect to the execution host.",
        -307672: "One or more targets failed to start within the specified timeout. Verify that any start trigger or clock signals are configured \
            correctly.",
        -307673: "Another VeriStand Gateway already is connected to the execution host. Only one VeriStand Gateway can be connected to an execution \
            host at a time.",
        -307674: "The Run Workspace function is no longer supported. Use the Connect to System function instead, which has a system definition file \
            parameter instead of a workspace file.",
        -307675: "The VeriStand Gateway cannot complete the specified operation because the number of streamed channels for one or more targets \
            exceeds the maximum size. Stop data logging configurations or graphs to reduce the number of streamed channels. You also can increase \
            the maximum streamed channel count for the targets by editing the system definition file in System Explorer.",
        -307676: "VeriStand cannot open the specified project file because another project is already open.",
        -307677: "The reference to the project file is no longer valid. The referenced project is no longer open.",
        -307678: "The specified workspace tool VI is not open.",
        -307679: "The VeriStand Gateway is no longer connected to the targets. One of the targets stopped running the system definition file.",
        -307680: "An exception occurred when the model parameter file was being parsed.",
        -307681: "Failed to read the VeriStand service configuration file. Repair your VeriStand installation.",
        -307682: "Could not complete one or more requests because a target is offline. A target is no longer connected and is not running the \
            system definition. Any future requests for this target will not be completed.",
        -307683: "Cannot deploy or connect to the system definition because all targets in the system are disabled. Enable one or more targets in \
            the system definition, and then try to deploy again.",
        -307684: "Cannot start server because the port address is already in use by another process. To change the port address for the server, \
            select Tools » Options, browse to the Port Settings page, and change the value of the corresponding control.",
        -307685: "Cannot initialize model parameter(s) defined in model parameter file because parameter was not found in system. 1) Ensure the \
            expression of the parameter is spelled correctly in the file. 2) If the file defines a temporary variable, ensure the system definition \
            allows temporary variables. 3) If the file contains aliases, ensure the path to an alias file is correct in the system definition. \
            Verify the contents of the file and the settings on the Simulation Models configuration page in System Explorer, and try again.",
        -307686: "The specified target is not defined in the deployed system definition.",
        -307687: "The given number of channels and number of values do not match.",
        -307688: "Timeout occurred while reconnecting a target to the gateway.",
        -307689: "The specified target is disabled. Change the target settings in the system definition and redeploy if you wish to use this \
            target.",
        -307690: "To reconnect to a target without deploying, the restart action for real-time (RT) targets must be set to Run System Definition. \
            To enable the Run System Definition restart action, select the System Initialization node in the System Explorer and select Run System \
            Definition. You must redeploy the system definition to make use of these changes.",
        -307691: "Import operation failed for the specified SLSC chassis.",
        -307692: "VeriStand encountered an unknown internal error while using WebDAV. Check your target's disk to determine if it is full.",
        -307700: "One or more Model Execution Loops failed to shut down properly.",
        -307701: "Timeout occurred while writing a parameter value to the VeriStand Engine.",
        -307702: "The size of the imported model data in the system definition file conflicts with the size in the specified model file. This error \
            can occur if the model file contains a different number of inports, outports, signals, or parameters than when it was imported. \
            This error also can occur if two or more models contain a global parameter with the same name but different dimensions. To correct this \
            error, reload the model in the System Explorer and verify the dimensions of any global parameters that multiple models contain. \
            Alternatively, on the Parameters page for a model in the Scope for Global Parameters drop-down, select Model to avoid conflicts caused \
            when the model shares the global parameter with other models.",
        -307703: "The specified model is incompatible with VeriStand. If you want to deploy the model to an RT target, launch the Console Viewer \
            tool to display the console output of the target, which includes information about the source of the error.",
        -307704: "The specified model is not compatible with the specified execution host.",
        -307705: "The specified model has an unsupported 32-bit architecture.",
        -307710: "The specified item is not an inline custom device. Pass in a valid reference to an inline custom device.",
        -307711: "A channel and the alias that references it both specify a data source mapping. A channel can only have one data source mapping. \
            Remove the mapping for either the channel or its alias.",
        -307718: "Setting Scan Interface mode failed. Before using this mode, make sure NI RIO IO Scan is installed on the target.",
        -307719: "Unable to discover XNET interface(s) before timeout elapsed. Contact NI support at ni.com/support for more information about \
            resolving this error.",
        -307720: "Failed to route PXI_Trig0 from bus segment of chassis master device to other bus segments. To address this issue, open MAX and \
            select the chassis. On the Triggers pane for the chassis, clear any reservation for PXI_Trig0 on the appropriate bus, set routing for \
                PXI_Trig0 to Dynamic, and try again.",
        -307721: "Cannot enable Slow Background Conversion Mode if hardware-timed single-point sample mode is disabled for analog input channels. \
            If you want to enable Slow Background Conversion Mode for this device, you must first enable hardware-timed single-point support for \
                its AI channels.",
        -307722: "A DAQ channel of an unexpected type was found.",
        -307723: "A property of a DAQ channel has an invalid value. Change the value the error message lists. If you used the System Definition API \
            to change the units property of a channel, restore the units to the original value.",
        -307724: "A DAQ channel initialization VI encountered an unexpected property name.",
        -307725: "The value does not match the dimensions of the specified channel.",
        -307726: "A calculated channel failed to compile correctly and cannot be executed.",
        -307727: "The requested DAQ device, the master timing source for the timed loop, is unavailable.",
        -307728: "One or more channel mappings have incompatible dimensions. Matrix channels only can be mapped to matrix channels with the same \
            dimension.",
        -307729: "The system definition file is missing. Deploy a valid system definition file.",
        -307730: "One or more asynchronous custom devices failed to shut down properly and the VeriStand Engine aborted them.",
        -307731: "The system definition file is not saved in the current version of VeriStand. VeriStand cannot mutate system definition files on a \
            real-time target. Use System Explorer to open and save the file.",
        -307732: "The system has become unresponsive. The Primary Control Loop has been shut down. To correct this error, enable Filter Watchdog \
            Errors on the Controller Configuration page of System Explorer. You can configure watchdog functionality by monitoring the Watchdog \
            Timer system channel using alarms and procedures.",
        -307733: "The version of the calibration file (HardwareCalibrationData.nivscal) is too old to mutate to the current version. Delete the file \
            and manually recreate the calibration settings.",
        -307734: "The scaling and calibration setting is invalid. The channel does not exist or is not scalable.",
        -307735: "A required resource is disabled in the current version of the VeriStand Engine. For example, a DAQ board is the master timing \
            device, but the current VeriStand Engine has disabled NI-DAQ. Remove the device or resource from the system definition file.",
        -307736: "Unable to share data for the channel. Either the source or destination target does not have reflective memory support.",
        -307737: "Unable to create dynamic data sharing between targets. Either the source or destination target does not have a data sharing \
            device.",
        -307738: "Unable to share data between two targets. There is not enough dynamic data sharing space.",
        -307739: "Data on reflective memory must have the correct byte alignment from memory address 0x0.",
        -307740: "Invalid data range. The reflective memory network requires a valid data range.",
        -307741: "VeriStand export data exceeds the allocated reflective memory address.",
        -307742: "The VeriStand Engine could not be loaded. Make sure that VeriStand and the required drivers, such as NI-DAQmx, are installed \
            correctly. Refer to the VeriStand readme.html for a list of required software and drivers.",
        -307743: "The VeriStand Engine failed to start. A configured start trigger or external timing source did not occur within the specified \
            timeout.",
        -307744: "An alarm failed to compile correctly and cannot be executed.",
        -307745: "You must specify a VISA device address for the reflective memory card.",
        -307746: "The maximum Windows target rate is 1 kHz. To achieve higher rates, use an NI-DAQ device or NI FPGA target.",
        -307747: "The system definition file contains two targets that are using the same IP address. Each target must have a unique IP address. \
            Only one target can be a Windows target.",
        -307748: "The VeriStand Engine rebooted while running the system definition file. You must reconnect to the execution host and possibly \
            redeploy the system definition file.",
        -307749: "A simulated DAQ device cannot be used as a Timed Loop timing source or as a chassis master hardware synchronization device. \
            In System Explorer, navigate to the Chassis Configuration page and choose a different DAQ device from the Chassis master hardware \
                synchronization device pull-down menu. On the Controller Configuration page, choose a different Primary Control Loop timing source. \
            Or, if all DAQ devices are simulated, disable hardware-timed single-point support for all of them or disable the DAQ device.",
        -307750: "Deserialization error. Failed to load macro file.",
        -307751: "The specified operation is not permitted while playing a macro.",
        -307752: "The specified operation is not permitted until a macro is loaded.",
        -307753: "The specified operation is not permitted unless running a macro.",
        -307754: "Serialization error. Unable to save macro.",
        -307755: "The specified operation is not permitted while recording a macro.",
        -307756: "Internal error: The DAQmx waveform producer received a command which was not declared as a publicly available.",
        -307780: "The specified feature is supported only if the VeriStand Gateway is running on the localhost machine.",
        -307781: "The channel group cannot be found in the specified log file.",
        -307782: "The channel cannot be found in the specified log file.",
        -307783: "The data structure contains a dependencies cycle.",
        -307784: "The STI file is not valid.",
        -307785: "No error provider exists to handle the error signals.",
        -307800: "A procedure failed to compile correctly and cannot be executed.",
        -307824: "The specified item is not a waveform.",
        -307825: "The specified item is not a channel.",
        -307826: "The specified item is not an alias for a channel.",
        -307827: "The specified item is not an expected type inside the system storage hierarchy.",
        -307828: "This dependency does not refer to a valid item. The item may have been deleted. Select a different dependency or re-add the \
            invalid item and click Update Dependencies.",
        -307829: "The specified node cannot be found.",
        -307830: "The channel dimension does not match the channel default value length.",
        -307831: "Unable to save file to the specified path.",
        -307832: "The depending file path is improperly formed or cannot be found.",
        -307850: "The target cannot be reached. Verify that the Ethernet cable is connected to the real-time (RT) target and that the RT target is \
            enabled and running.",
        -307851: "One or more system definition file dependency files differ from the originally imported version. This might cause unexpected \
            behavior or errors. Cancel the current operation and resolve any conflicts in System Explorer.",
        -307852: "The specified dependent file is contained within a LabVIEW library file (LLB), but the destination path on the target is not \
            contained in an LLB. Individual files cannot be copied out of an LLB. The destination path on the target must have an LLB as the parent \
                of the dependent file.",
        -307853: "The VeriStand Gateway was unable to establish a connection with the target. Confirm that the target is running and that the \
            VeriStand Engine successfully started. If you still cannot connect to the target, use MAX to reinstall the VeriStand Run-Time Engine \
                on the target. You may encounter this error if you attempt to connect to the target from a LabVIEW project, because a LabVIEW \
                project can update the start-up application for the target. To deploy a system definition to a target, the VeriStand Run-Time \
                Engine (VeriStand.rtexe) must be the start-up application.",
        -307860: "The specified trigger channel does not exist.",
        -307861: "The data logging configuration is invalid. One or more specified channels does not exist.",
        -307862: "The specified data logging configuration resulted in a buffer size that exceeds the maximum allowed size. Reduce the buffer size \
            by reducing the pre-trigger time, the logging rate, or the number of logged channels in the data logging configuration.",
        -307863: "The specified property value is not a valid data type for a TDMS property.",
        -307864: "The specified log file path is not valid. It might include invalid tags.",
        -307865: "The specified data logging session does not exist.",
        -307866: "An error occurred while logging data. Refer to the error description for more information.",
        -307867: "The specified data logging session name is already in use. Specify a unique data logging session name.",
        -307868: "The specified trigger condition contains syntax errors.",
        -307869: "Data was lost during logging. The log files may not contain every sample. The start and stop triggers may have also missed data \
            to evaluate.",
        -307870: "A compatible version of NI DIAdem is not installed. You must have NI DIAdem installed to load data in NI DIAdem.",
        -307871: "Cannot retrieve information for the specified log file. Ensure the session name and filename are correct.",
        -307872: "There was an error downloading one or more of the requested files. Please use the errors parameter for more detailed information.",
        -307881: "Cannot use legacy Channel Scaling and Calibration tool/API because this project contains calibration features from the new Channel \
            Calibration tool/API introduced in VeriStand 2012. This error occurs because the project contains a channel calibration file (.nivscf). \
            If you want to use the legacy Channel Scaling and Calibration tool, delete the .nivscf file under the Calibrations in Project Explorer \
            and redeploy. Otherwise, use the Channel Calibration Tool/API instead of the legacy Channel Scaling and Calibration tool/API.",
        -307882: "Cannot use Channel Calibration tool/API because this project does not contain a channel calibration file (.nivscf). If you want \
            to use the Channel Calibration tool/API, add a .nivscf file to the project under Calibrations in Project Explorer. Otherwise, you can \
            use the legacy Channel Scaling and Calibration Tool/API instead of the Channel Calibration tool/API.",
        -307883: "Cannot deploy project because the system definition file contains scales but the project does not contain a channel calibration \
            file (.nivscf). Delete the scales from the system definition file and redeploy.",
        -307887: "A polynomial scale mapped to a channel(s) does not have coefficients defined. Remove the mapping or update the scale to contain \
            coefficients, and then try to deploy the system definition again.",
        -307889: "A lookup table scale mapped to a channel(s) is empty. Remove the mapping or update the scale to contain pairs of pre-scaled values \
            and the corresponding values to which to scale them, and then try to deploy the system definition again.",
        -307891: "VeriStand only supports devices whose calibration password is the default value. Use NI MAX or the NI System Configuration API to \
            reset the calibration password on the device to the default value.",
        -307900: "The number of generator mappings exceeds the maximum allowed. Reduce the number of mapped channels or increase the maximum number \
            of mappings per generator using the Stimulus Configuration page.",
        -307901: "The number of compiled stimulus generator steps exceeds the maximum allowed. Reduce the number of steps in the stimulus generator \
            or increase the maximum number of steps per generator using the Stimulus Configuration page.",
        -307902: "The specified stimulus profile is empty. It contains no compiled steps.",
        -307903: "The number of data points exceeds the maximum auxiliary buffer size. Reduce the number of data points in the stimulus profile or \
            increase the maximum auxiliary buffer size in the Stimulus Configuration page of System Explorer.",
        -307904: "A stimulus profile failed to compile correctly. Verify that the stimulus profile links to valid channels.",
        -307905: "Timeout occurred while writing data to the auxiliary buffer.",
        -307906: "Timeout occurred while writing data to the analysis buffer.",
        -307907: "Multi-point data does not have the correct timing. The data must start at time 0 and increment at a multiple of Delta t value.",
        -307908: "The stimulus profile manager currently is reserved by a client.",
        -307909: "Unable to start stimulus profile generation. Stimulus profile file contains invalid profile steps or incorrect timing.",
        -307910: "Unable to start stimulus profile generation. CAN logging requires that the CAN Bus Monitor is running.",
        -307911: "Unable to start stimulus profile generation. One or more calibration files are not found.",
        -307912: "The number of data points exceeds the maximum analysis buffer size. Reduce the number of data points in the stimulus profile or \
            increase the maximum analysis buffer size using the Stimulus Configuration page of System Explorer.",
        -307913: "The number of stimulus generators exceeds the maximum allowed. Reduce the number of stimulus generators in the stimulus profile or \
            increase the maximum allowed using the Stimulus Configuration page of System Explorer.",
        -307914: "The specified CSV file does not contain a Timestamp column. The file you specify must have a Timestamp column that contains \
            values in milliseconds.",
        -307915: "The operation could not be completed. A stimulus profile is running.",
        -307916: "A stimulus profile generator contains a Set Variable step that attempts to set a variable on another target. A Set Variable step \
            only can set a variable on the same target as the generator containing the step.",
        -307917: "A stimulus profile generator contains channel mappings for channels on a different target than the target on which the generator \
            will execute. A generator can only map to channels on the target on which it will execute. Confirm that the generator is not mapped to \
                channels from different targets, or that the generator does not specify an execution target that is different than one of the \
            channel mappings.",
        -307925: "The specified node is not compatible with this operation.",
        -307926: "This node already exists in the system.",
        -307927: "Invalid argument. The node reference is not a valid channel.",
        -307928: "Found an existing FPGA target with the same RIO address configuration.",
        -307929: "The mapping definition is invalid. The source channel must be readable, the destination channel must be writable, and both \
            channels cannot be part of the stimulus generator.",
        -307930: "A node name cannot be an empty string.",
        -307931: "Model execution order group cannot be empty.",
        -307932: "The formula type must depend on variables.",
        -307933: "Attempted to write to a read-only property.",
        -307948: "Unable to establish a connection between the VeriStand Model Simulation Server and client. The VeriStand MDL client version is \
            incompatible with the currently loaded VeriStand Model Simulation Server.",
        -307949: "The selected model (.mdl) is invalid. Verify that the model can be compiled and run properly, that you have added an \
            NIVeriStandSignalProbe block to it, and that the stop time is set to inf.",
        -307950: "Unable to connect to the VeriStand Model Simulation Server.",
        -307951: "VeriStand requires that you compile a model (.mdl) before it can run on a real-time (RT) target.",
        -307970: "An inline custom device attempted to access invalid data in the VeriStand Engine. The inline custom device attempted to read or \
            write data using an invalid reference or a reference that did not have the read or write access required for that operation.",
        -307971: "A channel cannot have child items.",
        -307972: "Error provider received an electrical error that contains a signal it cannot handle. Verify the error provider is implemented \
            correctly and all errors contain the correct signals.",
        -307973: "Error provider received an electrical error with an unexpected number of signals. Verify the error provider is implemented \
            correctly and all errors contain the correct number of signals.",
        -307974: "Error provider received an unexpected configuration. Verify the error provider is implemented correctly and the errors can be \
            handled by the error provider.",
        -307980: "The specified stimulus profile session is locked. Unlock the stimulus profile session to control sequences in the session.",
        -307981: "The stimulus profile session does not contain a sequence with the specified name.",
        -307982: "The stimulus profile session is not deployed.",
        -307983: "The sequence containing the specified variable is currently running. You cannot probe a variable value while a sequence is \
            running.",
        -307984: "The stimulus profile session is already deployed.",
        -307985: "The sequence did not complete the timestep within the specified timeout. This could be due to a sequence that contains too much \
            processing or an infinite loop that does not yield. Evaluate the timing of your sequence or increase the timeout.",
        -307986: "The specified parameter assignment is not valid. The real-time sequence parameter does not exist.",
        -307987: "One or more real-time sequence parameters with a by-reference evaluation was not mapped to. Assign a value to all real-time \
            sequence parameters that have a by-reference evaluation type.",
        -307988: "The compiler failed because the specified real-time sequence contains one or more errors.",
        -307989: "The specified parameter assignment is not valid. The channel mapped to the parameter could not be found in the system.",
        -307990: "A system definition channel has been mapped to two or more real-time sequence parameters that are not the same data type. \
            A channel can only be mapped to multiple parameters if they share the same data type.",
        -307991: "A real-time sequence parameter assignment has an invalid data type. Match the data type of the value assigned to the parameter \
            to the parameter's data type.",
        -307992: "The specified operation cannot be completed. There is no project file currently open.",
        -307993: "The parameter dimension does not match the parameter default value length.",
        -307994: "The specified parameter cannot be found.",
        -307995: "VeriStand engine failed to retrieve data from the SLSC chassis status loop within the specified timeout. The System Definition \
            was undeployed.",
        -307996: "SLSC module not found in the specified slot. Check your SLSC hardware and make sure the custom device is inserted in the \
            correct slot.",
        -307997: "There are SLSC chassis added to the system definition that are not supported. Remove the SLSC chassis from the system definition.",
        -307998: "The switch load signal conditioning (SLSC) chassis name or IP address/hostname is empty. Provide a SLSC chassis name or IP \
            address/hostname.",
        # ---------- Networking Error Codes ----------
        -2147467263: "Not implemented.",
        -2147024809: "One or more arguments are invalid.",
        -1967390712: "Cannot resolve name to a network address.",
        -1967390711: "Network operation timed out.",
        -1967390703: "Could not resolve service to a port address.",
        -1967390702: "Timed out while trying to connect to peer.",
        -1967390686: "Computer name is not present in the URL.",
        -1967390685: "Computer name starts with a non-alphabetic character.",
        -1967390684: "Computer name contains an invalid character.",
        -1967390683: "Process name is not present in the URL.",
        -1967390682: "Process name contains an invalid character.",
        -1967390681: "Point or tag name is not present in the URL.",
        -1967390680: "Point or tag name contains an invalid character.",
        -1967390672: "Empty component in point or tag name.",
        -1967390668: "Thread initiation failed.",
        -1967390464: "URL does not start with two slashes.",
        -1967390463: "URL starts with more than two slashes.",
        -1967390462: "URL contains two consecutive delimiters.",
        -1967390460: "Unbalanced quotation marks in URL.",
        53: "Manager call not supported.",
        54: "The network address is ill-formed, Make sure the address is in a valid format, \
            For TCP/IP, the address can be either a machine name or an IP address in the form xxx,xxx,xxx,xxx, \
            If this error occurs when specifying a machine name, make sure the machine name is valid, Try to ping the machine name, \
            Check that you have a DNS server properly configured, If you are using the TCP Open Connection function, \
            ensure that the value of the remote port or service name is not 0.",
        55: "The network operation is in progress, If you receive this error while using the UDP Write function, \
            refer to the KnowledgeBase at ni.com for more information.",
        56: "The network operation exceeded the user-specified or system time limit.",
        57: "The network connection is busy.",
        58: "The network function is not supported by the system.",
        59: "The network is down, unreachable, or has been reset.",
        60: "The specified port or network address is currently in use, Select an available port or network address.",
        61: "The system could not allocate the necessary memory.",
        62: "The system caused the network connection to be aborted.",
        63: "The network connection was refused by the server, For TCP/IP, \
            make sure the server is running and listening on the port you want to use, Firewalls also can cause a server to refuse a connection, \
            For VI Server, make sure the VI Server is enabled on the VI Server page of the Options dialog box.",
        64: "The network connection is not yet established.",
        65: "The network connection is already established.",
        66: "The network connection was closed by the peer, If you are using the Open VI Reference function on a remote VI Server connection, \
            verify that the machine is allowed access by selecting Tools»Options»VI Server on the server side.",
        108: "Single cast connections cannot send to multicast addresses.",
        109: "Multicast connections cannot send to single cast addresses.",
        110: "Specified IP address is not in multicast address range.",
        111: "Cannot write to read-only multicast connection.",
        112: "Cannot read from write-only multicast connection.",
        113: "A message sent on a datagram socket was larger than the internal message buffer or some other network limit, \
            or the buffer used to receive a datagram was smaller than the datagram itself.",
        114: "Could not create TCP listener port because the port, service name, or net address conflict with a TCP listener that already exists.",
        119: "Illegal combination of Bluetooth discoverable and non-connectable modes, A discoverable Bluetooth system is connectable, \
            and non-connectable Bluetooth system is non-discoverable, The combination of discoverable and non-connectable is illegal.",
        120: "Error setting Bluetooth mode, Unknown internal error encountered while setting Bluetooth mode.",
        121: "Invalid GUID string, The GUID string has an invalid format, An example of the correct format is: B62C4E8D-62CC-404b-BBBF-BF3E3BBB1374.",
        126: "Could not query socket state, Either the socket is in a bad state (e.g. an error state, not connected, and so on) \
            and the requested information is not available, or the socket is unable to answer the query.",
        127: "The specified socket is not an IPv4 socket.",
        128: "Open connection limit exceeded, The application has exceeded the maximum number of open sockets allowed by the \
            “Max_Sockets” INI token.",
        1101: "Insufficient privileges to read, write, or create an item in the DataSocket Server, \
            Use the DataSocket Server Manager to configure these privileges.",
        1114: "This item is read-only, You must connect in read mode.",
        1115: "This item is write-only, You must connect in write mode.",
        1132: "Busy with another operation.",
        1133: "LabVIEW is busy connecting.",
        1134: "A different read operation is in progress.",
        1139: "A DataSocket item name cannot contain certain characters, This error occurs if the DataSocket item name contains \
            /, \\, ?, =, or &.",
        1140: "Exceeded maximum DataSocket item count, Use the DataSocket Server Manager to change the maximum number of dynamically created items \
            the data server will allow.",
        1141: "Exceeded maximum data item connection count, Use the DataSocket Server Manager to change the maximum number of connections the data \
            server will allow.",
        1142: "Multiple writers are not allowed, You can use the Shared Variable Properties dialog box to configure shared variables to accept \
            multiple writers.",
        1143: "Cannot load dataskt.llb.",
        1178: "LabVIEW reached end of file.",
        1179: "Access mode not supported for operation.",
        1180: "Pending operation in progress.",
        1181: "Protocol not recognized by LabVIEW, You must use a valid URL to establish a data connection.",
        1182: "Error parsing URL.",
        1183: "Synchronous operation not supported for connection, Append ?sync=true to URL to enable synchronous operations with the PSP protocol. \
             LabVIEW 8.0.1 and later support synchronous operations.",
        1184: "Path not found, FTP login incorrect, or no FTP write permission.",
        1185: "OPC item not found.",
        1337: "Not enough memory to complete this remote panel operation.",
        1338: "Network type not supported by remote panel protocol.",
        1339: "Remote panel connection is closed.",
        1340: "Invalid server IP address, Contact the server administrator to get the correct IP address or name of the computer to which you \
            want to connect.",
        1341: "Remote panel connection refused by the specified server, The server administrator must enable the LabVIEW Web Server, \
            Verify that the Server IP Address and Port you entered in the Connect to Remote Panel dialog box are correct.",
        1343: "Client does not have access to remote panel server.",
        1344: "The remote panel protocol version is incompatible, The client and server computers must be running the same version of LabVIEW, \
            If you are using a browser to view and control a remote front panel, you must use a version of the LabVIEW Run-Time Engine compatible \
            with the version of LabVIEW on the server computer, Also, be sure and contact the server administrator and have them make sure that \
            the HTML document specifies the correct version of the LabVIEW Run-Time Engine.",
        1345: "The LabVIEW client version is incompatible with the LabVIEW server version, Make sure you entered the IP address or computer name \
            of the server correctly.",
        1346: "Server does not support remote panels.",
        1347: "You cannot connect to the local LabVIEW application.",
        1348: "Remote panel server failed to send the requested VI, A memory or network problem occurred, This error might occur if you try to \
            connect to a large front panel, Try to connect to the front panel again, or request that the server administrator modify \
            the front panel so it uses less memory.",
        1349: "Client does not have access to specified VI, The server administrator must specify the VIs that clients can view or control.",
        1350: "Requested VI is broken and cannot be viewed or controlled.",
        1351: "Requested VI is not a standard VI, You cannot view or control a polymorphic VI, custom control, or global variable VI remotely.",
        1352: "Requested VI is not loaded into memory on the server computer.",
        1353: "Requested VI is not in run mode.",
        1354: "VI name required.",
        1355: "Fatal error occurred during operation, closing connection.",
        1356: "A remote panel connection does not exist for the specified VI.",
        1369: "Removing data connection from this control.",
        1383: "The data type of the data read does not match the data type of the type input.",
        1509: "The response from the NI Service Locator is not a valid HTTP response.",
        1510: "The requested service was not found as a registered service with the NI Service Locator, To correct this error, \
            check that the desired service name is correct, If the service name is correct, check that either the TCP Create Listener, \
            or the UDP Open functions are registering the service.",
        1511: "The requested service is a registered service with the NI Service Locator but it did not contain a port mapping, \
            The port number is missing or is registered incorrectly.",
        1567: "The control is not located in the same VI as the control reference, You can link a control reference only to controls or indicators \
            in the same VI.",
        1583: "LabVIEW Real-Time target is already connected to a host VI, You cannot initiate a remote panel connection to a Real-Time target \
            while also using a host VI to connect to the target, Choose only one method to connect to the target.",
        2308: "Found no configured network adapters.",
        363515: "The file exceeds the size limit on the server.",
        363516: "Client does not have access to the specified resource (access is forbidden).",
        363517: "Cannot find the remote file.",
        363518: "The remote file already exists.",
        363519: "Storage space limits on the server exceeded.",
        363520: "The server does not recognize the transfer encoding.",
        363521: "Number of redirects to other resources exceeded.",
        363522: "The network communication socket is not ready.",
        363523: "An unknown error occurred in the curl libraries.",
        363524: "The specified protocol is invalid or unsupported.",
        # ---------- VISA Error Codes ----------
        -1073807360: "Unknown system error (miscellaneous error).",
        -1073807346: "The given session or object reference is invalid.",
        -1073807345: "Specified type of lock cannot be obtained, or specified operation cannot be performed, because the resource is locked.",
        -1073807344: "Invalid expression specified for search.",
        -1073807343: "Insufficient location information or the device or resource is not present in the system.",
        -1073807342: "Invalid resource reference specified, Parsing error.",
        -1073807341: "Invalid access mode.",
        -1073807339: "Timeout expired before operation completed.",
        -1073807338: "The VISA driver failed to properly close the session or object reference, This might be due to an error freeing internal or \
            OS resources, a failed network connection, or a lower level driver or OS error.",
        -1073807333: "Specified degree is invalid.",
        -1073807332: "Specified job identifier is invalid.",
        -1073807331: "The specified attribute is not defined or supported by the referenced resource.",
        -1073807330: "The specified state of the attribute is not valid, or is not supported as defined by the resource.",
        -1073807329: "The specified attribute is read-only.",
        -1073807328: "The specified type of lock is not supported by this resource.",
        -1073807327: "The access key to the specified resource is invalid.",
        -1073807322: "Specified event type is not supported by the resource.",
        -1073807321: "Invalid mechanism specified.",
        -1073807320: "A handler was not installed.",
        -1073807319: "The given handler reference is invalid.",
        -1073807318: "Specified event context is invalid.",
        -1073807315: "The event queue for the specified type has overflowed, This is usually due to previous events not having been closed.",
        -1073807313: "You must be enabled for events of the specified type in order to receive them.",
        -1073807312: "User abort occurred during transfer.",
        -1073807308: "Violation of raw write protocol occurred during transfer.",
        -1073807307: "Violation of raw read protocol occurred during transfer.",
        -1073807306: "Device reported an output protocol error during transfer.",
        -1073807305: "Device reported an input protocol error during transfer.",
        -1073807304: "Bus error occurred during transfer.",
        -1073807303: "Unable to queue the asynchronous operation because there is already an operation in progress.",
        -1073807302: "Unable to start operation because setup is invalid (due to attributes being set to an inconsistent state).",
        -1073807301: "Unable to queue the asynchronous operation (usually due to the I/O completion event not being enabled or insufficient space \
            in the session's queue).",
        -1073807300: "Insufficient system resources to perform necessary memory allocation.",
        -1073807299: "Invalid buffer mask specified.",
        -1073807298: "Could not perform operation because of I/O error.",
        -1073807297: "A format specifier in the format string is invalid.",
        -1073807295: "A format specifier in the format string is not supported.",
        -1073807294: "The specified trigger line is currently in use.",
        -1073807290: "The specified mode is not supported by this VISA implementation.",
        -1073807286: "Service request has not been received for the session.",
        -1073807282: "Invalid address space specified.",
        -1073807279: "Invalid offset specified.",
        -1073807278: "Invalid access width specified.",
        -1073807276: "Specified offset is not accessible from this hardware.",
        -1073807275: "Cannot support source and destination widths that are different.",
        -1073807273: "The specified session is not currently mapped.",
        -1073807271: "A previous response is still pending, causing a multiple query error.",
        -1073807265: "No listeners condition is detected (both NRFD and NDAC are de-asserted).",
        -1073807264: "The interface associated with this session is not currently the controller in charge.",
        -1073807263: "The interface associated with this session is not the system controller.",
        -1073807257: "The given session or object reference does not support this operation.",
        -1073807256: "An interrupt is still pending from a previous call.",
        -1073807254: "A parity error occurred during transfer.",
        -1073807253: "A framing error occurred during transfer, If you receive this error while using a VISA read, refer to the KnowledgeBase at \
            ni.com for more information.",
        -1073807252: "An overrun error occurred during transfer, A character was not read from the hardware before the next character arrived.",
        -1073807250: "The path from trigSrc to trigDest is not currently mapped.",
        -1073807248: "The specified offset is not properly aligned for the access width of the operation.",
        -1073807247: "A specified user buffer is not valid or cannot be accessed for the required size.",
        -1073807246: "The resource is valid, but VISA cannot currently access it.",
        -1073807242: "Specified width is not supported by this hardware.",
        -1073807240: "The value of some parameter (which parameter is not known) is invalid.",
        -1073807239: "The protocol specified is invalid.",
        -1073807237: "Invalid size of window specified.",
        -1073807232: "The specified session currently contains a mapped window.",
        -1073807231: "The given operation is not implemented.",
        -1073807229: "Invalid length specified.",
        -1073807215: "Invalid mode specified.",
        -1073807204: "The current session did not have a lock on the resource.",
        -1073807202: "VISA or a code library required by VISA could not be located or loaded, This is usually due to a required driver not being \
            installed on the system.",
        -1073807201: "The interface cannot generate an interrupt on the requested level or with the requested statusID value.",
        -1073807200: "The value specified by the line parameter is invalid.",
        -1073807199: "An error occurred while trying to open the specified file, Possible reasons include an invalid path or lack of access rights.",
        -1073807198: "An error occurred while performing I/O on the specified file.",
        -1073807197: "One of the specified lines, trigSrc or trigDest, is not supported by this VISA implementation, or the combination of lines is \
            not a valid mapping.",
        -1073807196: "The specified mechanism is not supported for the given event type.",
        -1073807195: "The interface type is valid, but the specified interface number is not configured.",
        -1073807194: "The connection for the given session has been lost.",
        -1073807193: "The remote machine does not exist or is not accepting any connections, If the NI-VISA server is installed and running on the \
            remote machine, it might have an incompatible version or might be listening on a different port.",
        -1073807192: "Access to the resource or remote machine is denied, This is due to lack of sufficient privileges for the current \
            user or machine.",
        0: "Operation completed successfully.",
        1073676290: "Specified event is already enabled for at least one of the specified mechanisms.",
        1073676291: "Specified event is already disabled for at least one of the specified mechanisms.",
        1073676292: "Operation completed successfully, but queue was already empty.",
        1073676293: "The specified termination character was read.",
        1073676294: "The number of bytes transferred is equal to the requested input count, More data might be available.",
        1073676300: "VISA received more event information of the specified type than the configured queue size could hold.",
        1073676407: "The specified configuration either does not exist or could not be loaded, VISA-specified defaults will be used.",
        1073676413: "Session opened successfully, but the device at the specified address is not responding.",
        1073676414: "The path from trigSrc to trigDest is already mapped.",
        1073676416: "Wait terminated successfully on receipt of an event notification, There is at least one more event occurrence of the type \
            specified by inEventType available for this session.",
        1073676418: "The specified object reference is uninitialized.",
        1073676420: "Although the specified state of the attribute is valid, it is not supported by this resource implementation.",
        1073676421: "The status code passed to the operation could not be interpreted.",
        1073676424: "The specified I/O buffer is not supported.",
        1073676440: "Event handled successfully, Do not invoke any other handlers on this session for this event.",
        1073676441: "Operation completed successfully, and this session has nested shared locks.",
        1073676442: "Operation completed successfully, and this session has nested exclusive locks.",
        1073676443: "Operation completed successfully, but the operation was actually synchronous rather than asynchronous.",
        1073676457: "The operation succeeded, but a lower level driver did not implement the extended functionality.",
        # ---------- NI-DAQmx Driver Error Codes ----------
                -209886: "Setting the specified property does not allow multiple task configuration of the sample clock.",
        -209885: "A property is set to a value that is not supported by multiple task configuration of the sample clock.",
        -209884: "A common sample rate for all specified tasks could not be found. If your application contains both fast- and \
            slow-sampled devices, consider enabling allow repeated samples.",
        -209883: "A common sample rate for all specified tasks could not be found.",
        -209882: "The task contains multiple devices or chassis. Multiple task configuration only supports tasks with a single \
            device or chassis.",
        -209881: "The task does not support configuring its sample clock rate via multiple task configuration.",
        -209880: "Specified operation cannot be performed because the debug session's target task may have a registered timing \
            source. The debug session does not support debugging tasks with registered timing sources.",
        -209879: "Specified operation cannot be performed because the debug session's target task has logging enabled. The debug \
            session does not support debugging tasks with logging enabled. Turn off logging for the target task and try again.",
        -209878: "Specified operation cannot be performed because the debug session's target task has registered events. The debug \
            session does not support debugging tasks with registered events. Unregister the events for the target task and try again.",
        -209877: "Specified operation cannot be performed because the debug session's target task is invalid or does not exist.",
        -209876: "Requested function is not supported by the device.",
        -209875: "Multiple tasks were found that match the debug session target settings.The debug session does not support debugging \
            more than one task at a time. Change the target settings to match a specific task and try again.",
        -209874: "A task was not found that matches the debug session target settings.",
        -209873: "Specified operation cannot be performed because it is not supported in a debug session.",
        -209872: "Specified operation cannot be performed because it is not permitted in monitor mode.Make sure the debug session \
            is in control mode before requesting this operation.",
        -209871: "Attempt to get property failed because your device contains multiple banks, and the property has different values \
            for different banks. Get this property one bank at a time by changing the active device name to specify each individual bank.",
        -209870: "Timing source creation has failed because another timing source has already been registered for this task.",
        -209869: "Requested value is not a supported value for this hardware revision. However, it may be supported on later revisions. \
            Visit ni.com/info, and enter the info code fielddaqfilter for additional information.",
        -209868: "To set the sensor power supply voltage level, you must specify the sensor power configuration.",
        -209867: "To enable the sensor power supply, you must specify the sensor power voltage level.",
        -209866: "The hardware cannot acquire data from the configured scanlist. Please enter the info code that follows at ni.com/info \
            for additional information.",
        -209865: "All internal routes have been reserved. If you are using time-based synchronization, please refer to info code \
            TimeTriggerLimits at ni.com/info for additional information.",
        -209864: "The requested Reset Delay cannot be set based on your task configuration. If you are using C Series modules \
            from different chassis in the same task, it is possible that the sample rate and module types cannot be synchronized effectively.",
        -209863: "Exceeded total number of time triggers available. Try disabling time triggers that are enabled on one or more \
            DAQ tasks in your system. If no more time triggers can be disabled, try disabling other features that require internal routing \
            resources. Please refer to info code TimeTriggerLimits at ni.com/info for more information.",
        -209862: "Exceeded total number of timestamps available. Try disabling timestamps that are user-defined or enabled by \
            default on one or more DAQ tasks in your system.",
        -209861: "One or more devices in your task are not running the IEEE 802.1AS or IEEE 1588 synchronization protocol. Use \
            the NI-Sync LabVIEW API to enable 802.1AS or 1588. Refer to the NI-Sync help or LabVIEW examples for more information.",
        -209860: "One or more devices could not be added to your task because they have existing coherency requirements that conflict \
            with the new requirements of your current task. Stop the task(s) that use devices in this task and try running it again.",
        -209859: "The devices in your task must be synchronized to one another using the IEEE 802.1AS or IEEE 1588 synchronization \
            protocol. Connect the devices, either directly or via an 802.1AS or 1588-capable switch.",
        -209858: "FieldDAQ bank name specified is invalid. FieldDAQ bank names are of the form <FieldDAQ name>-Bank<Bank number>. \
            For example, FieldDAQ1-Bank1.",
        -209857: "Task contains physical channels on one or more devices that do not support the DAQmx hardware-timed single-point \
            sample mode.",
        -209856: "Bank type in the source storage does not match the bank type in the destination.",
        -209855: "FieldDAQ device does not support the specified number of banks. The bank number specified may be too large. \
            Change the bank number to be a valid bank number.",
        -209854: "The simulated FieldDAQ bank is not supported on this simulated FieldDAQ.",
        -209853: "The IsSimulated flags for FieldDAQ and banks must match. Change the IsSimulated flags in the import file so \
            that they match.",
        -209852: "The specified device is no longer supported within the NI-DAQmx API.",
        -209851: "The requested Sample Timing Engine does not support Use Only Onboard Memory.",
        -209850: "Task name specified conflicts with an existing task name in another project.",
        -209849: "A time Arm Start Trigger and time Start Trigger are configured. Ensure the Arm Start Trigger comes first.",
        -209848: "The time trigger cannot be configured because your device has lost synchronization lock to the grand master.",
        -209847: "Specified value is not supported for this property. Supported values are -1 (infinite window) or non-negative \
            numbers up to 15.768000e9.",
        -209846: "The property cannot be queried before or during a data acquisition. You must explicitly commit, run, and stop \
            your task before attempting to read this property.",
        -209845: "The Sample Clock Time base property you have requested is not supported by this task because it contains a reference \
            clock device. Use the Reference Clock properties instead.",
        -209844: "Attempted to query a timestamp before it is available. Use the DAQmx Wait for Valid Timestamp VI/function to \
            wait until the desired timestamp is available.",
        -209843: "Time operations are not supported by this device or task type.",
        -209842: "Timestamp requested is not enabled for this task.",
        -209841: "A time sync pulse and time start trigger are configured. Ensure the sync pulse comes first and the difference \
            between them is larger than the task sync time.",
        -209840: "The configured time trigger is in the past.",
        -209839: "A time trigger configured is too far in the future. Use I/O Device Timescale instead of Host Timescale, configure \
            the trigger at a point in the future closer to the trigger time, or schedule the trigger closer in time to the current Host Timescale \
            time.",
        -209838: "Synchronization lock was lost during operation. If the occasional loss of synchronization is acceptable, change \
            the Synchronization Unlock Behavior property to ignore sync loss. Otherwise, go to ni.com for more information about sync loss \
            management.",
        -209837: "The timescales for time start trigger and time sync pulse must be the same.",
        -209836: "The devices in your task cannot be synchronized. This may be because there are no available synchronization \
            mechanisms between the devices. Some synchronization paths are not available in interactive tools like the DAQ Assistant. To determine \
            whether synchronization between these devices is possible, try deploying and executing your task in your application environment.",
        -209835: "The specified property requires all associated channels to use the same range as specified by the Maximum and \
            Minimum properties. Try setting the same Maximum and Minimum Values on each channel or change the conflicting property.",
        -209834: "Sample rate exceeds the maximum sample rate for the number of channels and property values specified. Reduce \
            the sample rate or number of channels. Changing the specified property values may also increase the maximum possible sample rate.",
        -209833: "DAQmx Wait for Valid Timestamp is not supported by one or more devices in this task.",
        -209832: "Specified Trigger Window has elapsed without a trigger being detected.",
        -209831: "Not all devices in the task support the specified Trigger configuration.",
        -209830: "Not all devices in the task support the specified Data Transfer Mechanism.",
        -209829: "Onboard device memory overflow. Because of system and/or bus-bandwidth limitations, the driver could not read \
            data from the device fast enough to keep up with the data transfer throughput. Reduce the maximum data transfer rate of the device. \
            You can also increase bandwidth by reducing the number of programs your computer is executing.",
        -209828: "All channels used for the analog trigger source must be on the same device. Remove trigger configurations from \
            the task until all of the sources are channels from the same device.",
        -209827: "The device does not support using more than one trigger type at a time with the specified task configuration. \
            Configure the device to use only one trigger type or to use a configuration that supports using multiple trigger types.",
        -209826: "Multiple source triggering requires the same number of values for all user-specified trigger configurations.",
        -209825: "The specified AO DAC range must be consistent with all reserved tasks on this device. Ensure that all reserved \
            tasks on this device use the same value for the AO.DAC.Ref.Val channel attribute/property.",
        -209824: "The waveforms passed to DAQmx Write claim to be sampled at inconsistent rates. Check to make sure the data is \
            sampled at the correct rate and either re-sample the data or correct the dt element of the waveforms.",
        -209823: "The function called is no longer supported by DAQmx.",
        -209822: "Negative duration values other than -1 are not supported. -1 indicates to read all samples.",
        -209821: "No samples were acquired within the specified duration. Increase the duration or sample rate so that at least \
            one sample is acquired.",
        -209820: "The specified duration is too long. Specify a shorter duration.",
        -209819: "Duration-based reads are supported only in sample clock timing mode.",
        -209818: "The selected LED state is invalid.",
        -209817: "A device in your watchdog task does not support different output state types. Set all channels to the same output \
            state type or remove the channels from the task.",
        -209816: "Self-test of the device has failed because the measured power supply voltage is outside of tolerance. Please \
            contact National Instruments technical support.",
        -209815: "DAQmx Write does not support multiple samples in Hardware-Timed Single-Point tasks. Specify a single sample.",
        -209814: "You cannot use onboard regeneration for a task with this many channels. Reduce the number of channels in the \
            task, use fewer modules with more the 16-bits of precision, or set the AO.UseOnlyOnBrdMem attribute/property to false.",
        -209813: "To create watchdog task on this device, you must specify expiration states for all lines. Specify states for \
            the missing channels.",
        -209812: "The selected shunt source option for the shunt calibration is not valid for this device.",
        -209811: "The selected shunt select option for the shunt calibration is not valid for this device.",
        -209810: "This device does not support shunt calibration for the requested configuration of shunt select and shunt source. \
            Refer to the shunt calibration documentation for your application development environment for more information.",
        -209809: "The selected channels do not support buffered operations when alone in a task. Add an additional channel which \
            supports buffered operations to the task or reconfigure the task to use On-Demand timing.",
        -209808: "The specified feature is not supported on the attached accessory. Refer to your accessory documentation for \
            accessories that support the requested feature.",
        -209807: "The threshold voltage value must be consistent when using the same terminal with RSE terminal configuration \
            as a source for multiple inputs. For example, do not set 2.0 V on PFI0 for one input, and 3.0 V on PFI0 for another input.",
        -209806: "NI-DAQmx is not installed on the target system, is incompatible, or the installation is corrupt. Install or \
            repair the driver software.",
        -209804: "Your device has lost synchronization lock to the grand master. Any timestamp values for the task may be invalid, \
            but the task was not stopped because the SyncUnlockBehavior property is set to Ignore Lost Sync Lock. To query the status of \
            your device, read either the ReadSyncUnlockedChansExist or WriteSyncUnlockedChansExist property.",
        -209803: "The Onboard Memory Empty value of the AO.DataXferReqCond attribute/property is not supported on this device. \
            The value of this attribute/property is coerced to a different value after Output.BufSize is set. You can emulate the behavior \
            of the Onboard Memory Empty value by setting Output.BufSize to a lower value. The minimum value for this attribute/property is 2.",
        -209802: "DAQmx Wait for Next Sample Clock detected one or more missed sample clocks since the last call to Wait for Next \
            Sample Clock which indicates that your program is not keeping up with the sample clock. To remove this warning, slow down the sample \
            clock, or else change your application so that it can keep up with the sample clock.",
        -209801: "DAQmx Write did not complete before the arrival of the next sample clock which indicates that your program is \
            not keeping up with the hardware clock. To remove this warning, slow down the hardware clock, or else change your application so \
            that it can keep up with the hardware clock.",
        -209800: "DAQmx Read did not complete before the arrival of the next sample clock or change detection event, which indicates \
            that your program is not keeping up with the hardware clock or the external change event. For tasks using sample clock timing, \
            slow down the hardware clock or else change your application so that it can keep up with the hardware clock. For tasks using change \
            detection timing, decrease the frequency of your event or else change your application so that it can keep up with the change event.",
        -201510: "The digital filtering properties must be consistent when using the same terminal as a source for multiple inputs. \
            For example, digital filtering can either be enabled with the same minimum pulse width configuration whenever PFI0 is used, or \
            disabled for all cases.",
        -201509: "The logic level behavior must be consistent when using the same terminal as a source for multiple inputs. For \
            example, do not enable the pull-up on PFI0 for one input, and set it to none on PFI0 for another input.",
        -201508: "The terminal configuration must be consistent when using the same terminal as a source for multiple inputs. \
            For example, do not set PFI0 to differential for one input, and PFI0 to RSE for another input.",
        -201507: "A fatal hardware clocking error has occurred. The device is unusable until you restart it. If the problem persists, \
            please contact National Instruments Technical Support.",
        -201506: "A hardware clocking error has occurred. Try the operation again. If the problem persists, please contact National \
            Instruments Technical Support.",
        -201505: "The chassis requires at least one DAQ device directly cabled to it. Edit the chassis and assign a device.",
        -201504: "A fatal hardware clocking error has occurred. The device is unusable until you restart it. If you are using \
            an external reference clock, make sure it is connected and within the jitter and voltage level specifications. Also, verify that \
            the rate of the external clock matches the specified clock rate. If you are generating your clock internally, please contact National \
            Instruments Technical Support.",
        -201503: "The AI timing engine cannot be used for counter tasks. You can select a different timing engine or let the driver \
            automatically select one.",
        -200078: "Using USB DAQ devices on Windows XP might result in corrupt data or other errors. Visit ni.com/info and enter \
            info code WindowsXPUSBHotfix to obtain a patch.",
        -200077: "The NI PXIe-5611 is not configured properly and needs to be associated with an AWG and LO. Right-click on the \
            NI PXIe-5611 and select 'Configure' to associate the AWG and LO. For more information, refer to NI-RFSG documentation, RF Signal \
            Generators Getting Started Guide.",
        -200076: "The NI PXIe-5611 is not configured and needs to be associated with an AWG and LO. Right-click on the NI PXIe-5611 \
            and select 'Configure' to associate the AWG and LO. For more information, refer to NI-RFSG documentation, RF Signal Generators \
            Getting Started Guide.",
        -200075: "The NI PXI-5610 is not configured properly and needs to be associated with an AWG. Right-click on the NI PXI-5610 \
            and select 'Configure' to associate the AWG. For more information, refer to NI-RFSG documentation, RF Signal Generators Getting \
            Started Guide.",
        -200074: "The NI PXI-5610 is not configured and needs to be associated with an AWG. Right-click on the NI PXI-5610 and \
            select 'Configure' to associate the AWG. For more information, refer to NI-RFSG documentation, RF Signal Generators Getting Started \
            Guide.",
        -200073: "The NI PXI-5665 is not configured properly. Right-click on the NI PXIe-5606 and select 'Configure' to associate \
            the digitizer and LO.",
        -200072: "The NI PXIe-5606 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5606 and select 'Configure' \
            to associate the digitizer and LO.",
        -200071: "The NI PXIe-5667 (7 GHz) is not configured properly. Right-click on the NI PXIe-5605 and select 'Configure' \
            to associate the digitizer and LO. You can also associate the NI PXIe-5605 with additional IF conditioning and RF conditioning \
            modules.",
        -200070: "The NI PXI-5665 (14 GHz) is not configured properly. Right-click on the NI PXIe-5605 and select 'Configure' \
            to associate the digitizer and LO. You can also associate the NI PXIe-5605 with additional IF conditioning and RF conditioning \
            modules.",
        -200069: "The NI PXIe-5605 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5605 and select 'Configure' \
            to associate the digitizer and LO. You can also associate the NI PXIe-5605 with additional IF conditioning and RF conditioning \
            modules.",
        -200068: "The NI PXIe-5667 (3.6 GHz) is not configured properly. Right-click on the NI PXIe-5603 and select 'Configure' \
            to associate the digitizer and LO. You can also associate the NI PXIe-5603 with additional IF conditioning and RF conditioning \
            modules.",
        -200067: "The NI PXIe-5665 (3.6 GHz) is not configured properly. Right-click on the NI PXIe-5603 and select 'Configure' \
            to associate the digitizer and LO. You can also associate the NI PXIe-5603 with additional IF conditioning and RF conditioning \
            modules.",
        -200066: "The NI PXIe-5603 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5603 and select 'Configure' \
            to associate the digitizer and LO. You can also associate the NI PXIe-5603 with additional IF conditioning and RF conditioning \
            modules.",
        -200065: "The NI PXIe-5663E is not configured properly. Right-click on the NI PXIe-5601 and select 'Configure' to associate \
            the digitizer and LO.",
        -200064: "The NI PXIe-5663 is not configured properly. Right-click on the NI PXIe-5601 and select 'Configure' to associate \
            the digitizer and LO.",
        -200063: "The NI PXIe-5601 is not associated with a digitizer or an LO. Right-click on the NI PXIe-5601 and select 'Configure' \
            to associate the digitizer and LO.",
        -200062: "The NI PXI-5661 is not configured properly. Right-click on the NI PXI-5600 and select 'Configure' to associate \
            the digitizer.",
        -200061: "The NI PXI-5600 is not associated with a digitizer. Right-click on the NI PXI-5600 and select 'Configure' to \
            associate the digitizer.",
        -200060: "The same data is being read repetitively.",
        -200059: "The selected ports are not connected, so there is nothing to disconnect.",
        -200058: "The connection count stored on the EEPROM is invalid. Write a value to Accessory Connection Count to fix the \
            problem. Contact National Instruments if the problem persists.",
        -200057: "The network device already exists in the system.",
        -200056: "The connection count of the attached accessory has exceeded the recommended limit. Contact National Instruments \
            if the accessory appears to be functioning improperly.",
        -200055: "Power-up state section of the device EEPROM appears to be corrupt. Reconfigure the digital power-up states and \
            perform a self-calibration.",
        -200054: "EEPROM of the device appears to be corrupt. Contact National Instruments if the device appears to be functioning \
            improperly.",
        -200053: "Sample Rate specified may exceed device capabilities for some devices in the task. Specify a slower sample rate, \
            decrease the number of channels, or use a separate task for some of the devices in the task.",
        -200052: "Buffer size specified is not evenly divisible by 8 times the sector size. For optimal performance, use a buffer \
            size that is a multiple of 8 times the sector size. Refer to the NI-DAQmx Help for more information.",
        -200051: "Input voltage limits exceeded. Protection circuity disabled the inputs, however proper voltage levels are now \
            present, and the error state has been cleared.",
        -200050: "Output generation aborted by the reverse power protection circuitry of the device. Either the output signal \
            exceeded the output power limit, or power was driven back into the output of the device by an external source. Error state has \
            been cleared.",
        -200049: "Calibration changed the gain calibration constants only and not the offset calibration constants because the \
            necessary offset calibration data was not available. This device needs a reference signal of 0.0 Volts at gains of 1, 15, 20, and \
            310 in order to perform an offset calibration.",
        -200048: "Requested property value exceeds device specification limits. Device performance is not guaranteed. Use values \
            within device specifications, or set the Allow Out of Specification User Settings property to true.",
        -200047: "Self-calibration section of the EEPROM on the device appears to be corrupt. Perform a self-calibration on the \
            device.",
        -200046: "External calibration section of the EEPROM on the device appears to be corrupt. Perform an external calibration \
            on the device.",
        -200045: "EEPROM of the device appears to be corrupt. Contact National Instruments if the device appears to be functioning \
            improperly.",
        -200044: "Invalid enumeration value was encountered during export. The exported file will require modification in order \
            to successfully import.",
        -200043: "Date specified by the Channel Calibration Expiration Date property has expired. The channel calibration is applied \
            in spite of this because the Apply Calibration if Expired property was set to true. To eliminate this warning, update the channel \
            calibration, including the Expiration Date.",
        -200042: "Calibration constants stored in the EEPROM produced an invalid value for one or more analog output channels. \
            The device will continue to function, but the accuracy of the generated signals may be compromised. An incorrect calibration might \
            have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, \
            perform a self-calibration, or contact National Instruments Technical Support.",
        -200041: "Calibration constants stored in EEPROM produced an invalid value for one or more analog input channels. The \
            device will continue to function, but the accuracy of the measurements may be compromised. An incorrect calibration might have \
            been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, \
            perform a self-calibration, or contact National Instruments Technical Support.",
        -200040: "Sample clock rate specified is so high that it violates the settling time requirements for the generation. Reduce \
            the sample clock rate, or the accuracy of the generated signal might be compromised.",
        -200039: "Data may be invalid because the settling time of the enabled filter exceeds the period between two conversions \
            on the analog-to-digital converter (ADC) for a task with more than one channel. Disable the filter by setting AI Lowpass Enable \
            to false, acquire data from only one channel in the task, or increase the time between two ADC conversions by reducing \
            the Sample Clock Rate, the Sample Clock Delay, and/or the number of channels in the task.",
        -200038: "Data may be invalid because the settling time of the enabled filter exceeds the period between two conversions \
            on the analog-to-digital converter (ADC) for a task with more than one channel. Disable the filter by setting AI Lowpass Enable \
            to false, increase the time between two ADC conversions by reducing the AI Convert Rate, or acquire data from only one channel \
            in the task.",
        -200037: "Settings requested through a previous DAQmx Write were overwritten before they could be applied. This occurred \
            either because DAQmx Write was invoked more than once between two consecutive sample clocks or because the frequency of the generated \
            pulse train is lower than the sample clock rate (it takes more than one sample clock period to generate one period of the pulse train). \
            The settings requested by the most recent DAQmx Write will be applied on the next sample clock. To avoid this warning, \
            make sure that DAQmx Write is invoked exactly once between two consecutive sample clocks and that the frequency of the generated \
            pulse train is higher than the sample clock rate.",
        -200036: "Requested Sample Clock Rate is higher than the maximum supported per device specifications. Reduce the Sample \
            Clock Rate or use a device which supports the requested Sample Clock Rate.",
        -200035: "Clock rate specified is less than the minimum conversion rate of the ADC. Your data may be invalid.",
        -200034: "A sensor on the device detected a temperature approaching the device's maximum recommended operating temperature. \
            The device will shut down if its temperature exceeds the maximum recommended operating temperature. To avoid the shutdown, ensure \
            the device temperature does not get above the maximum recommended operating temperature. You can often prevent the shutdown by \
            periodically cleaning fan filters. Refer to user documentation for more information.",
        -200033: "DAQmx Write was invoked more than once between two consecutive sample clocks. Only the last DAQmx Write took \
            effect. To eliminate this warning, invoke DAQmx Write only once between two consecutive sample clocks.",
        -200032: "Output gain was coerced to the nearest acceptable value, because the original value was too high given the RF \
            Frequency.",
        -200031: "Output gain was coerced to the nearest acceptable value, because the original value was too low given the RF \
            Frequency.",
        -200030: "A sensor on the device detected a temperature approaching the device's maximum recommended operating temperature. \
            The device will shut down if its temperature exceeds the maximum recommended operating temperature. To avoid the shutdown, ensure \
            the device temperature does not get above the maximum recommended operating temperature. You can often prevent the shutdown by \
            periodically cleaning fan filters. Refer to user documentation for more information.",
        -200029: "RIS acquisition was completed, but some of the bins were not filled with a sufficient number of samples to perform \
            the requested RIS averaging. Data for those bins was computed from the available samples. Consider increasing the timeout for the \
            operation. Refer to documentation for details about RIS acquisitions.",
        -200028: "Some of the last samples acquired during the finite DMA acquisition are possibly invalid due to counter limitations. \
            Get the Number of Possibly Invalid Samples property to see how many samples might be invalid. Use continuous sample mode for DMA \
            acquisitions with this type of counter.",
        -200027: "Sample clock rate has been coerced to the minimum supported value because the specified value was too low. For \
            lower sample clock rates, use an external sample clock or an external sample clock timebase.",
        -200026: "Requested string could not fit into the given buffer. Only the first part of the string was copied into the \
            buffer. To allow for the terminating NULL character, the number of characters copied into the buffer is equal to the size of the \
            buffer minus one. Call the function twice. Call the function initially to determine the string size. Use the second function call \
            to get the full string value. In the first function call, pass NULL for the buffer and zero for the buffer size. \
            The positive return value of the function is the string size (which includes the terminating NULL). Use this value to allocate \
            a buffer of sufficient size, then use this buffer in the second function call.",
        -200025: "User-defined information to be stored in the EEPROM is too long. Only the leading portion was saved. Refer to \
            documentation for information about the maximum length allowed for user-defined information.",
        -200024: "One of more of the properties saved with a later version of NI-DAQ are not supported by the installed version \
            of NI-DAQ and are ignored. Upgrade the installed version of NI-DAQ to a version compatible with the version used when saving the \
            properties to take advantage of all the saved properties.",
        -200022: "Attempted writing a sample value that was too small. The driver automatically coerced it to the minimum supported \
            value.",
        -200021: "Attempted writing a sample value that was too large. The driver automatically coerced it to the maximum supported \
            value.",
        -200020: "Requested number of pretrigger samples per channel could not be configured, so it was coerced to the minimum \
            supported value.",
        -200019: "Requested read offset could not be configured, so the offset was coerced to the minimum supported value.",
        -200018: "Specified convert rate is too low to be generated using the onboard AI convert clock with the given timebase. \
            The rate was coerced to the slowest possible convert rate. For slower rates, you must use an external convert clock or an external \
            convert clock timebase.",
        -200017: "Specified sample rate is lower than the lowest rate that can be generated using the onboard clock. The rate \
            was coerced to the slowest possible sample rate. For slower rates, use an external sample clock or an external sample clock timebase.",
        -200016: "An attempt has been made to query the date/time of the last self calibration of a device that has never been \
            self-calibrated using the NI-DAQmx API, so the date/time is invalid. Self-calibrate the board using the NI-DAQmx API.",
        -200015: "While writing to the buffer during a regeneration, the actual data generated might have alternated between old \
            data and new data. That is, while the driver was replacing the old pattern in the buffer with the new pattern, the device might \
            have generated a portion of new data, then a portion of old data, and then a portion of new data again. Reduce the sample rate, \
            use a larger buffer, or refer to documentation about DAQmx Write for information about other ways to avoid this warning.",
        -200014: "The combination of sample rate and buffer size settings could result in a large number of interrupts, causing \
            the system to hang. Decrease your sample rate, or increase your buffer size. For acquisitions without a reference trigger, you \
            can disallow buffer overwrites. For generations, you can disable the regeneration of old samples.",
        -200013: "User-defined information string entered exceeds the maximum allowable string length. The string will be truncated \
            to its maximum allowable length.",
        -200012: "Clock rate specified exceeds the maximum conversion rate of the ADC. ADC overrun errors are likely.",
        -200011: "Clock rate specified is so high that it violates the settling time requirements for the acquisition. Reduce \
            the clock rate, or the accuracy of the measurement might be compromised.",
        -200010: "Finite acquisition or generation has been stopped before the requested number of samples were acquired or generated.",
        -200009: "Counter 1 DMA acquisition started while starting, committing, stopping, or uncommitting an analog output (AO) \
            task. This could cause the counter acquisition to stop. If possible, use counter 0 instead of counter 1. Otherwise, start/commit \
            the AO task before starting the counter 1 DMA acquisition, and stop/uncommit the AO task after stopping the counter 1 DMA acquisition.",
        -200008: "Counter 0 DMA acquisition started while starting, committing, stopping, or uncommitting an analog input (AI) \
            task. This could cause the counter acquisition to stop. If possible, use counter 1 instead of counter 0. Otherwise, start/commit \
            the AI task before starting the counter 0 DMA acquisition, and stop/uncommit the AI task after stopping the counter 0 DMA acquisition.",
        -200007: "PLL was unlocked. Your data might be invalid.",
        -200005: "ADC for one or more channels was overloaded. Your data might be invalid.",
        -200004: "Input termination resistor for one or more channels was overloaded. Your data might be invalid.",
        -200003: "Absolute timestamp counter has rolled over.",
        -200003: "Channel cannot be used more than once inside a list of channels. If you need to use the same physical channel \
            more than once inside your list of channels, refer to that physical channel under different names.",
        -200004: "Data requested has been overwritten in the device memory.",
        -200005: "Data requested has not been acquired yet.",
        -200006: "Record requested has been overwritten in the device memory.",
        -200007: "Record requested has not been acquired yet .",
        -200008: "Stop trigger has not occurred yet.",
        -200009: "Timestamps have been overwritten. You can no longer read any data.",
        -200010: "Onboard device memory overflow. Because of system and/or bus-bandwidth limitations, the driver could not read \
            data from the device fast enough to keep up with the device throughput. Reduce your sample rate. If your data transfer method is \
            interrupts, try using DMA or USB Bulk. You can also use a product with more onboard memory or reduce the number of programs your \
            computer is executing concurrently.",
        -200011: "Task cannot contain both input and output channels. Either use channels of one direction in a task or make two \
            separate tasks.",
        -200012: "Specified physical channel does not support digital output. Change the direction of the task, use another terminal, \
            or use another device.",
        -200014: "Terminal cannot appear multiple times within a single digital input or output task.",
        -200015: "Communication with SCXI failed. The communication cable to the SCXI hardware might have been disconnected or \
            exposed to excessive noise.",
        -200016: "Onboard device memory underflow. Because of system and/or bus-bandwidth limitations, the driver could not write \
            data to the device fast enough to keep up with the device output rate. Reduce your sample rate. If your data transfer method is \
            interrupts, try using DMA or USB Bulk. You can also use a product with more onboard memory or reduce the number of programs your \
            computer is executing concurrently.",
        -200017: "Onboard device memory underflow. Not enough new data has been sampled since the last read or the start of the \
            measurement. Increase the sample rate, increase the timeout value, or decrease the number of samples to read.",
        -200018: "DAC conversion attempted before data to be converted was available. Decrease the output frequency to increase \
            the period between DAC conversions, or reduce the size of your output buffer in order to write data more often. If you are using \
            an external clock, check your signal for the presence of noise or glitches.",
        -200019: "ADC conversion attempted before the prior conversion was complete. Increase the period between ADC conversions. \
            If you are using an external clock, check your signal for the presence of noise or glitches.",
        -200020: "Self-test of the device has failed.",
        -200022: "Resource requested by this task has already been reserved by a different task.",
        -200023: "Script contains an invalid character or symbol. Replace the invalid character with a valid symbol or alphanumeric \
            character.",
        -200024: "Valid identifier expected but not found in script. The identifier should specify a valid waveform or script \
            name. Identifiers cannot start with a number.",
        -200025: "Script name was expected, but not found in the script.",
        -200026: "Waveform name was expected, but not found in the script.",
        -200027: "Keyword was expected, but not found in the script.",
        -200028: "Waveform referenced in the script was not found in onboard memory. Write the waveform to the device before writing \
            the script.",
        -200029: "Marker specified in a generate instruction exceeds the waveform boundaries. Change the marker position or positions \
            to fit within the waveform, or increase the size of the waveform.",
        -200030: "Subset specified in a generate instruction exceeds the waveform boundaries. Change the subset start offset and/or \
            subset length so the subset fits within the waveform, or increase the size of the waveform.",
        -200031: "Marker position specified is not a multiple of alignment quantum.",
        -200032: "Subset length specified is not valid. Change the subset length to be longer than zero samples and a multiple \
            of the alignment quantum.",
        -200033: "Start offset of the subset is not a multiple of the alignment quantum.",
        -200034: "Marker position exceeds the length of the subset.",
        -200035: "Repeat loop is contained within too many levels of nested repeat loops. Unroll one of the repeat loops if \
            possible, or change the script and run it several times. To unroll a loop, remove the repeat and end repeat instructions and \
            explicitly replicate the instructions of the removed loop the desired number of times.",
        -200036: "Number of iterations specified for a finite repeat loop is invalid.",
        -200037: "Clear trigger instruction cannot be the last instruction of a repeat loop.",
        -200038: "Wait instruction cannot be the last instruction of a repeat until loop.",
        -200039: "Routing information associated with your device cannot be found.",
        -200040: "Source terminal to be routed could not be found on the device. Make sure the terminal name is valid for the \
            specified device. Refer to Measurement & Automation Explorer for valid terminal names.",
        -200041: "Destination terminal to be routed could not be found on the device. Make sure the terminal name is valid for \
            the specified device. Refer to Measurement & Automation Explorer or your hardware documentation for valid terminal names.",
        -200042: "Inversion requested is not possible. Either the hardware between the source and destination terminals does not \
            support the inversion, or other routes in the task might be interfering with this route.",
        -200043: "Hardware necessary for this route is in use by another task or tasks.",
        -200044: "Route cannot be made between the source and destination terminals. Either the hardware does not support this \
            route or other routes might be interfering with this route.",
        -200045: "Device was removed or powered down between task verification and reservation. Ensure that the device is not \
            being reset.",
        -200046: "Invalid identifier at the end of the switch action. A connection separator, sequence separator, or valid switch \
            action terminator must follow a switch action.",
        -200047: "Invalid identifier after the device identifier in the list entry.",
        -200048: "Invalid trigger line in the <sac> or <wfa> statement in the list entry. Refer to the documentation for valid \
            trigger lines.",
        -200049: "Invalid value in the <repeat> statement in the list entry. The syntax for a repeat statement is <repeat integer>. \
            Refer to the documentation for valid integer values.",
        -200050: "Invalid channel name in the list entry. Refer to the documentation for valid channel names for the device in \
            use.",
        -200051: "Invalid identifier after a separator in the list entry.",
        -200052: "Invalid identifier instead of an expected connection operator, ->, in the list entry. Refer to the documentation \
            for proper syntax for connections involving channel ranges.",
        -200053: "Channels in switch actions cannot span different devices.",
        -200054: "Semicolon or a semicolon modifier must follow a connection range statement. Refer to the documentation for information \
            on connection ranges and semicolon modifiers.",
        -200055: "Device identifier not specified in the list entry.",
        -200056: "Channel name not specified in the list entry.",
        -200057: "Duplicate device identifier in the device list. This is not allowed when waiting for devices to settle.",
        -200058: "Identifier in the list entry is too long.",
        -200059: "List cannot end with the connection separator &.",
        -200060: "Fully specified path cannot contain a connection range.",
        -200061: "Invalid identifier in the list entry. The connection separator && or sequence separator &&& was expected.",
        -200062: "Invalid identifier instead of an expected connection operator -> in the list entry.",
        -200063: "Invalid identifier instead of an expected terminator in the list entry.",
        -200064: "Unexpected connection separator & or sequence separator && in the list entry.",
        -200065: "Action at the designated position in the scanlist is not valid for the device.",
        -200066: "Connection operator is invalid at the designated point in the list entry.",
        -200067: "Settling time constraints for the device could not be satisfied. Refer to the documentation for details about \
            settling time constraints.",
        -200068: "Scanning is not supported by the specified device.",
        -200069: "Device specified is not a valid switch device.",
        -200070: "Advance trigger type specified is not supported by the device.",
        -200071: "Number of physical channels is too large.",
        -200072: "Duplicate channels in the list of physical channels are not supported by this device.",
        -200073: "SCXI module specified in the hardware configuration was not found. Make sure that the SCXI chassis is powered \
            on, the SCXI cable is properly connected between the chassis communicator and the SCXI module, and that the cabled module specified \
            in the hardware configuration is present in the specified slot.",
        -200074: "Device unable to store calibration constants. Make sure that your hardware is properly installed, and test the \
            regular operation of the device.",
        -200075: "Voltage data supplied is outside of the specified range. Change the range or the data. Refer to the documentation \
            for more information about possible ranges.",
        -200076: "Current data supplied is outside of the specified range.",
        -200077: "Requested value is not a supported value for this property. The property value may be invalid because it conflicts \
            with another property.",
        -200078: "Analog input (AI) task started or committed during a counter 0 DMA acquisition. If possible, use counter 1 instead \
            of counter 0. Otherwise, start/commit the AI task before starting the counter 0 DMA acquisition.",
        -200079: "Analog output (AO) task started or committed during a counter 1 DMA acquisition. If possible, use counter 0 \
            instead of counter 1. Otherwise, commit the AO task before starting the counter 1 DMA acquisition.",
        -200081: "Sample rate exceeds the maximum sample rate for the number of channels specified. Reduce the sample rate or \
            the number of channels. Increasing the convert rate or reducing the sample delay might also alleviate the problem, if you set either \
            of them.",
        -200082: "Minimum is greater than or equal to the maximum. Ensure the maximum value is greater than the minimum value. \
            If using a custom scale, ensure that the scaled maximum is greater than the scaled minimum.",
        -200086: "Physical channel range syntax in the input string is invalid because multiple devices were listed in the string.",
        -200087: "Channel is not in the task, and the channel is not a valid global channel. Make sure that the channel is in \
            the task or that the channel is a valid global channel. If you explicitly named the virtual channel in DAQmx Create Channel, you \
            must use the name assigned to that channel. Also, check for typing errors.",
        -200088: "Task specified is invalid or does not exist.",
        -200089: "Task name specified conflicts with an existing task name.",
        -200090: "Shared library was not found. This error might be the result of an inadvertent deletion of an NI-DAQmx component. \
            Reinstall NI-DAQmx, or download the latest version of the driver from the National Instruments website at ni.com. If the error \
            is still returned, contact NI Technical Support.",
        -200091: "Shared library version installed is incorrect. This error might be the result of an incorrect installation of \
            NI-DAQmx or a related software package. Reinstall NI-DAQmx, or download the latest version of the driver from the National Instruments \
            website at ni.com. If the error is still returned, contact NI Technical Support.",
        -200092: "Function supported for channel-based tasks only.",
        -200093: "Attempted to retrieve channel properties from a multichannel task without selecting a specific channel. Use \
            the Active Channel property to select a specific channel from which to retrieve properties.",
        -200094: "Digital waveform expected as input.",
        -200095: "Analog waveform expected as input.",
        -200096: "Number of samples to read must be -1 or greater.",
        -200097: "Attempted to retrieve channel properties from a multichannel task with more than one channel selected. You must \
            select an individual channel to retrieve channel properties. If you are programming with LabVIEW, use the Active Channel property \
            to specify the individual channel.",
        -200098: "Number of terminals requested cannot be greater than 1.",
        -200099: "Physical channel not specified.",
        -200100: "Specified DAQmx Read only can be used to read from a single channel. Use the multichannel DAQmx Read.",
        -200101: "Number of channels in data to write does not match the number of channels in the task.",
        -200102: "Pattern width specified does not match the number of lines in the digital channel.",
        -200103: "Number of samples to write must be the same for every channel.",
        -200104: "Bracket character ([ or ]) at the specified position in the list is invalid. Matching bracket cannot be \
            found. Check for nested fully specified paths or incorrectly paired brackets.",
        -200105: "Channel is invalid for the excitation mode of the SCXI-1122. Disable multiplexed excitation, or use one of the \
            physical channels between ai0 and ai7.",
        -200106: "Property must have the same value for all channels on this device.",
        -200107: "Module specified in the hardware configuration is not the module found. Make sure that the module specified \
            in the hardware configuration is present in the specified slot.",
        -200108: "Calibration session is already open on this device. You can have only one open calibration session for each \
            device. Use the handle obtained when the calibration session for this device was originally opened.",
        -200109: "Password is longer than four characters.",
        -200110: "Password supplied is incorrect.",
        -200111: "Password is required for this operation.",
        -200112: "Calibration handle is invalid. Open a calibration session to get a valid calibration handle. Use the valid calibration \
            handle obtained when the calibration session was opened.",
        -200113: "Device temperature is outside of the required range for calibration.",
        -200116: "Lines on the 8255 chip for this device are configured for output. Cannot tristate these lines at this time. \
            Read values using an input task on another port.",
        -200117: "Port C cannot be used for data input/output in a handshaking task.",
        -200118: "Port reserved for handshaking. Cannot reserve this port or any of its lines for another task at this time.",
        -200119: "Port is configured for static digital operations by another task. Cannot configure this port or any of its lines \
            for handshaking at this time.",
        -200120: "Port is configured for input. Cannot configure this port or any of its lines for output at this time.",
        -200121: "Port is configured for output. Cannot configure this port or any of its lines for input at this time.",
        -200122: "Lines 0 through 3 of this port are configured for input. Cannot configure these lines for output at this time.",
        -200123: "Lines 0 through 3 of this port are configured for output. Cannot configure these lines for input at this time.",
        -200124: "Lines 4 to 7 of this port are configured for input. Cannot configure these lines for output at this time.",
        -200125: "Lines 4 through 7 of this port are configured for output. Cannot configure these lines for input at this time.",
        -200126: "Lines on port C cannot be used for both handshaking control and static digital operations on an 8255 chip. Handshaking \
            tasks automatically reserve some lines on port C as control lines. These lines cannot be reserved for static digital operations \
            when the device is configured for handshaking. There are two likely causes for this error: 1. An attempt was made to reserve the \
            lines for static digital operations when a handshaking task was previously configured. 2. An attempt was made to create \
            a handshaking task when the lines were previously reserved for static digital operations. Refer to the documentation for information \
            about which lines on port C are not available when the 8255 chip is in handshaking mode.",
        -200127: "Port 0 or any of its lines cannot be used to create a handshaking task. Use port 1 or port 2 of the 8255 chip \
            on this device for handshaking.",
        -200128: "Property must have the same value for all repeated physical channels. Set the same property value for all of \
            the channels.",
        -200130: "Timebase divisor cannot be set for an external clock. You cannot divide down an externally supplied clock. If \
            you want to divide down an external clock, specifiy an external timebase source instead and set the clock source to be internal.",
        -200131: "Analog trigger source must be the first channel in the acquisition or a valid analog trigger terminal. If you \
            explicitly named the virtual channel in DAQmx Create Channel, you must use the name assigned to that channel.",
        -200132: "External timebase rate must be specified to translate the derived clock or timebase rate into ticks. Set the \
            external timebase rate, or set the divisor instead of the clock or timebase rate.",
        -200133: "Counter timebase source, counter timebase rate, master timebase divisor, and master timebase rate settings are \
            inconsistent with one another. The conflicting properties must satisfy the following constraint: Master Timebase Rate / Master \
            Timebase Divisor = Counter Timebase Rate",
        -200134: "Counter timebase source and counter timebase rate settings are inconsistent with one another. For internal counter \
            timebase source selections, if the counter timebase rate is set, its value must match the rate corresponding to the counter timebase \
            source. For example, 20 MHz corresponds to a rate of 20,000,000 Hz.",
        -200135: "Counter timebase source and counter timebase master timebase divisor settings are inconsistent with one another. \
            If the divisor is specified, the following must apply: Master Timebase Rate / Counter Timebase Master Timebase Divisor = Rate corresponding \
            to Counter Timebase Source.",
        -200136: "Frequency and Initial Delay property values are inconsistent with one or more counter timebase properties. The \
            conflicting properties must satisfy the following constraint: Counter Timebase Rate / Counter Maximum Count <= X <= Counter Timebase \
            Rate / 2 where X = Frequency and 1 / Initial Delay, and where Counter Timebase Rate = Master Timebase Rate / Counter Timebase Master \
            Timebase Divisor or is inferred from the Counter Timebase Source selection.",
        -200137: "Initial Delay, High Time, and Low Time property values are inconsistent with one or more counter timebase properties. \
            The conflicting properties must satisfy the following restraint: 2 / Counter Timebase Rate <= X <= Counter Maximum Count/ Counter \
            Timebase Rate where X = Initial Delay, High Time, and Low Time, and where Counter Timebase Rate = Master Timebase Rate / Counter \
            Timebase Master Timebase Divisor or is inferred from the Counter Timebase Source selection.",
        -200138: "A timebase could not be selected that covers the entire range specified in the Maximum and Minimum properties. \
            The conflicting properties must satisfy the following constraints: Maximum <= Counter Maximum Count / Counter Timebase Rate Minimum \
            >= 2 / Counter Timebase Rate.",
        -200139: "A timebase could not be selected that covers the entire range specified in the Maximum and Minimum properties. \
            The conflicting properties must satisfy the following constraints: Maximum <= Counter Timebase Rate / 2 Minimum >= Counter Timebase \
            Rate / Counter Maximum Count.",
        -200140: "Two consecutive active edges of the input signal occurred without a counter timebase edge. Use a faster counter \
            timebase.",
        -200141: "Data was overwritten before it could be read by the system. If Data Transfer Mechanism is Interrupts, try using \
            DMA or USB Bulk. Otherwise, divide the input signal before taking the measurement.",
        -200142: "Internal timebase could not be found that matches the rate specified in the Counter Timebase Rate property.",
        -200143: "Counter timebase rate must be specified for external counter timebase sources in order for frequency and/or \
            time calculations to be made correctly. Set the Counter Timebase Rate property to the appropriate value for your external source.",
        -200144: "Pause trigger is only valid for continuous pulse generations. Change the sample mode to continuous, or do not \
            use the pause trigger.",
        -200145: "Pause trigger is only valid for event counting if sample clock is not used.",
        -200146: "Pause and start triggers cannot both be active in this task.",
        -200147: "There cannot be multiple counters in the same task for input operations. Use a separate task for each counter.",
        -200148: "FREQOUT counter cannot generate the desired frequency. The FREQOUT counter is a 4-bit counter that can divide \
            either the master timebase rate / 2 or the master timebase rate / 200 by a number between one and 16. Choose a frequency within \
            this range.",
        -200149: "External timebase rate must be specified to translate the delay into ticks. Set the external timebase rate, \
            or set the delay in units of ticks.",
        -200150: "Channel is not available when the module is in parallel mode.",
        -200151: "Your SCXI system is not set up for performing analog input operations on given channels. The SCXI module cabled \
            to your digitizer cannot route analog signals from other modules to the digitizer, or is not configured to route them. To perform \
            the desired operation with multiple SCXI modules and one digitizer, cable the digitizer to one of the analog input modules. \
            The module your channels are on is one such module. Then, update the chassis configuration in MAX to reflect cabling change, \
            and ensure that the cabled module is in multiplexed mode. Alternatively, you can use multiple digitizers and SCXI modules in \
            parallel mode. For detailed information about cabling, refer to documentation.",
        -200152: "Data read from the EEPROM on the device is invalid. Verify that any accessories configured with this device \
            are connected. If the problem continues, contact National Instruments Technical Support. The device might need to be recalibrated \
            or repaired by NI.",
        -200153: "Reference voltage applied for calibration is outside the range defined for calibration of this device. Ensure \
            that the reference voltage falls within the range specified for this device.",
        -200154: "Reference current applied for calibration is outside the range defined for calibration of this device. Ensure \
            that the reference current falls within the range specified for this device.",
        -200155: "Reference resistance applied for calibration is outside the range defined for calibration of this device. Ensure \
            that the reference resistance falls within the range specified for this device.",
        -200156: "Reference frequency applied for calibration is outside the range defined for calibration of this device. Ensure \
            that the reference frequency falls within the range specified for this device.",
        -200157: "Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The \
            actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied \
            is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being \
            calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. 3. \
            The device is not functioning properly.",
        -200158: "Requested operation could not be performed because the necessary digital lines could not be reserved by SCXI. \
            Another task might have reserved these lines previously. For example, E Series devices use lines 0, 1, 2, and 4 on port 0 to communicate \
            with the SCXI module.",
        -200159: "Requested operation could not be performed because the digital lines are being used for communication with SCXI \
            or a TEDS carrier. For example, E Series devices use lines 0, 1, 2, and 4 on port 0 to communicate with a SCXI module. Therefore, \
            you cannot use lines 0, 1, 2, and 4 for regular digital I/O.",
        -200160: "Channel could not be created. All channels must be created before the task is verified. Before I/O can be performed \
            or properties can be retrieved, tasks are verified. Channels must be created before these actions can occur.",
        -200161: "Device to which the sensor is attached does not have an available internal excitation source. Select another \
            device with an available internal excitation source or supply external excitation.",
        -200162: "2-wire resistance configuration is incompatible with voltage excitation.",
        -200163: "Completion resistance value, R1, cannot be zero if the circuit uses voltage excitation.",
        -200166: "Output buffer underwrite. Your application was unable to write samples to the background buffer fast enough \
            for the device to get new samples at the specified sample rate. To avoid this error, you can do any the following: 1. Increase \
            the size of the background buffer by configuring the buffer. 2. Increase the number of samples you write each time you invoke a \
            write operation. 3. Write samples more often. 4. Reduce your sample rate. 5. Change the data transfer mechanism from interrupts to \
            DMA. 6. Initially write a sufficient number of samples to satisfy the specified data transfer request condition. 7. \
            Reduce the number of applications that your computer is executing concurrently. In addition, if you do not need to ensure that \
            each sample is generated once and only once, you can set the regeneration mode to allow regeneration.",
        -200167: "Device cannot acquire from _cjTemp and other channels in the same task. Create one task for reading _cjTemp \
            and another task for the other channels.",
        -200168: "Number of channels to acquire exceeds the device maximum. Reduce the number of channels. In some cases, you \
            can access a large number of channels if they are identically configured and created consecutively. Refer to the documentation \
            for more information.",
        -200169: "Memory mapping can be enabled only if Data Transfer Mechanism is Programmed IO. Enable memory mapping only when \
            Data Transfer Mechanism is Programmed IO.",
        -200170: "Physical channel specified does not exist on this device. Refer to the documentation for channels available \
            on this device.",
        -200171: "Virtual channel cannot be created. Another virtual channel with this name already exists.",
        -200172: "Buffer size must be zero when Data Transfer Mechanism is Programmed IO. Set buffer size to zero or Data Transfer \
            Mechanism to something other than Programmed IO.",
        -200173: "The combination of Sample Timebase Rate and Master Timebase Rate you specified is invalid. The driver computed \
            the Sample Timebase Source Divisor by dividing the Master Timebase Rate by the Sample Timebase Rate. The resulting value for the \
            Sample Timebase Source Divisor is not supported by your device. Refer to the documentation for more information about these three \
            properties.",
        -200175: "Hardware is not responding. Ensure your hardware is powered on and all cables are properly connected.",
        -200176: "Operation is not permitted while the switch device is scanning.",
        -200177: "Operation is permitted only while the switch device is scanning.",
        -200178: "Task was created with a settling time different from the current settling time. When scanning, you must use \
            the original settling time specified when the task was created.",
        -200179: "Explicit connection between the channels already exists. You can make only one connection between these channels.",
        -200180: "Path between two switch channels is not available.",
        -200181: "Channel name specified is not valid for the switch device.",
        -200182: "Switch channels cannot be disconnected because there is no explicit path between them.",
        -200183: "Switch channel names cannot be duplicated in the path string.",
        -200184: "Leg in path cannot contain two channels that are already directly connected.",
        -200185: "Path contains a leg with two channels that cannot be directly connected.",
        -200186: "Channels used to make the connection between two endpoints must be reserved for routing.",
        -200187: "Channel cannot be connected to itself.",
        -200188: "Connection cannot be made between the specified channels because they are connected to different source channels.",
        -200189: "Explicit connection cannot be made to a switch channel that is reserved for routing.",
        -200190: "Disconnection path is not the same as the existing path. You can programmatically find out the existing path. \
            Refer to your documentation for details.",
        -200191: "Task was created with a topology different from the current topology. When scanning, you must use the original \
            topology specified when the task was created.",
        -200192: "Switch device supports continuous scanning only.",
        -200193: "Switch device does not support this operation.",
        -200194: "Hardware was unexpectedly powered off and back on. To recover, reset the device (either programmatically or \
            by using Measurement & Automation Explorer).",
        -200195: "Switch configuration has caused the switch device to exceed its power limit because there were too many closed \
            relays. The switch was disabled. Reset it by doing one of the following: 1. Call DAQmx Switch Set Topology And Reset. 2. Call DAQmx \
            Device Reset. 3. Use Measurement & Automation Explorer.",
        -200196: "Action at the end of the scan list is not valid for this device.",
        -200197: "Device does not support this property.",
        -200198: "Topology specified is invalid. Make sure the spelling of the topology is correct and that the switch supports \
            that topology.",
        -200199: "Switch device must be reset before scanning. Reset the device by doing one of the following: 1. Call DAQmx Switch \
            Set Topology And Reset. 2. Call DAQmx Device Reset. 3. Use Measurement & Automation Explorer.",
        -200200: "Switch channel is already in exclusive use within another connection.",
        -200201: "Switch scan list is too large to fit in the onboard memory of the device.",
        -200202: "Relay name is invalid.",
        -200203: "Switch hardware is incapable of driving multiple trigger lines simultaneously.",
        -200204: "Unexpected identifier within the fully-specified path in the list.",
        -200205: "Topology does not support scanning.",
        -200206: "Advance trigger and Advance Complete event must use the same polarity in this particular switch device.",
        -200207: "Device identifier in the list entry is invalid.",
        -200208: "Range statement in the list entry contains an invalid character sequence.",
        -200209: "Duplicate device identifier found in the terminal list when trying to set the property. Only one instance of \
            the device identifier is permitted.",
        -200210: "Multiple device identifiers from one chassis are not allowed in the terminal list.",
        -200211: "Multiple relay names were specified for a single relay operation.",
        -200212: "Measurement units specified for the channel are not valid for the Measurement Type of the channel.",
        -200213: "Pretrigger Samples per Channel requested plus minimum number of posttrigger samples exceed the requested Number \
            of Samples per Channel. Decrease the number of Pretrigger Samples per Channel, or increase Number of Samples per Channel.",
        -200214: "Analog trigger circuitry unavailable on the device. Select a non-analog trigger type, or use a device with analog \
            triggering hardware.",
        -200215: "Memory Mapping is not supported for buffered operations. Turn Memory Mapping off, set Buffer Size to 0, or do \
            not configure the buffer for the operation.",
        -200216: "Buffered operations cannot use a Data Transfer Mechanism of Programmed I/O for this device and Channel Type. \
            Non-buffered operations cannot use a Data Transfer Mechanism of Interrupts or DMA for this device and Channel Type.",
        -200217: "Buffered operations cannot use On Demand for Sample Timing Type. Set your buffer size to 0 for On Demand sample \
            timing. Otherwise, configure your sample clock, or change your sample timing type for buffered operations.",
        -200218: "Data Transfer Mechanism must be Programmed I/O when not using hardware timing. Set Data Transfer Mechanism to \
            Programmed I/O, configure your sample clock timing, or set Sample Timing Type to Sample Clock.",
        -200219: "Analog output virtual channels cannot be created out of order with respect to their physical channel numbers \
            for the type of device you are using. For example, a virtual channel using physical channel ao0 must be created before a virtual \
            channel with physical channel ao1.",
        -200220: "Device identifier is invalid.",
        -200221: "Amount of time allocated to perform this operation was exceeded.",
        -200222: "Acquisition has been stopped to prevent an input buffer overwrite. Your application was unable to read samples \
            from the buffer fast enough to prevent new samples from overwriting unread data. To avoid this error, you can do any of the following: \
            1. Increase the size of the buffer. 2. Increase the number of samples you read each time you invoke a read operation. \
            3. Read samples more often. 4. Reduce the sample rate. 5. If your data transfer method is interrupts, try using DMA or USB Bulk. \
            6. Reduce the number of applications your computer is running concurrently. In addition, if you do not need to read every sample \
            that is acquired, you can configure the overwrite mode to overwrite unread data, and then use the Relative To and Offset properties \
            to read the desired samples.",
        -200223: "Specified threshold and hysteresis values for this channel create a triggering range that is not supported by \
            your device. On the SCXI-1126, threshold minus hysteresis must be between -0.5 and 4.48.",
        -200224: "No registered trigger lines could be found between the devices in the route. If you have a PXI chassis, identify \
            the chassis correctly in MAX, and make sure it has been configured properly. If you are using PCI devices, make sure they are connected \
            with a RTSI cable and that the RTSI cable is registered in MAX. Otherwise, make sure there is an available trigger line on the \
            trigger bus shared between the devices.",
        -200225: "Trigger line requested could not be reserved because it is already in use.",
        -200226: "Trigger bus to which the device is connected does not have any free trigger lines for the driver to choose. \
            To free up trigger lines, you can do any of the following: 1. Stop other tasks that are connected to the same trigger bus as this \
            device. 2. Use DAQmx Disconnect Route to stop any immediate routes that span this trigger bus. 3. Make more trigger lines on this \
            trigger bus available to the driver.",
        -200227: "Device does not have any free trigger lines for the device driver to choose. Although there might be trigger \
            lines available on the respective trigger bus, the device cannot use the trigger bus because the device does not have enough free \
            resources to do so. To free up trigger lines, you can do any of the following: 1. Stop other tasks that are connected to this device. \
            2. Use DAQmx Disconnect Route to stop any immediate routes that span this trigger bus and device.",
        -200228: "Buffer is too small to fit the string.",
        -200229: "Buffer is too small to fit read data.",
        -200230: "NULL pointer was passed for a required parameter.",
        -200231: "Property requested cannot be set.",
        -200232: "Property requested cannot be read.",
        -200233: "Property specified is not valid for this function.",
        -200234: "Buffer is too small for requested samples to be written.",
        -200235: "Explanation could not be found for the requested status code. Verify that the requested status code is correct.",
        -200236: "Property requested cannot be reset.",
        -200237: "Hardware clocking error occurred. If you are using an external reference clock, make sure it is connected and \
            within the jitter and voltage level specifications, and its rate is correctly specified. If you are generating your clock internally, \
            please contact National Instruments Technical Support.",
        -200238: "Hardware clocking error occurred. If you are using an external reference clock, make sure it is connected and \
            within the jitter and voltage level specifications at all times, and its rate is correctly specified. If you are generating your \
            clock internally, please contact National Instruments Technical Support.",
        -200239: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200240: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches \
            the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200241: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches \
            the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200242: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches \
            the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200243: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches \
            the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200244: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200245: "PLL could not phase-lock to the external reference clock. Make sure your reference clock is connected and that \
            it is within the jitter and voltage specifications. Also, make sure the reference clock rate is correctly specified.",
        -200246: "PLL has lost phase-lock to the external reference clock. Make sure your reference clock is connected and that \
            it is within the jitter and voltage level specifications at all times. Also, make sure the reference clock rate is correctly specified \
            at all times.",
        -200247: "Integer was expected but not found in the script. Insert an appropriate integer at this location in the script.",
        -200248: "Specified marker position is too close to the end of the last generate statement in a repeat until loop. \
            Move the marker position farther away from the end of the last generate statement in the repeat until loop.",
        -200249: "Length of waveform subset is too small for the last generate statement in a repeat until loop.",
        -200250: "Length of waveform is too small for the last generate statement in a repeat until loop.",
        -200251: "No DMA channels or USB Bulk Endpoints are available. Either shut down other tasks that might be using these \
            resources or consider changing your data transfer mechanism to Interrupts if supported.",
        -200252: "Terminal cannot be tristated because it is busy. Disconnect any routes spanning this terminal, or stop any tasks \
            using this terminal.",
        -200253: "Terminal could not be tristated because the hardware cannot tristate this terminal.",
        -200254: "Terminal for the device is invalid.",
        -200255: "Built-in temperature sensor is not supported on this channel. This channel is not configured to support a built-in \
            temperature sensor. Make sure the accessory specified in the hardware configuration is correct and that the hardware supports a \
            built-in temperature sensor on this channel.",
        -200256: "Specified topology cannot be used to reset the switch, because that topology is not supported by the connected \
            terminal block. Refer to the documentation for supported topologies for the given terminal block, or disconnect the terminal block \
            from the switch.",
        -200257: "Excitation property must be the same for related physical channels. Refer to the documentation for information \
            about setting excitation across related physical channels.",
        -200258: "Gain value conflicts with specified AI Minimum and AI Maximum properties. The specified gain and AI Minimum \
            and/or AI Maximum would cause the device to exceed the hardware limit. Lower the gain, or adjust AI Minimum and/or AI Maximum.",
        -200259: "Value selected for this jumper-controlled property must match the value specified in Measurement & Automation \
            Explorer. Make sure the value specified in Measurement & Automation Explorer matches the value in your program and that the value \
            corresponds to the selection made using the jumper on the device.",
        -200260: "Memory mapping has been enabled, and the sample clock has been configured; but the buffer size has not been \
            set, and the data transfer mechanism has either not been set or was set to something other than Programmed I/O. Set the buffer \
            size to 0, and/or change the data transfer mechanism to Programmed I/O.",
        -200261: "An attempt has been made to use an analog trigger in multiple situations with differing properties. Change the \
            analog trigger properties so they are the same, or do not use an analog trigger for all situations.",
        -200262: "An attempt has been made to configure a trigger without configuring the appropriate sample clock properties \
            or when Sample Timing Type was set to On Demand. Configure the sample clock type to something other than On Demand to use a trigger.",
        -200263: "Device supports an analog channel as the source of an analog pause trigger only when it is the only channel \
            in the task. Remove all of the channels currently in the task except the channel that will be used as the analog trigger source, \
            or change the analog trigger source to a terminal.",
        -200264: "Device supports an analog channel as the source of an analog reference trigger only when it is the only channel \
            in the task. Remove all of the channels currently in the task except the channel that will be used as the analog trigger source, \
            or change the analog trigger source to a terminal.",
        -200265: "An attempt has been made to use an invalid analog trigger source. Ensure that the trigger source you specify \
            matches the name of the virtual channel in the task or matches the name of a non-scannable terminal that the device can use as \
            an analog trigger source.",
        -200266: "Minimum and maximum values for the channel are not symmetric.",
        -200267: "Product of AO channel properties Maximum Value and Gain exceeds the maximum voltage for the device.",
        -200268: "Specified Offset is too small given AO Gain and Minimum Value. The following constraint must hold: Offset > \
            (Gain * Minimum Value / 2)",
        -200269: "Specified Offset is too large for the given AO Gain and Maximum Value. The following constraint must hold: Offset \
            < (Gain * Maximum Value / 2)",
        -200270: "Interpolation rate specified is not possible for the given sample rate.",
        -200271: "Product of AO Channel properties Minimum Value and Gain exceeds the minimum voltage for the device.",
        -200272: "Sample clock rate requested is too low for the selected divide-down clock. Use the high resolution clock, or \
            increase your sample rate.",
        -200273: "Sample clock rate and the sample clock divisor values are inconsistent with one another. Consider settting either \
            the sample clock rate or the sample clock divisor, but not both. This allows the driver to automatically select an appropriate \
            value for the other property. Alternatively, make sure the sample clock rate and sample clock divisor satisfy the following constraint: \
            rate = timebase / divisor",
        -200274: "Sample clock rate desired is too high for an external clock being brought in through the backplane. Bring in \
            your external sample clock through one of the higher-frequency front panel connectors, or use a lower sample rate.",
        -200275: "Sample rate desired is too low for an external clock being brought in through the ClkIn connector. Change the \
            sample rate so it is within limits, or use DDC_ClkIn to bring in your sample clock.",
        -200276: "Reference clock source and sample clock source cannot be the same. Use different terminals to bring in your \
            reference clock and sample clock, or use only one of them at a time.",
        -200277: "Invalid combination of position and offset. The position and offset specified a sample prior to the first sample \
            acquired (sample 0). Make sure any negative read offset specified will select a valid sample when combined with the read position.",
        -200278: "Attempted to read a sample beyond the final sample acquired. The acquisition has stopped, therefore the sample \
            specified by the combination of position and offset will never be available. Specify a position and offset which selects a sample \
            up to, but not beyond, the final sample acquired. The final sample acquired can be determined by querying the total samples acquired \
            after an acquisition has stopped.",
        -200279: "The application is not able to keep up with the hardware acquisition. Increasing the buffer size, reading the \
            data more frequently, or specifying a fixed number of samples to read instead of reading all available samples might correct the \
            problem.",
        -200281: "Reading relative to the reference trigger or relative to the start of pretrigger samples position before the \
            acquisition is complete. Wait for the acquisition to complete before reading, or increase your read timeout. Also, make sure the \
            hardware is set up and wired correctly, the signal for the reference trigger is correct, and that the reference trigger occurs while \
            the device is acquiring data.",
        -200282: "Reading relative to the reference trigger or relative to the start of a pretrigger sample is not supported with \
            the current task configuration. If you have not configured a reference trigger or if one of your devices is utilizing an onboard \
            buffer to transfer data after an acquisition has completed, reading relative to reference trigger or relative to the first pretrigger \
            sample is not supported, Configure a reference trigger, or configure read position differently.",
        -200283: "Acquisition has stopped to prevent the intermediate buffer from overflowing. The background was running too \
            fast for the application to keep up, and the application was unable to read samples from the intermediate buffer fast enough to \
            prevent losing samples. To avoid this error, you might reduce the sample rate, reduce the number of applications your computer is \
            executing concurrently, or not read any samples until the acquisition is complete.",
        -200284: "Some or all of the samples requested have not yet been acquired. To wait for the samples to become available \
            use a longer read timeout or read later in your program. To make the samples available sooner, increase the sample rate. If your \
            task uses a start trigger, make sure that your start trigger is configured correctly. It is also possible that you configured the task \
            for external timing, and no clock was supplied. If this is the case, supply an external clock.",
        -200286: "No data is available to read, because no acquisition has been started. Start the acquisition before attempting \
            to read data, either explicitly or by enabling auto start and stop.",
        -200287: "Attempted to write to an invalid combination of position and offset. The position and offset specified a sample \
            prior to the first sample generated (sample 0). Make sure any negative write offset specified will select a valid sample when combined \
            with the write position.",
        -200288: "Attempted to write a sample beyond the final sample generated. The generation has stopped, therefore the sample \
            specified by the combination of position and offset will never be available. Specify a position and offset which selects a sample \
            up to, but not beyond, the final sample generated. The final sample generated can be determined by querying the total samples generated \
            after a generation has stopped.",
        -200289: "Attempted to write samples that have already been generated or have already been sent to the device for generation. \
            Increasing the buffer size or writing the data more frequently might correct the problem.",
        -200290: "The generation has stopped to prevent the regeneration of old samples. Your application was unable to write \
            samples to the background buffer fast enough to prevent old samples from being regenerated. To avoid this error, you can do any \
            of the following: 1. Increase the size of the background buffer by configuring the buffer. 2. Increase the number of samples you write \
            each time you invoke a write operation. 3. Write samples more often. 4. Reduce the sample rate. 5. If your data transfer method is \
            interrupts, try using DMA or USB Bulk. 6. Reduce the number of applications your computer is executing concurrently. In addition, \
            if you do not need to write every sample that is generated, you can configure the regeneration mode to allow regeneration, and then \
            use the Position and Offset attributes to write the desired samples.",
        -200291: "The generation has stopped because an intermediate buffer overflowed. The background was running too fast for \
            the application to keep up, and the application was unable to write samples to the intermediate buffer fast enough to prevent \
            regenerating old samples. To avoid this error, you can reduce the sample rate, reduce the number of applications your computer is \
            executing concurrently, or write all samples before the generation starts.",
        -200292: "Some or all of the samples to write could not be written to the buffer yet. More space will free up as samples \
            currently in the buffer are generated. To wait for more space to become available, use a longer write timeout. To make the space \
            available sooner, increase the sample rate.",
        -200293: "The generation is not yet started, and not enough space is available in the buffer. Configure a larger buffer, \
            or start the generation before writing more data than will fit in the buffer.",
        -200294: "Not enough samples were written to satisfy the initial data transfer request condition. To successfully start \
            a generation, increase the number of samples initially written to the buffer before starting. Alternatively, decrease the number \
            of samples required to start by changing the data transfer request condition.",
        -200295: "Attempt was made to write samples after start of generation where only onboard memory was used. In this case, \
            all samples must be written to the device before the start of generation. No samples may be updated once the generation has started. \
            If you wish to modify samples in the generation after the start of the generation, do not enable the onboard memory.",
        -200297: "This property is unavailable when using onboard memory.",
        -200300: "Invalid timing type for this channel.",
        -200301: "Cannot update the Pulse Generation property. The pulse generation with previous property settings must complete \
            a full cycle before the property can be updated.",
        -200302: "Signal being measured is slower than the specified measurement time. Increase the measurement time, or use a \
            different measurement method.",
        -200303: "External sample clock source must be specified for this application.",
        -200304: "External master timebase rate must be specified for this channel given the selected measurement units. Specify \
            the master timebase rate, or use ticks as the measurements units.",
        -200305: "Desired finite pulse train generation is not possible. Change the number of samples to be generated, increase \
            the rate of the pulse train, or choose a different timebase source. Refer to the documentation for more details.",
        -200306: "An attempt was made to set the Samples per Channel property to a value greater than the maximum supported number.",
        -200307: "Specified master timebase rate does not match specified master timebase source. Do not set the master timebase \
            rate when you are using an internal master timebase source. In this case, the driver sets the master timebase rate for you.",
        -200308: "Specified sample timebase rate does not match specified sample timebase source. Do not set the sample timebase \
            rate when you are using an internal sample timebase source. In this case, the driver sets the sample timebase rate for you.",
        -200309: "Specified master timebase divisor (belonging to sample clock timebase) is not appropriate for the specified \
            sample timebase source. Do not set the master timebase divisor when you are using an internal sample timebase source. In this case, \
            the driver sets the master timebase divisor for you.",
        -200310: "The waveform you are trying to allocate on the device has been previously allocated. Make sure you are not trying \
            to allocate the same waveform twice, or delete the existing waveform before allocating it again.",
        -200311: "You cannot write data outside the boundaries of your waveform. Make sure you are not trying to write more data \
            than your waveform can accomodate and that your write location and write offset are set correctly.",
        -200312: "Waveform is not in the device memory. Make sure you are referring to a previously allocated and/or written waveform \
            by its correct name. Also, make sure that the waveform was not deleted.",
        -200313: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches \
            the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200314: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage specifications. Also, verify that the rate of the external clock matches \
            the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200315: "There is not enough free device memory for your waveform. Delete waveforms or scripts not in use to free memory. \
            If you have deleted multiple waveforms or scripts, the memory might have become fragmented. To avoid fragmentation, you can change \
            the order in which you write/delete your waveforms and scripts.",
        -200316: "Device data underflow. The device was not able to move data fast enough to keep up with the sample rate for \
            the active script. Run the operation at a lower sample rate, or look for the following in the active script: markers might be too \
            close together, waveforms might be too small, waits might be too short, or subsets might be too small. If you are using an external \
            clock, the provided clock might have gone away during your generation.",
        -200317: "There is not enough free device memory for your script. Delete waveforms or scripts not in use to free memory. \
            If you have deleted multiple waveforms or scripts, the memory might have become fragmented. To avoid fragmentation, you can change \
            the order in which you write/delete your waveforms and scripts.",
        -200318: "Invalid excitation value specified to be used for scaling with full bridge configuration. Change the excitation \
            value if you want it to be used for scaling with full bridge configuration. Alternatively, change the bridge configuration, or \
            do not use excitation value for scaling.",
        -200319: "Your SCXI system is not set up to perform the analog input operation on given channels. The SCXI module cabled \
            to your digitizer cannot route AI Convert Clock from the digitizer to the other modules. To perform the desired operation with \
            multiple SCXI modules and one digitizer, cable the digitizer to one of the modules that can route the AI Convert signal, such as \
            the module your channels are on. After cabling the digitizer to the module, update the chassis configuration in Measurement & \
            Automation Explorer to reflect the cabling change. For detailed information about cabling, refer to the documentation.",
        -200320: "Your SCXI system is not set up for analog input with simultaneous sample and hold on the given channels. The \
            SCXI module cabled to your digitizer cannot route the signal needed for simultaneous sample and hold from the digitizer to the \
            other modules. To perform the desired operation with multiple SCXI modules and one digitizer, cable the digitizer to one of the modules \
            that can route the signal needed for simultaneous sample and hold. The simultaneous sample and hold module in your chassis is one \
            such module. After cabling the digitizer to the module, update the chassis configuration in Measurement & Automation Explorer to \
            reflect the cabling change. For detailed information about cabling, refer to the documentation.",
        -200321: "Attenuation Value conflicts with the specified AI Minimum and AI Maximum properties. The specified attenuation \
            and AI Minimum and/or AI Maximum would cause the device to exceed the hardware limit. You should increase the Attenuation Value \
            or adjust the AI Minimum and/or AI Maximum.",
        -200322: "Data transfer has been stopped to prevent the computer from becoming completely unresponsive. Could not transfer \
            enough data to satisfy the data transfer requirements with Interrupts as the Data Transfer Mechanism. Reduce your Sample Clock \
            Rate, use DMA as your Data Transfer Mechanism, or use a different Data Transfer Request Condition.",
        -200323: "Cannot perform a multidevice scan with Advance Trigger Type set to None. Without the advance trigger, the devices \
            in the scan list cannot be synchronized.",
        -200324: "NI-DAQmx is unable to communicate with the device. Make sure the device is present in and accessible to the \
            system, is not currently being reset, and is not reserved by another driver such as Traditional NI-DAQ (Legacy).",
        -200325: "Reverse coefficients must be specified to scale your data using the polynomial scale.",
        -200326: "An attempt has been made to perform a route when the source and the destination are the same terminal. In many \
            cases, such as when configuring an external clock or a counter source, you must select a PFI, PXI Trigger, or RTSI line as the \
            source terminal.",
        -200327: "You have specified an invalid value for dt in the waveform cluster. The value for dt must be greater than zero.",
        -200328: "Switch driver cannot open the topology configuration file for the switch device. A switch device cannot function \
            without its configuration file. The configuration file is installed with the driver. The file might have been removed, renamed, \
            or corrupted after installation. Make sure the configuration file is available to the driver at the expected location, or reinstall \
            the product, as that will reinstall the configuration file.",
        -200329: "An error has occurred while attempting to configure the device for an analog input acquisition. If an external \
            master timebase is being used, make sure the source is connected and generating an appropriate clock. Otherwise, contact National \
            Instruments Technical Support.",
        -200330: "An attempt has been made to use the PFI0 terminal of the device for both an analog and digital source. Use a \
            terminal other than PFI0 as the source of your digital signal.",
        -200331: "Specified sample rate is lower than the lowest rate that can be generated using the onboard clock. The rate \
            has been coerced to the slowest possible sample rate. For slower rates, use an external sample clock or an external sample clock \
            timebase.",
        -200332: "Specified sample rate is higher than the fastest rate supported by the device.",
        -200333: "Delay from the start trigger is shorter than the shortest delay that can be generated using the onboard clock \
            with a timebase suitable for generating the sample clock. For shorter delays, use a sample clock timebase with a higher rate, if \
            applicable.",
        -200334: "Delay from start trigger is longer than the longest delay that can be generated using the onboard clock with \
            a timebase suitable for generating the sample clock. For longer delays, use a slower sample clock timebase rate, if applicable.",
        -200335: "Specified AI convert rate is higher than the fastest rate possible with the current timebase.",
        -200336: "Delay from the sample clock is shorter than the shortest delay that can be generated using the onboard clock \
            with a timebase suitable for generating the convert clock. For shorter delays, use a faster convert clock timebase rate, if applicable.",
        -200337: "Delay from the sample clock is longer than the longest delay that can be generated using the onboard clock with \
            a timebase suitable for generating the convert clock. For longer delays, use a slower convert clock timebase rate, if applicable.",
        -200338: "An attempt has been made to read the calibration temperature for a device without an internal temperature sensor.",
        -200339: "Pulse width measurement was started while the input signal was active, and no additional pulses were received, \
            which caused the measurement not to complete during the specified timeout. When measuring a single pulse width, make sure the \
            measurement. Counter is started before the pulse to be measured is active, or provide a timeout sufficient for at least one \
            additional pulse to be measured.",
        -200340: "By setting Number of Samples per Channel to -1, you indicated that all available data should be read. This is \
            not valid for acquisitions without a buffer. Specify a value greater than or equal to zero for Number of Samples per Channel. Do \
            not specify a value of zero for Buffer Size when configuring the input buffer.",
        -200341: "Generation was configured to use only onboard memory, but the corresponding buffer is larger than onboard memory. \
            Buffer size is provided implicitly when data is written or explicitly when the buffer is configured. Configure the generation so \
            that the Use Only Onboard Memory property is false. Alternatively, you can make sure the number of samples written and/or the size of \
            the configured buffer do not exceed the onboard memory size.",
        -200342: "Script is not in the device memory. Make sure you are referring to a previously written script by its correct \
            name. Also, make sure the script has not been deleted.",
        -200343: "Driver cannot determine the number of samples to read for a continuous task that has not yet started. Start \
            the task explicitly, or specify the number of samples to read in DAQmx Read.",
        -200344: "Requested number of samples per channel is invalid. The number of samples per channel must be an integer multiple \
            of the number of samples per channel increment.",
        -200345: "Event delay is outside of the legal range. Change the value of the delay, and/or verify that the units are correct.",
        -200346: "Event pulse width is outside of the legal range. Change the value of the pulse width, and/or verify that the \
            units are correct.",
        -200347: "Invalid intermediate buffer size. The size of the intermediate buffer must be an integer multiple of the intermediate \
            buffer size increment.",
        -200348: "Scaled Values must be specified for the table scale.",
        -200349: "Prescaled Values must be specified for the table scale.",
        -200350: "Number of Prescaled Values needs to be equal to the number of Scaled Values in the table scale.",
        -200351: "Forward coefficients must be specified for the polynomial scale.",
        -200352: "Physical channel corresponding to the virtual channel specified for cold-junction compensation is already being \
            used for a thermocouple measurement, so it cannot be used as the cold-junction compensation channel.",
        -200353: "Specified property value cannot be used, because it requires resources that are currently in use.",
        -200354: "Specified property value is not a valid terminal name.",
        -200355: "Specified property value cannot be used, because the hardware does not support it.",
        -200356: "Custom scale cannot be created. A saved scale with this name already exists.",
        -200357: "Measurement device cannot acquire data from the sensor in its current configuration. The voltage output range \
            of your sensor does not overlap with the voltage input range of your measurement device. If your measurement device supports different \
            gains or input ranges, try using a lower gain or a wider input range. If the device has a fixed gain/range, you might need to change \
            sensor attribute settings such as Excitation Value or use a measurement device that supports a wider voltage input range.",
        -200358: "An attempt has been made to configure a reference trigger when the sample mode of the sample clock has been \
            configured for continuous sampling. Reference trigger is only applicable for finite sampling. Change the sample mode to finite \
            to use a reference trigger, or do not configure a reference trigger.",
        -200359: "Counter signals cannot be exported, because there is more than one counter channel in the task. Create separate \
            tasks for each counter channel.",
        -200360: "CJC Source has been set to Channel, while the CJC channel has not been specified. Specify the CJC channel, or \
            set CJC Source to a value other than Channel.",
        -200361: "Onboard device memory overflow. Because of system and/or bus-bandwidth limitations, the driver could not read \
            data from the device fast enough to keep up with the device throughput. Reduce your sample rate. If your data transfer method is \
            interrupts, try using DMA or USB Bulk. You can also use a product with more onboard memory or reduce the number of programs your \
            computer is executing concurrently.",
        -200362: "The Overloaded Channels Exist property was not read prior to reading the specified property. The driver retrieves \
            the overload state from the hardware when the application reads the Overloaded Channels Exist property. After the Overloaded Channels \
            Exist property has been read, other information about overloaded channels may be read, such as which channels are overloaded.",
        -200363: "Specified inversion cannot be satisfied, because the hardware does not support it.",
        -200364: "Specified polarity is not supported by the hardware.",
        -200365: "Specified inversion cannot be satisfied, because it requires resources that are currently in use by another \
            route.",
        -200366: "Specified inversion cannot be satisfied, because it requires resources that are currently in use by another \
            route within this task.",
        -200367: "Specified polarity cannot be satisfied, because it requires resources that are currently in use by another route \
            within this task.",
        -200368: "Specified route cannot be satisfied, because the hardware does not support it.",
        -200369: "Specified route cannot be satisfied, because it requires resources that are currently in use by another route.",
        -200370: "Specified route cannot be satisfied, because it requires resources that are currently in use by another route \
            within this task.",
        -200371: "Requested multiple virtual channels that correspond to the same physical channel within a task. A task cannot \
            contain multiple physical channels of a specified type. Use different physical channels for each virtual channel.",
        -200372: "Trigger type requested to be sent as the software trigger is invalid.",
        -200373: "Trigger type requested to be sent as software trigger is not supported for the specified task running on the \
            given device.",
        -200374: "Signal type requested to be exported is not valid.",
        -200375: "Signal type requested to be exported is not supported for the specified task running on the given device.",
        -200376: "Requested creation of a separate channel for each line is not possible when a digital port is specified as the \
            physical channel. Specify a range of digital lines, such as Dev1/port0/line0:7, as the physical channel.",
        -200377: "Requested operation is not supported by the device during a scan. The device only supports operations on front-end \
            channels (for example, ch0, ch1, ... or cjtemp) while scanning. Other operations, such as operations on analog bus channels (such \
            as ab0 and ab1), are not supported by the device during a scan. Make sure your scan list contains only supported operations.",
        -200378: "Custom scale specified does not exist.",
        -200379: "External clock frequency and external clock divisor values result in an invalid cutoff frequency for this device. \
            The relationship between cutoff frequency, external clock frequency, and external clock divisor is: cutoffFreq = extClkFreq / (100 \
            * extClkDiv) Change your external clock frequency or external clock divisor.",
        -200380: "Strain gage calibration procedure has failed. Make sure the strain gages are connected to all the specified \
            strain channels, the strain gage connections are appropriate for their bridge type configurations, the shunt resistor location \
            is specified correctly, and your hardware jumpers (if any) are set up correctly.",
        -200381: "Unable to configure requested delay property given the current clock rate. Make sure the sample clock rate is \
            greater than or equal to the phase shift DMC threshold of your device, or do not configure the delay. Consult your documentation \
            for more information.",
        -200382: "Specified trigger type for pattern match mode could not be configured, because all pattern matchers are already \
            in use.",
        -200383: "Reference Clock Source specified is invalid, given the Sample Clock Source. When Sample Clock Source is anything \
            other than OnboardClock, you must set Reference Clock Source to None, and you cannot export the Reference Clock.",
        -200384: "Static output cannot be performed, because some data lines have already been reserved for a dynamic output.",
        -200385: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200386: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200387: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200388: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200389: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200390: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200391: "Hardware clocking error occurred. If you are using an external sample clock or an external reference clock, \
            make sure it is connected and within the jitter and voltage level specifications. Also, verify that the rate of the external clock \
            matches the specified clock rate. If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200392: "Specified output voltage is not valid with the given sample clock rate. Make sure your output voltage level \
            is compatible with your sample clock rate by altering the output voltage level or the sample clock rate. Consult your documentation \
            for more information.",
        -200393: "You are attempting to write to a read-only register.",
        -200394: "Requested value for the property is invalid, because it is not an unsigned integer. Even though the datatype \
            of the property is a floating point number, the value must be an unsigned integer less than or equal to 9,007,199,254,740,992 (2^53).",
        -200395: "There are no shared trigger lines between the two devices which are acceptable to both devices. While each of \
            these two devices support some shared trigger lines, none of these shared trigger lines work for both devices for the specified \
            property and corresponding value. Consider routing the signal through the I/O connectors of the two devices, if applicable.",
        -200396: "There are no shared trigger lines between the two devices that are acceptable to both devices. While each of \
            the two devices support some shared trigger lines, none of the shared trigger lines work for both devices for the specified source \
            and destination terminals. Consider routing the signal through the I/O connectors of the two devices, if applicable.",
        -200397: "Unable to load NI-DAQmx dynamic link library NICAIU.DLL. Make sure that NI-DAQmx is installed on your computer.",
        -200398: "Unable to find function in NI-DAQmx dynamic link library NICAIU.DLL. The DLL exists on your computer, but the \
            version is incorrect. Install the correct version of the DLL on your computer.",
        -200399: "No extended error information is available for the last error code. It is possible that there was a problem \
            initializing the internal errors database. Please contact National Instruments Technical Support.",
        -200400: "Requested waveform length is invalid, because the number of samples is not an integer multiple of the waveform \
            length increment.",
        -200401: "Number of points to compute over the range of x values is not positive. Specify a value greater than 0 for this \
            input.",
        -200402: "Order of the reverse polynomial to compute is not positive. Specify a value greater than 0 for this input.",
        -200403: "Order of the reverse polynomial to compute is less than or equal to the number of points to compute over the \
            range of x values. Reduce the order of the reverse polynomial or increase the number of points to compute over the range of x values.",
        -200404: "Forward and Reverse Coefficients for a polynomial scale are not specified. Each of these two sets of coefficients \
            must contain at least one term. If only one set of coefficients is available, use the Compute Reverse Polynomial Coefficient utility \
            to calculate the other set of coefficients.",
        -200405: "Forward Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least \
            one term. If the coefficients are not available, you can pass the supplied Reverse Coefficients to the Compute Reverse Polynomial \
            Coefficients utility to calculate the required Forward Coefficients.",
        -200406: "Reverse Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least \
            one term. If the coefficients are not available, use the Compute Reverse Polynomial Coefficient utility to calculate the required \
            coefficients from the supplied Forward Coefficients.",
        -200407: "Forward Coefficients for a polynomial scale are all set to zero. At least one of these coefficients must be \
            non-zero.",
        -200408: "Reverse Coefficients for a polynomial scale are all set to zero. At least one of these coefficients must be \
            non-zero.",
        -200409: "Slope for a linear scale is set to zero. The slope must be non-zero.",
        -200410: "Requested record number is invalid. Use the Records Done property to find out how many records are available. \
            Record numbers start at 0. Use -1 for all available records.",
        -200411: "AC coupling is not allowed with 50 Ohm impedance for this device. Use DC coupling, or configure a different \
            impedance setting.",
        -200412: "Requested analog input attenuation is invalid.",
        -200413: "Insufficient onboard memory for requested Number of Records and Samples per Channel combination. Reduce the \
            Number of Records and/or Samples per Channel.",
        -200414: "Requested sample clock source is invalid.",
        -200415: "Requested reference clock source is invalid.",
        -200416: "Multiple records are not available with RIS.",
        -200417: "TDC is not enabled during RIS mode. TDC must be enabled when the digitizer is in the RIS mode. Enable TDC, or \
            do not use RIS.",
        -200418: "Requested immediate trigger type while in RIS mode. Immediate triggering is not compatible with the RIS mode. \
            Select a different trigger type, or do not use RIS.",
        -200419: "Requested Read Position is invalid in RIS mode.",
        -200420: "Requested sample rate exceeds maximum real-time sample rate. If you want a higher sampling rate and have a repetitive \
            signal, enable RIS.",
        -200421: "Requested Hysteresis is not valid with the configured Trigger Level and AI Minimum. Configure the task so the \
            following formula is satisfied: Trigger Level - Hysteresis > AI Minimum",
        -200422: "Requested Trigger Level is not valid with the configured AI Minimum and AI Maximum. Configure the instrument \
            so the following formula is satisfied: AI Minimum < Trigger Level < AI Maximum",
        -200423: "Requested window trigger level is not valid with the configured AI Minimum and AI Maximum. Configure the instrument \
            so the following formula is satisfied: AI Minimum < Window Trigger Level < AI Maximum",
        -200424: "Requested video trigger line number is incompatible with the chosen video signal format.",
        -200425: "Requested hysteresis is not valid with the configured trigger level and AI Maximum. Configure the task so the \
            following formula is satisfied: Trigger Level + Hysteresis < AI Maximum",
        -200426: "Requested impedance for the external trigger is invalid. Specify an impedance that is appropriate for the external \
            trigger, or choose a different trigger source.",
        -200427: "Configured reference clock rate is invalid. The reference clock rate must be within the valid range and a multiple \
            of the increment value.",
        -200428: "Value passed to the Task/Channels In control is invalid. The value must refer to a valid task or valid virtual \
            channels.",
        -200429: "Value passed to the Task/Channels In control is an empty string (or I/O control). The value must refer to a \
            valid task or valid channels.",
        -200430: "I/O type of the physical channel does not match the I/O type required for the virtual channel you are creating.",
        -200431: "Selected physical channel does not support the measurement type required by the virtual channel you are creating. \
            Create a channel of a measurement type that is supported by the physical channel, or select a physical channel that supports the \
            measurement type.",
        -200432: "Selected physical channel does not support the output type required by the virtual channel you are creating. \
            Create a channel of an output type that is supported by the physical channel, or select a physical channel that supports the output \
            type.",
        -200433: "Scaled Values for a table scale must contain at least two values.",
        -200434: "Prescaled Values for a table scale must contain at least two values.",
        -200435: "Delay from sample clock is not available when an external convert source is specified. Change the convert source \
            to onboard clock, or do not configure the delay from sample clock.",
        -200436: "Start trigger delay is not available when an external sample clock source is specified. Change the sample clock \
            to onboard clock, or do not configure the start trigger delay.",
        -200437: "External calibration constants are invalid. Perform an external calibration. Contact National Instruments Technical \
            Support if you need additional information.",
        -200438: "Invalid calibration area selected. Select self-calibration or external calibration.",
        -200439: "Requested operation only can be used during an external calibration session.",
        -200440: "Requested calibration close action is invalid. Select Store or Abort.",
        -200441: "Unable to detect the external stimulus frequency. Verify that the external stimulus is properly connected and \
            has the correct frequency and amplitude.",
        -200442: "Unable to synchronize to the external stimulus frequency. Verify that the external stimulus has the correct \
            frequency, amplitude, and stability. Consult the documentation for the calibration procedure for valid ranges.",
        -200443: "Attempt to store calibration constants without completing all the necessary external calibration steps. Refer \
            to the documentation for the calibration procedure. Verify that all necessary steps are performed before closing the external \
            calibration session.",
        -200444: "Invalid physical channel selected for calibration.",
        -200445: "Requested calibration function is not supported by the device.",
        -200446: "External stimulus voltage read was outside the expected range. Verify that the external stimulus voltage is \
            properly connected and has the correct amplitude.",
        -200447: "Units for the channel must be set to From Custom Scale when a custom scale is used with a channel.",
        -200448: "DAC Range High is not equal to the DAC Reference Voltage Value. When you do not set the DAC Range High property, \
            the driver always makes sure it is equal to the DAC Reference Voltage value. If you do set the DAC Range High property make sure \
            DAC Range High and DAC Reference Voltage Value are equal.",
        -200449: "DAC Range Low must be equal to either the negative DAC Reference Voltage Value or to zero. If you do not set \
            the DAC Range Low property, the driver sets it for you. Otherwise, make sure DAC Range Low is equal to either the negative DAC \
            Reference Voltage Value or to zero.",
        -200450: "Specified property cannot be set while the task is running.",
        -200451: "You can get the specified property only while the task is committed or running.",
        -200452: "Specified property is not supported by the device or is not applicable to the task.",
        -200453: "Specified timeout value is not supported. Supported timeout values are 0 (try or check once and return), positive \
            numbers up to 4294967, and -1 (try or check until success or error).",
        -200454: "You cannot get the specified property, because the task is not a buffered output task.",
        -200455: "You cannot get the specified property, because the task is not a buffered input task.",
        -200456: "Specified property is not supported, because the task is not an output task.",
        -200457: "Specified property is not supported, because the task is not an input task.",
        -200459: "Write failed, because there are no output channels in this task to which data can be written.",
        -200460: "Read failed, because there are no channels in this task from which data can be read.",
        -200461: "Specified channel name is invalid.",
        -200462: "Generation cannot be started because the output buffer is empty. Write data before starting a buffered generation. \
            The following actions can empty the buffer: changing the size of the buffer, unreserving a task, setting the Regeneration Mode \
            property, changing the Sample Mode, or configuring retriggering.",
        -200463: "Specified read or write operation failed, because the number of lines in the data for a channel does not match \
            the number of lines in the channel. If you are using the Digital Waveform datatype, make sure the number of lines in the digital \
            waveform matches the number of lines in the channel. If you are using boolean data, make sure the array dimension for lines in the \
            data matches the number of lines in the channel.",
        -200464: "If performing a Write operation, the operation cannot be performed, because the number of channels in the specified \
            data does not match the number of channels in this task. Adjust the data to match the number of channels in this task. If you are \
            performing a read operation, the operation cannot be performed because this DAQmx Read only returns data from a single channel, and \
            there are multiple channels in this task. Use the multichannel DAQmx Read.",
        -200465: "Specified digital channel contains more bits than what is supported by DAQmx Port Write. With the U8 version, \
            channels must contain 8 bits or less; while for the U32 version, channels must contain 32 bits or less.",
        -200466: "Specified digital channel contains more bits than what is supported by DAQmx Port Read. With the U8 version, \
            channels must contain 8 bits or less; while for the U32 version, channels must contain 32 bits or less.",
        -200467: "Specified string is not valid, because it is empty.",
        -200469: "Specified channel cannot be loaded, because it was saved with an incompatible, more recent version of NI-DAQ. \
            Create the channel again, or upgrade NI-DAQ to a version compatible with the version used to save the channel. Consult the documentation \
            for the version of NI-DAQ used to create the channel for more details.",
        -200470: "Specified task cannot be loaded, because it was saved with an incompatible, more recent version of NI-DAQ. Create \
            the task again, or upgrade NI-DAQ to a version compatible with the version used to save the task. Consult the documentation for \
            the version of NI-DAQ used to create the task for more details.",
        -200472: "Write cannot be performed when the auto start input to DAQmx Write is false, and timing for the task is not \
            configured or Timing Type is set to On Demand. Set auto start to true, or configure timing and specify Timing Type other than On \
            Demand.",
        -200473: "Read cannot be performed when the Auto Start property is false and the task is not running or committed. Start \
            the task before reading, or set Auto Start to true.",
        -200474: "Specified operation did not complete, because the specified timeout expired.",
        -200475: "Specified operation can be performed only when the task is running. Start the task before requesting this operation.",
        -200477: "Specified operation cannot be performed when there are no devices in the task.",
        -200478: "Specified operation cannot be performed when there are no channels in the task.",
        -200479: "Specified operation cannot be performed while the task is running.",
        -200481: "Specified device cannot be added to the task, because it is already in the task.",
        -200482: "Specified device is not in the task.",
        -200483: "Specified virtual channel cannot be saved, because a virtual channel with that name already exists in Data Neighborhood \
            in MAX. Save the virtual channel under a different name, or specify that the existing virtual channel should be replaced.",
        -200484: "Specified task cannot be saved, because a task with that name already exists in Data Neighborhood in MAX. Save \
            the task under a different name, or specify that the existing task should be replaced.",
        -200485: "The specified task cannot be loaded, because it is not in Data Neighborhood. Check Data Neighborhood in MAX. \
            Look for similar characters, such as the capital letter O and the number zero.",
        -200486: "Specified channel is not in the task.",
        -200488: "Specified virtual channel cannot be added to the task, because it does not exist. You cannot specify a physical \
            channel. Instead, create a virtual channel using the DAQ Assistant or DAQmx Create Virtual Channel, and then add the virtual channel \
            to the task.",
        -200489: "Specified channel cannot be added to the task, because a channel with the same name is already in the task.",
        -200490: "Sample value detected outside of the specified range.",
        -200491: "Reserved parameter must be zero.",
        -200492: "Reserved parameter must be NULL.",
        -200493: "Reserved character string parameter must be NULL or an empty string.",
        -200494: "Specified task cannot be loaded, because it requires a device that supports timing, and the associated device \
            does not support timing. Create a new task without timing, or associate this task with a device that supports timing.",
        -200495: "An intermediate acquisition buffer has overflowed. The driver was unable to read samples from the intermediate \
            buffer fast enough to prevent the buffer from overflowing.",
        -200496: "Pattern contains an invalid character.",
        -200497: "Attempted to enable output data lines that were not previously disabled. Make sure that you are enabling data \
            lines for output only after explicitly disabling them.",
        -200498: "Syntax for a range of objects in the input string is invalid. For ranges of objects, specify a number immediately \
            before and after every colon (:) in the input string. Or, if a name is specified after the colon, it must be identical to the \
            name specified immediately before the colon. Colons are not allowed within the names of the individual objects.",
        -200499: "Value passed is not between 0 and 4,294,967,295 (unsigned 32-bit integer).",
        -200500: "Error code could not be found. Reinstalling the driver might fix the issue. Otherwise, contact National Instruments \
            technical support.",
        -200501: "EEPROM contains an invalid calibration date and/or time. The calibration data in the EEPROM might have been \
            corrupted. Perform an external calibration, perform a self-calibration, or contact National Instruments Technical Support.",
        -200502: "A measurement taken during adjustment of main path pre-amplifier offset produced an invalid calibration constant. \
            Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and \
            repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments \
            Technical Support.",
        -200503: "A measurement taken during adjustment of main path pre-amplifier gain produced an invalid calibration constant. \
            Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and \
            repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments \
            Technical Support.",
        -200504: "A measurement taken during adjustment of main path post-amplifier gain and offset produced an invalid calibration \
            constant. Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, \
            and repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National \
            Instruments Technical Support.",
        -200505: "A measurement taken during adjustment of direct path gain produced an invalid calibration constant. Make sure \
            that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the \
            calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments \
            Technical Support.",
        -200506: "A measurement taken during adjustment of main path output impedance produced an invalid calibration constant. \
            Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and \
            repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National \
            Instruments Technical Support.",
        -200507: "A measurement taken during adjustment of direct path output impedance produced an invalid calibration constant. \
            Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and \
            repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National \
            Instruments Technical Support.",
        -200508: "A measurement taken during adjustment of the oscillator frequency produced an invalid calibration constant. \
            Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and \
            repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National \
            Instruments Technical Support.",
        -200509: "A measurement taken during adjustment of calibration ADC produced an invalid calibration constant. Make sure \
            that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and repeat the \
            calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments \
            Technical Support.",
        -200510: "Requested an invalid configuration value for adjusting the main path pre-amplifier offset. Refer to the documentation \
            for a list of valid configuration values.",
        -200511: "Requested an invalid configuration value for adjusting the main path pre-amplifier gain. Refer to the documentation \
            for a list of valid configuration values.",
        -200512: "Requested an invalid configuration value for adjusting the main path post-amplifier gain and offset. Refer to \
            the documentation for a list of valid configuration values.",
        -200513: "Requested an invalid configuration value for adjusting the main path output impedance. Refer to the documentation \
            for a list of valid configuration values.",
        -200514: "Requested an invalid configuration value for adjusting the direct path output impedance. Refer to the documentation \
            for a list of valid configuration values.",
        -200515: "Specified number of reads to average from the calibration ADC is invalid. The number of reads to average must \
            be greater than 0.",
        -200516: "Calibration constants stored in the EEPROM produced an invalid value for the gain DAC. An incorrect calibration \
            might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, perform \
            a self-calibration, or contact National Instruments Technical Support.",
        -200517: "Calibration constants stored in the EEPROM produced an invalid value for the offset DAC. An incorrect calibration \
            might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, or \
            a self-calibration, or contact National Instruments Technical Support.",
        -200518: "Calibration constants stored in the EEPROM produced an invalid value for the oscillator phase DAC. An incorrect \
            calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, \
            perform a self-calibration, or contact National Instruments Technical Support.",
        -200519: "Calibration constants stored in the EEPROM produced an invalid value for the oscillator frequency DAC. An incorrect \
            calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, \
            or contact National Instruments Technical Support.",
        -200520: "Calibration constants stored in the EEPROM and used to adjust reads from the cal ADC are invalid. An incorrect \
            calibration might have been performed, or the calibration data in the EEPROM might have been corrupted. Perform an external calibration, \
            or contact National Instruments Technical Support.",
        -200521: "A measurement taken during adjustment of the oscillator phase DAC produced an invalid calibration constant. \
            Make sure that the measured values passed to the calibration VI or function are correct. Verify the calibration procedure, and \
            repeat the calibration. If the problem persists, there might be a hardware malfunction with your device. Contact National Instruments \
            Technical Support.",
        -200522: "A self-calibration cannot be performed during external calibration.",
        -200523: "Read cannot be performed because this version of DAQmx Read only returns data from a single channel, and there \
            are multiple channels in the task. Use the multichannel version of DAQmx Read.",
        -200524: "Write cannot be performed, because the number of channels in the data does not match the number of channels \
            in the task. When writing, supply data for all channels in the task. Alternatively, modify the task to contain the same number \
            of channels as the data written.",
        -200525: "Read cannot be performed because this version of DAQmx Read does not match the type of channels in the task. \
            Use the version of DAQmx Read that corresponds to the channel type.",
        -200526: "Write cannot be performed because this version of DAQmx Write does not match the type of channels in the task. \
            Use the version of DAQmx Write that corresponds to the channel type.",
        -200527: "Requested values of the Minimum and Maximum properties for the counter channel are not supported for the given \
            type of device. The values that can be specified for Minimum and Maximum depend on the counter timebase rate.",
        -200528: "Requested line grouping is invalid. Either choose one channel for all lines or one channel for each line as \
            the line grouping.",
        -200529: "Unexpected identifier following the switch operation in the connection list. Switch operations must be separated \
            by a comma inside the connection list.",
        -200530: "Unexpected identifier following the relay name in the relay list. Relay names must be separated by a comma inside \
            the relay list.",
        -200531: "Relay name is not specified in the list entry.",
        -200532: "Unexpected identifier following switch channel name.",
        -200533: "Identifier found in the script is too long. Use identifiers with no more than 511 characters.",
        -200534: "Waveform name is too long. Use waveform names with no more than 511 characters.",
        -200535: "Specified value is larger than the maximum value supported for this property.",
        -200536: "Specified value is smaller than the minimum value supported for this property.",
        -200537: "Supplied forward and reverse coefficients yield inconsistent results when they are used for computations related \
            to this property. In other words, using the result of the forward scale as input to the reverse scale does not yield the original \
            data. Based on the forward coefficients, the value for the property is invalid. Supply forward and reverse coefficients that yield \
            consistent results.",
        -200538: "Action requested is invalid.",
        -200539: "Device does not support analog writes with multiple samples per channel. To output multiple samples, call DAQmx \
            Analog Single Sample Write multiple times.",
        -200540: "DAC Reference Voltage Value is not set. When the DAC Reference Voltage Source property for a channel is set \
            to External, the DAC Reference Voltage Value property must be set. Set the DAC Reference Voltage Value property so the value matches \
            the reference voltage source connected to your device. Alternatively, consider using the internal DAC reference voltage source \
            available on the device.",
        -200541: "Last Self Calibration Date/Time has not been stored on the device by NI-DAQmx. Self-calibrate the board using \
            NI-DAQmx. Alternatively, externally calibrate the board using NI-DAQmx, and then call DAQmx Restore Last External Calibration Constants.",
        -200542: "Last Self Calibration Temperature has not been stored on the device by NI-DAQmx. Self-calibrate the board using \
            NI-DAQmx. Alternatively, externally calibrate the board using NI-DAQmx, and then call DAQmx Restore Last External Calibration Constants.",
        -200543: "Last External Calibration Date/Time has not been stored on the device by NI-DAQmx. Externally calibrate the \
            board using NI-DAQmx.",
        -200544: "Last External Calibration Temperature has not been stored on the device by NI-DAQmx. Externally calibrate the \
            board using NI-DAQmx.",
        -200545: "Self-calibration failed. The self-calibration date has not changed. Disconnect the device from external signals, \
            as they might introduce noise. Externally calibrate the device to recalibrate the onboard voltage reference that is used for \
            self-calibration.",
        -200546: "External calibration failed, and the external calibration data has not been changed. Make sure that the reference \
            signal used for the calibration is stable and that the voltage matches the value specified to the calibration software. Disconnect \
            the device from any external signals that might be introducing noise.",
        -200547: "DAQmx Write failed, because a previous DAQmx Write automatically configured the output buffer size. The buffer \
            size is equal to the original number of samples written per channel, so no more data can be written prior to starting the task. \
            Start the generation before the second DAQmx Write, or set Auto Start to true in all occurences of DAQmx Write. To incrementally \
            write into the buffer prior to starting the task, call DAQmx Configure Output Buffer before the first DAQmx Write.",
        -200548: "Requested coupling type is only valid when the trigger source is an external trigger channel.",
        -200549: "Self-calibration constants are invalid. Perform a self-calibration. Contact National Instruments Technical Support \
            if you need additional information.",
        -200550: "Hardware clocking error occurred. If you are using an external reference or sample clock, make sure it is connected \
            and within the jitter and voltage level specifications. Also, verify that its rate matches the specified clock rate. If you are \
            generating your clock internally, please contact National Instruments Technical Support.",
        -200551: "Hardware clocking error occurred. If you are using an external reference or sample clock, make sure it is connected \
            and within the jitter and voltage level specifications at all times. Also, verify that its rate matches the specified clock rate. \
            If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200552: "Specified string is not valid, because it contains an invalid character.",
        -200553: "Specified string is not valid, because its first character is a space character.",
        -200554: "Specified string is not valid, because its last character is a space character.",
        -200555: "Specified string is not valid, because its first character is an underscore.",
        -200556: "You only can get the specified property while the task is committed or while the task is running. Commit or \
            start the task prior to getting the property.",
        -200557: "Specified property cannot be set while the task is running. Set the property prior to starting the task, or \
            stop the task prior to setting the property.",
        -200558: "One task cannot contain multiple independent devices. Create one task for each independent device.",
        -200559: "Task cannot contain a channel with the specified channel type, because the task already contains channels with \
            a different channel type. Create one task for each channel type.",
        -200560: "Wait Until Done did not indicate that the task was done within the specified timeout. Increase the timeout, \
            check the program, and make sure connections for external timing and triggering are in place.",
        -200561: "Attempted writing analog data that is too large or too small. Change Minimum Value and Maximum Value to reflect \
            the range of the channel.",
        -200562: "Attempted writing digital data that is not supported.",
        -200563: "Specified digital channel contains more bits than supported by the 8-bit version of DAQmx Port Read. Use a version \
            of DAQmx Port Read that supports wider digital ports.",
        -200564: "Specified digital channel contains more bits than supported by the 32-bit version of DAQmx Read. Use a version \
            of DAQmx Read that returns an array of Boolean values or digital waveforms.",
        -200565: "Specified digital channel contains more bits than supported by the 8-bit version of DAQmx Port Write. Use the \
            version of DAQmx Port Write that supports wider digital ports.",
        -200566: "Specified digital channel contains more bits than supported by the 32-bit version of DAQmx Port Write.",
        -200567: "Generation cannot be started, because the buffer size was changed since the last write, and this change caused \
            data to be lost. Write data after changing the buffer size.",
        -200568: "Generation cannot be started, because the Regeneration Mode property was changed since the last write, and this \
            change caused data to be lost. Write data after changing the Regeneration Mode property.",
        -200569: "Type of channel collection used to access the specified channel does not match the channel type. Access the \
            channel through the channel collection that matches the channel type.",
        -200570: "Requested channel index is invalid. The value of the index must be between one and the number of channels in \
            the task.",
        -200571: "Input Source Select property is set to an internal source for channels in different channel groups. On this \
            device, only one channel group at a time can be configured to use an internal source. Refer to the documentation for details.",
        -200572: "Input Source Select property is set differently for channels in one channel group on a device that supports \
            only identical settings within a channel group. Refer to the documentation for more details.",
        -200573: "Input Source Select property is set to different internal sources on some channels. On this device, Input Source \
            Select must be set to the same value for all channels with internal sources. Refer to the documentation for more details.",
        -200574: "Driver cannot complete the route, because the only way to make the route requires a trigger bus line, and no \
            trigger bus has been configured in MAX for this device. If you have a PXI chassis, make sure it has been properly identified in \
            MAX. If you are using a PCI device, create a RTSI cable in MAX that includes your PCI device even if you are not using any RTSI cables.",
        -200575: "Requested value for Samples per Channel is too high when a reference trigger is used. In this case, Samples \
            per Channel cannot exceed the sum of Pretrigger Samples per Channel and the maximum Post-trigger Samples per Channel. Reduce Samples \
            per Channel. Alternatively, consider performing an acquisition with Continuous Sample Mode, or increase the Pretrigger Samples per \
            Channel.",
        -200576: "CJC Source cannot be set to Built-In for the specified thermocouple channel. The physical channel does not support \
            a built-in CJC temperature sensor. If your hardware contains a CJC temperature sensor on the physical channel corresponding to \
            the built-in CJC source, make sure that the hardware configuration (including any accessories and/or terminal blocks) is correct. \
            Alternatively, specify a different CJC Source, or use hardware with a built-in CJC temperature sensor.",
        -200577: "Requested AI Minimum value is too large.",
        -200578: "Requested AI Minimum value is too small.",
        -200579: "Requested AI Maximum value is too large.",
        -200580: "Requested AI Maximum value is too small.",
        -200581: "Specified property is not supported, because Reference Clock Source is None.",
        -200582: "Values for AO channel properties lead to an output voltage that exceeds the maximum for the device.",
        -200583: "Values of the AO channel properties lead to an output voltage that is less than the minimum for the device.",
        -200584: "Write failed, because the number of samples to write per channel is invalid. The number of samples to write \
            per channel must be an integer multiple of the samples to write per channel increment.",
        -200585: "Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within \
            specifications. If you are generating your sample clock internally, please contact National Instruments Technical Support.",
        -200586: "Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within \
            specifications. If you are generating your sample clock internally, please contact National Instruments Technical Support.",
        -200587: "Requested operation could not be performed, because the specified digital lines are either reserved or the device \
            is not present in NI-DAQmx. It is possible that these lines are reserved by another task, the device is being used through the \
            Traditional NI-DAQ interface, or the device is being reset. You might also get the error if the specified resource is currently in \
            use by LabVIEW network variables bound to the DAQ Channel, or if the DAQ Channel is being used in any OPC Client software. \
            If you are using these lines with another task, wait for the task to complete. If you are using the device through the Traditional \
            NI-DAQ interface, and you want to use it with NI-DAQmx, reset (initialize) the device using the Traditional NI-DAQ interface. \
            If you are resetting the device, wait for the reset to finish.",
        -200588: "Specified event handler cannot be removed, because it is installed on a different NI-DAQmx object. Remove the \
            event handler from the NI-DAQmx object on which it was installed.",
        -200589: "Specified event handler cannot be removed, because it has already been removed.",
        -200590: "Specified event handler cannot be removed, because it is invalid. It has never been installed on this or any \
            other NI-DAQmx object.",
        -200591: "Negative buffer size was supplied. The buffer size must be zero or greater.",
        -200592: "Given range in the input string contains too many objects. Check the string. If necessary, split the input string \
            into smaller ranges.",
        -200593: "Value of this property cannot be determined until the containing task is verified. Before attempting to get \
            the value of this property, you must make sure the task has been verified. You can do this by starting the task, using the task \
            control method to verify the task, reading from the task if the Read Auto Start property is true, or writing to the task and \
            specifying true for the auto start parameter.",
        -200594: "Value passed for the direction parameter is invalid. Use one of the values of the corresponding enumeration.",
        -200595: "Invalid identifier at the beginning of the switch operation in the list entry.",
        -200596: "Channels in the switch operation span different devices.",
        -200597: "Specified output operation cannot be satisfied, because it requires lines that are currently in use by another \
            output operation.",
        -200598: "Repetition of a number in the Prescaled Values is invalid for input operations.",
        -200599: "Repetition of a number in Scaled Values is invalid for output operations.",
        -200600: "NI-DAQmx cannot generate virtual channel names for some of the physical channels specified, because the numeric \
            suffix of the resulting channel names would be too large. Either explicitly specify a virtual channel name for each physical channel \
            name, or decrease the numeric suffix of the last set of virtual channel names.",
        -200601: "Property not supported by this scale type.",
        -200602: "Prescaled Minimum cannot be equal to Prescaled Maximum for input operations.",
        -200603: "Scaled Minimum cannot be equal to Scaled Maximum for output operations.",
        -200604: "NULL pointer was passed for a required parameter.",
        -200605: "Given range in the input string contains a number that is too large. Check the string. Use smaller numbers in \
            the range, or replace the range with a comma-separated list.",
        -200606: "Requested channel index is invalid. The value of the index must be between one and the number of channels in \
            the task.",
        -200607: "Two signals cannot be simultaneously exported on the same terminal.",
        -200608: "Acquisition cannot be started, because the selected buffer size is too small. Increase the buffer size.",
        -200609: "Generation cannot be started, because the selected buffer size is too small. Increase the buffer size.",
        -200610: "Requested sample clock source is invalid for output. The specified sample clock source terminal is only supported \
            for input.",
        -200611: "Operation cannot be performed, because there are no channels of the requested type in the task.",
        -200612: "Requested channel index is invalid. The value of the index must be between 0 and the number of channels in the \
            task minus one.",
        -200613: "Acquisition has been stopped to prevent an input buffer overwrite. Your application was unable to read samples \
            from the buffer fast enough to prevent new samples from overwriting unread data. To avoid this error, you can do any of the following: \
            1. Increase the size of the buffer. 2. Increase the number of samples you read each time you invoke a read operation. \
            3. Read samples more often. 4. Reduce the sample rate. 5. If your data transfer method is interrupts, try using DMA or USB Bulk. \
            6. Reduce the number of applications your computer is running concurrently. In addition, if you do not need to read every sample \
            that is acquired, use the Relative To and Offset properties to read the desired samples.",
        -200614: "Combination of Samples to Read, Position, and Offset results in an attempt to read past the end of the record. \
            You only can read samples within the record.",
        -200615: "Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within \
            the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. \
            If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200616: "Specified asynchronous operation handle is invalid.",
        -200617: "Output generation was aborted by the reverse power protection circuitry of the device. Either the output signal \
            exceeded the output power limit, or power was being driven back into the output of the device by an external source. Correct the \
            problem, then generate the signal again.",
        -200618: "Analog input virtual channels cannot be created out of order with respect to their physical channel numbers \
            for the type of analog device you are using. For example, a virtual channel using physical channel ai0 must be created before a \
            virtual channel with physical channel ai1.",
        -200619: "Chassis cannot be used for more than one scanning operation at the same time. Do only one scanning operation, \
            or combine multiple scanning operations into a single operation.",
        -200620: "Requested multiple virtual channels that correspond to the same analog input physical channel within a single \
            task. A task cannot contain multiple analog input physical channels for this type of device. Use different physical channels for \
            each virtual channel.",
        -200621: "Onboard device memory underflow. Because of system and/or bus-bandwidth limitations, the driver could not write \
            data to the device fast enough to keep up with the device output rate. Reduce your sample rate. If your data transfer method is \
            interrupts, try using DMA or USB Bulk. You can also reduce the number of programs your computer is executing concurrently.",
        -200622: "Requested number of samples to write is invalid. Change the number of samples to be written to a number equal \
            to or greater than zero.",
        -200623: "Device has shut down because a sensor on the device detected a temperature above the device's maximum recommended \
            operating temperature. To use the device again, either turn the chassis/computer off until the device has cooled, or ensure the \
            device has cooled, and reset the device (either programmatically or through Measurements & Automation Explorer).",
        -200624: "You have not specified an active channel when getting a property. Specify a single line as the active physical \
            channel.",
        -200625: "You have specified more than one line as the active physical channel when getting a property. Specify a single \
            line.",
        -200626: "An empty physical channel has been specified within the power up states array. Specify a correct physical channel.",
        -200627: "Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within \
            the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. \
            If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200628: "Pause and reference triggers are both configured, which is not supported in this task.",
        -200629: "Requested different values for properties that must have equal values on this device.",
        -200630: "Requested write offset is invalid, because it is not an integer multiple of the write increment.",
        -200631: "Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within \
            the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. \
            If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200632: "Hardware clocking error occurred. If you are using an external sample clock, make sure it is connected and within \
            the jitter and voltage level specifications. Also, verify that the rate of the external clock matches the specified clock rate. \
            If you are generating your clock internally, please contact National Instruments Technical Support.",
        -200633: "Script name is the same as an existing waveform name. Make sure that the script name is different from the names \
            of previously written or allocated waveforms.",
        -200634: "Waveform name is the same as an existing script name. Make sure that the waveform name is different from the \
            names of previously written scripts.",
        -200635: "You have attempted to control a Watchdog Task, but the task supplied was not a Watchdog Task.",
        -200636: "For this device, any connection specified in the scan list must wait for a trigger (;). If your scan list contains \
            an action sequence similar to ch0->com0 & or ch0->com0 &&, change the action sequence to ch0->com0;",
        -200637: "For this device, an action separator (& or &&) is required after breaking a connection in the scan list. If \
            your scan list contains an action sequence similar to ~ch0->com0;, change the action sequence to ~ch0->com0 & or ~ch0->com0 &&",
        -200638: "For this device, two consecutive wait for triggers are not supported after any connection in the scan list. \
            If your scan list contains an action sequence similar to ch0->com0;;, change the action sequence to ch0->com0;.",
        -200639: "For this device, connections specified in the scan list must be disconnected before making new connections. \
            If your scanlist contains an action sequence similar to ch0->com0;;, change the action sequence to ch0->com0; ~ch0->com0",
        -200640: "For this device, send advance complete (<sac>) is not supported after any wait for triggers (;) in the scan \
            list. If your scan list contains an action sequence similar to ch0->com0; <sac>, change the action sequence to ch0->com0;",
        -200641: "Property cannot be set separately for each line. When setting this property, specify a virtual channel as the \
            active channel.",
        -200642: "You have not specified an active channel when getting a property. Specify a single line as the active channel.",
        -200643: "You have specified more than one line when getting a property. Specify a single line as the active channel.",
        -200644: "Attempt to reset watchdog timer failed, because the timer had already expired. Clear expiration of the watchdog \
            timer, or configure a longer watchdog timer timeout.",
        -200645: "Attempt to set the digital filter interval failed, because another task has already configured a different digital \
            filter interval. Use the same digital filter interval in the two tasks, or wait for the other task to finish before starting or \
            committing this task.",
        -200646: "Some of the physical channels in the task are configured for different filter intervals, which is not supported \
            by this type of device. Configure all lines in the task to use the same digital filter interval.",
        -200647: "Specified physical channel does not support digital input. Change the direction of the task, use another terminal, \
            or use another device. To read from digital output lines, create a digital output task and use DAQmx Read.",
        -200648: "Device identifier of the physical channel specified is not the same as the device used in the task. Use only \
            the physical channels on the device used in the task.",
        -200649: "Specified a physical channel for change detection that is not contained by any channel in the task. Use only \
            physical channels already contained by a channel, or create an additional channel containing the desired physical channel .",
        -200650: "Attempt to set programmable powerup state failed, because the specified physical channel only supports digital \
            input, and the programmable powerup state does not apply.",
        -200651: "Attempt to set watchdog timer expiration state failed, because the specified physical channel only supports \
            digital input, and watchdog timer expiration state does not apply.",
        -200652: "Attempt to set programmable powerup state failed, because only some of the channels from the port were specified. \
            For this type of device, you must specify programmable powerup state for entire ports.",
        -200653: "Attempt to set programmable powerup state failed, because some of the lines in a port were tristated and others \
            were not. For this type of device, programmable powerup states of all lines in a port have to be either tristated or not tristated.",
        -200654: "Attempt to set watchdog timer expiration state failed, because some of the lines in a port were tristated, and \
            others were not. For this type of device, watchdog timer expiration states of all lines in a port have to be either tristated or \
            not tristated.",
        -200655: "Attempted to read more samples than what was configured in the acquisition. Restart the acquisition, increase \
            the Samples Per Channel property, or set the Sample Mode property to Continuous Samples.",
        -200656: "Operation failed, because an attempt was made to use only the onboard memory for generation when regeneration \
            of data was not allowed. Set the Regeneration Mode property to Allow Regeneration or set the Use Only Onboard Memory property to \
            false.",
        -200657: "Attempt to get property failed, because you specified multiple channels, and the property has different values \
            for different channels. Get this property one channel at a time.",
        -200658: "Attempt to get property failed, because your task contains multiple channels, and the property has different \
            values for different channels. Get this property one channel at a time using Active Channel to specify each individual channel.",
        -200659: "Attempt to get property failed, because the single channel you specified corresponds to multiple physical channels, \
            and the property has different values for those different physical channels. Get this property one physical channel at a time. \
            For digital channels, you might have to specify a single digital line.",
        -200660: "Requested Sample Clock Rate is not available because this task shares the Sample Clock Source or the Sample \
            Clock Timebase with another task. The other task has already programmed one of those properties in a manner inconsistent with the \
            requested Sample Clock Rate. Specify a Sample Clock Rate consistent with the settings in the other task, or change the settings in \
            the other task. Refer to documentation for more detailed information.",
        -200661: "Requested operation is not supported because the Reference Clock Source is None",
        -200662: "Attempt to create a watchdog timer task failed because the device does not support the feature, or the wrong \
            device type was specified. For NI CompactDAQ devices supporting this feature, specify the chassis name on which to create a watchdog \
            timer task.",
        -200663: "Attempt to set programmable powerup states failed because the device does not support the feature.",
        -200664: "Specified operation cannot be performed because the task has not been started, committed, or reserved. Call \
            DAQmx Start or DAQmx Control with action set to Commit or Reserve prior to requesting this operation.",
        -200665: "Expiration states requested are not supported by the lines in the port. For this device, the Watchdog Timer \
            Expiration States must be either No Change for all lines in a port or a combination of values other than No Change for all lines \
            in a port. For example, the combination of No Change for one line and High for another line is not supported, while a value of Low \
            for one line and High for another line is supported.",
        -200666: "Attempt to configure a port or any of its lines for input failed, because this port is currently configured \
            for digital output by the watchdog timer. Choose another port, or modify the watchdog timer task to set the expiration state of \
            the port to Tristate or No Change.",
        -200667: "Attempt to configure a port or any of its lines to have an expiration state of Output failed, because the port \
            or some of its lines are currently reserved for use by an input task. Set the expiration state of the port to Tristate or No Change, \
            or choose a different port for digital input.",
        -200668: "Requested value is not a supported value for Watchdog Timer Timeout. Use special value -1.0 to indicate that \
            the internal timer should be disabled, and the watchdog timer will expire based on the external expiration trigger, or specify \
            another valid value.",
        -200669: "Attempt to set the Connect DAC Reference to Ground property failed, because the Allow Connecting DAC Reference \
            to Ground property was not True. To connect DAQ reference to ground, you must set two properties to True: Connect DAC Reference \
            to Ground and Allow Connecting DAC Reference to Ground.",
        -200670: "DAC Range Low is not equal in magnitude and opposite in sign from DAC Reference Value. If you do not set the \
            DAC Range Low property, the driver sets it for you. Otherwise, ensure DAC Range Low and DAC Reference Voltage Value are equal in \
            magnitude and opposite in sign.",
        -200671: "Switch device has been disabled to prevent it from exceeding its simultaneous relay drive limit. To recover, \
            call DAQmx Disconnect All, or reset the device. The device can be reset either programmatically or by using Measurement & Automation \
            Explorer.",
        -200672: "Input arrays are of different sizes. These arrays must have the same size.",
        -200673: "Multiple samples cannot be written using a single sample write. Ensure the waveform contains only a single sample.",
        -200674: "Switch operation failed due to a previous error. The device may have been powered off and back on. To use the \
            device again, reset the device either programmatically or by using Measurement & Automation Explorer.",
        -200675: "Input Source Select is set to an internal source for channels in different channel groups. On this device, only \
            one channel group at a time can be configured to use an internal source. Refer to documentation for details.",
        -200676: "Input Source Select property is set differently for channels in one channel group on a device that supports \
            only identical settings within a channel group. Refer to documentation for details.",
        -200677: "Input Source Select property is set to different internal sources on some channels. On this device, Input Source \
            Select must be set the same way for all channels with internal sources. Refer to documentation for details.",
        -200678: "Write failed because at least one of the lines in the task is also in a watchdog timer task whose watchdog timer \
            has expired. Clear the expiration of the watchdog timer before writing by using DAQmx Control Watchdog Task, by restarting the \
            watchdog timer task, or by resetting the device programmatically or through the Measurements & Automation Explorer. To prevent this \
            error in the future reset the watchdog timer more frequently or increase the watchdog timer timeout.",
        -200679: "When Sample Mode is Hardware Timed Single Point, Memory Mapping for Programmed IO Enable cannot be true. Set \
            Memory Mapping for Programmed IO Enable to false or change Sample Mode.",
        -200680: "Device has shut down because a sensor on the device detected a temperature above the device's maximum recommended \
            operating temperature. To use the device again, either turn the chassis/computer off until the device has cooled, or ensure the \
            device has cooled, and reset the device (either programmatically or through Measurements & Automation Explorer).",
        -200681: "Route failed because either the source or destination of the route is also a line in a watchdog timer task whose \
            watchdog timer has expired. Clear the expiration of the watchdog timer before routing by using DAQmx Control Watchdog Task, by \
            restarting the watchdog timer task, or by resetting the device programmatically or through Measurements & Automation Explorer. \
            To prevent this error in the future reset the watchdog timer more frequently or increase the watchdog timer timeout.",
        -200682: "Data could not be read because the reference trigger master session is unavailable. To avoid this error, read \
            data before closing the reference trigger master session.",
        -200683: "NI-DAQmx has detected a corrupt installation. Please re-install NI-DAQmx. If you continue to receive this message, \
            please contact National Instruments for assistance.",
        -200684: "Pulse duty cycle specified is not supported for this device given the pulse frequency and Counter Timebase Rate.",
        -200685: "Pulse frequency specified is not supported for this device given the Counter Timebase Rate.",
        -200686: "Pulse high time specified is not supported for this device given the Counter Timebase Rate.",
        -200687: "Pulse low time specified is not supported for this device given the Counter Timebase Rate.",
        -200688: "Pulse high tick count specified is not supported for this device.",
        -200689: "Pulse low tick count specified is not supported for this device.",
        -200690: "Buffered operations are not supported if Sample Mode is Hardware Timed Single Point. Do not configure a buffer, \
            or change the Sample Mode value.",
        -200691: "Buffered operations are not compatible with the requested Wait Mode. Do not configure a buffer, or set Wait \
            Mode to Yield.",
        -200692: "Number of samples per channel to write multiplied by the number of channels in the task cannot be an odd number \
            for this device. Adjust the number of samples per channel to write or the number of channels in the task so that their product \
            is an integer multiple of two.",
        -200693: "Buffer size (in samples per channel) multiplied by the number of channels in the task cannot be an odd number \
            for this device. Adjust the buffer size or the number of channels in the task so that their product is an integer multiple of two.",
        -200694: "AI Minimum was not specified for an operation that requires it.",
        -200695: "AI Maximum was not specified for an operation that requires it.",
        -200696: "Bridge offset nulling calibration is not supported by the specified channels. Specify only the analog input \
            channels that are configured to measure sensors in a bridge configuration.",
        -200697: "Calibration data could not be acquired. Ensure that the device(s) are configured and functioning properly.",
        -200698: "Route failed because the PXI chassis is not identified. The existence of the source terminal depends on the \
            chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis.",
        -200699: "Route failed because the PXI chassis is not identified. The existence of the destination terminal depends on \
            the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis.",
        -200700: "PXI_Star is not available as a source terminal for devices in PXI slot 2. PXI slot 2 has specific PXI_Star<n> \
            lines, such as PXI_Star3. Move your device to one of slots 3 through 15, or select a different source terminal.",
        -200701: "PXI_Star is not available as a destination terminal for devices in PXI slot 2. PXI slot 2 has specific PXI_Star<n> \
            lines, such as PXI_Star3. Move your device to one of slots 3 through 15, or select a different destination terminal.",
        -200702: "PXI_Star is not available as a destination terminal for devices in PXI slots 16 and above. Move your device \
            to one of slots 3 through 15, or select a different destination terminal.",
        -200703: "PXI_Star is not available as a source terminal for devices in PXI slots 16 and above. Move your device to one \
            of slots 3 through 15, or select a different source terminal.",
        -200704: "PXI_Star<n> is available as a source terminal only for devices in the star trigger controller slot (slot 2). \
            To use PXI_Star (without any numbers), do not specify a star line number. To use PXI_Star<n>, move your device to slot 2.",
        -200705: "PXI_Star<n> is available as a destination terminal only for devices in the star trigger controller slot (slot \
            2). To use PXI_Star (without any numbers), do not specify a star line number. To use PXI_Star<n>, move your device to slot 2.",
        -200706: "PXI_Clk10In is available as a destination terminal only for devices in the star trigger controller slot (slot \
            2). Move your device to PXI slot 2.",
        -200708: "Getting a property that pertains to multiple items failed because the value was different for different items. \
            Get the specified property for one item at a time. For example, if you are getting a property for two markers, such as marker0:1 \
            or marker0, marker1, and the property values are different for the two markers, you must get them in two steps \
            (one for marker0 and another for marker1).",
        -200709: "No TEDS sensor was detected on the specified physical channel. Ensure that your sensor is properly connected. \
            If the sensor is connected to a TEDS interface device with addresses, make sure the configured address matches the address set \
            on the interface device.",
        -200710: "Input Source Select property is set to an internal source with more than one channel in the task. On this device, \
            an internal input source is supported only when there is one channel in the task. Remove all of the channels currently in the task \
            except the channel that will be used to acquire the internal input source.",
        -200711: "An attempt has been made to use an analog trigger with the Input Source Select property set to an internal source. \
            Either change the Input Source Select property ot specify an external source, or use a different analog trigger source.",
        -200712: "Digital input configuration failed because at least one of the lines in the task was in an expired watchdog \
            task, and the expiration state of the line was set to output. Clear the expiration of the watchdog task by using DAQmx Control \
            Task, by restarting the watchdog task, or by resetting the device either programmatically or by using Measurement & Automation Explorer. \
            To prevent this error in the future, reset the watchdog timer more frequently or increase the watchdog timer timeout.",
        -200713: "Channels specified cannot appear in the same task on this device. Create a separate task for each of the channels \
            specified.",
        -200714: "Acquisition has stopped because the driver could not transfer the data from the device to the computer memory \
            fast enough. This was caused by computer system limitations. Reduce your sample clock rate, the number of channels in the task, \
            or the number of programs your computer is executing concurrently.",
        -200715: "Digital input detected a new sample clock before the previous sample was latched into onboard memory. If you \
            are using an external sample clock, ensure that it is connected, within the jitter and voltage level specifications, and without \
            glitches. If applicable, reduce your sample clock rate or use a product capable of higher sample clock rates.",
        -200716: "Digital output detected a new sample clock edge before the previous sample could be written from the onboard \
            memory. If you are using an external sample clock, ensure that it is connected, within jitter and voltage level specifications, \
            and without glitches. If applicable, reduce your sample clock rate or use a product capable of higher sample clock rates.",
        -200717: "Measurement taken during calibration produced an invalid AI offset calibration constant. If performing an external \
            calibration, ensure that the reference voltage value passed to the calibration VI or function is correct. Repeat the calibration. \
            If the error persists, contact National Instruments Technical Support.",
        -200718: "Measurement taken during calibration produced an invalid AI gain calibration constant. If performing an external \
            calibration, ensure that the reference voltage value passed to the calibration VI or function is correct. Repeat the calibration. \
            If the error persists, contact National Instruments Technical Support.",
        -200719: "Measurement taken during calibration produced an invalid AO offset calibration constant. If performing an external \
            calibration, ensure that the reference voltage value passed to the calibration VI or function is correct. Repeat the calibration. \
            If the error persists, contact National Instruments Technical Support.",
        -200720: "Measurement taken during calibration produced an invalid AO gain calibration constant. If performing an external \
            calibration, ensure that the reference voltage passed to the calibration VI or function is correct. Repeat the calibration. If \
            the error persists, contact National Instruments Technical Support.",
        -200721: "Computed frequency resolution of the VCXO CalDAC circuitry is not sufficient to perform timebase calibration. \
            Ensure that the reference frequency is stable and that the frequency passed to the calibration VI or function is correct. Repeat \
            the external timebase calibration. If the error persists, contact National Instruments Technical Support.",
        -200722: "Timebase calibration algorithm failed to converge within the required tolerance. Ensure that the reference frequency \
            is stable and that the frequency passed to the calibration VI or function is correct. Repeat the external timebase calibration. \
            If the error persists, contact National Instruments Technical Support.",
        -200723: "Variance of the measured external reference frequency is too large to perform timebase calibration. Ensure that \
            the reference frequency is stable. Repeat the external timebase calibration. If the error persists, contact National Instruments \
            Technical Support.",
        -200724: "Digital Input Tristate property has different values for different channels in the task, which is not supported \
            for this type of device. Change the property to a single value for all channels in the task, or use more than one task.",
        -200725: "Some or all of the lines in the task are used by another task for handshaking input. These lines cannot be used \
            in a static input task. Use a line that is not in a handshaking input task or stop using the line in the handshaking input task.",
        -200726: "Some or all of the lines in the task are used by another task for static input. These lines cannot be used in \
            a handshaking input task. Use a port that is not already used by a static input task or stop using the line in the static input \
            task.",
        -200727: "Some or all of the lines in the task are used by another task for handshaking control. These lines cannot be \
            used in a static input task. Use a line that is not also a control line in a handshaking task, or stop using the line for handshaking \
            control.",
        -200728: "Some or all of the handshaking control lines for this task are used by another task for static input. These \
            lines cannot be used for handshaking control. Use a port whose handshaking control lines are not already used by a static input \
            task or stop using the lines for handshaking control.",
        -200729: "Value of the Tristate property for some or all of the channels in the task is False, and Sample Timing Type \
            is Handshake, which is not supported by this device. Set the Tristate property to True for all channels or change the Sample Timing \
            Type.",
        -200730: "Value of Tristate property for some or all of the channels in the task is False, and Sample Timing Type is Change \
            Detection, which is not supported by this device. Set the Tristate property to True for all channels or change the Sample Timing \
            Type.",
        -200731: "Sample Mode is Hardware Timed, and Sample Timing Type is On Demand, which is not supported by this device. Change \
            Sample Mode or Sample Timing Type.",
        -200732: "Some of all of the lines in the task have had their Digital Filter Enable property set, which is not supported \
            when the value of the Tristate property is False. Change the value of the Tristate property, or do not set the Digital Filter Enable \
            property.",
        -200733: "Some or all of the lines in the task have ahd their Digital Filter Minimum Pulse Width property set, which is \
            not supported when the value of the Tristate property is False. Change the value of the Tristate property, or do not set the Digital \
            Filter Minimum Pulse Width property.",
        -200734: "Device does not support DMA for the Data Transfer Mechanism when performing non-buffered acquisitions. Set Data \
            Transfer Mechanism to Programmed I/O.",
        -200735: "Given the specified Reference Clock Source, you must set the Reference Clock Rate to a value equal to the frequency \
            of the supplied signal.",
        -200736: "FREQOUT counter cannot generate the desired frequency. The FREQOUT counter is a 4-bit counter that can divide \
            either the 10 MHz Timebase or the 100 kHz Timebase by a number between one and sixteen. Chose a frequency within this range.",
        -200737: "For this type of device, the Input Buffer Size (in Samples per Channel) must be equal to the value of the Sample \
            Quanity-Samples per Channel property when Sample Mode is Finite Samples.",
        -200738: "Specified timing source does not exist.",
        -200739: "Specified property is not supported for the given timing source.",
        -200740: "Task used as the timing source for a Timed Loop was started before the Timed Loop was executed. Let the Timed \
            Loop start the task, or use the task without the Timed Loop.",
        -200741: "A TEDS sensor not supported by DAQmx is connected to the specified physical channel. Consider using MAX to create \
            a Task, a Global Channel, or a Scale to acquire data using this sensor.",
        -200742: "Memory of the TEDS sensor connected to the specified physical channel is corrupted, as indicated by an invalid \
            check-sum. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider using \
            MAX to create a Task, a Global Channel, or a Scale to acquire data using this sensor.",
        -200743: "For this device, a TEDS terminal block must be connected to the device and configured in MAX in order to perform \
            a TEDS operation.",
        -200744: "Specified reference clock rate does not match the specified reference clock source. Do not set the refererence \
            clock rate when you are using an internal reference clock source. In this case, the driver sets the reference clock rate for you.",
        -200745: "Frequency and Initial Delay property values are inconsistent with one or more counter timebase properties. The \
            conflicting properties must satisfy the following constraints: Counter Timebase Rate / Counter Maximum Count <= Frequency <= Counter \
            Timebase Rate / 4 Counter Timebase Rate / Counter Maximum Count <= 1 / Initial Delay <= Counter Timebase Rate / 2 If the Counter \
            Timebase Rate is not specified, it is inferred from the Counter Timebase Source selection.",
        -200746: "Initial Delay, High Time, and Low Time property values are inconsistent with one or more counter timebase properties. \
            The conflicting properties must satisfy the following constraints: 2 / Counter Timebase Rate <= Initial Delay <= Counter Maximum \
            Count / Counter Timebase Rate 2 / Counter Timebase Rate <= High Time <= Counter Maximum Count / Counter Timebase Rate 2 / Counter \
            Timebase Rate <= Low Time <= Counter Maximum Count / Counter Timebase Rate If the Counter Timebase Rate is not specified, it is \
            inferred from the Counter Timebase Source selection.",
        -200747: "Acquisition type specified is not supported by the FREQOUT channel. To use the FREQOUT channel, set the acquisition \
            type to a value supported by FREQOUT. To use specified output type, use a different counter output channel.",
        -200748: "DAQmx Write was invoked more than once between two consecutive sample clocks. When Sample Mode is Hardware Timed \
            Single Point, invoke DAQmx Write only once between two consecutive sample clocks.",
        -200749: "Specified gain is not supported.",
        -200750: "Specified voltage is invalid for the given gain.",
        -200751: "Sample Timing Type was set to Change Detection but no physical channels on which to detect changes were specified. \
            Specify the Change Detection Digital Input Rising and/or Falling Edge Physical Channels, or specify a different Sample Timing Type.",
        -200752: "You have specified more than one physical channel as the active channel which is not supported. Specify a single \
            physical channel.",
        -200753: "TEDS sensor data or the Virtual TEDS data file contains an error which was detected during parsing. Ensure your \
            TEDS sensor or Virtual TEDS data file conforms to the specification. If this is not possible, use custom scales with the sensor.",
        -200754: "TEDS template specifies parameters that are not supported by DAQmx. Use custom scales with this sensor.",
        -200755: "TEDS sensor data or Virtual TEDS data file contains multiple calibration templates. Only one calibration template \
            is supported by DAQmx. Use custom scales with this sensor.",
        -200756: "Type of TEDS sensor associated with the channel is incompatible with the Measurement Type. Use the TEDS sensor \
            for measurements compatible with the sensor.",
        -200757: "Sample Timing Type is set to On Demand which is not supported for analog input on this device. Set Sample Timing \
            Type to Sample Clock. You can achieve this whlie setting related properties through DAQmx VIs or functions for configuring timing.",
        -200758: "Sample Timing Type is set to On Demand which is not supported for analog output on this device. Set Sample Timing \
            Type to Sample Clock. You can achieve this while setting related properties through DAQmx VIs or functions for configuring timing.",
        -200759: "Range specified by the AO Maximum and Minimum Value, and AO Voltage Units properties does not lie within the \
            range specified by the AO DAC Range High and Low properties. Change the values of these properties. If you do not specify AO DAC \
            Range High and Low, the driver will set them based on other properties.",
        -200760: "Range specified by the AO Maximum and Minimum Value, and AO Voltage Units properties does not lie within the \
            range specified by the AO Gain property. Change the values of these properties. If you do not specify AO Gain, the driver will \
            set it based on other properties.",
        -200761: "Task cannot issue sync pulse because another task is currently running on this device. For this type of device, \
            the task can issue a sync pulse if it is the only task running on the device. If your task is not being used for synchronization, \
            set the Sync Pulse Source property to "" or None to avoid receiving an error.",
        -200762: "Task cannot issue sync pulse because the task has an external sample clock timebase. For this type of device, \
            the task can issue a sync pulse if the Sample Clock Timebase Source is Onboard Clock.",
        -200763: "For analog input with the current Data Transfer Mechanism on this type of device, the input buffer size (in \
            samples per channel) must be an integer multiple of the transfer size. Change the Data Transfer Mechanism or the input buffer size.",
        -200764: "TEDS sensor connected to the specified physical channel uses a linear mapping method and specifies the linear \
            slope to be zero. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider \
            using MAX to create a Task, Global Channel, or a Scale to acquire data using this sensor.",
        -200765: "Mapping method of the TEDS sensor connected to the specified physical channel is invalid or is not supported \
            by the driver. If the sensor is defective, replace it or have it repaired. Otherwise, consider using MAX to create a Task, Global \
            Channel, or a Scale to acquire data using this sensor.",
        -200766: "Legacy template ID of the TEDS sensor connected to the specified physical channel is invalid or is not supported \
            by the driver. If the sensor is defective, replace it or have it repaired. Otherwise, consider using MAX to create a Task, Global \
            Channel, or a Scale to acquire data using this sensor.",
        -200767: "Data Transfer Mechanism is set to Programmed I/O which is not supported for buffered analog output. Change Data \
            Transfer Mechanism or use non-buffered analog output.",
        -200768: "Data Transfer Mechanism is not set to Programmed I/O, the only value supported for non-buffered analog output. \
            Set your Data Transfer Mechanism to Programmed I/O or use buffered analog output.",
        -200769: "Data Transfer Mechanism is not set to Programmed I/O, the only value supported when the Sample Mode is Hardware \
            Timed Single Point. Set your Data Transfer Mechanism to Programmed I/O or change the Sample Mode.",
        -200770: "Digital Filter Enable and Digital Synchronization Enable properties cannot be true at the same time.",
        -200771: "Digital Filter Enable is set to true but the Minimum Pulse Width property is not configured. Configure the Minimum \
            Pulse Width property or set Digital Filter Enable to false.",
        -200772: "Digital filtering is not available for the given terminal.",
        -200773: "Digital synchronization is not available for the given terminal.",
        -200774: "Terminal has already been configured with a different Minimum Pulse Width by another property in this task.",
        -200775: "Terminal has already been configured with a different Minimum Pulse Width by another task.",
        -200776: "Desired Minimum Pulse Width could not be produced. Minimum Pulse Width is affected by the Digital Filter Timebase \
            Source and the Digital Filter Timebase Rate. To see how these two property settings can affect the Minimum Pulse Width, refer to \
            product documentation for more details.",
        -200777: "Desired Minimum Pulse Width could not be produced by the device.",
        -200778: "Sample Mode is set to a value other than Hardware Timed Single Point. This is the only value supported for counter \
            generations when Sample Timing Type is set to Sample Clock. Change the Sample Mode or the Sample Timing Type.",
        -200779: "Reverse Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least \
            one term. The polynomial scale class constructor has overloads that can calculate the Reverse Coefficients from the Forward Coefficients \
            if only one set of coefficients is available.",
        -200780: "Forward Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least \
            one term. The polynomial scale class constructor has overloads that can calculate the Reverse Coefficients from the Forward Coefficients \
            if only one set of coefficients is available.",
        -200781: "Forward and Reverse Coefficients for a polynomial scale are not specified. Each of these two sets of coefficients \
            must contain at least one term. The polynomial scale class constructor has overloads that can calculate one set of coefficients \
            from the other set if only one set is available.",
        -200782: "Reverse Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least \
            one term.",
        -200783: "Forward Coefficients for a polynomial scale are not specified. This set of coefficients must contain at least \
            one term.",
        -200784: "Virtual TEDS file could not be found at the specified location. Specify correct location for the Virtual TEDS \
            file.",
        -200785: "Timing source created is invalid because of the Sample Timing Type settings. To use this timing source with \
            a Timed Loop, set the Sample Timing Type to Change Detection. You can configure the Sample Timing Type to Change Detection while \
            setting related properties through the DAQmx Timing (Change Detection) VI or function.",
        -200786: "Requested Sample Clock Rate cannot be generated given the specified external Sample Clock Timebase Rate. To \
            keep the specified Sample Clock Timebase Rate, use one of the Sample Clock Rates that can be generated.",
        -200787: "Specified Start Trigger Type is not supported for counter output tasks when the Sample Mode is Hardware Timed \
            Single Point on this type of device. Set the Start Trigger Type to None to use this Sample Mode.",
        -200788: "Measured bridge offset is outside the limits allowed for offset nulling calibration for this device. Ensure \
            your sensor is wired and functioning properly, and that its output offset is within device limits.",
        -200789: "Read cannot be performed because this version of DAQmx Read uses a data type that is too small for the channels \
            in this task. Use a different version of DAQmx Read.",
        -200790: "Write cannot be performed because this version of DAQmx Write uses a data type that is too small for the channels \
            in this task. Use a different version of DAQmx Write.",
        -200791: "TEDS cannot be configured for the specified channel. Ensure that your TEDS sensor is connected to the channel \
            through a TEDS interface (for example BNC-2096, SC-2350, or SCXI-1314T), and that this interface is configured in MAX. Alternatively \
            a virtual TEDS file can be used.",
        -200792: "You have specified more than one physical channel which is not supported. Specify a single physical channel.",
        -200793: "For a device of this type, setting the AO Idle Output Behavior to Maintain Existing Value is not supported when \
            analog output is synchronized.",
        -200794: "You cannot use DAQmx Write for multiple counter channels within one task. If appropriate, create one task per \
            counter output channel. To update multiple counter channels within one task use counter output properties.",
        -200795: "There was an overflow of the device onboard memory while performing a hardware timed non-buffered generation. \
            Write only one sample per channel between two consecutive sample clocks to avoid this condition.",
        -200796: "Hardware timed non-buffered analog output could not be performed because Memory Mapping for Programmed I/O Enable \
            was set to true. Disable memory mapping for hardware timed non-buffered analog output.",
        -200797: "An empty string was specified as a terminal name which is not supported. Specify a valid terminal name.",
        -200798: "Device does not support change detection for lines that do not allow digital input. Use lines that allow digital \
            input for change detection.",
        -200799: "DAQmx Create Timing Source created an invalid source because the specified Sample Mode is not supported when \
            the signal is Event Counting. To use this timing source with a Timed Loop, change the Sample Mode.",
        -200800: "Event source signal specified is not supported with the Measurement Type and/or Sample Timing Type of the task.",
        -200801: "DAQmx Create Timing Source created an invalid source because the requested signal is not supported for counter \
            output. To use this task as the timing source with a Timed Loop, specify the Counter Output Event as the signal.",
        -200802: "Write cannot be performed when the task is not started, the sample timing type is something other than On Demand, \
            and the output buffer size is zero. Call DAQmx Start before DAQmx Write, set auto start to true on DAQmx Write, modify the sample \
            timing type, or change the output buffer size.",
        -200803: "Write cannot be performed before you start the task for on demand or hardware-timed single-point operations. \
            Start the task before you write samples, set the autostart input on DAQmx Write to true, or use hardware timing with a sample mode \
            of finite or continuous.",
        -200804: "Last External Calibration Date/Time is not available, because the last external calibration if the device was \
            not performed using the NI-DAQmx API. Last External Calibration Date/Time will become available after you perform external calibration \
            of the device using the NI-DAQmx API.",
        -200806: "Requested Minimum Pulse Width cannot be applied because the programmable filter clock has already been configured \
            with a different Minimum Pulse Width by another task. For this type of device, there is only one programmable filter clock per \
            device.",
        -200807: "Requested Minimum Pulse Width cannot be applied because the programmable filter clock has already been configured \
            with a different Minimum Pulse Width when a different terminal was configured by the same task. For this type of device, there \
            is only one programmable filter clock per device, and the device can use only one external timebase filter at a time.",
        -200808: "TEDS sensors cannot be configured on real-time (RT) systems. Use MAX to configure the TEDS sensor instead.",
        -200809: "TEDS sensors cannot be cleared on real-time (RT) systems.",
        -200810: "Requested string contains characters that cannot be interpreted by DAQmx due to installed language support and \
            system locale settings. Ensure that the appropriate language support is installed on the system, and that the system locale is \
            set correctly. For most Windows operating systems, this is done through the Regional Settings option in Control Panel. For a LabVIEW RT \
                target, you should install Language Support for LabVIEW RT and change the locale setting for the remote system under the \
                System Settings tab in MAX.",
        -200811: "Specified string contains characters that cannot be interpreted by DAQmx due to installed language support and \
            system locale settings. If possible, do not use this character. Otherwise, ensure that the appropriate language support is installed \
            on the system, and that the system locale is set correctly. For most Windows operating systems, this is done through the Regional \
            Settings option in the Control Panel. For a LabVIEW RT target, you should install Language Support for LabVIEW RT and change the \
            locale setting for the remote system under the System Setting tab in MAX.",
        -200812: "An attempt has been made to configure a trigger when analog output Sample Mode was set to Hardware Timed Single \
            Point. Configure the analog output sample mode to something other than Hardware Timed Single Point to use a trigger.",
        -200813: "Selected Sample Mode is not supported with counter input position measurements.",
        -200814: "Onboard Clock is not supported as an Input Terminal for counter measurements. Refer to user documentation for \
            a list of supported input terminals.",
        -200815: "TEDS sensor specifies a value for the Minimum Physical Value that is greater than or equal to the Maximum Physical \
            Value. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider using MAX \
            to create a Task, a Global Channel, or a Scale to acquire data using this sensor.",
        -200816: "TEDS sensor specifies a value for the Minimum Electrical Value that is greater than or equal to the Maximum \
            Electrical Value. Replace the sensor or have the sensor repaired. If the memory is the only defective part of the sensor, consider \
            using MAX to create a Task, a Global Channel, or a Scale to acquire data using this sensor.",
        -200817: "Excitation Value can only be zero when the Input Terminal Configuration is set to Differential on this device. \
            Change the Input Terminal Configuration or set the Excitation Value to zero.",
        -200818: "Device has shut down because a sensor on the device detected a temperature in excess of the maximum recommended \
            operating temperature. Possible causes incude excessive current on the device channels and inadequate chassis cooling. To use the \
            device again, reduce the current and/or improve the chassis cooling. Ensure that the device has cooled and reset the device \
            (either programmatically or through Measurements & Automation Explorer).",
        -200819: "Programmed I/O is not supported as the Data Transfer Mechanism when the Use Only On Board Memory property is \
            set to true. Change the Data Transfer Mechanism or set Use Only On Board Memory to false.",
        -200820: "Sample Mode of Hardware Timed Single Point is not supported for analog input channels on this type of device \
            when the number of channels in the task is odd (not divisible by 2). Add a channel to the task, remove a channel from the task, \
            or use a different Sample Mode.",
        -200821: "Sample Mode of Hardware Timed Single Point is not supported for analog input channels on this type of device. \
            Use a different Sample Mode, or select a device which supports Hardware Timed Single Point.",
        -200822: "Attempt to write to the PROM on the TEDS failed because the TEDS sensor does not contain a PROM. Write the Basic \
            TEDS data to the EEPROM of the sensor or replace the sensor.",
        -200823: "Attempt to write to the PROM on the TEDS sensor failed because the PROM has already been written and it cannot \
            be rewritten. Do not write the Basic TEDS data to the TEDS sensor or replace the sensor.",
        -200824: "Attempt to write the Basic TEDS data to the EEPROM failed because the PROM on the TEDS sensor already contains \
            Basic TEDS data. A TEDS sensor can contain the Basic TEDS data in either the PROM or the EEPROM, but not in both. Do not write \
            the Basic TEDS data to the TEDS sensor or replace the sensor.",
        -200825: "Write failed because the data size is greater than the size of the EEPROM on the TEDS sensor. Make sure the \
            data size does not exceed the EEPROM size.",
        -200826: "TEDS sensor data being written to the TEDS sensor contains an error. Ensure your TEDS sensor data conforms to \
            the specification.",
        -200827: "Virtual TEDS data file being written to the TEDS sensor contains an error. Ensure your Virtual TEDS data file \
            conforms to the specification.",
        -200828: "Writing to TEDS sensors is not supported on real-time (RT) systems.",
        -200829: "DAQmx Write failed because the counter channels have different Output Types. Writes to multiple counter output \
            channels are supported only when all of the counters have identical Output Types. Use identical Output Types for all channels. \
            Alternatively, create multiple tasks (one for each Output Type).",
        -200830: "On Demand Simultaneous Analog Output Enable and Memory Mapping for Programmed IO Enable cannot both be set to \
            true for this device.",
        -200832: "DAQmx Read is not supported if the Sample Timing Type is On Demand, the Auto Start property is false, and the \
            task is not running. Start the task before reading samples by calling DAQmx Start Task, set the Read.Auto Start property to true, \
            or change the Sample Timing Type.",
        -200833: "DAQmx Read is not supported if the Sample Mode is Hardware Timed Single Point, the Auto Start property is false, \
            and the task is not running. Start the task before reading samples by calling DAQmx Start Task, set the Read.Auto Start property \
            to true, or change the Sample Mode.",
        -200834: "DAQmx Read is not supported for non-buffered acquisitions if the Auto Start property is false and the task is \
            not running. Start the task before reading samples by calling DAQmx Start Task, set the Read.Auto Start property to true, or call \
            DAQmx Configure Input Buffer with a buffer size greater than zero.",
        -200835: "SCXI device cannot be used in this task because the power to the device was turned off after the task had been \
            created. Call DAQmx Clear Task and then create a new task to use this SCXI device.",
        -200836: "Attempt to write to the TEDS sensor failed, possibly because the sensor is not connected properly or because \
            the sensor is defective. Make sure the TEDS sensor is properly connected. Write to the TEDS sensor again. If the write fails again, \
            try using another TEDS sensor. You may need to have the original TEDS sensor repaired.",
        -200837: "Samples per Channel must be an integer multiple of the transfer size for this device with the current Data Transfer \
            Mechanism. Change Samples per Channel or the Data Transfer Mechanism.",
        -200838: "Output buffer size (in samples per channel) must be an integer multiple of the transfer size for this device \
            with the current Data Transfer Mechanism. Change the output buffer size or the Data Transfer Mechanism.",
        -200839: "Tristate property cannot be set to False for any channel in the task when Sample Timing Type is Sample Clock \
            on this device. Set the Tristate property to True for all channels or change the Sample Timing Type.",
        -200840: "Prescaler value requested is not supported by this device, given the requested Timebase Source. Set Prescaler \
            to 1, or change the Timebase Source.",
        -200841: "Prescaler value requested is not supported by this device, given the requested Input Terminal. Set Prescaler \
            to 1, or change the Input Terminal.",
        -200842: "Data Transfer Mechanism is not set to Programmed I/O, the only value supported when the Sample Mode is Hardware \
            Timed Single Point. Set your Data Transfer Mechanism to Programmed I/O or change the Sample Mode.",
        -200843: "DAQmx Read did not complete before the arrival of three sample clocks which indicates that your program is not \
            keeping up with the hardware clock. Slow down the hardware clock or else change your application so that it can keep up with the \
            hardware clock.",
        -200844: "Task contains a 'freqout' counter channel, which cannot be updated while the task is running. Create separate \
            tasks for the 'freqout' channel and the other counter channels if you wish to write to the other counter channels. Alternatively, \
            stop the task, reprogram the counters, and restart the task.",
        -200845: "Data Transfer Mechanism is not set to Programmed I/O or DMA, the only values supported for non-buffered operations \
            for this device and Channel Type. Set your Data Transfer Mechanism to Programmed I/O or DMA, or use buffering.",
        -200846: "Write cannot be performed when the auto start input to DAQmx Write is false, task is not running, and timing \
            for the task is not configured or Timing Type is set to On Demand. Set auto start to true, start the task, or configure timing \
            and specify Timing Type other than On Demand.",
        -200847: "Data Transfer Mechanism is set to Programmed I/O, which is not supported for buffered operations for this device \
            and Channel Type. Change Data Transfer Mechanism or do not use buffering.",
        -200848: "DAQmx Every N Samples Event is not supported within non-buffered tasks. To receive Every N Samples Event notifications, \
            configure your task to use buffering.",
        -200849: "Number of samples to wait in a finite wait instruction must be a multiple of the alignment quantum.",
        -200850: "Number of samples to wait in a finite wait instruction must be greater than 0.",
        -200851: "Physical channel specified is not available through the cabled device connector used for the SCC carrier. To \
            use the specified channel with an SCC, connect the SCC carrier to the appropriate connector on the cabled device and specify the \
            new configuration through MAX.",
        -200852: "Given devices cannot be synchronized in a multiple-device task. Ensure that one of the devices in the task is \
            in PXI slot 2, or specify the Synchronization Pulse Source and the Sample Clock Timebase Source to be from a device in PXI slot \
            2, even if that device is not in the task.",
        -200853: "Terminal specified must include the device name for the given multiple-device task. Include the device name \
            in the terminal name. Example syntax is myDevice3/PFI4.",
        -200854: "Given devices cannot be synchronized in a multiple-device task because the Sample Clock Timebase Source specifies \
            a different device from the Synchronization Pulse Source. Modify the Synchronization Pulse Source and/or the Sample Clock Timebase \
            Source to be from the same device or leave one or both unspecified.",
        -200855: "Devices cannot be added to a task after configuring timing, triggering, buffers, and/or exported signals. Add \
            all devices to the task before configuring other aspects of the task.",
        -200856: "Simulation disabling is not supported for this device, because it was created as a simulated device.",
        -200857: "Specified low pass cutoff frequency is not supported.",
        -200858: "To use Sample Clock as the Sample Timing Type for analog output on this device, call DAQmx Write before DAQmx \
            Start.",
        -200859: "To use Sample Clock as the Sample Timing Type for analog output on this device, specify buffer size greater \
            than 0 in DAQmx Configure Output Buffer.",
        -200860: "Combination of specified AI Maximum Sound Pressure Level and AI Microphone Sensitivity settings is not supported \
            by the device. Consider using a microphone with lower sensitivity. If clipping signals at high levels is acceptable, you can use \
            the microphone with specified sensitivity as long as you reduce the AI Maximum Sound Pressure.",
        -200861: "Combination of specified AI Maximum Sound Pressure Level, AI Microphone Sensitivity, and other related AI property \
            settings is not supported by the device. Change the values of the related AI properties or do not set them at all. If you do not \
            set the related AI properties, NI-DAQmx sets them for you. Alternatively, consider using a microphone with lower sensitivity.",
        -200862: "One or more devices from a multiple-device task are in an unidentified PXI chassis, which is not supported. \
            Identify the PXI chassis in MAX.",
        -200863: "DAQmx Wait for Next Sample Clock is not supported by the given device for tasks containing channels of the given \
            type or timing type. DAQmx Wait for Next Sample Clock is only supported for the hardware-timed single-point timing type.",
        -200864: "Data Transfer Request Condition being set to When Acquisition Complete is only supported when the Reference \
            Trigger Type is other than None. Change the Data Transfer Request Condition or configure a reference trigger for the task.",
        -200865: "Data Transfer Request Condition is set to When Acquisition Complete, but the Number of Samples per Channel is \
            greater than the On Board Buffer Size. Decrease the Number of Samples per Channel, remove some channels from the task, or change \
            the Data Transfer Request Condition.",
        -200866: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Reference and Offset Values. \
            To keep the specified AO DAC Reference and Offset Values, change the AO Minimum and Maximum Values. To keep the specified AO Minimum \
            and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Reference Value. Alternatively, supply an \
            appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, \
            to get the optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details.",
        -200867: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Reference Value. To keep \
            the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Reference Value. \
            To keep the specified AO DAC Reference Value, change the AO Minimum and Maximum Values. Alternatively, supply an appropriate external \
            DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, to get the optimum accuracy, \
            you should manually calibrate the offset. Refer to user documentation for details.",
        -200868: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Reference Value. To keep \
            the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Reference Value. \
            To keep the specified AO DAC Reference Value, change the AO Minimum and Maximum Values.",
        -200869: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Offset Value. To keep the \
            specified AO Minimum and Maximum Values, supply an appropriate offset and specify the corresponding AO DAC Offset Value. To keep \
            the specified AO DAC Offset Value, change the AO Minimum and Maximum Values. Alternatively, supply an appropriate external DAC \
            reference and specify the corresponding AO DAC Reference Value.",
        -200870: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Offset Value. To keep the \
            specified AO Minimum and Maximum Values, supply an appropriate offset and specify the corresponding AO DAC Offset Value. To keep \
            the specified AO DAC Offset Value, change the AO Minimum and Maximum Values.",
        -200871: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Range Low and High, and \
            AO DAC Offset Value. To keep the specified AO DAC Range and Offset Values, change the AO Minimum and Maximum Values. To keep the \
            specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Range. Alternatively, \
            supply an appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, \
            to get the optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details.",
        -200872: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Range Low and High. To \
            keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Range Low \
            and High. To keep the specified AO DAC Range Low and High, change the AO Minimum and Maximum Values. Alternatively, supply an \
            appropriate external DAC offset and specify the corresponding AO DAC Offset Value. When supplying an external DAC offset, to get the \
            optimum accuracy, you should manually calibrate the offset. Refer to user documentation for details.",
        -200873: "Specified AO Maximum and Minimum Values are not supported given the specified AO DAC Range Low and High. To \
            keep the specified AO Minimum and Maximum Values, supply higher reference voltage and specify the corresponding AO DAC Range Low \
            and High. To keep the specified AO DAC Range Low and High, change the AO Minimum and Maximum Values.",
        -200874: "DAQmx Write is supported for counter output channels only while the task is running. To use DAQmx Write with \
            the given task, invoke DAQmx Start prior to DAQmx Write. To specify the low and/or high time while the task is not running, set \
            DAQmx properties instead of invoking DAQmx Write.",
        -200875: "DAQmx Write is supported for counter output channels only while the task is running. To use DAQmx Write with \
            the given task, invoke DAQmx Start prior to DAQmx Write. To specify the frequency and/or the duty cycle while the task is not running, \
            set DAQmx properties instead of invoking DAQmx Write.",
        -200876: "DAQmx Write is supported for counter output channels only while the task is running. To use DAQmx Write with \
            the given task, invoke DAQmx Start prior to DAQmx Write. To specify the low and/or high ticks while the task is not running, set \
            DAQmx properties instead of invoking DAQmx Write.",
        -200877: "Requested Every N Samples Event Interval is not supported for the given Data Transfer Mechanism and buffer size. \
            To keep DMA or USB Bulk as the Data Transfer Mechanism, modify the buffer size and/or the Every N Samples Event Interval so the \
            buffer size is an even multiple of the Every N Samples Event Interval. To keep the same Every N Samples Event Interval and buffer size, \
            change the Data Transfer Mechanism to Interrupts if supported.",
        -200878: "Specified digital channel contains more bits than supported by the 16-bit version of DAQmx Port Read. Use a \
            version of DAQmx Port Read that supports wider digital ports.",
        -200879: "Specified digital channel contains more bits than supported by the 16-bit version of DAQmx Port Write. Use the \
            version of DAQmx Port Write that supports wider digital ports.",
        -200880: "Zero is not a supported value for the Every N Samples Event Interval. Specify an event interval greater than \
            zero.",
        -200881: "Every N Samples Event registration has failed because the event is already registered within the task. Unregister \
            the event before registering it again.",
        -200882: "Specified channel is not a valid global channel. Ensure that the Channel Name matches a channel in the Data \
            Neighborhood in MAX. Check for typing errors.",
        -200883: "Task specified cannot be saved with interactive editing allowed, because the DAQ Assistant does not support \
            at least one of the specified properties. Save the task with 'allow interactive editing' set to false, or specify only properties \
            supported by the DAQ Assistant.",
        -200884: "Channel specified cannot be saved with interactive editing allowed, because the DAQ Assistant does not support \
            at least one of the specified properties. Save the channel with 'allow interactive editing' set to false, or specify only properties \
            supported by the DAQ Assistant.",
        -200885: "Combination of Reference Clock Source and Sample Clock Timebase Source specified is not supported by this device. \
            To use the Reference Clock Source specified, do not set the Sample Clock Timebase Source. NI-DAQmx will set it to its default value: \
            OnboardClock. To use the Sample Clock Timebase Source specified, do not set the Reference Clock Source. NI-DAQmx will set it to its \
            default value: none.",
        -200886: "Start Trigger Digital Pattern Source requested is not supported because at least one of the corresponding channels \
            is not tristated. Ensure all the corresponding channels are tristated or choose different channels.",
        -200887: "Start Trigger Digital Pattern Source requested is not supported because at least one of the corresponding channels \
            is not in the task. Ensure all the corresponding channels are in the task or choose different channels.",
        -200888: "Reference Trigger Digital Pattern Source requested is not supported because at least one of the corresponding \
            channels is not tristated. Ensure all the corresponding channels are tristated or choose different channels.",
        -200889: "Reference Trigger Digital Pattern Source requested is not supported because at least one of the corresponding \
            channels is not in the task. Ensure all the corresponding channels are in the task or choose different channels.",
        -200890: "Active Edge requested is not supported because the Sample Clock Source is OnboardClock. To use the selected \
            Sample Clock Source, set Sample Clock Active Edge to Rising Edge.",
        -200891: "Export of sample clock is supported by this device only when the Sample Clock Source is OnboardClock. Consider \
            alternative methods for gaining access to the clock signal.",
        -200892: "When the Sample Timing Type is Change Detection and the Trigger Type is Digital Pattern Match, the relevant \
            physical channels must be consistent for this device. Specifically, the Change Detection Rising Edge Physical Channels must match \
            the physical channels from the Trigger Digital Pattern Source for which the Trigger Digital Pattern string is 0 or 1.",
        -200893: "Change Detection Rising and Falling Edge Physical Channels must be set identically on this device.",
        -200894: "Number of values specified via the Start Trigger Digital Pattern does not match the number of physical lines \
            requested via the Start Trigger Digital Pattern Source. Change one or both of the properties so these two numbers are equal.",
        -200895: "Number of values specified in Reference Trigger Digital Pattern does not match the number of physical lines \
            requested in Reference Trigger Digital Pattern Source. Change one or both of the properties so these two numbers are equal.",
        -200896: "Export of the requested trigger is supported on this device only when the corresponding Trigger Type is Digital \
            Edge.",
        -200897: "Task contains a physical channel not supported by this device, given the requested Sample Timing Type. To keep \
            the Sample Timing Type, use physical lines from port0/line0 through port3/line7. To access the requested channel, change the Sample \
            Timing Type.",
        -200898: "Partial use of physical lines within a physical port is not supported by this device, given the requested Sample \
            Timing Type. Consider specifying the entire port and tristating the lines you do not want driven.",
        -200899: "Port 1 cannot be used without port 0 on this device given the Sample Timing Type. You can use ports 0 and 2 \
            by themselves. To use port 1, you also need to use port 0.",
        -200900: "Port 3 cannot be used without port 2 on this device given the Sample Timing Type. You can use ports 0 and 2 \
            by themselves. To use port 3, you also need to use port 2.",
        -200901: "Digital Pattern string specified contains an invalid character.",
        -200902: "Data Voltage Low Level and Data Voltage High Level must be within a common voltage range.",
        -200903: "Reference clock is not supported by this device. Do not set the Reference Clock property.",
        -200904: "Start Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing Type, \
            do not set the Start Trigger Type property. NI-DAQmx automatically selects a compatible Start Trigger Type setting. To use the \
            requested Start Trigger Type, select a different Timing Type.",
        -200905: "Handshake Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing \
            Type, do not set the Handshake Trigger Type property. NI-DAQmx automatically selects a compatible Handshake Trigger Type setting. \
            To use the requested Handshake Trigger Type, select a different Timing Type.",
        -200906: "Pause Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing Type, \
            do not set the Pause Trigger Type property. NI-DAQmx automatically selects a compatible Pause Trigger Type setting. To use the \
            requested Pause Trigger Type, select a different Timing Type.",
        -200907: "Reference Trigger Type requested is not supported given the requested Timing Type. To use the requested Timing \
            Type, do not set the Reference Trigger Type property. NI-DAQmx automatically selects a compatible Reference Trigger Type setting. \
            To use the requested Reference Trigger Type, select a different Timing Type.",
        -200908: "Sample Clock Source requested is not supported given the requested Timing Type. To use the requested Timing \
            Type, do not set the Sample Clock Source property. NI-DAQmx automatically selects a compatible Sample Clock Source setting. To \
            use the requested Sample Clock Source, select a different Timing Type.",
        -200909: "20 Mhz Timebase Output Terminal requested is not supported given the requested Timing Type. To use the requested \
            Timing Type, do not set the 20 Mhz Timebase Output Terminal property. NI-DAQmx automatically selects a compatible20 Mhz Timebase \
            Output Terminal. To use the requested 20 Mhz Timebase Output Terminal, select a different Timing Type.",
        -200910: "Sample Clock Output Terminal requested is not supported given the requested Timing Type. To use the requested \
            Timing Type, do not set the Sample Clock Output Terminal property. NI-DAQmx automatically selects a compatible Sample Clock Output \
            Terminal. To use the requested Sample Clock Output Terminal, select a different Timing Type.",
        -200911: "Start Trigger Output Terminal requested is not supported given the requested Timing Type. To use the requested \
            Timing Type, do not set the Start Trigger Output Terminal property. NI-DAQmx automatically selects a compatible Start Trigger Output \
            Terminal. To use the requested Start Trigger Output Terminal, select a different Timing Type.",
        -200912: "Reference Trigger Output Terminal requested is not supported given the requested Timing Type. To use the requested \
            Timing Type, do not set the Reference Trigger Output Terminal property. NI-DAQmx automatically selects a compatible Reference Trigger \
            Output Terminal. To use the requested Reference Trigger Output Terminal, select a different Timing Type.",
        -200913: "Ready For Transfer Event Output Terminal requested is not supported given the requested Timing Type. To use \
            the requested Timing Type, do not set the Ready For Transfer Event Output Terminal property. NI-DAQmx automatically selects a compatible \
            Reference Trigger Event Output Terminal. To use the requested Ready For Transfer Trigger Event Output Terminal, select a different \
            Timing Type.",
        -200914: "Change Detection Event Output Terminal requested is not supported given the requested Timing Type. To use the \
            requested Timing Type, do not set the Change Detection Event Output Terminal property. NI-DAQmx automatically selects a compatible \
            Change Detection Output Terminal. To use the requested Change Detection Event Output Terminal, select a different Timing Type.",
        -200915: "Handshake Event Output Terminal requested is not supported given the requested Timing Type. To use the requested \
            Timing Type, do not set the Handshake Event Output Terminal property. NI-DAQmx automatically selects a compatible Handshake Event \
            Output Terminal. To use the requested Handshake Event Output Terminal, select a different Timing Type.",
        -200916: "Sample Timebase Divisor requested is not supported given the requested Timing Type. To use the requested Timing \
            Type, do not set the Sample Timebase Divisor property. NI-DAQmx automatically selects a compatible Sample Timebase Divisor. To \
            use the requested Sample Timebase Divisor, select a different Timing Type.",
        -200917: "Every N Samples Event Interval requested must be an integer multiple of two for analog output tasks on this \
            device.",
        -200918: "Global channel name specified is already used for a task in the Data Neighborhood. NI-DAQmx does not support \
            overlapping task and global channel names. Select a different name.",
        -200919: "Task name specified is already used for a global channel in the Data Neighborhood. NI-DAQmx does not support \
            overlapping task and global channel names. Select a different name.",
        -200920: "Requested Every N Samples Event Interval is not supported for the given buffer size. Modify the buffer size \
            and/or the Every N Samples Event Interval so the buffer size is an even multiple of the Every N Samples Event Interval.",
        -200921: "Channel specified cannot be saved with interactive editing allowed, because the only digital channels with multiple \
            lines supported by the DAQ Assistant are entire ports. Save the channel with 'allow interactive editing' set to false. Alternatively, \
            change the channel so it contains an entire port, or break it up into channels with individual lines.",
        -200922: "Channel specified cannot be saved with interactive editing allowed, because the DAQ Assistant does not support \
            digital channels with different settings for different lines. Save the channel with 'allow interactive editing' set to false. \
            Alternatively, \
            set all the lines in the channel identically, or break the channel up into channels with individual lines.",
        -200923: "Wait Mode property is not supported for the given non-buffered task. Do not use this property inside the task, \
            or change the task to be buffered.",
        -200924: "Wait Mode specified is not supported for the given non-buffered task. Specify a different Wait Mode, or change \
            the task to be buffered.",
        -200925: "Rising and Falling Edge Physical Channels for Change Detection requested are not supported because at least \
            one of the channels is not tristated. Ensure all the corresponding channels are tristated or choose different channels.",
        -200926: "Rising and Falling Edge Physical Channels for Change Detection requested are not supported because at least \
            one of the corresponding channels is not in the task. Ensure all the corresponding channels are in the task or choose different \
            channels.",
        -200927: "Trigger Type was set to Digital Pattern Match but no physical channels were specified as the Digital Pattern \
            Source. Specify physical channels for property.",
        -200928: "Pattern match hardware for this device can only be used for one trigger.",
        -200929: "Two specified ports alone are not supported given the Sample Timing Type on this device. To use only two ports, \
            specify ports 0 and 1, or ports 2 and 3. To use the two ports specified, use four ports (0, 1, 2, and 3) on the device, and disregard \
            data from the unwanted ports.",
        -200930: "Two specified ports alone are not supported given the Sample Timing Type on this device. To use only two ports, \
            specify ports 0 and 1, or ports 2 and 3. To use the two ports specified, use four ports (0, 1, 2, and 3) on the device. Ensure \
            the lines from the unwanted ports are unwired, tristated, or are connected so no equipment can be damaged.",
        -200931: "Three ports alone are not supported given the Sample Timing Type on this device. Specify four ports (0, 1, 2, \
            and 3), and disregard data from the unwanted port.",
        -200932: "Three ports alone are not supported given the Sample Timing Type on this device. Specify four ports (0, 1, 2, \
            and 3). Ensure the lines from the unwanted port are unwired, tristated, or are connected so no equipment can be damaged.",
        -200933: "Operation cannot be performed, because the Channel Calibration Expiration Date is not specified, and Channel \
            Calibration Enable property is set to True. To use channel calibration, specify the Expiration Date; otherwise, set Channel Calibration \
            Enable to false.",
        -200934: "Operation cannot be performed, because the Channel Calibration Expiration Date has passed, and the Channel Calibration \
            Apply Calibration if Expired property is False. Update the channel calibration, including the Expiration Date, or set Apply Calibration \
            If Expired to True.",
        -200935: "Operation cannot be performed, because the Channel Calibration Scale Type is not specified and Channel Calibration \
            Enable property is set to True. To use channel calibration, specify the Scale Type; otherwise, set Channel Calibration Enable to \
            false.",
        -200936: "Operation cannot be performed, because the Channel Calibration Table Pre-Scaled Values property is not specified \
            when the Channel Calibration Scale Type is Table.",
        -200937: "Operation cannot be performed, because the Channel Calibration Table Scaled Values property is not specified \
            when the Channel Calibration Scale Type is Table.",
        -200938: "Operation cannot be performed, because the number of elements in the array specified for the Channel Calibration \
            Table Pre-Scaled Values property is not equal to the number of elements in the array specified for Channel Calibration Table Scaled \
            Values.",
        -200939: "The Channel Calibration Table Scale Pre-Scaled Values specified is not supported, because one of the numbers \
            appears more than once in the specified array. Ensure unique numbers are specified in the array.",
        -200940: "Operation cannot be performed, because the Channel Calibration Polynomial Forward Coefficients property is not \
            specified when the Channel Calibration Scale Type is Polynomial.",
        -200941: "Operation cannot be performed, because the Channel Calibration Polynomial Reverse Coefficients property is not \
            specified when the Channel Calibration Scale Type is Polynomial.",
        -200942: "Call mechanism set to synchronous event callbacks is not supported for DAQmx events on this platform. To use \
            DAQmx events on this platform, set the call mechanism to asynchronous event callbacks.",
        -200943: "Operation failed because the Data Transfer Custom Threshold property is not set, and the Data Transfer Request \
            Condition is set to Onboard Memory Custom Threshold. Specify a value for the Data Transfer Custom Threshold, or change the Data \
            Transfer Request Condition.",
        -200944: "Operation failed because the Data Transfer Custom Threshold property is set, and no value is specified for the \
            Data Transfer Request Condition. To use the specified Data Transfer Custom Threshold, set Data Transfer Request Condition to Onboard \
            Memory Custom Threshold. If you set Data Transfer Request Condition to any value other than Onboard Memory Custom Threshold, the Data \
            Transfer Custom Threshold property is ignored.",
        -200945: "Operation failed because the Data Transfer Request Condition is set to Onboard Memory Custom Threshold. This \
            device supports this Data Transfer Request Condition only when the Data Transfer Mechanism is set to DMA. To use the specified \
            Data Transfer Request Condition, set Data Transfer Mechanism to DMA. Otherwise, specify a different Data Transfer Request Condition.",
        -200946: "Task could not be started, because the driver could not write enough data to the device. This was due to system \
            and/or bus-bandwidth limitations. Reduce the number of programs your computer is executing concurrently. If possible, perform operations \
            with heavy bus usage sequentially instead of in parallel. If you can't eliminate the problem, contact National Instruments support at \
            ni.com/support.",
        -200947: "DAQmx Events are not supported in this version of LabVIEW. To use DAQmx Events, install LabVIEW 7.1 and the \
            LabVIEW 7.1.1 patch. The patch is available at ni.com/downloads.",
        -200948: "DAQmx tasks cannot provide a source for a Timed Loop and contain a DAQmx Signal Event at the same time. DAQmx \
            Signal events include the Counter Output event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection \
            event. Tasks that contain a Timed Loop can contain DAQmx Events as long as the events are not a type of DAQmx Signal Event. \
            See documentation for more details.",
        -200949: "You can only register one DAQmx Signal Event at a time on a task. DAQmx Signal events include the Counter Output \
            event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event. Unregister the event before \
            registering it again.",
        -200950: "Done Event registration has failed because the event is already registered within the task. Unregister the event \
            before registering it again.",
        -200951: "DAQmx Write for counter output detected that no sample clock has occurred since the last call to write which \
            means that the writes are happening at a rate that exceeds the sample clock rate. To avoid this problem use the Wait for Next Sample \
            Clock in your application.",
        -200952: "Event Output Terminal cannot include the Trigger Source terminal in the same task for this device.",
        -200953: "Start Trigger Source cannot be the same as the Sample Clock Source in the same task for this device.",
        -200954: "Sample Clock Output Terminal cannot include the Start Trigger Source terminal in the same task for this device.",
        -200955: "Two channels in the task have different raw data format property values, which is not supported. All channels \
            in the task must have identical raw data format property values when raw data compression is configured. Only include channels \
            with identical raw data format property values in the task when compression is configured.",
        -200956: "Raw data compression has been configured for a channel that does not support raw data compression. Remove the \
            channel from the task or set the Raw Data Compression Type to None.",
        -200957: "Compressed Sample Size exceeds the Resolution of the channel. Configure the Compressed Sample Size to be less \
            than or equal to the channel Resolution.",
        -200958: "TEDS interface device configured in MAX was not detected. Make sure that the type of TEDS interface device configured \
            in MAX is correct and that the device is properly connected.",
        -200959: "Two channels in the task have different raw data compression property values, which is not supported. All channels \
            in the task must have the same raw data compression property values.",
        -200960: "DAQmx software event cannot be registered because the task is running. Register all your DAQmx software events \
            prior to starting the task.",
        -200961: "Firmware for the device could not be downloaded, and the device cannot be used. This failure is due to a missing \
            or damaged firmware image file. Reinstall the driver to eliminate this error.",
        -200962: "Firmware for this device could not be downloaded, and the device cannot be used. The failure may be due to damaged \
            hardware. Contact National Instruments support at ni.com/support",
        -200963: "Requested Sample Timing Type is not allowed, because there is already another task with analog output channels \
            from the same device configured for a different Sample Timing Type. This is not supported on this device. Change your application \
            so that all the channels from this device are used in one task, set Sample Timing Type to On Demand for all tasks, or consider using \
            two devices for the two tasks.",
        -200964: "Every N Samples Acquired Into Buffer Event cannot be registered, because it is not supported for output tasks. \
            Use the Every N Samples Transferred From Buffer Event.",
        -200965: "Every N Samples Transferred from Buffer Event cannot be registered, because it is not supported for input tasks. \
            Use the Every N Samples Acquired Into Buffer Event.",
        -200966: "Every N Samples Acquired Into Buffer Event registration has failed because the event is already registered within \
            the task. Unregister the event before registering it again.",
        -200967: "Every N Samples Transferred From Buffer Event registration has failed because the event is already registered \
            within the task. Unregister the event before registering it again.",
        -200968: "Requested operation cannot be performed inside the asynchronous DAQmx Event callback thread. Use synchronous \
            callback mechanism or perform the operation in a different thread.",
        -200969: "TEDS operation failed because the corresponding physical channel is not an analog input channel.",
        -200970: "Every N Samples Event Interval requested must be an integer multiple of two for analog input tasks on this device.",
        -200971: "Property cannot be set because the task is not running or committed. Start or commit the task prior to setting \
            the specified property.",
        -200972: "Property cannot be set because the task is not running. Start the task prior to setting the specified property.",
        -200973: "Property cannot be queried because the task is not running. Start the task prior to getting the specified property.",
        -200974: "Allow Connecting DAC Reference to Ground at Runtime set to True is not supported by this device when DAC Reference \
            Voltage Source is set to External.",
        -200975: "Querying the Counter Output Ready for New Value property is not supported by this device when the Sample Mode \
            is set to Hardware Timed Single Point. Use DAQmx Wait for Next Sample Clock before DAQmx Write to make sure the counter is ready \
            to accept the new value.",
        -200976: "Thermocouple CJC (cold junction compensation) Channel specified cannot be used for CJC because the corresponding \
            physical channel does not support temperature measurement. Select a different CJC Channel, set CJC Source to Internal, or set CJC \
            Source to Constant Value and use CJC Value to specify the temperature of the cold junction.",
        -200977: "Channel specified cannot be saved with Allow Interactive Editing set to True, because the DAQ Assistant does \
            not support polynomial calibration scales. Save the channel with Allow Interactive Editing set to False, or use a table calibration \
            scale.",
        -200978: "DAQmx Software Events cannot be registered with different call mechanisms on the same task. The software events \
            for a task must all be registered with synchronous callbacks or they must be all registered with asynchronous callbacks.",
        -200979: "When you use synchronous events, you can clear, stop, abort, unreserve, or start a task only from the thread \
            in which you registered synchronous events.",
        -200980: "DAQmx Every N Samples Transferred from Buffer Event is not supported by the channel types or devices in your \
            task.",
        -200981: "DAQmx Every N Samples Acquired into Buffer Event is not supported by the channel types or devices in your task.",
        -200982: "DAQmx Signal Events are not supported by your device. DAQmx Signal events include the Counter Output event, \
            the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event.",
        -200983: "You only can get the specified property while the task is reserved, committed or while the task is running. \
            Reserve, commit or start the task prior to getting the property.",
        -200984: "Auto Start cannot be set to True when one or more DAQmx events are registered for the task. Set Auto Start to \
            False and start the task manually.",
        -200985: "DAQmx Write parameter Auto Start cannot be set to True when one or more DAQmx events are registered for the \
            task. Set Auto Start to false and start the task manually.",
        -200986: "DAQmx software event cannot be unregistered because the task is running. Unregister all your DAQmx software \
            events prior to starting the task.",
        -200987: "DAQmx Signal Event type requested is not supported by the channel types or the devices in your task. DAQmx Signal \
            events include the Counter Output event, the Sample Complete Event, the Sample Clock Event, and the Digital Change Detection event. \
            Refer to product documentation for more details on which DAQmx Signal Events are supported by the channel types and devices in your \
            task.",
        -200988: "Combination of requested values for Read Wait Mode and Wait for Next Sample Clock Wait Mode properties is not \
            supported for the given task on this device. Set both properties to Wait for Interrupt or do not set either of the properties to \
            Wait for Interrupt.",
        -200989: "Combination of requested values for Read Wait Mode and Wait for Next Sample Clock Wait Mode properties is not \
            supported for the given task on this device. Set both properties to Wait for Interrupt or set Read Wait Mode to a value other than \
            Wait for Interrupt.",
        -200990: "All synchronous events for the task must be registered from the same thread.",
        -200991: "Task cannot be stopped, because at least one installed event handler has not been removed. Remove all installed \
            event handlers by calling CNiDAQmxEvent::RemoveEventHandler or CNiDAQmxEvent::RemoveAllEventHandlers. See the documentation for \
            more information.",
        -200992: "DAQmx Software Events are generated too quickly for the driver to keep up, and some of them have been lost. \
            Reduce the rate at which your application is generating the events. Consider reconfiguring the events you are using, or using different \
            events.",
        -200993: "DAQmx Write failed, because it was called before the previously written value was output. This is likely a result \
            of the sample clock period being shorter than the period of the generated pulse train. To correct this issue, increase your sample \
            clock period and/or reduce the period of the generated pulse train.",
        -200994: "Requested property cannot be set while the task is running and the Sample Mode is set to Hardware Timing Single \
            Point. Use DAQmx Write instead of setting the property.",
        -200995: "Requested Memory Mapping for Programmed IO Enable value, True, is not supported when Sample Mode is set to Hardware \
            Timed Single Point. Change one or both of the properties.",
        -200996: "Data Transfer Mechanism is not set to Programmed I/O, which is the only value supported when the Sample Mode \
            is Hardware Timed Single Point. Set your Data Transfer Mechanism to Programmed I/O or change the Sample Mode.",
        -200997: "Requested Sample Timing Type value, On Demand, is not supported when Sample Mode is Hardware Timed Single Point. \
            Change Sample Timing Type and/or Sample Mode.",
        -200998: "Hardware Timed Single Point is not a supported Sample Mode for the specified Measurement Type. Change Sample \
            Mode and/or Measurement Type.",
        -200999: "Requested property, Ready For New Value, is not supported when the Sample Timing Type is On Demand. To use the \
            Ready For New Value property, change the Sample Timing Type.",
        -201000: "DAQmx Events are not supported in this version of LabVIEW. LabVIEW 8.0 or later is required to use DAQmx Events.",
        -201001: "Sample Clock Rate requested is supported only if Enhanced Alias Rejection Enable is True. Set Enhanced Alias \
            Rejection Enable to True or increase the Sample Clock Rate.",
        -201002: "Sample Clock Rate must match the frequency of the internal timebase specified as the Sample Clock Source. To \
            use the specified Sample Clock Rate, set the Sample Clock Source to OnboardClock. To use the specified timebase as the Sample Clock, \
            set the Sample Clock Rate to the frequency of that timebase.",
        -201003: "Device cannot be accessed. Possible causes: Device is no longer present in the system. Device is not powered. \
            Device is powered, but was temporarily without power. Device is damaged. Ensure the device is properly connected and powered. Turn \
            the computer off and on again. If you suspect that the device is damaged, contact National Instruments at ni.com/support.",
        -201004: "Device does not support simultaneous calibration of multiple channels. Calibrate channels one channel at a time, \
            passing individual channels to different invocations of DAQmx Setup Calibration.",
        -201005: "Invoke DAQmx Setup Calibration before invoking the corresponding DAQmx Adjust Calibration.",
        -201006: "Device does not support an external calibration password.",
        -201007: "Generate or finite Wait instruction expected before If-Else block. Insert a Generate or finite Wait \
            instruction before the If-Else block.",
        -201008: "Waveform length is too small for the Generate instruction before the If-Else block.",
        -201009: "Length of waveform subset is too small for the Generate instruction before If-Else block.",
        -201010: "Marker position specified is too close to the end of the waveform in the Generate statement before the If-Else \
            block.",
        -201011: "Wait duration is too small for the Wait instruction before the If-Else block.",
        -201012: "Clear Trigger instruction cannot be the last instruction in an If-Else block.",
        -201013: "If-Else blocks are not allowed in Repeat Until loops.",
        -201014: "If-Else blocks are not allowed in Finite Repeat loops. If possible, remove the Repeat and End Repeat \
            instructions and explicitly duplicate the instructions originally in the loop the desired number of times.",
        -201015: "PLL lock operation failed or timed out. Ensure the module is fully inserted into the carrier.",
        -201016: "Too many compiled instructions in loop. Generate and Wait instructions each result in at least one compiled \
            instruction. Each marker adds an additional compiled instruction. Clear instruction does not result in a compiled instruction. \
            If possible, reduce the number of generate instructions by concatenating the waveforms on two or more consecutive generate instructions.",
        -201017: "Byte order marker of the specified file is not supported by NI-DAQmx. For tab-delimeted files, NI-DAQmx supports \
            UTF-8, UTF-16 / UCS-2 little endian, and UTF-32 / UCS-4 little endian. For ini files, NI-DAQmx only supports UTF-8. Save the file \
            in one of the supported formats with the appropriate byte order marker.",
        -201018: "You have selected an external clock source for the task, but the device importing the clock does not have the \
            longest pipeline of all the devices in the task. This leads to an incomplete acquisition on that device because the device will \
            not receive enough Sample Clock pulses. Route the external clock signal into the device with the longest pipeline. Refer to device \
            documentation for information on pipeline depth.",
        -201019: "Pause triggering is not supported in a multi-device task. To configure pause triggering in a multi-device configuration, \
            \
            you must use no more than one device per task and manually route the clock signals in the application.",
        -201020: "Lines specified do not support change detection. Select lines that support change detection.",
        -201021: "Write recovery could not complete before detecting another Sample Clock pulse. Reduce the Sample Clock rate, \
            increase the frequency of the generated pulse train, or set Write Recovery Mode to Poll.",
        -201022: "Write recovery could not complete before detecting another Sample Clock pulse. Reduce the Sample Clock rate \
            or increase the frequency of the generated pulse train.",
        -201023: "DAQmx Write failed because the previously written value has not been generated. This error can occur if the \
            Sample Clock period is shorter than the period of the generated pulse train. Reduce the Sample Clock rate, increase the frequency \
            of the generated pulse train, or set Write Recovery Mode to Poll.",
        -201024: "DAQmx Write failed because the previously written value has not been generated. This error can occur if the \
            Sample Clock period is shorter than the period of the generated pulse train. Reduce the Sample Clock rate or increase the frequency \
            of the generated pulse train.",
        -201025: "Non-buffered hardware-timed operations are not supported for this device and Channel Type. Set the Buffer Size \
            to greater than 0, do not configure Sample Clock timing, or set Sample Timing Type to On Demand.",
        -201026: "Data Transfer Mechanism is set to Programmed I/O which is not supported for hardware-timed operations for this \
            device and Channel Type. Change Data Transfer Mechanism, do not configure Sample Clock timing, or set Sample Timing Type to On \
            Demand.",
        -201027: "Counter task detected three or more missed Sample Clock pulses. Samples were lost before the application could \
            read them. Decrease the Sample Clock rate or restructure the application so that DAQmx Read runs more frequently. Setting the Convert \
            Error to Warning property to True does not eliminate the error, because samples were lost.",
        -201028: "Name specified is already in use. Specify a name that is not currently in use.",
        -201029: "Device specified is already connected to a RTSI cable. To connect the device to another RTSI cable, remove it \
            from the RTSI cable to which it is currently connected.",
        -201030: "Device specified cannot be connected to a RTSI cable. If the device does not have a RTSI connector, you cannot \
            connect it to a RTSI cable. If the device is a PXI device then it is automatically connected to the PXI backplane, and therefore \
            does not need to be manually configured as connected to a RTSI cable.",
        -201031: "Address specified is already in use. Specify an address that is not in use.",
        -201032: "SCXI slot number specified is invalid. Specify a slot number that is valid for the specified chassis.",
        -201033: "Slot specified is already occupied. Either specify a slot that is unoccupied or remove the module occupying \
            the desired slot.",
        -201034: "Cascade digitization mode is not supported for SCXI. Select a different digitization mode.",
        -201035: "Digitizing Device Channels property is specified, but the Digitization Mode property is not set to parallel. \
            Either remove the Digitizing Device Channels property or set the Digitizing property to parallel.",
        -201036: "Format of the time value specified is invalid. Enter the time value in the format: YYYY-MM-DDTHH:mm:ssZ UTC \
            Where YYYY is the four digit year, MM is the two digit month, DD is the two digit day of the month, HH is the two digit hour of \
            the day (24 hour clock), mm is the two digit minutes into the hour, and ss is the two digit seconds into the minute. T is a literal \
            separator between date and time. For example, the string: 2004-10-19T16:30:45Z UTC Represents October 19th, 2004 at 4:30:45 PM GMT.",
        -201037: "Time value specified is invalid. Ensure that the time entered has only valid values for each of the fields in \
            the time format. For example: the month section must be between 01 and 12.",
        -201038: "Author property cannot be set on a local channel. Remove the author property from the local channel.",
        -201039: "Object lacks a required property. Add the required property to the object.",
        -201040: "Object specified contains an extra property. Remove the extra property from the object.",
        -201041: "Product type and product number specified do not refer to the same product. Remove either the product type or \
            the product number from the object.",
        -201042: "Device specification provided does not match any hardware in the system. Change the device specification to \
            match a device present in your system. You can also change your device specification to be less specific.",
        -201043: "Device specification provided matches more than one device in the system. Change the device specification to \
            be more specific.",
        -201044: "Specified accessory name is invalid. The name of the accessory should be in this format: accessoryProductType \
            / connectedDeviceIdentifier / connectorNumber Connector numbers start at zero. A device with only one connector only has a connector \
            zero.",
        -201046: "Accessory type specified cannot be connected to the specified device. Enter an accessory type that can be connected \
            to the device specified.",
        -201047: "Device and connector specified by the accessory can not be configured because there is already an accessory \
            configured for that connector and device. Enter a device and connector that is not currently occupied, or remove the configuration \
            of the existing accessory.",
        -201048: "Accessory setting specified does not apply to the accessory type. Remove the non-applicable accessory setting \
            from the accessory specification.",
        -201049: "Digitizing device specified for the SCC carrier is not capable of digitizing for SCC carriers. Specify a device \
            that is capable of digitizing for SCC carriers.",
        -201050: "Carrier specified for the SCC module could not be found. Ensure that the SCC carrier specified for the module \
            is also defined in the configuration file.",
        -201051: "Controlling device specified for the TEDS interface is not capable of controlling a TEDS interface.",
        -201052: "Physical channels specified for the TEDS interface are too great in number for the specified type of TEDS interface. \
            Reduce the number of physical channels specified.",
        -201053: "Physical channel specified for the TEDS interface is already connected to a TEDS interface. Enter a physical \
            channel that is not currently occupied, or remove the existing physical channel configuration.",
        -201054: "Enumerated value specified is not a valid value for that enumeration. The enumerated value may have been exported \
            from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version specified \
            in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or change the \
            value to one supported by the version of NI-DAQmx you have installed.",
        -201055: "Object contains two references to the same property. Remove one of the duplicate properties.",
        -201056: "Numeric value specified is in an invalid format. Remove any non-numeric characters from the specified numeric \
            value.",
        -201057: "Hardware product type specified is invalid. Enter a valid product type. If the product number you entered is \
            an actual product type, ensure the product type is appropriate for the object you are configuring. For example, do not use the \
            product type of a PXI device where an SCXI module is expected.",
        -201058: "Hardware product number specified is invalid. Enter a valid product number. If the product number you entered \
            is an actual product number, ensure the product type is appropriate for the object you are configuring. For example, do not use \
            the product number of a PXI device where an SCXI module is expected.",
        -201059: "Device information retrieval failed because PXI chassis is not identified. Use MAX or nipxiconfig to identify \
            your chassis.",
        -201060: "Syntax error encountered in INI file. Valid INI syntax allows for the following 3 types of lines: section headers, \
            items, and comments. A section header begins with an open bracket and ends with a closed bracket. Example: [mySection] An item \
            has an equals sign in between two strings. Example: myItem = 46 A comment begins with a semicolon. Example: ; This is my comment.",
        -201061: "Property specified cannot return its value because the custom scale for the channel does not include the value \
            in the range or table of pre-scaled values. Ensure that the custom scale includes all potential values for this property in the \
            range or table of pre-scaled values, or use a linear or polynomial scale.",
        -201062: "Selected lines do not support buffered operations. Ensure only lines that support buffered operations are being \
            used in the task. If using change detection timing, the task must be changed to non-buffered to support these lines.",
        -201063: "Device ID value in the driver does not match the device ID value from the device. Ensure the correct driver \
            is being used for this device.",
        -201064: "Configuration file is missing the required header fields. Add required header information at the top of the \
            text file prior to any data.",
        -201065: "Configuration file contains property names or values that are not contained within a valid table. Add the appropriate \
            start of table string prior to property names.",
        -201066: "Property setting found in a column with no property name heading. Remove the property setting from the column \
            or add the property name to the table definition.",
        -201067: "Configuration file contains an invalid start of table identifier. The table identifier may have been exported \
            from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version specified \
            in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or remove the \
            table from the file.",
        -201068: "Configuration file string contains invalid character escape sequence.",
        -201069: "Local channel name specified is invalid. Local channel names are of the form <task name>/<channel name>. Example: \
            task1/chan1",
        -201070: "Task does not include the Channels property. Specify the Channels property for this task.",
        -201071: "Task references a local channel from another task. Reference only global channels and local channels that belong \
            to this task.",
        -201072: "Task references a local channel that does not exist in this task. Remove the reference to the missing local \
            channel or create the local channel.",
        -201073: "Local channel specified is from a task that does not exist. Specify the task in question, move the local channel \
            to an existing task, or change the local channel to a global channel.",
        -201074: "Import operation supports tasks, channels, and scales only, but a hardware object was found in the file. Remove \
            the hardware objects from the input file.",
        -201075: "Import operation does not support tasks, channels, and scales, but such an object was found. Remove all tasks, \
            channels, and scales from the input file.",
        -201076: "NI-DAQmx version specified in the input file is newer than the installed NI-DAQmx version. Change the version \
            in the file to match the installed version. The import might still fail if the file contains properties that are not supported \
            by the installed version of NI-DAQmx.",
        -201077: "Section name specified is invalid. The format of the section name is [<objectType> <objectName>]. Example: [DAQmxDeviceDev1]",
        -201078: "Section identifier specified is invalid. Refer to the NI-DAQmx configuration file documentation for a list of \
            valid section identifiers. The section identifier may have been exported from a later version of NI-DAQmx and is not supported \
            by the version of NI-DAQmx installed on your system. Check the version specified in the file against the installed version of NI-DAQmx. \
            You can upgrade the version of NI-DAQmx installed on your system, or remove the section from the file.",
        -201079: "SCC slot number specified is invalid. Specify a slot number that is valid for the specified carrier.",
        -201080: "SCC specified cannot be placed in the slot specified. Specify a supported SCC for the given slot or specify \
            a slot that supports the given SCC.",
        -201081: "Channel was listed more than once in the task. A task cannot contain a channel with the same name twice. Remove \
            the duplicate entries from the configuration file.",
        -201082: "Hidden channel was listed more than once in the task. A task cannot contain a hidden channel with the same name \
            twice. Remove the duplicate entries from the configuration file.",
        -201083: "Task must contain at least one channel. Add a channel to the task in the configuration file.",
        -201084: "Hidden channels listed for the task were not in the channels list for the task. Add the missing hidden channels \
            to the channel list in the configuration file.",
        -201085: "Thermocouple CJC channel name property must be set when the thermocouple CJC source property is Channel. Set \
            the thermocouple CJC channel name property or set the thermocouple CJC source property to a value other than Channel.",
        -201086: "Attribute name specified is invalid. Validate the attribute name using your ADE. The attribute may have been \
            exported from a later version of NI-DAQmx and is not supported by the version of NI-DAQmx installed on your system. Check the version \
            specified in the file against the installed version of NI-DAQmx. You can upgrade the version of NI-DAQmx installed on your system, or \
            remove the attribute from the file.",
        -201087: "Task contains physical channels on one or more devices that require you to specify the Sample Clock rate. Use \
            the Sample Clock Timing function/VI to specify a Sample Clock rate. You cannot specify a Sample Clock rate if Mode is set to On \
            Demand.",
        -201088: "Task contains physical channels on one or more devices that require a different Sample Clock Timebase Source \
            than the one specified. Do not specify the Sample Clock Timebase Source. DAQmx will set the Sample Clock Timebase Source appropriately.",
        -201089: "Task contains physical channels on one or more devices that require a different Sample Clock Timebase Rate than \
            the one specified. Do not specify the Sample Clock Timebase Rate. DAQmx will set the Sample Clock Timebase Rate appropriately.",
        -201090: "Task contains physical channels on one or more devices that require the driver to select the Sync Pulse Source. \
            Do not specify the Sync Pulse Source. DAQmx will set the Sync Pulse Source appropriately.",
        -201091: "Minimum delay time between the sync pulse and start must be specified when using an external Sync Pulse Source. \
            Specify SyncPulse.MinDelayToStart.",
        -201092: "Sync pulse cannot be exported when using an external sync pulse source. Do not export the sync pulse, or use \
            the internal chassis sync pulse source.",
        -201093: "Task contains physical channels that have incompatible hardware restrictions for their Sample Clock Rates. Remove \
            incompatible physical channels from the task.",
        -201094: "An active device was specified for the attribute but it is not supported for channel expansion tasks. Do not \
            specify an active device when setting the attribute or do not use channel expansion.",
        -201095: "Driver was unloaded and then reloaded at a different base address after the session was created. Session is \
            unusable. Close and reopen the session.",
        -201096: "Sample clock timebase rate must be specified when using an external sample clock timebase.",
        -201097: "Sample Clock Rate requested is supported only if Enhanced Alias Rejection Enable is False. Set Enhanced Alias \
            Rejection Enable to False or decrease the Sample Clock Rate.",
        -201098: "When enabling auto zero on this device, all channels that are using auto zero must have the same auto zero mode. \
            Channels with auto zero disabled may be present in the same task as channels with auto zero enabled. Select the same auto zero \
            mode for all channels that are using auto zero.",
        -201099: "Task specified cannot be saved because the DAQmx Timing properties were specified on a per device basis using \
            the More: AI Convert: ActiveDevs property.",
        -201100: "Sample clock timebase divisor may not be specified when an external sample clock source is specified. Change \
            the sample clock source to onboard clock or do not configure the sample clock timebase divisor.",
        -201101: "Number of channels in task exceeds the device maximum given the requested Timing Type. Reduce the number of \
            channels or select a different Timing Type.",
        -201102: "Analog trigger source must be the first channel of the device in the acquisition or a valid analog trigger terminal. \
            Create your channels in a different order so that this channel is first, select a different channel from this device, or select \
            the first channel from another device in the task. If you explicitly named the virtual channel in DAQmx Create Channel you must use the \
            name assigned to that channel.",
        -201103: "Device support an analog channel as the source of an analog pause trigger only when it is the only channel from \
            this device in the task. Remove all of this device's channels currently in the task except the channel that will be used as the \
            analog trigger source, change the analog trigger source to a terminal, or select a channel from another device that only has one \
            channel in the task.",
        -201104: "An attempt has been made to use an analog trigger in multiple situations with differing properties. Change the \
            analog trigger properties so they are the same, select an analog trigger source from another device for one of the triggers, or \
            do not use an analog trigger for all situations.",
        -201105: "Resource requested by this task has already been reserved by a different task with conflicting settings. Unreserve \
            any other tasks using this device, or change their settings to be compatible with this task.",
        -201106: "Physical channel specified may only be used if the C Series module is installed in a slot that supports this \
            physical channel. Move your cDAQ module to a slot that supports this physical channel.",
        -201107: "Selected lines do not support buffered operations if the C Series module is installed in the specified slot. \
            Ensure only lines that support buffered operations are being used in the task. If using change detection timing, the task must \
            be changed to nonbuffered to support these lines. Move your cDAQ module to a slot that supports buffered operations.",
        -201108: "Device does not support both analog modulation and digital modulation simultaneously.",
        -201109: "You cannot use the Ref In/Out connector as both an input and an output at the same time.",
        -201110: "Digital Modulation User Defined Waveform is invalid.",
        -201111: "Device does not support User Defined Waveform with OOK modulation.",
        -201112: "Device component test failed. If problem persists, contact National Instruments technical support at www.ni.com/support.",
        -201113: "Power level is too low. OOK modulation requires the bypass path to be used, and power levels this low must use \
            the main path.",
        -201114: "Multi-device tasks with channels from both 446x and 447x devices require a 446x device to be in PXI slot 2.",
        -201115: "Waveform length must be a multiple of the waveform quantum.",
        -201117: "Property setting must be identical for all channels in the task.",
        -201118: "Operation must be performed on the entire task. It cannot be performed only on specific devices in the task. \
            Do not use the indexer, Item property in Visual Basic, or index operator in C++ to specify device names when performing this operation.",
        -201119: "Next Write is Last property not settable if Regeneration Mode is set to Allow Regeneration.",
        -201120: "Property requested is incompatible with the given Timing Response Mode. NI-DAQmx can automatically select a \
            compatible property value for you. To use the requested Timing Response Mode, do not set the specified property and allow NI-DAQmx \
            to set it for you. To use the requested property value, choose a different value for the Timing Response Mode.",
        -201121: "Task cannot be reserved because the CPU does not support the Streaming SIMD Extensions (SSE).",
        -201122: "Property requested is incompatible with the given Timing Type. NI-DAQmx can automatically select a compatible \
            property value for you. To use the requested Timing Type, do not set the specified property and allow NI-DAQmx to set it for you. \
            To use the requested property value, chose a different value for the Timing Type.",
        -201123: "Device supports an analog channel as the source of an analog reference trigger only when it is the only channel \
            from this device in the task. Remove all of the channels from this device in the task except the channel that you want to use as \
            the analog trigger source, change the analog trigger source to a terminal, or select a channel from another device that only has one \
            channel in the task.",
        -201124: "Only one task is permitted to have the Digital Output Memory Mapping for Programmed I/O Enable set to true at \
            a time. If the value is unset, NI-DAQmx will choose a value that is compatible with the system while reserving the task. Do not \
            set the property to true explicitly, set the property to false explicitly, or set the value to the default value to allow NI-DAQmx to \
            choose a value that is compatible with the system.",
        -201125: "Channel properties conflict. If Analog Input Source is _aignd_vs_aignd, then Analog Input Coupling must be set \
            to GND. If Analog Input Source is _external_channel, then Analog Input Coupling must be DC.",
        -201126: "DAQmx Timing property specified requires per device configuration. Explicitly specify the device(s) to which \
            this property should apply.",
        -201127: "Your ratiometric device must use excitation for scaling. The Use Excitation for Scaling property cannot be set \
            to false on this device. Use excitation for scaling by setting the Use Excitation for Scaling property to true. This will cause \
            NI-DAQmx to return ratiometric data instead of voltage data which is not supported by ratiometric devices.",
        -201128: "Device index requested is invalid. The value of the index must be between one and the number of devices in the \
            task.",
        -201129: "Memory Mapping for Programmed IO Enable cannot be set to true when Output Drive Type is Open Collector. Change \
            Output Drive Type to Active Drive or change Memory Mapping for Programmed IO Enable to false.",
        -201130: "Memory Mapping for Programmed IO Enable setting is not compatible with some of the physical channels in the \
            task. Change Memory Mapping for Programmed IO Enable to false or do not create the task with the incompatible physical channels.",
        -201131: "Reference and start trigger sources cannot be the same. Make the reference and start trigger sources different \
            from one another.",
        -201132: "Attempted to write a sample beyond the final finite sample. The sample specified by the combination of position \
            and offset will never be writable. Specify a position and offset which selects a sample up to but not beyond the final sample to \
            generate.",
        -201133: "Device cannot be configured for input or output because lines and/or terminals on this device are in use by \
            another task or route. This operation requires temporarily reserving all lines and terminals for communication, which interferes \
            with the other task or route. If possible, use DAQmx Control Task to reserve all tasks that use this device before committing any tasks \
            that use this device. Otherwise, uncommit or unreserve the other task or disconnect the other route before attempting to configure the \
            device for input or output.",
        -201134: "Number of values specified with Pause Trigger Digital Pattern property does not match the number of physical \
            lines requested with the Pause Trigger Digital Pattern Source property. Change one or both of the properties so the two numbers \
            are equal.",
        -201135: "Reference Trigger Digital Pattern Source property can be used only with the data lines of the devices. Do not \
            specify a PFI or a RTSI line in the pattern match source.",
        -201136: "Pause Trigger Digital Pattern Source property can only be used with the data lines of the devices. Do not specify \
            a PFI or a RTSI line in the pattern match source.",
        -201137: "Start Trigger Digital Pattern Source property can only be used with the data lines of the devices. Do not specify \
            a PFI or a RTSI line in the pattern match source.",
        -201138: "Task cannot be restarted because the first sample is not available to generate.",
        -201139: "Hardware revision is newer that the latest revision supported by the currently installed driver. Please upgrade \
            your driver to the version supplied with the device. Driver updates can also be downloaded from ni.com.",
        -201140: "Currently installed driver no longer supports this revision of the hardware. Please downgrade your driver to \
            the version supplied with the device. Older driver versions can also be downloaded from ni.com.",
        -201141: "EEPROM format is newer than the latest revision supported by the currently installed driver. Either self-calibrate \
            your device (this may modify the EEPROM format) or upgrade your driver to the version supplied with the device. Driver updates \
            can also be downloaded from ni.com. If uncertain, contact National Instruments technical support.",
        -201142: "Currently installed driver no longer supports the EEPROM format. Either self-calibrate your device (this may \
            modify the EEPROM format) or downgrade your driver to the version supplied with the device. Older driver versions can also be downloaded \
            from ni.com. If uncertain, contact National Instruments technical support.",
        -201143: "Hardware external calibration data format is newer than the latest revision supported by the currently installed \
            driver. Either externally calibrate your device (this may modify the calibration data) or upgrade your driver to the version supplied \
            with the device. Driver updates can also be downloaded from ni.com. If uncertain, contact National Instruments technical support.",
        -201144: "Hardware self-calibration data format is newer than the latest revision supported by the currently installed \
            driver. Either self-calibrate your device (this may modify the calibration data) or upgrade your driver to the version supplied \
            with the device. Driver updates can also be downloaded form ni.com. If uncertain, contact National Instruments technical support.",
        -201145: "Currently installed driver no longer supports the hardware external calibration data format. Either externally \
            calibrate your device (this may modify the calibration data) or downgrade your driver to the version supplied with the device. \
            Older driver versions can also be downloaded from ni.com. If uncertain, contact National Instruments technical support.",
        -201146: "Currently installed driver no longer supports the hardware self-calibration data format. Either self-calibrate \
            your device (this may modify the calibration data) or downgrade your driver to the version supplied with the device. Older driver \
            versions can also be downloaded from ni.com. If uncertain, contact National Instruments technical support.",
        -201147: "Calibration procedure has failed to resolve the calibration data format conflict. Perform a complete external \
            calibration on your device. This may modify the calibration data.",
        -201148: "Channel you are triggering on is not enabled. Enable the trigger source channel.",
        -201149: "Number of input/output points entered for the specified channel is insufficient for calibration. At least two \
            points are needed because this device has only gain error calibration constants and not offset calibration constants. Enter more \
            points to eliminate this error.",
        -201150: "Simulated device cannot be imported to replace a non-simulated device of the same name. Change the device name \
            in the import file and try importing again.",
        -201151: "PXI slot and PXI chassis numbers are required when creating a new simulated PXI device. Add PXI slot and chassis \
            number values for the device in the import file.",
        -201152: "IsSimulated flags for SCXI chassis and SCXI modules must have the same value. Either make both simulated or \
            make both non-simulated in the import file.",
        -201153: "Non-simulated SCXI module cannot be connected to a simulated digitizer. Change the SCXI Module IsSimulated flag \
            or change the SCXI Module so that it connects to a digitizer with the same simulation setting.",
        -201154: "Non-simulated SCXI module cannot be connected to a simulated cabled device. Change the SCXI module IsSimulated \
            flag or change the SCXI module so that it connects to a cabled device with the same simulation flag setting.",
        -201155: "SCXI module type specified does not support simulation. Remove the module from the import file or change the \
            module type.",
        -201156: "IsSimulated flags for an SCC carrier and all of the contained modules must be set to the same value. Change \
            the IsSimulated flags to match.",
        -201157: "Non-simulated SCC carriers cannot be connected to simulated devices. Change the cabled device of the SCC carrier \
            or change the IsSimulated flags on the SCC carrier to true.",
        -201158: "IsSimulated flag for cDAQ chassis and C Series modules must match. Change the IsSimulated flags in the import \
            file so that they match.",
        -201159: "cDAQ chassis does not have a slot that matches the specified slot number. The slot number specified is probably \
            too large. Change the slot number to be a valid slot number.",
        -201160: "Device type specified does not support simulation. Remove the IsSimulated flag from the import file for this \
            device or change the device type to one that supports simulation.",
        -201161: "Specified cDAQ chassis slot is already occupied by a C Series module. Change the slot numbers of the C Series \
            modules in your import file so that they are unique.",
        -201162: "Physical channel cannot be used by the task because an output task has reserved this line and the Digital Input \
            Tristate property is set to true. Set the Digital Input Tristate property to false.",
        -201163: "Physical channel cannot be used by the task because an input task has reserved this line to be tristated.",
        -201164: "Sample clock cannot be exported in this mode when the sample clock comes from an external source or an external \
            timebase source.",
        -201165: "Firmware for this device is too new. Downgrade the firmware for this device. If you need help downgrading, visit \
            ni.com/support.",
        -201166: "Firmware for this device is corrupt. Contact National Instruments for help with this device.",
        -201167: "Firmware for this device could not be updated. Contact National Instruments for help with this device.",
        -201168: "Firmware for this device is too old. Upgrade the firmware for this device.",
        -201169: "Device import failed because the device is not supported by the installed version and/or platform of NI-DAQmx. \
            Change the device type or do not import this device.",
        -201170: "Device import failed because the device does not support simulation and a device to overwrite could not be found. \
            Change the device type or do not import this device.",
        -201171: "Minimum temperature specified for the thermocouple measurement falls outside of the accuracy limit when using \
            polynomial scaling. Specify a value greater than the minumum temperature for polynomial scaling with this thermocouple type, or \
            set the Thermocouple Scale Type property to Table.",
        -201172: "AI channels on this device do not support using DC coupling while using IEPE excitation. Set excitation source \
            to none or the coupling mode to AC.",
        -201173: "Power supply configuration failed. Reboot or cycle the power on the device.",
        -201174: "SCXI-1600 does not support import through MAX. Deselect the SCXI-1600 in the import dialog or remove it from \
            the import file.",
        -201175: "Dev.AssociatedResourceIDs property is not supported by the device. Remove the Dev.AssociatedResourceIDs property \
            from the import file.",
        -201176: "Sample clock rate specified is too fast for the burst handshaking timing type. Change the sample clock rate \
            to be equal to or less than the maximum value or consider using the pipelined sample clock timing type. If you use the pipelined \
            sample clock timing type, refer to the device documentation for the differences between the burst handshake timing type and the \
            pipelined sample clock timing type.",
        -201177: "Device is not usable. The firmware was recently upgraded, and the system was not powered down and restarted. \
            Power down the computer and restart.",
        -201178: "Sample clock rate specified is too fast for the sample clock timing type. Change the sample clock rate to be \
            equal to or less than the maximum value or consider using the pipelined sample clock timing type. If you use the pipelined sample \
            clock timing type, refer to device documentation for the differences between the sample clock timing type and the pipelined sample \
            clock timing type.",
        -201179: "db reference value must be greater than zero.",
        -201180: "Input cal data point must be an AC Voltage for this module.",
        -201181: "Input source in not valid. Ensure that AI Input Source and AI Coupling are not both set for the same task.",
        -201182: "Internal excitation voltage selected for calibration is not valid.",
        -201183: "Internal excitation frequency selected for calibration is not valid.",
        -201184: "Device specified for PXI backplane communication is not a PXI device.",
        -201185: "Device specified for PXI backplane communication is not in the PXI chassis.",
        -201186: "Device specified for PXI backplane communication is not in the rightmost slot of the PXI chassis.",
        -201187: "Cold junction compensation channel cannot be used unless the corresponding analog input channel is configured \
            to measure temperature using a thermocouple. Use the thermocouple version of the DAQmx Create Channel VI/function to configure \
            the channel.",
        -201188: "Onboard device memory overflow. Because of system and/or bus bandwidth limitations, the driver could not read \
            data from the device fast enough to keep up with the device throughput. Reduce the number of programs your computer is executing \
            concurrently or use a different computer to calibrate your device.",
        -201189: "Onboard device memory overflow. Because of system and/or bus bandwidth limitations, the driver could not read \
            data from the device fast enough to keep up with the device throughput. This device supports high-speed (480Mb/s) USB but it is \
            connected to a full-speed (12 Mb/s) USB port. Connect this device to a high-speed (480 Mb/s) USB port, reduce the number of programs \
            your computer is executing concurrently, or use a different computer to calibrate your device. If you are using a USB hub, ensure \
            that it supports high-speed operation.",
        -201190: "Device is currently not usable and must be placed into firmware loader mode. Unplug the device USB cable and \
            plug it back in. If the device is plugged into a USB hub, ensure that you unplug the device from the hub.",
        -201191: "Property specified is not supported unless excitation is enabled. Enable excitation before attempting to access \
            the property.",
        -201192: "Connection to target failed for the requested configuration operation. Confirm that NI-DAQmx is installed on \
            the target.",
        -201193: "SCXI chassis address specified is invalid. Specify an SCXI chassis address between 0 and 31.",
        -201194: "Property cannot be read before reading the corresponding Channels Exist property. NI-DAQmx retrieves the channel \
            state from the hardware when the application reads the corresponding Channels Exist property. After reading the corresponding Channels \
            Exist property, you can retrieve other information about these channels.",
        -201195: "PCI Express interface layer error detected. Contact National Instruments for support.",
        -201196: "PCI Express interface layer error detected. Contact National Instruments for support.",
        -201197: "Circuit connected to the prototyping board causes channels to use too much power. Those channels were disabled \
            to prevent the device from using too much power. Turn the prototyping board power switch to the off position; correct the circuit \
            connected to the prototyping board; then turn the prototyping board power switch back on.",
        -201198: "Circuit connected to the prototyping board causes a short between the specified physical channel and the voltage \
            source. The output of the function generator has been suspended to prevent the device from using too much power. Turn the prototyping \
            board power switch to the off position; correct the circuit connected to the prototyping board; then turn the prototyping board power \
            switch back on.",
        -201199: "Circuit connected to the prototyping board causes too much power to be drawn from the specified source. The \
            output of the source has been suspended to prevent the device from using too much power. Turn the prototyping board power switch \
            to the off position; correct the circuit connected to the prototyping board; then turn the prototyping board power switch back on.",
        -201200: "Requested operation could not be completed because the prototyping board has been removed or disabled. The prototyping \
            board can be disabled by either switching the prototyping board switch to the off position, or by an incorrect connection on the \
            prototyping board causing too much power to be drawn from the device. Ensure that all connections on the prototyping board are correct \
            and that the prototyping board is properly inserted and powered on before attempting the operation.",
        -201201: "Offset error measured for this calibration task is out of range for the device. Ensure that the reference voltage \
            is accurate, specified correctly, and connected to the correct channel. Also ensure that the measured output voltage is specified \
            correctly and that the device is functioning properly.",
        -201202: "Gain error measured for this calibration task is out of range for the device. Ensure that the reference voltage \
            is accurate, specified correctly, and connected to the correct channel. Also ensure that the measured output voltage is specified \
            correctly and that the device is functioning properly.",
        -201203: "Virtual channel specified does not support the strain gage shunt calibration procedure.",
        -201204: "Virtual channel specified does not support the Wheatstone bridge shunt calibration procedure.",
        -201205: "Device simulation flag does not match the simulation flag of the RTSI cable.",
        -201206: "Task cannot contain a mixture of simulated devices and physical devices. Ensure the physical channels added \
            to the task refer to all physical devices or all simulated devices.",
        -201207: "Active Device cannot be specified when reading or writing timing properties in this multidevice task, due to \
            synchronization requirements.",
        -201208: "Sample rate specified is too fast for the ADC Timing Mode selected for this device. Decrease the sample rate \
            or use a faster ADC Timing Mode.",
        -201209: "Waveform length is too small for the Generate instruction before break block.",
        -201210: "Waveform subset length is too small for the Generate instruction before break block.",
        -201211: "Wait duration is too small for the Wait instruction before break block.",
        -201212: "Waveform length is too small for the Generate instruction in break block.",
        -201213: "Waveform subset length is too small for the Generate instruction in break block.",
        -201214: "Wait duration is too small for the Wait instruction in break block.",
        -201215: "Marker position specified is either too close to the end or the beginning of the waveform, or too close to another \
            marker in the Generate statement in break block.",
        -201216: "Wait until trigger instruction not allowed in a break block.",
        -201217: "Repeat until trigger instruction not allowed in a break block.",
        -201218: "If-Else block not allowed in a break block.",
        -201219: "break block cannot be nested in other break blocks.",
        -201220: "Clear Trigger instruction not allowed in a break block.",
        -201221: "break blocks are not allowed in finite or conditional loops.",
        -201222: "Generate or finite Wait instruction expected before a break block.",
        -201223: "Tristate setting must be identical for all lines in the port.",
        -201224: "Tristate setting must be applied to all lines in the port. Include all lines in the port in the Active Channel \
            list.",
        -201225: "Change detection timing cannot be used on this device while Memory Mapping for Programmed IO is enabled. Set \
            MemMapEnable to false or use a different timing type.",
        -201226: "Memory Mapping for Programmed IO Enable setting must be the same for all virtual channels in the task.",
        -201227: "Timing engine requested can only be used with lines that span two contiguous ports. Use the default timing engine \
            for the specified physical channels, use some lines from two contiguous ports, or use all of the physical data channels on the \
            device.",
        -201228: "Watchdog timer task could not be created because one of the digital output lines in the task uses memory mapping \
            for programmed I/O. Set DO.MemMapEnable to false for all lines in the task, or do not use a watchdog timer task.",
        -201229: "Memory mapping for programmed I/O cannot be enabled for the specified lines because a watchdog timer task uses \
            these lines. Set DO.MemMapEnable to false for all lines in the task, or do not use a watchdog timer task.",
        -201230: "Simulation flag of the referenced device does not match the simulation flag of the target.",
        -201231: "Local channel is not referenced by the task specified in the local channel name.",
        -201232: "Target storage was altered by another process before the changes could be saved.",
        -201233: "Object specified could not be found in storage.",
        -201234: "Storage specified is not valid or could not be found.",
        -201235: "Required object dependency was not found in storage.",
        -201236: "Communication mode specified is not valid for the SCXI Chassis.",
        -201237: "Physical channel name specified is invalid. Physical channel names are of the form <device name>/<physical channel \
            name>, for example, dev1/ai0.",
        -201238: "SCXI digitization is not supported by the device or physical channel.",
        -201239: "SCXI multiplexed digitization is not supported by the device.",
        -201240: "Digitization mode specified is not supported by the SCXI module.",
        -201241: "Connector 0 on the SCXI chassis communication device must be cabled to the SCXI module.",
        -201242: "SCXI chassis communication is not supported by the device.",
        -201243: "Address specified is invalid.",
        -201244: "Module type in the source storage does not match the module type in the destination.",
        -201245: "User defined information string entered exceeds the maximum allowable string length.",
        -201246: "Device cannot be created in MAX because the carrier contains no cartridge. Plug in a cartridge and attempt to \
            create the device again.",
        -201247: "Device cannot be created in MAX because a driver could not be found for the device. You may need to upgrade \
            NI-DAQmx.",
        -201248: "Device configuration may not be changed at this time because the device is locked.",
        -201249: "Wireless security setting is invalid. Ensure that all necessary settings are specified.",
        -201250: "Connection to the network device has timed out. The network device did not respond properly for a period of \
            time. If timeouts persist, contact your system administrator.",
        -201251: "Device could not be found on the network. This usually indicates an incorrect hostname or a DNS failure.",
        -201252: "Device cannot be reached because no known route to the device exists on the network.",
        -201253: "Network is currently unavailable. This usually indicates an unplugged network cable, a failing network component, \
            or an improperly configured network.",
        -201254: "Serial numbers of the network device do not match the serial numbers NI-DAQmx expected. Replace the original \
            device or module and try again, or use the reconnect button in MAX to locate the original device.",
        -201255: "EEPROM of this device has changed since this task began. Restart the task or reset the device to refresh the \
            EEPROM contents.",
        -201256: "Wireless channel specified is not available for this country code configuration.",
        -201257: "Country code is not configured. This setting is required to determine available wireless channels.",
        -201258: "Wireless configuration has been rejected by the device.",
        -201259: "Network configuration has been rejected by the device.",
        -201260: "Manual control attribute cannot be read when manual control is disabled. Enable manual control before reading \
            this attribute.",
        -201261: "Sample clock rate cannot be changed at this time. When changing the Sample clock rate for a running task, one \
            full period of the Sample clock must complete at the previous rate before NI-DAQmx can safely update the timing circuitry.",
        -201262: "Property specified is not supported for the bus type of the device.",
        -201263: "Firmware for this device could not be downloaded. To retry downloading the firmware, unplug the device and plug \
            it back in. If this problem continues, contact National Instruments for assistance.",
        -201264: "Scaled waveform is too large. After multiplication by the software scaling factor, the magnitude of each sample \
            must be less than 1.0.",
        -201265: "Input voltage limits exceeded. Protection circuity disabled the inputs. Ensure proper voltage levels on device \
            inputs.",
        -201266: "Property requested was not found. The property is either not supported by the object or has not been set.",
        -201267: "User defined information string entered is of an invalid length.",
        -201268: "Current limit specified cannot be applied to the channel because all current limit resources on the device have \
            been reserved. Use a current limit setting that is already in use for another channel, or free a current limit resource by disabling \
            current limiting on all channels that use a common current limit.",
        -201269: "Calibration operation cannot be completed unless the prototyping board is powered on.",
        -201270: "Certificate provided is not in PEM (Privacy Enhanced Mail) format. Only PEM certificates are supported.",
        -201271: "Product at the address provided was not the expected type. This may be due to a module being replaced or IP \
            addresses on the network being reassigned. Reconnect to the device in MAX or delete it from your system and rediscover it.",
        -201272: "IP address provided is invalid. IP addresses must be of the form x.x.x.x where x is a number from 0 to 255.",
        -201273: "Network device is already in use by another host.",
        -201274: "Device specified is not supported in 64-bit applications. To use this device, configure your development environment \
            to create a 32-bit application, or use a 32-bit development environment. Refer to the documentation for your development environment \
            for more information.",
        -201275: "Device cannot be calibrated using the coupling specified. Calibrate using a different coupling mode.",
        -201276: "Certificate provided is not in PEM (Privacy-enhanced Electronic Mail) or DER (Distinguished Encoding Rules) \
            format. Only PEM or DER certificates are accepted.",
        -201277: "Certificate file is too large to transfer to the device.",
        -201278: "Consecutive writes to a digital line occurred more frequently than the device can safely allow.",
        -201279: "Coupling specified conflicts with the Measurement Type of the channel. Configure the channel to use a coupling \
            appropriate for the measurement and sensor. For example, use DC coupling for DC sensors.",
        -201280: "Vertical Offset is not supported by this device.",
        -201281: "Device does not support using more than one trigger at a time. Configure the device to use only one trigger, \
            or use a device that supports using multiple triggers.",
        -201282: "Device power up failed. Try resetting the device. If the error persists contact National Instruments.",
        -201283: "Internal serial communication bus failed. Try resetting the device. If the error persists, contact National \
            Instruments.",
        -201284: "Improper chassis power levels detected. The +3.3 V fuse on the device might have blown, or there might be a \
            problem with the +3.3 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments.",
        -201285: "Improper chassis power levels detected. The +5 V fuse on the device might have blown, or there might be a problem \
            with the +5 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments.",
        -201286: "Improper chassis power levels detected. The +12 V fuse on the device might have blown, or there might be a problem \
            with the +12 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments.",
        -201287: "Improper chassis power levels detected. The -12 V fuse on the device might have blown, or there might be a problem \
            with the -12 V rail on the chassis. Try resetting the device. If the error persists, contact National Instruments.",
        -201288: "Property specified cannot be set while the task is reserved. Set the property prior to reserving the task or \
            unreserve the task prior to setting the property.",
        -201289: "Calibration procedure for your device does not support shorted inputs. Refer to the calibration procedure for \
            your device for more information.",
        -201290: "WEP key must be either 10 or 26 characters long.",
        -201291: "Pulse specifications cannot be written to a finite counter output task on this device.",
        -201292: "Sample Clock Overrun and Underflow Behaviors must be set to consistent values. Either set Overrun Behavior to \
            Stop Task and Error and Underflow Behavior to Halt Output and Error, or set Overrun Behavior to Ignore Overruns and Underflow Behavior \
            to Pause Until Data Available.",
        -201293: "Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The \
            actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied \
            is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being \
            calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. \
            3. The device is not functioning properly.",
        -201294: "Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The \
            actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied \
            is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being \
            calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. \
            3. The device is not functioning properly.",
        -201295: "Device could not complete the calibration operation. Calibration could fail for the following reasons: 1. The \
            actual reference signal applied for calibration was different from the value you specified. Ensure that the reference signal applied \
            is the same as the values that were input. 2. The reference signal was not stable over the period of time that the hardware was being \
            calibrated. Ensure that the reference signal specified is free of noise and does not drift over the duration of the calibration. \
            3. The device is not functioning properly.",
        -201296: "Sample Timing Type specified is not supported for counter output tasks on this device. Change the Sample Timing \
            Type to Implicit.",
        -201297: "Sample and hold is not supported for SCXI modules in parallel mode using digitizer channels other than 0 through \
            7. Disable sample and hold, use only digitizer channels 0 through 7, or use multiplexed mode.",
        -201298: "Property specified is not supported in conjunction with a conflicting property.",
        -201299: "Log Only mode is only supported for buffered tasks. Either use Log and Read mode or configure the task as Finite \
            or Continuous.",
        -201300: "Property specified is not supported when logging data.",
        -201301: "Reading samples is not supported in the specified logging mode. To access the samples while logging, either \
            open the file being written to or use a different logging mode.",
        -201302: "File permission error. You do not have the correct permissions for the file.",
        -201303: "Logging to this file format is not supported by NI-DAQmx. Convert the file to TDMS version 2.0 or later, or \
            specify a different file.",
        -201304: "File path specified is invalid, or the file is not a valid TDMS file. Specify the location of a valid TDMS file.",
        -201305: "Disk is full. Free up disk space, or specify a different file path.",
        -201306: "File specified is already opened for output by another task. Specify a different file path.",
        -201307: "Logging is not supported for this measurement type. Change the measurement type in order to use logging.",
        -201308: "Logging is not supported for finite counter tasks on this device. Change the Sample Mode of the task to continuous.",
        -201309: "Unable to write to disk. Ensure that the file is accessible. If the problem persists, try logging to a different \
            file.",
        -201310: "TDMS support is not installed or is too old. Use an NI-DAQmx runtime that includes TDMS support, or install \
            a supported version of TDMS from a stand-alone installer.",
        -201311: "File specified is already opened for output. NI-DAQmx requires exclusive write access.",
        -201312: "Logging is not supported for this channel and/or measurement type. Use a different measurement type or channel.",
        -201313: "Non-responsive counter detected. NI-DAQmx reset the counter. Counter timebases at the specified speed must remain \
            periodic, otherwise the counter can become non-responsive. Use an internal timebase or an external timebase that remains periodic.",
        -201314: "Multiple Sample Clock pulses were detected within one period of the input signal. Use a Sample Clock rate that \
            is slower than the input signal. If you are using an external Sample Clock, ensure that clock signal is within the jitter and voltage \
            level specifications and without glitches.",
        -201315: "Events cannot be configured after writing samples to the task.",
        -201316: "Timebase specified is too fast for a hardware-timed single-point counter output task.",
        -201317: "Multiple counters are not allowed in a buffered counter output task.",
        -201318: "Sample Clock pulse occurred before a pulse could be generated using the previous pulse specification. Use a \
            Sample Clock that is slower than the pulse train you want to generate.",
        -201319: "Sample Clock pulse occurred before the previous sample was acquired from all channels in the task. Use a Sample \
            Clock rate that allows time for the device to acquire samples from all channels. If you are using an external Sample Clock, ensure \
            that clock signal is within the jitter and voltage level specifications and without glitches.",
        -201320: "Retriggering can only be enabled for finite task with a Start trigger configured.",
        -201321: "Memory-mapped task detected data corruption because the memory was accessed by another program, such as a debugger \
            or virus scanner. Disable other programs that might access this memory, or disable memory mapping for the task.",
        -201322: "Memory mapping must be the same setting for all simultaneous tasks that use channels from a single subsystem.",
        -201323: "Sample Clock timing is not supported when using a two-counter measurement method. Use a one-counter measurement \
            method, or use a different timing type.",
        -201324: "Multiple counters are not allowed in a single counter output task when using Sample Clock timing.",
        -201325: "Module specified cannot be used as the first stage of a dual -stage analog input channel.",
        -201326: "Module specified cannot be used as the second stage of a dual-stage analog input channel.",
        -201327: "Modules specified are not valid for dual-stage analog input channels.",
        -201328: "Second stage of a dual-stage analog input channel cannot be empty.",
        -201329: "Data Transfer Mechanism must be DMA when Sample Mode is Hardware Timed Single Point on this device.",
        -201330: "Pulse train specifications cannot be modified while the task is running if Auto Increment Count is greater than \
            0",
        -201331: "Memory mapping is not supported on this device for non-buffered tasks using Sample Clock timing. Disable memory \
            mapping or change the buffer size.",
        -201332: "Logging is not supported for output tasks.",
        -201333: "Required scaling parameter has not been specified.",
        -201334: "Linear scaling requires unique electrical and physical values.",
        -201335: "Table scaling requires the same number of electrical values as physical values.",
        -201336: "Bridge scales are not supported for this measurement type. Use a custom scale for additional scaling.",
        -201337: "Device names must be 254 characters or shorter.",
        -201338: "Shunt resistor location specified is not valid for this calibration procedure.",
        -201339: "External timebase rate specified is too fast for this device. Reduce the timebase rate to less than 1/4 the \
            device oscillator frequency.",
        -201340: "Firmware on the device is out of date. Use Measurement & Automation Explorer to update the device firmware.",
        -201341: "Accessory cannot be connected while the task runs. The accessory uses different scaling or is unsupported. Ensure \
            the accessory is seated properly and restart the task.",
        -201342: "Unsupported accessory is connected to the module. Insert a supported accessory and restart the task.",
        -201343: "Overcurrent detected in the power supply for the accessory connected to the module. Check the external wiring \
            and ensure the accessory, if present, is properly seated. Then, reset the module using DAQmx Reset Device or Measurement & Automation \
            Explorer.",
        -201344: "ADC Timing Mode property was set to Custom, but the Custom Timing Mode property was not set. Specify a value \
            for Custom Timing Mode or change the ADC Timing Mode.",
        -201345: "Custom Timing Mode property is not supported unless the ADC Timing Mode property is set to Custom. Set ADC Timing \
            Mode to Custom before setting Custom Timing Mode.",
        -201346: "Synchronization Type cannot be Slave without configuring the device to use an external Sync Pulse. Set the Synchronization \
            \
            Type to Master or configure the device to use an external Sync Pulse.",
        -201347: "Sync Pulse was not detected before attempting to start the task. Ensure you connected the source of the Sync \
            Pulse to the device.",
        -201348: "Retriggered counter tasks do not support trigger skew correction. Set the Synchronization Type to Default or \
            disable retriggering.",
        -201349: "Multidevice tasks using the specified devices do not support a Start Trigger and Reference Trigger from different \
            devices. Using triggers from different devices can cause unwanted latency or incorrect behavior. Use triggers from a single device \
            or manually synchronize the devices.",
        -201350: "Synchronization Type cannot be Slave unless you configure the device to use a trigger with an external source. \
            Configure an external trigger or set Synchronization Type to None or Master.",
        -201351: "Memory mapping is not supported by this device for on-demand acquisitions.",
        -201352: "Analog bus line(s) in use by another device. Verify other devices are not currently using the analog bus line(s). \
            If you intend to share the line(s) between devices, ensure the Analog Bus Sharing Enabled property is True for all shared channels.",
        -201353: "Analog bus needed by the current operation is invalid. Verify that all carriers connected using expansion bridge(s) \
            are functioning properly.",
        -201354: "Cards specified cannot be used to create a SwitchBlock device. Use the current set of cards as single-card devices, \
            or use a different set of cards to create a valid combination.",
        -201355: "Switch device has been disabled to prevent it from exceeding the power limit for the carrier. To recover, call \
            DAQmx Disconnect All, or reset the device. The device can be reset either programmatically or by using Measurement & Automation \
            Explorer. Refer to your device documentation for more information.",
        -201356: "Topology specified is not supported by this card.",
        -201357: "Device must consist of at least one card.",
        -201358: "Simulation flag must be the same for the cards, devices, and carrier.",
        -201359: "Multicard devices must consist of cards contained in the same carrier.",
        -201360: "Carrier slot number specified for the card is invalid.",
        -201361: "Sync pulse cannot originate from the specified device for this combination of devices.",
        -201362: "Analog reference trigger and sync pulse must come from the same device.",
        -201363: "Minimum and maximum values specified are outside the bounds of the specified physical values for the table. \
            Change the table or the minimum and maximum value appropriately.",
        -201364: "Trigger detected that could not be acted upon by the device. Slow down your trigger source.",
        -201365: "Onboard regeneration cannot be used when there are more than 16 channels in the task. Reduce the number of channels \
            in the task or set Use Only Onboard Memory to false.",
        -201366: "Reference Clock signal was not found at the specified source.",
        -201367: "Filtering or digital synchronization of an internal signal is not supported by the device.",
        -201368: "Invalid number of calibration adjustment points provided. Use DAQmx Adjust Calibration to provide calibration \
            points for the device.",
        -201369: "Hostname specified is in use by another device.",
        -201370: "IP address specified is in use by another device.",
        -201371: "Multicast DNS service instance specified is in use by another device.",
        -201372: "Open thermocouple condition detected on thermocouple channel(s) you are attempting to calibrate. Ensure thermocouples \
            are properly connected and functioning before performing lead offset nulling calibration.",
        -201373: "Output peer-to-peer streaming with the Stream statement is not allowed in a script with If Else, Repeat Until, \
            or Break statements.",
        -201374: "Self-calibration failed. Performing an external calibration may fix the problem.",
        -201375: "Thermocouple lead offset nulling calibration is not supported by the specified channels. Make sure the device \
            supports thermocouple lead offset nulling calibration. Make sure all channels are thermocouple channels. Make sure open thermocouple \
            detection is enabled. Set skip unsupported channels to true.",
        -201376: "Data read from the EEPROM on the accessory attached to the device is invalid. Verify that any accessories configured \
            with this device are connected. If the problem continues, contact National Instruments technical support. The device might need \
            to be recalibrated or repaired by NI.",
        -201377: "Device is unusable while firmware update is in progress.",
        -201378: "Firmware version requested was not found on the system.",
        -201379: "Network devices are not supported on this platform.",
        -201380: "The requested operation is not supported by this device.",
        -201381: "One or more connections to external power rails are drawing too much power. The operation has been aborted to \
            prevent the device from using too much power. Remove the connection(s) to the external power rails and restart your task.",
        -201382: "The file write size specified is not evenly divisible by the volume sector size.",
        -201383: "The file write size specified is too large. Performance can suffer if the file write size is larger than one-fourth \
            the size of the buffer length.",
        -201384: "The simulated C Series module is not supported on this simulated chassis.",
        -201385: "Self-calibration failed to converge. Performing an external calibration may fix the problem.",
        -201386: "Self-calibration failed. Contact National Instruments technical support at ni.com/support.",
        -201387: "The DAQmx Adjust DSA AI Calibration with Gain and Coupling function/VI was executed more than once for the same \
            combination of gain and coupling settings. Call the DAQmx Adjust DSA AI Calibration with Gain and Coupling function/VI only once \
            for the following combination of gain and coupling settings:",
        -201388: "Network device is not reserved for this host.",
        -201389: "Modules were inserted or removed while the connection to the network device was lost. Reset the chassis using \
            DAQmx Reset Device or Measurement & Automation Explorer and wait for the modules to be redetected before proceeding.",
        -201390: "Connection to the network device was lost. This can indicate an unplugged network cable, a failing network component, \
            or a network device that is reserved by another host.",
        -201391: "Device could not complete calibration because calibration was not performed for all gain and coupling settings. \
            Use DAQmx Adjust DSA AI Calibration function/VI to calibrate for the following gain and coupling settings:",
        -201392: "Device does not support configuring tristate logic level in software.",
        -201393: "Tristate logic level is not supported on output only lines.",
        -201394: "Tristate logic level is only port configurable for this device.",
        -201395: "The task is not buffered or has no channels. If the task is not buffered, use the scalar version of this function. \
            If the task has no channels, add one to the task.",
        -201396: "Filter Delay Removal is not supported when an analog start trigger is in use. Change Filter Delay Removal to \
            false when using an analog start trigger. Refer to Filter Delay Removal in your DSA documentation for more details.",
        -201397: "Change detection has detected interrupts occurring at a higher rate than can be handled. The change detection \
            task has been stopped to prevent the device from being reset because of this condition. If this is the result of unwanted noise \
            on a digital signal, use a digital filter to eliminate unwanted digital transitions.",
        -201398: "Requested value is not supported for this property. If you did not directly set this property to the unsupported \
            value, check other properties that you have set, as they can influence the scaled value of this property.",
        -201399: "Multi-device timed DIO tasks require all modules to be the same type. You can select either all your serial \
            digital modules or all your parallel digital modules in this task.",
        -201400: "Failed to reserve file size. File size pre-allocation might require you to run the application with administrator \
            privileges. If the operating system uses User Account Control, configure this control properly.",
        -201401: "Retrieving properties from the network device failed. Make sure the device is connected.",
        -201402: "The samples per file specified is not evenly divisible by the file write size. Either change the samples per \
            file or modify the file write size. If not explicitly set, the file write size can be inferred from the buffer size, which is based \
            on the sample rate.",
        -201403: "You have specified a new file path but did not call DAQmx Start New File. To change the file path while logging, \
            configure Logging.SampsPerFile or call DAQmx Start New File.",
        -201404: "One or more cards for your NI SwitchBlock device have been inserted and/or removed while your system was powered \
            on. This can lead to unexpected behavior. Restart your system.",
        -201405: "An expansion bridge has been inserted or removed while your system is powered on. This can lead to unexpected \
            behavior. Restart your system.",
        -201406: "The 5 V fuse on your NI SwitchBlock carrier is blown. Refer to your documentation for help with replacing the \
            fuse.",
        -201407: "Specified property is not supported unless Sample Mode is set to Hardware Timed Single Point.",
        -201408: "Averaging of data is only supported when the Sample Mode is set to Hardware Timed Single Point and the Sample \
            Clock source is external to the device.",
        -201409: "The requested delay from Sample Clock is out of range for a hardware-timed single-point acquisition.",
        -201410: "The requested Sample Clock rate is too fast for hardware-timed single point. Consider decreasing the Sample \
            Clock rate, increasing the convert rate, or decreasing the delay from the Sample Clock. If using an external Sample Clock source, \
            you might also decrease the number of samples to average.",
        -201411: "The accessory attached to the device does not support connections. Attach an accessory that supports connections.",
        -201412: "The specified accessory channels are not present on this device. The accessory channels should be specified \
            for the device in the calibration session.",
        -201413: "There is no accessory attached to the device.",
        -201414: "The specified connection is not supported on the attached accessory. Refer to your accessory documentation for \
            supported connections.",
        -201415: "The module is not supported by the NI 9163.",
        -201416: "Switch device has been disabled to prevent it from exceeding its simultaneous relay drive limit. To recover, \
            disconnect a relay or channel.",
        -201417: "Timing is configured without supplying a clock signal. Either supply an external clock or use an internal timebase.",
        -201418: "Device firmware has not been updated because the firmware file uploaded is corrupt or is not a valid firmware \
            image file. Please verify that the file specified is a valid National Instruments firmware image.",
        -201419: "Device firmware has not been updated because the firmware file uploaded is for a different type of device or \
            an older revision of this device. Please verify that the firmware file is correct for this device.",
        -201420: "The network device is currently reserved by another host. Specify whether you want to override the other host's \
            reservation.",
        -201421: "The accessory attached to the device does not support this property.",
        -201422: "Your SwitchBlock carrier contains one or more cards with power characteristics unknown to the driver. To protect \
            the hardware from overheating, all devices within your carrier are disallowed from drawing power. Upgrade your software driver \
            to the latest version or shutdown your system and remove any unknown or invalid card(s).",
        -201423: "Communication with the chassis has been interrupted. Check the cabling and/or the wireless signal to the chassis. \
            Then reset the chassis using DAQmx Reset Device or Device Reset in MAX to re-establish communication.",
        -201424: "The multidevice task cannot be synchronized in its current configuration.",
        -201425: "The multidevice task does not have a method for synchronizing timing that is compatible with all of the included \
            devices.",
        -201426: "One or more devices do not support multidevice tasks.",
        -201427: "The specified device is not supported within the NI-DAQmx API.",
        -201428: "More than one sync pulse was detected. For proper operation, only a single sync pulse signal can be provided \
            to all DSA modules in a task.",
        -201429: "Start trigger delay is not available when a C Series Delta-Sigma module or a Reference Clock module is in the \
            task.",
        -201430: "You have requested an invalid number of reference voltages to write. Ensure the number of values to write is \
            the same as the number of entries in the array.",
        -201431: "Calibration offset adjustment has failed because the wrong channel was selected. Check the module calibration \
            procedure to decide which channel to use for the calibration offset adjustment.",
        -201432: "Calibration adjustment cannot be completed on a device performing different types of measurements (for instance, \
            voltage and current measurements). Make sure only one measurement type is being calibrated in each calibration session.",
        -201433: "Write failed because a watchdog timer task expired and changed the direction of the lines to tristate after \
            the digital output task was committed. To avoid this, unreserve and recommit the digital output task after the watchdog timer expiration \
            has been cleared to reconfigure the lines to output.",
        -201434: "Configuration failed because the task tried to change the direction of a line while the watchdog timer is expired. \
            Clear the expiration of the watchdog timer task before trying to change the direction of any line, even if the line is not watched \
            by the watchdog timer task.",
        -201435: "No samples provided to DAQmx Write to initialize buffered generation.",
        -201436: "Unable to route signals through the analog bus that are composed of different wire modes. Please disconnect \
            any devices of different wire modes from the analog bus before routing this device through the analog bus.",
        -201437: "The timeout value specified exceeds the maximum timeout value supported by this device.",
        -201438: "The device was rebooted after a watchdog timer expired due to unresponsive firmware or hardware components. \
            A watchdog timer that times out can cause digital output lines to change state. To clear this error, reset or power cycle the device. \
            Please also contact National Instruments technical support.",
        -201439: "Retriggering is not allowed for finite Sample Clock-timed counter output tasks. Reconfigure the task to use \
            a different sample timing type or disable retriggering.",
        -201440: "Neither an external reference clock nor a sample clock timebase has been specified. For multi-device synchronization, \
            you must specify the sync pulse source and either an external reference clock or sample clock timebase. \
            Refer to the device documentation for details on multi-device synchronization.",
        -201441: "On an NI 449x, specify either the sync pulse source or the sample clock timebase source but not both.",
        -201442: "Cannot measure two-edge separation with both the first and second terminal set to the same signal and both the \
            first and second edge set to the same edge. To measure the period of a signal, use a counter input period task. Otherwise, change \
            one of the terminals to a different signal, or change one of the edges to be different from the other.",
        -201443: "FREQOUT counter cannot generate the desired frequency. The 4-bit FREQOUT counter can divide the 20 MHz, 10 MHz \
            (20 MHz / 2), or 100 kHz (20 MHz / 200) timebase by a number between 1 and 16. Choose a frequency within this range.",
        -201444: "Multidevice tasks cannot use the on-demand sample timing type. Configure timing to synchronize and acquire samples \
            from multiple devices.",
        -201445: "You must configure strain gage channels for each arm of the rosette. Specify the strain gage channel names.",
        -201446: "Each tee rosette requires two physical channels. Make sure the physical channel list contains two physical channels \
            for each tee rosette.",
        -201447: "The selected rosette requires three physical channels. Make sure the physical channel list contains three physical \
            channels for each rosette.",
        -201448: "No rosette measurements specified. Please specify one or more rosette measurements.",
        -201449: "The requested port connection string is not in a valid format. The valid format is <device name>/port<port number> \
            (e.g. Dev1/port2).",
        -201450: "The requested device does not support cDAQ Sync connections.",
        -201451: "The operation cannot be completed on only one port. Two ports are required.",
        -201452: "The operation has been aborted.",
        -201453: "Cannot find disconnected connections between devices in different states (present and simulated). Please check \
            requested set.",
        -201454: "Carrier physically unable to contain the declared cards.",
        -201455: "cDAQ Sync connections are not allowed between physical and NI-DAQmx simulated devices. Use cDAQ Sync for either \
            only physical devices or only NI-DAQmx simulated devices.",
        -201456: "The devices attempting to be configured for cDAQ Sync do not have a common sync connection strategy.",
        -201457: "cDAQ Sync cannot add a connection from a port to the same port. Add a connection to a different port instead.",
        -201458: "Specified timeout value is not supported. Set the timeout to to a value > 0 or -1 (wait infinitely).",
        -201459: "Specified devices do not support cDAQ Sync connections. Please select a different set of devices.",
        -201460: "No devices scanned support cDAQ Sync connections. Requesting an empty string only scans physical devices (present \
            and offline) and ignores NI-DAQmx simulated devices. Please check your hardware configuration.",
        -201461: "Reference clock is not present. This task requires a reference clock to be present before configuring hardware.",
        -201462: "The attempted connection is not between an output port and an input port. Port 0 is input only. All other ports \
            are output only. Please check your connection and try again.",
        -201463: "The requested ports are not reciprocal. Make sure that the ports point at each other.",
        -201464: "A hardware fault has occurred. Please contact National Instruments technical support. To clear the fault, power \
            cycle the device.",
        -201465: "Cannot perform auto-configure on offline devices. Please remove offline devices from the requested set.",
        -201466: "Cannot auto-configure connections between devices in different states (present, offline, and simulated). Please \
            check requested set.",
        -201467: "Associated channels have conflicting properties. Make the conflicting property values consistent across channels \
            to fix the error.",
        -201468: "The requested cDAQ Sync device cannot be configured because the master timebase is not present. Tasks containing \
            cDAQ Sync devices that export or import a timebase must be committed in cascading order from the source to the destination. Use \
            DAQmx Control Task to commit the master timebase source task prior to committing or starting a slave task.",
        -201469: "You selected a different digitizer and communicator for an SCXI module that is in multiplexed mode. Configure \
            the SCXI module with the digitizer set to the same mode as the chassis communicator in MAX.",
        -201470: "Invalid calibration adjustment point(s) provided. Use DAQmx Get Calibration Adjustment Points to retrieve valid \
            adjustment values.",
        -201471: "The physical channel string contains multiple devices. You can include multiple physical channels on a single \
            device (for example, Dev1/ao0:3) but not multiple physical channels on multiple devices (for example, Dev1/ao0:3, Dev2/ao2).",
        -201472: "You must specify exactly one timestamp channel for a Navigation With Timestamp read call.",
        -201474: "The device is not supported on the local system, is incompatible, or the installation is corrupt. Install and/or \
            repair the appropriate driver.",
        -201475: "Auxiliary power not detected. Verify that the auxiliary power source is properly connected to the device and \
            that the auxiliary input fuse has not blown. Refer to the NI-DCPower documentation for information about replacing the input fuse.",
        -201476: "Task reservation failed because a watchdog timer task is reserved. Unreserve or commit the watchdog timer task \
            to reserve a new task.",
        -201477: "Reservation of watchdog timer task failed because another task is reserved or running. Stop and unreserve all \
            other tasks before reserving a watchdog timer task.",
        -201478: "Watchdog timer task has expired. Reset the chassis to resume normal operation.",
        -201479: "The attribute/property ArmStart.Term cannot be queried when a software arm start trigger is configured because \
            it cannot be exported to any terminal. Configure an external arm start trigger and query the desired attribute/property.",
        -201480: "There is already a session open to the device from another process, or a calibration session is open. You must \
            close the open session, exit the application holding the device, or release the device in the Soft Front Panel.",
        -201481: "If you specify an expiration state for any line on an NI 9401 in the range of line 0:3 or line 4:7, you must \
            specify an expiration state for every line in that range.",
        -201482: "The current number of channels chosen for calibration is incorrect. You must specify all channels for calibration.",
        -201483: "The selected master for the configured multi-device task is not able to export signals. Make sure that the first \
            channel in the task is from a device on a chassis that has an NI 9469 capable of exporting signals to the slave devices. If you \
            have any delta-sigma modules in your task, at least one must be in the master chassis. For time-based synchronization, \
            ensure all the chassis in the task are in the same synchronization network.",
        -201484: "The current task contains channels from both delta-sigma and non delta-sigma devices. Make sure the first channel \
            in the task is from a delta-sigma device and that it is located in a chassis that is able to share signals with its slave chassis \
            through an NI 9469, or the task is running on devices that support time-based network synchronization.",
        -201485: "Measured data size does not match reference data size. The module acquires data and receives reference data \
            in different functions. Please make sure these calibration functions are executed the same number of times during calibration.",
        -201486: "You must call DAQmx Setup Calibration first in order to calibrate this module.",
        -201487: "You must disable automatic firmware updates before attempting to manually update the firmware of your device.",
        -201488: "Firmware update failed. System attempted to update a different device than what you specified. Try updating \
            again.",
        -201489: "Invalid state for firmware update. You must call the firmware update action after calling beginFirmwareAction \
            and before calling disposeFirmwareAction.",
        -201490: "Firmware version being installed is older than the currently installed firmware.",
        -201491: "Firmware version being installed matches the currently installed version.",
        -201492: "Attempted operation is not supported on simulated devices.",
        -201493: "Shunt calibration failed. The calculated gain adjust is out of range. Ensure that the shunt calibration terminals \
            are connected properly and that the shunt resistance and shunt element location settings match how the hardware is wired.",
        -201494: "Device does not support simultaneous calibration of multiple channels. Calibrate channels one channel at a time \
            passing individual channels to different invocations of DAQmx Adjust Calibration.",
        -201495: "Device calibration requires all ranges to be calibrated for a single channel. Calibrate the ranges specified \
            in the procedure.",
        -201496: "Voltage settings not calibrated. Ensure all voltage settings are calibrated before trying to calibrate bridge \
            settings.",
        -201497: "You must run setupCalibration before running getCalDataPoints.",
        -201498: "AI channels on this device do not support using AC coupling while not using IEPE excitation. Enable IEPE excitation \
            or set the coupling mode to DC.",
        -201499: "The selected calibration mode cannot query calibration data points. Make sure you follow the calibration procedure.",
        -201500: "The channel in calibration adjustment did not call calibration setup. Make sure you call calibration setup before \
            calibration adjustment for this channel.",
        -201501: "The reference value input of calibration adjustment is out of range.",
        -201502: "DAC Offset Voltage Value is not set. When the DAC Offset Voltage Source property for a channel is set to External, \
            the DAC Offset Voltage Value property must be set. Set the DAC Offset Voltage Value property so the value matches the offset voltage \
            source connected to your device. Alternatively, use the internal DAC offset voltage source available on the device.",
        -209800: "DAQmx Read did not complete before the arrival of the next sample clock or change detection event which indicates \
            that your program is not keeping up with the hardware clock or the external change event. For tasks using sample clock timing, \
            slow down the hardware clock or else change your application so that it can keep up with the hardware clock. For tasks using change \
            detection timing, decrease the frequency of your event or else change your application so that it can keep up with the change event.",
        200079: "When specifying No Change as a watchdog state on a DSA channel, the actual behavior is determined by \
            the idle output behavior configured by the last task run on the module.",
        -209801: "DAQmx Write did not complete before the arrival of the next sample clock which indicates that your program is \
            not keeping up with the hardware clock. Slow down the hardware clock or else change your application so that it can keep up with \
            the hardware clock.",
        -209802: "DAQmx Wait for Next Sample Clock detected one or more missed sample clocks since the last call to Wait for Next \
            Sample Clock which indicates that your program is not keeping up with the sample clock. To remove this error, slow down the sample \
            clock, or else change your application so that it can keep up with the sample clock. Alternatively, consider setting the Convert \
            Errors to Warnings property to true and then handling the warning case appropriately.",
        -209803: "DAQmx Wait for Next Sample Clock detected 3 or more missed sample clocks since the last call to Wait for Next \
            Sample Clock which indicates your program is not keeping up with the sample clock, and data was subsequently lost before it could \
            be read by the application. To remove this error, slow down the sample clock. Consider restructuring the application so you can call \
            DAQmx Read more often. Setting the Convert Error to Warning property to True will not eliminate the error because the data is lost.",
        -209805: "Task with counter output detected a sample clock before the corresponding DAQmx Write was completed. This may \
            have occurred because the frequency of the counter output is too low for the given sample clock rate. A full output period must \
            complete before new data can be written. To avoid this problem make sure that the counter output frequency is significantly higher \
            than the sample clock rate.",
        -200831: "On Demand Simultaneous Analog Output Enable cannot be set to true unless Sample Timing Type is On Demand.",
        -201045: "Device connector number specified is invalid. Enter a valid connector number.",
        -201116: "Hardware timed non-buffered analog output is not supported on this device.",
        # ---------- General LabVIEW Error Codes ----------
        -2147467259: "Unspecified error.",
        -1967345152: "Invalid refnum. A specified refnum was not valid.",
        -1967345151: "Invalid property code. The specified property code is not valid for this refnum.",
        -1967345150: "Invalid privilege ID. The specified privilege ID is out of range.",
        -1967345149: "Invalid access type. The specified access type is not valid.",
        -1967345148: "Invalid argument. One of the specified arguments is invalid.",
        -1967345147: "Entry not found. The requested entry could not be found.",
        -375012: "A JSON numeric value is out of the range of a LabVIEW numeric type.",
        -375011: "LabVIEW failed to read or write a -Infinity or +Infinity floating-point value. You must enable LabVIEW JSON extensions \
            to allow support for a value of Infinity.",
        -375010: "LabVIEW failed to read or write a NaN floating-point value. You must enable LabVIEW JSON extensions to allow support \
            for a value of NaN.",
        -375009: "The JSON string contains an invalid multi-dimensional array.",
        -375008: "The array has an invalid number of dimensions.",
        -375007: "The cluster or JSON string contains an invalid number of elements. When strict validation is enabled, the number of \
            elements in the JSON string must match the number of elements in the input cluster.",
        -375005: "Type mismatch between JSON and LabVIEW.",
        -375004: "The path cannot be found in the JSON string.",
        -375003: "The JSON string is invalid. JSON strings must be encoded in UTF-8 and must conform to the JSON grammar.",
        -375002: "The cluster element name is invalid. Each element of the cluster must have either a unique name or no name, such as \
            an empty string.",
        -375001: "The JSON root container must be an array or cluster.",
        -375000: "The data type cannot be converted to or from JSON. Supported data types include arrays and clusters of booleans, numerics, \
            strings, and other arrays and clusters.",
        -120000: "SignalExpress is required to open this Express VI. Install SignalExpress or visit www.ni.com/signalexpress to download \
            an evaluation version.",
        -4850: "Device driver not present or not supported. The device driver needed to execute the In Port and Out Port VIs is not present. \
        LabVIEW does not support this device driver on Windows Vista or later.",
        -4824: "Clipped Floating-point data to fit the range [-1.0, 1.0]. The floating point data was outside of the range [-1.0, 1.0]. \
            The values were clipped to fit within this range.",
        -4820: "A buffer underflow has occurred. A buffer underflow has occurred because the application is not writing data quickly enough.",

        -4803: "The sound driver or card does not support the specified operation. The sound driver or card cannot accommodate the specified \
            configuration. Ensure that the parameters values are within the supported range for the hardware and drivers.",
        -4407: "LabVIEW cannot locate a palette item. LabVIEW cannot locate a palette item. Verify the path for each item in the items \
            array. The file might have been moved or deleted, or the path might be incorrectly formatted for the operating system. \
            For example, use \\ as path separators on Windows, : on OS X (32-bit), and / on Linux and OS X (64-bit).",
        -4406: "A VI item in the palette data array is not supported in this version of LabVIEW. A VI item in the palette data array is \
            not supported in this version of LabVIEW. This error can occur if you use a VI that is not supported in the LabVIEW \
            Run-Time Engine.",
        -4404: "The value for palette width is invalid. The value for palette width must be 0 or greater.",
        -4403: "A palette item is invalid. A palette item is invalid. Verify the path for each item in the items array. Paths to VIs and \
            palette files (.mnu) must be valid.",
        -4402: "The palette view format is invalid. The palette view format must be Icons, Icons and Text, or Text. Select Customize»View \
            This Palette As from the Controls or Functions palette to change the palette view format.",
        -4401: "The specified file is not a valid palette file (.mnu). The specified file is not a valid palette file (.mnu). Enter a \
            path to an existing palette file to read data from the palette file. Enter a path to a valid palette file to write data to the \
            file.",
        -4400: "The palette type is invalid. The palette type input is invalid. The palette type value has enumeration values of Controls \
            or Functions. The value provided was beyond the defined range.",
        -2584: "DIAdem could not be started. You must have DIAdem 9.1 Service Pack 2 or later installed to use the DIAdem Report Express \
            VI.",
        -2580: "The Write to Measurement File Express VI cannot append new data to frequency domain waveforms. Frequency domain waveforms \
            are constructed with a base frequency f0 and a delta frequency df. The frequency for a data point is then calculated as f0+N*df. \
            This calculation leads to erroneous results if data is appended to the waveform. This error can occur when you write a frequency \
            domain waveform to a file with Segment Headers set to One header only. Set Segment Headers to One header per segment to correct \
            this error.",
        1: "An input parameter is invalid. For example if the input is a path, the path might contain a character not allowed by the OS \
            such as ? or @. If you receive this error while trying to run File I/O VIs, refer to the KnowledgeBase at ni.com for more \
            information.", \
        2: "Memory is full. If you receive this error while developing a large application or storing large sets of data in LabVIEW, refer \
            to the KnowledgeBase at ni.com for more information.",
        4: "End of file encountered.",
        5: "File already open.",
        6: "Generic file I/O error. A possible cause for this error is the disk or hard drive to which you are trying to save might be \
            full. Try freeing up disk space or saving to a different disk or drive. Another possible cause for this error is there might be \
            a bad network connection. For example, the network connection is down or a network cable is unplugged.",
        7: "File not found. The file might be in a different location or deleted. Use the command prompt or the file explorer to verify \
            that the path is correct. Another possible cause for this error is there might be a bad network connection. For example, \
            the network connection is down or a network cable is unplugged.",
        8: "File permission error. You do not have the correct permissions for the file. To correct this error, verify that the file is \
            not in use by another application and that file permissions are set correctly. On Windows, navigate to the file, right-click the \
            file, select Properties, and set the Read-only option in the dialog box. On Linux or Mac OS X use chmod to set file permissions. \
            If you only need read access, you can use the Open/Create/Replace File function with the access input set to Read-only. \
            If you receive this error while trying to build an executable in LabVIEW 8.5 or later with the Report Generation \
            toolkit 1.1.2 or later , refer to the KnowledgeBase at ni.com for more information.",
        9: "Disk full. The disk or hard drive does not have enough free space to complete the operation. Try freeing up disk space or \
            saving to a different disk or drive.",
        10: "Duplicate path. If you receive this error while building an application in LabVIEW, refer to the KnowledgeBase at ni.com \
            for more information. If you receive this error while using a File I/O function or VI, you may be attempting to overwrite a file \
            or folder that already exists. Refer to the specific function or VI reference topic in the LabVIEW Help for information about \
            overwriting files or folders.",
        11: "Too many files open.",
        12: "Some system capacity necessary for operation is not enabled.",
        13: "Failed to load dynamic library because of missing external symbols or dependencies, or because of an invalid file format.",
        14: "Cannot add resource.",
        15: "Resource not found. This error might occur if you remove the front panel of the VI when building a stand-alone application.",
        16: "Image not found.",
        17: "Not enough memory to manipulate image.",
        18: "Pen does not exist.",
        19: "Configuration type invalid.",
        20: "Configuration token not found.",
        21: "Error occurred parsing configuration string.",
        22: "Configuration memory error.",
        23: "Bad external code format.",
        24: "External subroutine not supported.",
        25: "External code not present.",
        26: "Null window.",
        27: "Destroy window error.",
        28: "Null menu. If you reconnect a removable device, restart LabVIEW to use the device.",
        29: "Print aborted.",
        30: "Bad print record.",
        31: "Print driver error.",
        32: "Operating system error during print.",
        33: "Memory error during print.",
        34: "Print dialog error.",
        35: "Generic print error.",
        36: "Invalid device refnum.",
        37: "Device not found.",
        38: "Device parameter error.",
        39: "Device unit error.",
        40: "Cannot open device.",
        41: "Device call aborted.",
        42: "Generic error.",
        43: "Operation cancelled by user. If the VI or function that throws this error has an error out parameter, wire error out to the \
            selector terminal of a case structure to avoid this error message. If you are using the Open/Create/Replace File function or \
            Open/Create/Replace Datalog function, you can wire cancelled to the selector terminal of the case structure instead. \
            If the VI or function does not have error out, you can edit the error handling within the VI or function to avoid this error. \
            Double-click the VI or function and replace the general error handling with an error out indicator or some other form of \
            error handling. Save the new VI or function to a different directory than vi.lib so you do not overwrite the original.",
        44: "Object ID too low.",
        45: "Object ID too high.",
        46: "Object not in heap.",
        47: "Unknown heap.",
        48: "Unknown object (invalid DefProc).",
        49: "Unknown object (DefProc not in table).",
        50: "Message out of range.",
        51: "Null method.",
        52: "Unknown message.",
        67: "Interapplication Manager initialization error.",
        68: "Bad occurrence.",
        69: "Handler does not know what occurrence to wait for.",
        70: "Occurrence queue overflow.",
        71: "File datalog type conflict.",
        72: "Semaphore not signaled.",
        73: "Interapplication Manager unrecognized type error.",
        74: "Memory or data structure corrupt.",
        75: "Failed to make temporary DLL.",
        81: "Format specifier type mismatch. A format specifier does not match the data type of its corresponding argument in a Format \
            Into String or Scan From String function.",
        82: "Unknown format specifier. A bad format specifier was found in the Format String input to a Format Into String or Scan From \
            String function.",
        83: "Too few format specifiers. There are not enough format specifiers to match all of the arguments of a Format Into String or \
            Scan From String function.",
        84: "Too many format specifiers. There are more format specifiers than the number of arguments of a Format Into String or Scan \
            From String function.",
        85: "Scan failed. The input string does not contain data in the expected format. The Scan From String function was unable to scan \
            its input because the data was not in the expected format. Right-click the Scan From String function and select Edit Format String \
            to configure the format string to match the input data. You also can receive this error if the Scan From File or Scan From \
            String functions reach the end of the file. Refer to the KnowledgeBase at ni.com for more information about this use case.",
        87: "Error converting to variant. An error occurred converting from LabVIEW type to OLE variant type.",
        88: "Run-time menu error.",
        89: "Another user tampered with the VI password.",
        90: "Variant attribute not found.",
        91: "The data type of the variant is not compatible with the data type wired to the type input.",
        97: "A null or previously deleted refnum was passed in as an input.",
        98: "Incorrect file type. Attempted to read from or write to a file of a type incompatible with the operation. This normally is \
            a user data file.",
        99: "Incorrect file version. Attempted to read from or write to a file of a version incompatible with the write/read function \
            version. This file normally is a user data file.",
        100: "File contains erroneous data. This normally is a user data file.",
        116: "Unflatten or byte stream read operation failed due to corrupt, unexpected, or truncated data.",
        117: "Directory path supplied where a file path is required. A file path with the filename is required, but the supplied path \
            is a path to a directory.",
        118: "The supplied folder path does not exist.",
        122: "The resource you are attempting to open was created in a more recent version of LabVIEW and is incompatible with this version.",
        123: "A timeout occurred.",
        124: "A string contained an unexpected null character.",
        125: "A stack overflow occurred. To correct this error, restart LabVIEW and review your code for recursive data structures.",
        1000: "The VI is not in a state compatible with this operation. This error can occur for several reasons. This error can occur \
            if you attempt to edit a VI that is running or reserved for running. This error also can occur if you attempt to open a reference \
            to a VI that is running or reserved for running. A VI is reserved for running when you open a reference to the VI by \
            wiring a type specifier VI Refnum to the Open VI Reference function, or when you have a Static VI Reference linked to the \
            VI within a running VI. This error also can occur if you try to run a VI using the run method while the target VI is \
            running or reserved for running. To correct this error, ensure the target VI is idle or reentrant. If it is reentrant, \
            use the Open VI Reference function with the options input set to 0x08 to prepare the VI for reentrant run or use the \
            Open VI Reference function with the type specifier VI Refnum wired to a strictly typed VI reference. This error also can \
            occur if you attempt to obtain a VI's image while the VI is being modified programmatically. Wait until the VI is not being \
            modified to get the image of a panel or diagram.",
        1001: "The VI front panel is not open. Use the Window Appearance page to configure if the front panel is shown when the VI is \
            run or loaded. You also can use the Front Panel:Open method to open the front panel programmatically.",
        1002: "The VI cannot run because it has a front panel control in an error state.",
        1003: "The VI is not executable. This error may occur because the VI is either broken or contains a subVI that LabVIEW cannot \
            locate. Select File»Open to open the VI and verify that you can run it. Refer to the KnowledgeBase at ni.com if you receive this \
            error in one of the following situations: while using the VI Server to call a VI dynamically or while building an application.",
        1004: "The VI is not in memory.",
        1005: "VI execution has been disabled in the VI Properties dialog box. Open the Execution page of the VI Properties dialog box \
            to change the settings for the VI execution.",
        1006: "FPDCO on connector pane thinks it is constant.",
        1007: "No IP record in summary.",
        1008: "Cannot load connector pane.",
        1009: "Variant tag out of range.",
        1010: "No default or operate data.",
        1011: "VI Creation failed.",
        1012: "Cannot load block diagram.",
        1013: "Cannot load front panel. Make sure you include the front panel of the VI when building a stand-alone application.",
        1014: "Linker error.",
        1015: "Printer is not responding. Check printer configuration.",
        1016: "Cannot load History.",
        1017: "VI has been modified on disk since it was last loaded or saved.",
        1018: "Unspecified error occurred.",
        1019: "One or more untitled subVIs exist. This file cannot be saved until all dependent files have been named.",
        1022: "Wizard Template not found.",
        1023: "Wizard template does not have a diagram.",
        1024: "Call Instrument aborted.",
        1025: "Application Reference is invalid.",
        1026: "VI Reference is invalid.",
        1027: "For the requested operation, the reference cannot be reserved as requested, is in an improper reservation mode, or the \
            execution state must be set to running or reserved.",
        1028: "Attribute selector is invalid.",
        1029: "VI Server property is read-only.",
        1030: "VI Reference is already reserved for editing.",
        1031: "VI Reference type does not match VI connector pane.",
        1032: "VI Server access denied. If this error is returned from the Open VI Reference function on a remote connection, use the \
            VI Server page of the Options dialog box to ensure that the VI is exported. If this error is returned from a Property or Invoke \
            Node, the property or method might not be allowed for remote VI Server connections. For example, the Application:All VIs In \
            Memory property is allowed locally, but remotely you should use the Application:Exported VIs In Memory property instead. \
            Refer to the help for the property or method to determine if it is allowed remotely.",
        1033: "Bad run-time menu file version.",
        1034: "Bad run-time menu file.",
        1035: "Operation is invalid for this type of VI.",
        1036: "Method selector is invalid.",
        1037: "Incompatible VI Server protocol version.",
        1038: "Required parameter missing.",
        1039: "VI was aborted.",
        1040: "VI is password protected.",
        1041: "Incorrect password.",
        1042: "Attempted recursive call.",
        1043: "The property or method is not supported in this version of LabVIEW. This error can occur if you use a property or method \
            that is not supported in the LabVIEW Run-Time Engine.",
        1044: "VI is locked.",
        1045: "Null Refnum passed to Close Reference.",
        1051: "A LabVIEW file of that name already exists in memory, or exists within a project library already in memory. To resolve \
            this error, give the file a unique name that does not already exist in the application instance.",
        1052: "The LabVIEW filename is invalid.",
        1054: "The specified object was not found.",
        1055: "Object reference is invalid.",
        1056: "Specified object is not scriptable in this version.",
        1057: "Type mismatch: Object cannot be cast to the specified type.",
        1058: "Specified property not found.",
        1059: "Unexpected file type.",
        1060: "Object cannot contain (own) the specified object.",
        1061: "Unable to create new object.",
        1062: "Specified objects cannot be wired together.",
        1063: "Specified terminal not found in the object.",
        1066: "Hardware open error.",
        1067: "Hardware close error.",
        1068: "Hardware transact error.",
        1069: "Hardware DLL missing.",
        1070: "Hardware no session error.",
        1071: "LabVIEW cannot locate the specified method.",
        1072: "This property or method is not yet implemented.",
        1073: "This property is writable only when the VI is in edit mode, or this method is available only when the VI is in edit mode. \
            Refer to the KnowledgeBase for more information about this error.",
        1074: "Cannot create a control/indicator for the specified terminal.",
        1075: "Cannot create a constant for the specified terminal.",
        1076: "VI is not debuggable.",
        1077: "Invalid property value.",
        1082: "Operation not valid for strict type definition instance.",
        1086: "Wrong control type. The operation is not allowed on this kind of control or a control at this level.",
        1087: "There is no DataSocket information available for the object.",
        1088: "Bad value for parameter.",
        1089: "Error occurred while executing script. Error message from server: %s.",
        1090: "Specified object cannot be moved.",
        1091: "The VI Server or client received an unrecognized message.",
        1094: "Queue and notifier references of the same name must be obtained using the same data type. When you obtain a reference to \
            a queue or notifier, you can specify which data type the mechanism stores. You can receive this error when future requests to obtain \
            a reference to the same mechanism do not wire the same data type as the original specified data type. Unnamed mechanisms do not have \
            this restriction, because each request to obtain an unnamed mechanism creates a new mechanism. Refer to the KnowledgeBase at ni.com \
            for more information about avoiding this error.",
        1095: "This container cannot be left without a subtype. Right-click the container border and select Replace or drag new subtype.",

        1096: "The Open VI Reference function cannot prepare a non-reentrant VI for reentrant run. Verify the values you wired to the \
            Open VI Reference function.",
        1097: "An exception occurred within the external code called by a Call Library Function Node. The exception might have corrupted \
            the LabVIEW memory. Save any work to a new location and restart LabVIEW. Verify the values you wired to theCall Library Function \
            Node.",
        1098: "Cannot disconnect type definitions or polymorphic VIs if the block diagram is not available.",
        1100: "No object of that name was found. No reference could be returned. You can use the Obtain Queue or Obtain Notifier function \
            to look up a queue or notifier by name. If create if not found? is FALSE and a queue or notifier with that name was not found, \
            LabVIEW returns this error.",
        1102: "The string wired to the xml string input is empty.",
        1103: "The XML tag describing the type of data is not recognized.",
        1104: "No end tag was found for an XML start/end tag pair.",
        1105: "An unknown or unexpected XML tag was discovered.",
        1106: "The XML tag describing the type of data does not match the wired type.",
        1107: "The XML enumerated type choice(s) does not match the wired type.",
        1108: "XML value text is illegal or out of range for type and/or format.",
        1109: "Unsupported data type.",
        1110: "No longer used.",
        1111: "Release Semaphore called on a semaphore that was not currently acquired.",
        1122: "Refnum became invalid while node waited for it.",
        1123: "You cannot create an object (such as control caption) in built applications. You must create these objects in the LabVIEW \
            development system.",
        1124: "VI is not loadable.In a built application, this error might occur because the VI being loaded was last compiled for a different \
            OS or with CPU features, such as SSE, that this target does not support. In this case you must rebuild the application for the \
            target OS and make sure SSE compiler settings in the build specifications match the target platform. This error also might occur if the \
            VI is a polymorphic VI, which cannot be loaded in the LabVIEW Run-Time Engine. You must load an instance of the polymorphic VI \
            instead of the polymorphic VI itself.",
        1125: "File version is later than the current LabVIEW version.",
        1126: "VI version is too early to convert to the current LabVIEW version. Refer to the Converting VIs topic in the LabVIEW Help \
            for more information about converting VIs to the current LabVIEW version.",
        1127: "Cannot instantiate template VI because it is already in memory.",
        1128: "Input unit is not compatible with the current unit.",
        1129: "You cannot assign the same numeric value to two or more strings in a ring control. You also cannot assign the same string \
            value to two or more strings in a combo box control. If you receive this error while trying to write to the Strings and Values \
            [] property of a control, refer to the KnowledgeBase at ni.com for more information.",
        1130: "The VI Server connection peer is unresponsive. Refer to the Connection Responsiveness: Check Method topic in the LabVIEW \
            Help for more information about connection polling.",
        1131: "You cannot use this property with this system control.",
        1135: "The tree control's active item is not valid for this property.",
        1136: "You wired an invalid item tag to a tree control property or method.",
        1137: "Tree control's internal data is corrupt.",
        1138: "An exception occurred within external code called by LabVIEW. This might have corrupted the LabVIEW memory. Save any work \
            to a new location and restart LabVIEW.",
        1144: "Cannot insert VI in a subpanel control because VI is already open.",
        1145: "Cannot open VI because it is already in a subpanel control.",
        1146: "You attempted an operation that would change a child-only item into a parent item.",
        1147: "Cannot insert a remote VI in a subpanel control.",
        1148: "This property is read only while the VI is in a subpanel.",
        1149: "Cannot close or set the state of a closed front panel. The front panel must already be open before you close it or set \
            its state.",
        1150: "Cannot open a front panel that is already open. To set the state of the open front panel, use the Front Panel Window:State \
            property.",
        1151: "Invalid input for front panel state.",
        1156: "Memory full error, possibly due to a data format not matching expected data type. This is caused by trying to allocate \
            a buffer that is too large for memory. Although normal allocation might run the system out of memory, frequently an out of memory \
            error is caused by interpreting the data incorrectly and treating something that is data as the size of the data. Before assuming \
            that the system needs more memory to complete the operation, make sure the read format you are requesting is valid for the data \
            being read.",
        1157: "You cannot use this property with a numeric indicator.",
        1174: "Invalid return parameter for Call Library Function Node. The return type must be Void, Numeric, or String. Numeric return \
            types are passed by value. Strings return types are passed as a C String Pointer or a Pascal String Pointer.",
        1175: "Invalid array dimension in Call Library Function Node configuration. An array must have 1 or more dimensions.",
        1176: "Invalid waveform dimension in Call Library Function Node configuration. A waveform must have 0 or 1 dimensions.",
        1177: "Invalid data type for Call Library Function Node parameter. Void can be used only as return type of function.",
        1186: "Cannot show or hide the label on its own. Label visibility is controlled by the label owner.",
        1187: "Internet Explorer is required for this operation but it is not installed.",
        1188: "The static VI reference is not configured. Right-click the Static VI Reference function on the block diagram and select \
            Browse for Path. Navigate to the VI for the reference and click the Open button to configure the reference.",
        1190: "The operation is not allowed when the control has key focus.",
        1191: "The wire already has a probe on it.",
        1192: "No data range set for digital displays.",
        1193: "When a Boolean control has a latch mechanical action, you cannot use the Value property to read or write its value. When \
            a Boolean control is configured with a latching mechanical action, the Value property always returns an error. Due to race conditions \
            that can occur when you have a Boolean value with latching mechanical action, you cannot programmatically read Boolean values \
            that are set with a latching mechanical action.",
        1194: "This Express VI requires DIAdem 8.1 or later and the LabVIEW DIAdem Connectivity VIs version 2.1 or later. The Connectivity \
            VIs are available for free download from ni.com. Refer to the National Instruments Web site to download the VIs.",
        1196: "Cannot list the same terminal more than once in the grown region of the expandable subVI.",
        1197: "This operation is not valid for static VI references. To run a VI using a static VI reference, use an Invoke Node to call \
            the Run VI method. Set the Invoke Node class to VI and select the Run VI method.",
        1198: "The VI is not in a state compatible with this operation. Change the execution mode of the referenced VI to reentrant for \
            this operation.",
        1301: "The dimension of the array passed in does not match the expected dimension for the operation.",
        1303: "The elements of the array are not unique. There are duplicated items in the array.",
        1304: "The array index is outside of the array bounds.",
        1305: "The required page cannot be found.",
        1306: "Unable to load new code resource to the node. Code resource already loaded.",
        1307: "Subpanel control could not open the VI window. You tried to insert a VI into a subpanel control, but the front panel or \
            block diagram window you want to insert does not exist.",
        1308: "The Property or Invoke Node is not linked to a front panel control.",
        1309: "The Property or Invoke Node reference input terminal is already wired.",
        1310: "The object is not in the same VI as the Property or Invoke Node. The control reference of the control does not belong to \
            the VI that owns the Property or Invoke Node.",
        1311: "The input for class name is not correct or is in the wrong format. The input for class name is not correct or is in the \
            wrong format. The correct format should begin with the class type followed by the path to the object using the long names. For \
            example, VI Server:Generic:GObject",
        1312: "Structure frame index is out of range. This error occurs when you use an index value that is out of range to access a frame \
            in a Case, Stacked Sequence, or Event structure.",
        1313: "You cannot use this property on a control in a radio buttons control.",
        1314: "You cannot use this property on an instance of a type definition set to update automatically from the master copy of the \
            type definition.",
        1315: "You have attempted to create a data type with a descriptor that is too large.",
        1319: "Cannot insert a VI into a subpanel that is not in a running state.",
        1320: "In run mode, LabVIEW cannot get or set a property for a control part that has not been created.",
        1321: "NI License Manager is not initialized. Verify that NI License Manager is installed on the computer by selecting Start>>All \
            Programs>>National Instruments>>NI License Manager.",
        1322: "Invalid project build reference.",
        1357: "A LabVIEW file from that path already exists in memory, or exists within a project library already in memory. To resolve \
            this error, give the file a path that does not already contain a LabVIEW file in any open application instance.",
        1358: "The splitter bar cannot be moved to this position because it violates the minimum or maximum size of a descendant pane. \
            When LabVIEW tries to move the splitter bar to the specified position, at least one pane shrinks smaller than its set minimum size. \
            For example, if you have a VI with one vertical splitter bar, and the minimum size of the left pane is 50, wiring 10 to the Splitter \
            Position property will return this error. To correct this error, set the minimum size of the pane to a smaller value, or wire a value \
            to the Splitter Position property that does not shrink the pane beyond its minimum size.",
        1359: "A drag cannot start because a previous drag transaction is still pending.",
        1360: "Cannot provide the type of data requested for this drag and drop operation. To correct this error, ensure that a drag and \
            drop operation is in progress when you call this function and that the data type and drag data name match what is currently available \
            during the drag and drop operation.",
        1361: "The name or data type of a drag data element conflicts with the built-in LabVIEW drag data types. You cannot use the prefix \
            LV_ on a data name.",
        1362: "Cannot use this property with this string display mode or if word wrapping is enabled. Change the display mode to 0 (normal) \
            and/or disable word wrapping to use this property.",
        1363: "The specified name or GUID is invalid.",
        1364: "The provider plug-in is not installed or somehow corrupt.",
        1365: "Failed to generate a valid GUID.",
        1366: "You cannot hide or show the scroll bars of a subpanel control when a VI containing multiple panels is inserted.",
        1370: "The selected build failed to complete.",
        1376: "A Diagram Disable structure cannot have a default frame. This error occurs when you try to use the Default Frame property \
            with a Diagram Disable structure. You can use this property only with the Conditional Disable structure.",
        1377: "A Diagram Disable structure cannot have conditions. You can use the Conditions property and the Get Frame Index method \
            only with the Conditional Disable structure.",
        1378: "Cannot set the Active Frame property on a Conditional Disable structure. This error occurs when you try to use the Active \
            Frame property with a Conditional Disable structure. You cannot use this property with a Conditional Disable structure because \
            conditions determine the active frame. You can use this property only with a Diagram Disable structure.",
        1380: "License checkout failure. Unable to checkout the requested license feature because the license is invalid or does not exist.",
        1381: "Cannot create semaphores with a size less than one.",
        1384: "Cannot start dragging because duplicate names for drag data types were passed to the Start Drag method or Drag Starting? \
            event. To correct this error, ensure that the names you use for drag data are unique in each element of the data array for the \
            method or event.",
        1385: "Cannot start a drag and drop operation because the data provided is invalid. To correct this error, verify that the drag \
            data array is not NULL and that all elements have names and data fields.",
        1388: "The block diagram you are attempting to access belongs to a VI that is either in evaluation mode or has an invalid license. \
            To correct this error, you must obtain a valid license for the VI and its containing library.",
        1389: "You are attempting to save or copy a VI that is either in evaluation mode or has an invalid license. To correct this error, \
            you must obtain a valid license for the VI and its containing library.",
        1390: "You attempted to open a VI Server reference to an out-of-scope VI. A VI can open VI Server references only to other VIs \
            that it could call as subVIs. After the reference is opened, that VI can return the reference to other VIs that could not normally \
            open the reference.",
        1396: "Cannot convert text from the source character set to the destination character set.",
        1397: "You have not wired a required input on this subVI. To correct this error, wire the required input.",
        1398: "The subVI cannot be inlined because there is a local variable in the block diagram.",
        1399: "The subVI cannot be inlined because a front panel terminal is not on the root diagram. For example, this error might occur \
            when a front panel terminal is inside a structure.",
        1430: "The path is empty or relative. You must use an absolute path.",
        1432: "The specified format cannot be used with floating point data. For example, hexadecimal notation is not a valid format for \
            floating point numbers.",
        1434: "The precision is greater than the maximum allowed value for this format.",
        1436: "Numeric precision cannot be negative.",
        1438: "Archive version is later than the current LabVIEW version.",
        1439: "A project library cannot be copied to the same folder as the original library because the new library files would conflict \
            with the original library files on disk. You must specify a different location on disk when copying a project library.",
        1440: "The filename does not match the expected name. The file specified must have the same filename as the original file.",
        1443: "Debug connection refused by specified server. Only one debug connection is allowed per application or shared library.",
        1444: "No VIs to download from application, connection closed.",
        1445: "Open VI Reference no longer matches VIs in memory by filename. A filename is no longer sufficient because the full name \
            of a VI now includes any owning libraries. You can use the Strip Path function to wire the filename as a string, but this will \
            not work for VIs in libraries.",
        1447: "There was a name conflict while saving for previous. VIs in libraries are saved in the form LIBRARYNAME_VINAME. There is \
            already a VI in this hierarchy with this name.",
        1449: "Arrays must have at least one dimension and a maximum of 63 dimensions.",
        1450: "One or more untitled library dependencies exist. This file cannot be saved until all dependent files have been named.", \
        1451: "One or more untitled dependencies exist. This file cannot be saved until all dependent files have been named.",
        1452: "This library was saved in an earlier version of LabVIEW. It must be loaded and saved in the current version of LabVIEW.",
        1453: "You may only set the vertical arrangement on a label, caption or free label.",
        1454: "LabVIEW classes cannot be flattened as XML in this version of LabVIEW.",
        1455: "Revert failed. This item has been edited in another context on this machine. Only that instance can be reverted.",
        1468: "Specified ability not supported by the library. Verify the ability name does not contain spaces.",
        1469: "Specified ability already exists. You cannot add an ability multiple times.",
        1470: "Specified folder is outside the library. You cannot add library items to folders that do not belong to the library.",
        1483: "Cannot change width of the plot legend when you configure the plot legend to automatically resize, or if the legend has \
            more than one entry and you arrange the plot legend horizontally. Right-click the graph or chart and deselect Autosize Plot Legend \
            in the shortcut menu to disable automatic resizing and make sureyou arrange the plot legend vertically.",
        1484: "LabVIEW cannot inline the subVI into its calling VIs because the block diagram of the subVI contains an implicit control \
            reference. To correct this error and inline the subVI, remove the implicit control reference.",
        1485: "LabVIEW cannot inline the subVI into its calling VIs because the block diagram of the subVI contains an implicit Property \
            Node or Invoke Node. To correct this error and inline the subVI, remove the implicit Property Node or Invoke Node.",
        1488: "The migration file cannot load because it is no longer supported.",
        1489: "The migration file cannot load because its content is not valid or is corrupt.",
        1490: "The migration file cannot load because it makes references to data that does not exist or is invalid.",
        1491: "If you obtain a queue reference in one application instance, you cannot use that queue reference in another application \
            instance. You cannot use queues for communication between LabVIEW application instances.",
        1492: "If you obtain a notifier reference in one application instance, you cannot use that notifier reference in another application \
            instance. You cannot use notifiers for communication between LabVIEW application instances.",
        1493: "The save operation failed because multiple files of the same name cannot be saved into a single LLB. To correct this error, \
            save to a folder instead of an LLB.",
        1497: "Cannot unlock a library for edit when instances in running VIs exist.",
        1498: "Library has errors. Fix the errors before attempting this operation.",
        1499: "Library has edits in another context. Sync up changes before attempting this operation.",
        1500: "If you obtain a user event reference in one application instance, you cannot use that user event reference in another application \
            instance. You cannot use user events for communication between LabVIEW application instances.",
        1502: "Cannot save a bad VI without its block diagram.",
        1503: "Cannot save a clone of a reentrant VI.",
        1504: "Cannot save a remote panel.",
        1517: "An error occurred in the Call Library Node processing. This error was most likely a configuration mismatch between the \
            calling conventions of the Call Library Node and the function being called in the DLL.",
        1523: "Passed an invalid number of strings to the Strings [ ] property. You must pass either 1 string or 6 strings.",
        1524: "The target version for save is not formatted correctly. The target version for save must be a valid LabVIEW version in \
            the form x.x or xx.x, where x is a number. Refer to the LabVIEW Help for a list of valid versions.",
        1526: "This property does not apply when the plot legend of a graph or chart is in tree view.",
        1529: "There are too many nested VI calls. This typically results from recursion without a proper termination condition to stop \
            the recursion.",
        1532: "The target application instance is currently being destroyed. You cannot get a new reference to the application instance \
            or load a VI in the application instance.",
        1533: "A shared variable node cannot be created from the specified terminal.",
        1534: "The semaphore you specified does not exist. LabVIEW cannot return a reference to the semaphore. This error might occur \
            if the create if not found input of the Obtain Semaphore Reference VI is FALSE and LabVIEW cannot find a semaphore with the name \
            you specify.",
        1535: "The semaphore reference you specified is invalid. To correct this error, make sure the reference to the semaphore is valid.",
        1544: "LabVIEW attempted a read, write, or seek on a file opened in unbuffered mode, and the data size is not a multiple of the \
            disk sector size. Use the Get Volume Info function to return the proper sector size. If you do not have the right amount of data \
            to align to a sector size, you must pad the data with filler data and delete the filler data before LabVIEW reads back the file.",
        1545: "LabVIEW attempted to read or write data to a file opened in unbuffered mode, and the data is not aligned properly. LabVIEW \
            determines how data is aligned and you cannot alter that alignment. If this error occurs, you must enable buffering and reopen \
            the file.",
        1546: "The VI must be in a project to use this property.",
        1548: "Queue refnum cannot be obtained with a size of zero. Size input must be a positive number or -1 for unlimited size.",
        1550: "The license for the I/O server type is invalid.",
        1553: "The LabVIEW Run-Time Engine cannot load the polymorphic VI. This error occurs in stand-alone applications when the VI is \
            polymorphic. To correct this error, load an instance of the polymorphic VI rather than the polymorphic VI itself.",
        1554: "The current LabVIEW target cannot load control VIs.",
        1556: "The reference is invalid. This error might occur because the reference has been deleted.",
        1557: "LabVIEW tried to access duplicate references at the same time.",
        1558: "There is a type mismatch between the wire type and the internal data type of the reference. This problem might occur due \
            to a type cast error.",
        1564: "Project file cannot be saved at this time. The project has a locked untitled dependency. The lock prevents giving the untitled \
            item a name so it cannot be saved.",
        1571: "You cannot open a packed library saved in a version earlier than the current version of LabVIEW.",
        1573: "You cannot load a packed library built for a target or operating system different than the current target or operating \
            system.",
        1574: "Cannot open a file with separated compiled code in the LabVIEW Run-Time Engine. Contact the distributor of the file. The \
            distributor must include compiled code in the file for it to run in the LabVIEW Run-Time Engine.",
        1579: "Specified paths do not share a common directory. The paths must share a directory. Consider building caches for each set \
            of paths that share a common directory.",
        1580: "Cannot find the compiled code in the compiled object cache. Verify that the VI is marked to save its compiled code separately \
            and that it is not broken. Then compile the VI.",
        1581: "Cannot use this property on either .NET or ActiveX Container.",
        1584: "The data in the reference cannot be resized. There is a size mismatch between the data in the reference and the data wired \
            to the Data Value Reference Write Element border node.",
        1586: "Compiled code is out of date.",
        1587: "VI is not marked to separate compiled code from source file.",
        1588: "Compiled object cache is corrupt.",
        1590: "The qualified name of one of the dependencies of the specified file is not what LabVIEW expected. This mismatch implies \
            that the dependency report is unreliable, so the ReadLinkInfo operation was aborted.",
        1595: "The RT target does not have enough memory to load the startup application.",
        1596: "Cannot use SSL on this operating system because SSL is either not configured, not installed, or not supported.",
        1597: "The Paste Data operation attempted to paste data into a destination that would have had a dimmed 'paste' option in the \
            shortcut menu.",
        1599: "An empty string is not a valid method name.",
        1603: "The Open VI Reference function does not support using an asynchronous call by reference option with the Prepare for reentrant \
            run option. Both the 0x80 and 0x100 option flags conflict with the 0x08 option flag. The 0x08 flag is useful when running VIs with \
            the Run VI method. The 0x08 flag is not useful when performing asynchronous calls. To correct this error, remove either the 0x08 \
            option or the 0x80 and 0x100 options.",
        1604: "The Open VI Reference function does not support using the option 0x08 (Prepare for reentrant run) with the asynchronous \
            call by reference options 0x80 (Prepare to call and forget) or 0x100 (Prepare to call and collect).",
        1611: "An internal error occurred because a front panel item has no execute data. Recompiling the VI may fix this issue.",
        1616: "The path to save the report is not valid. A valid path cannot contain any illegal characters",
        1617: "LabVIEW is unable to generate a VI comparison report. Make sure you have write permission to the path you specified and \
            generate the report again.",
        1619: "LabVIEW is unable to find the Microsoft Word components. Make sure you installed Microsoft Word correctly.",
        1620: "LabVIEW is unable to create the Microsoft Word report. Try generating the report again. If the problem persists, contact \
            National Instruments technical support.",
        1621: "LabVIEW is unable to create the Microsoft Word report. Try generating the report again. If the problem persists, contact \
            National Instruments technical support.",
        1622: "LabVIEW is unable to create the Microsoft Word report. Make sure you installed Microsoft Word correctly and create the \
            report again.",
        1623: "LabVIEW is unable to find the Microsoft Word components. Make sure you installed Microsoft Word correctly.",
        1624: "You can only generate web page or plain text reports on OS X and Linux.",
        1627: "The control index at position %d is invalid.",
        1628: "LabVIEW cannot convert the input data type at position %d to the control data type.",
        1629: "The control must have a terminal on the block diagram..",
        1630: "If you wire a variant or a LabVIEW class library file (.lvclass) to this function, you must call the function on a VI in \
            the same application instance.",
        1632: "You cannot insert a custom control directly into a subpanel. Use a VI with the custom control on its front panel instead.", \

        1640: "Channels are incompatible with asynchronous call by reference options 0x80 (Prepare for call-and-forget) and 0x100 (Prepare \
            for call-and-collect). Channels currently express only intraprocess communication. Channels cannot maintain their state properly \
            if one endpoint or the other shuts down independently. Both of the asynchronous call modes Prepare for call-and-forget and Prepare \
            for call-and-collect allow the called VI to have a different run lifetime from its direct caller.",
        4800: "Selected Device is Invalid The currently selected device index is invalid. This could be caused by an invalid sound driver.",

        4801: "Invalid sound task refnum. No sound driver is available for use, or the given GUID is not a valid DirectSound device ID.",

        4802: "The sound device is busy. Another application is currently using the device. Raising this application's priority level \
            could resolve this issue.",
        4803: "The sound driver or card cannot accommodate the specified configuration. Check that the parameters entered are within the \
            supported range for the hardware and drivers. If you receive this error while using the Sound Output Configure VI, refer to the \
            KnowledgeBase at ni.com for more information.",
        4804: "Cannot write in file playback. The application attempted to write to the file while it was being played. This error code \
            is not currently reported by the LVSound library.",
        4805: "Could not find the sound file. The specified sound file could not be found.",
        4806: "DirectX 8.0 or higher is required to run. To correct this error, install the latest version of DirectX from \
        http://www.microsoft.com/downloads.",
        4810: "Cannot recognize sound format. The sound format of this file is not recognizable. The file may be corrupt.",
        4811: "Cannot support sound format. The specified wave format is not supported. This could be a limitation of the hardware, driver, \
            or both.",
        4820: "A buffer underflow has occurred. A buffer underflow has occurred because the application is not writing data quickly enough.",
        4821: "Overwrite error. An overwrite error has occurred because the application is not reading data quickly enough from the buffer.",
        4822: "A timeout occurred before the operation finished. A timeout error occurred because the application was unable to successfully \
            acquire a mutex.",
        4823: "You cannot perform this operation without an active task. Ensure that a task is active and try again. An input task might \
            stop running if the input buffer overflows. Overflow occurs when the data is not read fast enough.",
        56000: "Generic project error.",
        56001: "An item with this name already exists in the project.",
        56002: "An item with this path already exists in the project.",
        56003: "Adding this item would cause a conflict with another item.",
        56004: "The project item could not be found.",
        56005: "The item type is not compatible with the target type.",
        56006: "You cannot add a packed library to a project library.",
        66464: "The global time on the controller was altered, which might affect the period of an iteration of the NI Scan Engine. A \
            timing source such as IEEE-1588 or GPS modified the global time value on the controller. This can result in a temporary phase shift, \
            which would alter the update period for NI Scan Engine variables for one iteration."}

    def __init__(self) -> None:
        pass

    def _convert_hex_to_u32integer(self, error_hex):
        """
        Convert hex number to unsigned 32 bit integer

        *Arguments:*

        error_hex: Hex number usually from NI's exception
        """
        # Covert hex to Unsigned 32 bit integer
        if error_hex < 2**31:
            error_hex = error_hex < 2**31
        else:
            error_hex = error_hex-2**32

        return error_hex

    def get_error_message(self, error_message):
        """ Convert hex number returned from National Instrument API to error message.

        *Arguments:*

        error_message (str): Exception message returned from National Instrument
        """
        # Split Exception into list of strings
        error_msg_split = str(error_message).split()

        # Veristand hex code error code is not in message, return itself
        if "0x" not in error_message:
            return error_message

        # Find index where hex number locates
        index_nbr = [i for i, item in enumerate(
            error_msg_split) if item.startswith("0x")][0]

        # List don't contain hex number
        if index_nbr is None or index_nbr == "":
            return "No error message."

        # Get error hex number
        error_dec = int(error_msg_split[index_nbr], 16)
        error_dec = self._convert_hex_to_u32integer(error_dec)
        print(f"Error hex in decimal:{error_dec}")

        # Get error message from error dictionary
        return ni_errors.NI_ERRORS.get(error_dec)


if __name__ == "__main__":
    # Testing API that is works OK and returns human readable error message.
    api = ni_errors()
    tmp = api.get_error_message("Consult NI VeriStand help for error code 0xfffcf0e6 error message DAQmx Start Task.vi:7220001<append>\
    <B>Task Name: </B>PXI1Slot15_AO")
    print(f"Error message:{tmp}")
