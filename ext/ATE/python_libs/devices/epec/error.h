/*!
 * @file        error.h
 * @brief       Header file for error codes
 *
 * Error codes start from 33000.
 * 33000 - Generic error codes
 * 33100 - Main
 * 33200 - SIL2 runtime context handling
 * 33300 -
 * 33400 - ADC Driver
 * 33500 - IO Driver
 * 33600 - ETPU
 * 33700 -
 * 33800 - Password
 * 33900 - Parameters
 * 34000 - NVRAM
 * 34100 - FLASH Driver
 * 34150 - FLASH
 * 34200 - DSPI Driver
 * 34250 - PCU Driver
 * 34300 - PIT Driver
 * 34400 - CANOPEN
 * 34500 - CAN OD
 * 34600 - EQADC
 * 34700 - FlexCAN Driver
 * 34720 - Message buffer
 * 34750 - Can interface
 * 34800 - Diagnostic errors
 * 34870 - Diangostic ADC
 * 34880 - Diagnostic Temperature
 * 34890 - Diagnostic CMU
 * 34900 - Diagnostic PMC
 * 34910 - Diagnostic CRC driver
 * 34920 - Diagnostic GPIO
 * 34930 - Diagnostic CAN
 * 34940 - Diagnostic SSCM
 * 34960 - Diagnostic OVP
 * 34970 - Diagnostic External RAM
 * 34980 - Diagnostic EMIOS
 * 35000 - Diagnostic Safety swich
 * 35100 - Diagnostic FCCU
 * 35150 - Diagnostic ERM driver
 * 35200 - Diagnostic Log
 * 35300 - SBC
 * 35450 - STCU
 * 35500 - Safety Switch
 * 35600 - CmpSystem
 * 35700 - CSE Driver
 * 35800 - Log
 * 35900 - GPIO driver
 * 35950 - Ext GPO driver
 * 36000 - SIU driver
 * 36100 - CAN message fifo
 * 36200 - Shared memory
 * 37000 - Comm cycle monitoring
 * 37100 - External C-application errors
 * 37200 - System monitor
 * 37300 - Dynamic library
 * 37400 - Memory Handler
 * 37500 - User management
 * 37600 - Inertial Measurement Unit
 * 37700 - RTOS
 * 37800 - Ethernet
 * 37900 - SENT Driver
 * 40000 - Boot
 * 57005 - Fatal errors - 0xDEADh
 * 57100 - 3S runtime control and application loading
 * 57200 - SBC FS8x
 * 57300 - Reference outputs
 * 57350 - Cable detection
 * 57370 - Measurement monitor
 * 57400 - HS/LS
 *
 *
 *    @version     3.3
 *
 *    @authors     Epec FW team, Initial author J Vieri
 *    @copyright   Epec Oy
 *
 *    @review      TFS ID: 24932
 *
 *    Change history
 *
 *    3.3 7.11.2024
 *    Ext GPO errors added
 *
 *    3.2 25.4.2022
 *    Updated SBC error codes for Vpre, Vcca and Vaux.
 *
 *    3.1 23.10.2020
 *    Merged SL84 and SC10 error codes
 *
 *    3.0  2019    Epec FW team
 *    Released version in Safety firmware version 1.2.1.33099
 *
 *    2.3  8.10.2019  Jarno Mannisto
 *    New FCCU error codes for errata e7227.
 *
 *    2.2  28.8.2019  Jarno Mannisto
 *    New eMIOS error code FW_ERR_EMIOS_CHANNEL_WRONG_STATE.
 *
 *    2.1  19.6.2019  Jarno Mannisto
 *    New SBC error code FW_ERR_SBC_SS_RESET_IN_SAFETY_PATH_TEST.
 *    SBC error code comments updated.
 *
 *    2.0  2019    Epec FW team
 *    Released version in Safety firmware version 1.1.1.29111
 *
 *    1.0  2018    Epec FW team
 *    Released version in Safety firmware version 1.0.0.34
 *
 *    0    2015    J Vieri
 *
 *
 */

#ifndef FW_ERROR_H
#define FW_ERROR_H

/*-----------------------------------------------------------------------------
  <-- GLOBAL TYPES -->
  ---------------------------------------------------------------------------*/

typedef enum err_t
{
   /*--------------------------------------------------------------------------
        Generic error codes
    --------------------------------------------------------------------------*/

    /*!< Function executed OK. */
    FW_ERR_OK = 0,

    /** Safety firmware error code range start value */
    FW_ERR_START = 33000,
    /** Temporal failure on function execution. */
    FW_ERR_FAIL = 33001,
    /** Function execution result are valid. */
    FW_ERR_VALID = 33002,
    /** Function output values are not valid. */
    FW_ERR_INVALID = 33003,
    /** Component is busy and can not do requested action. */
    FW_ERR_BUSY = 33004,
    /** Illegal input parameter. */
    FW_ERR_PARAMETER = 33005,
    /** Component has not been initialized properly. */
    FW_ERR_UNINITIALIZED = 33006,
    /** Component is active and the action is not done. */
    FW_ERR_ACTIVE = 33007,
    /** Component is reserved and can not select. */
    FW_ERR_RESERVED = 33008,
    /** Pointer is not an optional parameter. */
    FW_ERR_NULLPOINTER = 33009,
    /** Function is not implemented. Is normally used for CODESYS functions which are implemented in firmware. */
    FW_ERR_NO_IMPLEMENTED = 33010,
    /** Timeout occured. */
    FW_ERR_TIMEOUT = 33011,
    /** Unknown error reason. */
    FW_ERR_UNKNOWN = 33012,
    /** Error in CRC calculation. */
    FW_ERR_CRC = 33013,
    /** Generic error which is returned if functionality is not implemented. */
    FW_ERR_FUNCTIONALITY_NOT_IMPL = 33014,
    /** System execution exits main code. */
    FW_ERR_SYSTEM_EXIT = 33015,
    /** Tried to use not supported feature. */
    FW_ERR_NOT_SUPPORTED = 33016,
    /** CmpEpecPlcShell command registration failed.
        Info contains failed command index for registration. */
    FW_ERR_PLCSHELL_REGISTER = 33017,
    /** All callbacks are all fully used. */
    FW_ERR_CALLBACKS_FULL = 33018,

    /*--------------------------------------------------------------------------
        Main error codes
    --------------------------------------------------------------------------*/

    /** Error in production data checksum calculation. */
    FW_ERR_PRODUCTION_DATA_CHECKSUM = 33100,
    /** Lock-step mode not enabled. */
    FW_ERR_DIAG_LOCKSTEP_NOT_ENABLED = 33101,
    /** MCU Reset Escalation not enabled. */
    FW_ERR_DIAG_MCU_RESET_ESCALATION_NOT_ENABLED = 33102,
    /** Safety switch count invalid in production data (not 1 or 2). */
    FW_ERR_DIAG_PRODUCTION_DATA_SAFETY_SWITCH_ERROR = 33103,
    /** Wrong system clock source selected. */
    FW_ERR_DIAG_WRONG_SYSCLKSEL = 33104,
    /** Wrong MCU version for the used firmware version. */
    FW_ERR_DIAG_MCU_EXPECTED_VERSION_WRONG = 33105,
    /** Error occurred while reading FACTORY_RESET state */
    FW_ERR_FACTORY_RESET_ERROR_READING_PIN_STATE = 33106,
    /** Factory Reset not started (FACTORY_RESET was TRUE for too short time) */
    FW_ERR_FACTORY_RESET_TRUE_FOR_TOO_SHORT_TIME = 33107,
    /** Factory Reset not started (FACTORY_RESET was TRUE for too long time) */
    FW_ERR_FACTORY_RESET_TRUE_FOR_TOO_LONG_TIME = 33108,
    /** Factory Reset done (just to inform, not an error) */
    FW_ERR_FACTORY_RESET_DONE = 33109,
    /** An assertation has failed - used during development. */
    FW_ERR_ASSERT_FAILED = 33110,
    /** Factory Reset failed */
    FW_ERR_FACTORY_RESET_FAILED = 33111,
    /** Error occurred while reading supply voltage (in check for Factory Reset) */
    FW_ERR_FACTORY_RESET_ERROR_READING_SUPPLY_VOLTAGE = 33112,
    /* Factory Reset not started (Supply voltage too low) */
    FW_ERR_FACTORY_RESET_SUPPLY_VOLTAGE_TOO_LOW = 33113,
    /* Factory Reset not started (Supply voltage too high) */
    FW_ERR_FACTORY_RESET_SUPPLY_VOLTAGE_TOO_HIGH = 33114,
    /* Factory Reset not initialized properly */
    FW_ERR_FACTORY_RESET_NOT_INITIALIZED = 33115,
    /* Board type does not match this firmware.
       Info field contains the hw version read from production data */
    FW_ERR_UNKNOWN_BOARD_TYPE = 33116,

    /*--------------------------------------------------------------------------
        3S Context handling error codes
    --------------------------------------------------------------------------*/

    /** Not in unsafe context. */
    FW_ERR_NOT_IN_UNSAFE_CONTEXT = 33200,
    /** Not in safe context. */
    FW_ERR_NOT_IN_SAFE_CONTEXT = 33201,
    /** Not in system context. */
    FW_ERR_NOT_IN_SYSTEM_CONTEXT = 33202,

    /*--------------------------------------------------------------------------
        ADC error codes
    --------------------------------------------------------------------------*/

    /** Error when recalibrating ADC. */
    FW_ERR_CALIBRATION = 33400,
    /** Error in reference channel when calibrating ADCs. */
    FW_ERR_SAMPLE_REF_CHN = 33401,
    /** External VREF correction value was out of specified range. */
    FW_ERR_CALIBRATION_OUT_OF_RANGE = 33402,
    /** ADC MUX startup test failed - error in EXT VREF or GND measurements. */
    FW_ERR_ADC_MUX_STARTUP_TEST_FAILED = 33403,

    /*--------------------------------------------------------------------------
       IO-driver error codes
    --------------------------------------------------------------------------*/
    /** Software IO-channels is tried to init to unsupported mode */
    FW_ERR_IODRV_ERR_NOT_SUPPORTED_MODE = 33500,
    /** IO-driver is in state which doesn't support call of the function. */
    FW_ERR_IODRV_ERR_FUNCTION_EXECUTION_BLOCKED = 33501,
    /** Invalid io-channel number used for function */
    FW_ERR_IODRV_ERR_CHN_NUMBER_NOT_VALID = 33502,
    /** User with higher priority is already using this channel. */
    FW_ERR_IODRV_ERR_HIGH_PRIORITY_ID_USAGE = 33503,
    /** Invalid state transfer for IO-driver */
    FW_ERR_IODRV_ERR_NOT_VALID_STATE_TRANSFER = 33504,
    /** Invlaid driver number (pwm, ai, ...) */
    FW_ERR_IODRV_ERR_NOT_VALID_DRIVER_NBR = 33505,
    /** Data type is not supported for this io-channel */
    FW_ERR_IODRV_NOT_SUPPORTED_DATA_TYPE = 33506,
    /** IO-channel hw is not configured correctly */
    FW_ERR_IODRV_HW_NOT_CONFIGURED = 33507,
    /** IO-channel is already in use. */
    FW_ERR_IODRV_CHN_ALREADY_IN_USE = 33508,
    /** HW-update failed. */
    FW_ERR_IODRV_CHN_HW_UPDATE_FAILED = 33509,
    /** IO-channel is in wrong mode for demanded action. */
    FW_ERR_IODRV_CHN_IN_WRONG_MODE = 33510,
    /** HW type for io-channel is undefined. */
    FW_ERR_IODRV_UNDEFINED_HW_UNIT_TYPE = 33511,
    /** Hw version defined in device description doesn't match actual unit. */
    FW_ERR_IODRV_HAL_HW_MISSMATCH = 33512,
    /** HW init error */
    FW_ERR_IODRV_HAL_HW_INIT_ERROR = 33513,
    /** Reseted channel for pulse input reset configuration is not configured to PI mode. */
    FW_ERR_IODRV_RESETED_CHANNEL_NOT_CONFIGURED = 33514,
    /** Given reseted channel is not valid. */
    FW_ERR_IODRV_ERR_CHN_NUMBER_NOT_VALID_RESETED_CHN = 33515,
    /** Error for channels which are set to work as pair for reset channel. */
    FW_ERR_IODRV_HW_MISSMATCH_FOR_RESET_CHN = 33516,
    /** Parameter error for PWFM channel. */
    FW_ERR_IODRV_HAL_PWFM_PARAMETER_ERROR = 33517,
    /** Wrong number of samples given to ai filtering. */
    FW_ERR_IODRV_AI_WRONG_NBR_OF_SAMPLES = 33518,
    /** IO-variable handling failed */
    FW_ERR_IODRV_IO_VAR_HANDLE_FAILED = 33519,
    /** Wanted action is not supported for this driver. */
    FW_ERR_IODRV_ACTION_NOT_SUPPORTED_THIS_DRV = 33520,
    /** Error in initialization of the one of drivers. */
    FW_ERR_IODRV_INIT_ERROR = 33521,
    /** Reset channel number is not valid. */
    FW_ERR_PI_DRV_RESET_CHN_NOT_VALID = 33522,
    /** Too many task used in application. There is no slots for all tasks. */
    FW_ERR_IODRV_TASK_MON_TOO_MANY_TASKS = 33523,
    /** Time out for task monitoring.  Extra info defines parameter id which was used for monitoring of the task. */
    FW_ERR_IODRV_TASK_MON_TIMEOUT = 33524,
    /** IO-drvier is not in corect state for actions  */
    FW_ERR_IODRV_NOT_IN_CORRECT_STATE = 33525,
    /** Invalid triggering method for PI-channel */
    FW_ERR_IODRV_INVALID_TRIGGERING_METHOD = 33526,
    /** Not valid gate time value for gate time setting */
    FW_ERR_IODRV_INVALID_GATE_TIME_VALUE = 33527,
    /** Application initiated request for safe state. */
    FW_ERR_IODRV_SAFE_STATE_APPLICATION = 33528,
    /** Tag error for io-driver. This occurs normally because there is problems in memory reservation in io-data */
    FW_ERR_IODRV_INVALID_TAG = 33529,
    /** Error when reserving shared io-data area */
    FW_ERR_IODRV_SHM_MEM_RES_FAILED = 33530,
    /** Error when trying to init shared memory trough shared memory driver */
    FW_ERR_IODRV_SHM_DRIVER_RESERVATION = 33531,
    /* Core ID missmatch */
    FW_ERR_IODRV_CORE_ID_MISSMATCH = 33532,
    /** Other client is already reserved IO-channel. */
    FW_ERR_IODRV_CHANNEL_USED_BY_OTHER_CLIENT = 33533,
    /** Hw configuration not compatible */
    FW_ERR_IODRV_HW_MISSMATCH = 33534,
    /* Pulse input channel's virtual channel is not valid */
    FW_ERR_IODRV_PI_VIRTUAL_CHANNEL_ERROR = 33535,
    /** Io driver TAG not correct */
    FW_ERR_IODRV_DATA_STRUCTURE_TAG_NOT_CORRECT = 33536,
    /** Dither is not configured for sync channel */
    FW_ERR_IODRV_DITHER_SYNC_CHANNEL_NOT_IN_DITHER_MODE = 33537,
    /** Dither configuration error. Dither possible to adjust only if ratio is 0. */
    FW_ERR_IODRV_DITHER_RATIO_NOT_ZERO = 33538,
    /** Dither amplitude too small */
    FW_ERR_IODRV_DITHER_AMPL_TOO_SMALL = 33539,
    /** Dither amplitude too high */
    FW_ERR_IODRV_DITHER_AMPL_TOO_HIGH = 33540,
    /** Dither frequency too small */
    FW_ERR_IODRV_DITHER_FREQ_TOO_SMALL = 33541,
    /** Dither frequency too high */
    FW_ERR_IODRV_DITHER_FREQ_TOO_HIGH = 33542,
    /** Dither base frequency not valid */
    FW_ERR_IODRV_DITHER_BASE_FREQ_NOT_VALID = 33543,
    /** All outputs are forced off because Safe state is requested */
    FW_ERR_IODRV_OUTPUTS_ARE_FORCED_OFF = 33544,
    /** Supply group number not valid. */
    FW_ERR_IODRV_SUPPLY_GRP_NBR_NOT_VALID = 33545,
    /** Short cut error in output */
    FW_ERR_IODRV_SHORT_CUT_ERROR = 33546,
    /** Hw missmatch in short cut diagnostic */
    FW_ERR_IODRV_HW_MISS_MATCH_SHORT_CUT = 33547,
    FW_ERR_IODRV_HAL_PWM_CHANNEL_CONF_READ = 33548,
    FW_ERR_IODRV_HAL_DI_CHANNEL_CONF_READ = 33549,
    FW_ERR_IODRV_HAL_AI_CHANNEL_CONF_READ = 33550,
    FW_ERR_IODRV_HAL_DO_CHANNEL_CONF_READ = 33551,
    FW_ERR_IODRV_HAL_PI_CHANNEL_CONF_READ = 33552,

    /** Used mode doesn't support frequency measurement */
    FW_ERR_IODRV_HAL_PI_FREQ_NOT_SUPPORTED = 33553,
    /** Used mode doesn't support pulse width  measurement */
    FW_ERR_IODRV_HAL_PI_PULSE_WIDTH_NOT_SUPPORTED = 33554,
    /** Used mode doesn't support count measurement */
    FW_ERR_IODRV_HAL_PI_COUNT_NOT_SUPPORTED = 33555,
    /** Special pulse input mode is used only for eMIOS types */
    FW_ERR_IODRV_HAL_PI_WRONG_IO_TYPE_FOR_SPECIAL_MODE = 33556,
    /** Read production calibration data was out of range */
    FW_ERR_IODRV_HAL_RANGE_ERROR_PROD_DATA = 33558,
    /** CRC error in production calibration data */
    FW_ERR_IODRV_HAL_CRC32_ERROR_PROD_DATA = 33559,
    /** ADC pullup voltage is too small compared to ADC vin to calculate ohms for thermistors  */
    FW_ERR_IODRV_THERM_ADC_PULL_VOLT_TOO_SMALL = 33560,
    /** ADC pullup and ADC vin voltages are too smalle */
    FW_ERR_IODRV_THERM_VOLTS_NOT_VALID = 33561,
    /** Invalid configuration for thermistor input */
    FW_ERR_IODRV_THERM_INV_CONF = 33562,
    /** GPIO readback did not match with default value */
    FW_ERR_IODRV_GPO_INIT_READBACK_ERR = 33563,
    /** Looking up ADC unit and ADC channel for calibrating current measurement failed */
    FW_ERR_IODRV_HAL_CALIB_ETPU_LOOKUP_FAILED = 33564,
    /** Dither current measurement channel not found */
    FW_ERR_IODRV_DITHER_CM_NOT_FOUND = 33565,
    /*--------------------------------------------------------------------------
        ETPU error codes
    --------------------------------------------------------------------------*/
    /** Wrong eTPU engine number */
    FW_ERR_ETPU_WRONG_ENG_NBR = 33600,
    /** Wrong eTPU channel number */
    FW_ERR_ETPU_WRONG_CHN_NBR= 33601,
    /** Error when making diagnostic channel check for engine 1. */
    FW_ERR_ETPU_ENG_A_DIAG_CHN_ERR = 33602,
    /** Error when making diagnostic channel check for engine 2. */
    FW_ERR_ETPU_ENG_B_DIAG_CHN_ERR = 33603,
    /** Error when making diagnostic channel check for engine 3. */
    FW_ERR_ETPU_ENG_C_DIAG_CHN_ERR = 33604,
    /** ETPU system is not initialized correctly. */
    FW_ERR_ETPU_SYSTEM_NOT_INITED_OK = 33605,
    /** ETPU code in the flash has wrong TAG in the start of binary */
    FW_ERR_ETPU_WRONG_TAG_IN_FLASH_START = 33606,
    /** Data pointer for ETPUA diagnostic channel is NULL */
    FW_ERR_ETPU_A_WRONG_DATA_PTR_DIAG_CHN = 33607,
    /** Data pointer for ETPUB diagnostic channel is NULL */
    FW_ERR_ETPU_B_WRONG_DATA_PTR_DIAG_CHN = 33608,
    /** Data pointer for ETPUC diagnostic channel is NULL */
    FW_ERR_ETPU_C_WRONG_DATA_PTR_DIAG_CHN = 33609,
    /** Data pointer for ETPUC diagnostic channel is NULL */
    FW_ERR_ETPU_DATA_CMP_ERR_IN_DOWNLOAD = 33610,
    /** Invalid group number for current mean triggering. */
    FW_ERR_ETPU_CURRENT_MEAN_INVALID_GRP = 33611,
    /** ETPU system not ok. */
    FW_ERR_ETPU_SYSTEM_NOT_OK = 33612,
    /** ETPU wrong hsr signal number */
    FW_ERR_ETPU_INVALID_HSR_SIGNAL = 33613,
    /** ETPU binary is too big */
    FW_ERR_MAX_IMG_SIZE = 33614,
    /** ETPU watchdog triggered */
    FW_ERR_ETPU_WATCH_DOG = 33615,

    /** ETPU AB interrupt handler detected exception. */
    FW_ERR_ETPU_AB_INTERRUPT = 33616,
    /** ETPU C interrupt handler detected exception. */
    FW_ERR_ETPU_C_INTERRUPT = 33617,

    /** ETPU AB exception. */
    FW_ERR_ETPU_AB_EXCEPTION = 33618,
    /** ETPU C exception. */
    FW_ERR_ETPU_C_EXCEPTION = 33619,

    /** ETPU AB DERSR */
    FW_ERR_ETPU_AB_DERSR = 33620,
    /** ETPU AB CERSR */
    FW_ERR_ETPU_AB_CERSR = 33621,

    /** ETPU C DERSR */
    FW_ERR_ETPU_C_DERSR = 33622,
    /** ETPU C CERSR */
    FW_ERR_ETPU_C_CERSR = 33623,

    FW_ERR_ETPU_AB_DERAR = 33624,
    FW_ERR_ETPU_C_DERAR = 33625,

    FW_ERR_ETPU_AB_MESR = 33626,
    FW_ERR_ETPU_C_MESR = 33627,
    /** Error when reserving shared io-data area */
    FW_ERR_ETPU_SHM_MEM_RES_FAILED = 33628,

    /*--------------------------------------------------------------------------
        Password error codes
    --------------------------------------------------------------------------*/
    /** Error when trying to unlock password */
    FW_ERR_PSW_PASSWORD_NOT_MATCH = 33800,
    /** Error password system is not initialized before use of functions. */
    FW_ERR_PSW_INIT_ERR = 33801,
    /** Error password system locked */
    FW_ERR_PSW_SYS_LOCKED = 33802,
    /** Error password system too many saved passwords. */
    FW_ERR_PSW_TOO_MANY_INITED_PASSWORD = 33803,
    /** Error given username is not defined. */
    FW_ERR_PSW_NO_USERNAME_DEFINED = 33804,
    /** Error password system no initialised */
    FW_ERR_PSW_SYS_NOT_INITIALIZED = 33805,
    /** Error given puk code doesn't match */
    FW_ERR_PSW_PUK_CODE_MISMATCH = 33806,
    /** Application is given password unlock command. */
    FW_ERR_PSW_APP_PASS_UNLOCK = 33807,


   /*--------------------------------------------------------------------------
        Parameter error codes
    --------------------------------------------------------------------------*/
    /** Error default parameter area tag is not correct. */
    FW_ERR_PAR_START_TAG_ERROR_DEF_PAR = 33900,
    /** Error default parameter area end tag is not correct. */
    FW_ERR_PAR_END_TAG_ERROR_DEF_PAR = 33901,
    /** Error saved parameter area tag is not correct. */
    FW_ERR_PAR_START_TAG_ERROR_SAVED_PAR = 33902,
    /** Error saved parameter area end tag is not correct. */
    FW_ERR_PAR_END_TAG_ERROR_SAVED_PAR = 33903,
    /** Error request parameter is not find. */
    FW_ERR_PAR_NOT_FIND = 33904,
    /** Error buffer length too smalle in parameter read. */
    FW_ERR_PAR_BUFFER_LENGHT_TOO_SMALL = 33905,
    /** Error buffer length too large for parameter write. */
    FW_ERR_PAR_BUFFER_LENGHT_TOO_LARGE = 33906,
    /** Error parameter system not ready. */
    FW_ERR_PAR_SYSTEM_NOT_READY = 33907,
    /** Error parameter index not find. */
    FW_ERR_OBJECT_NOT_FIND = 33908,
    /** Error enabling parameter saving fails */
    FW_ERR_PAR_SAVE_ENABLING_FAILED = 33909,
    /** Error reserved flash area is too small for parameter saving. */
    FW_ERR_FLASH_AREA_IS_TOO_SMALL = 33910,
    /** Error parameter saving is blocked  */
    FW_ERR_PAR_SAVING_BLOCKED = 33911,
    /** Error parameter area wrong type  */
    FW_ERR_PAR_WRONG_AREA = 33912,
    /** Error no write access to parameter. */
    FW_ERR_PAR_NO_WRITE_ACCESS = 33913,
    /** Error parameter is not saved */
    FW_ERR_PAR_NO_SAVING_SUPPORT = 33914,
    /** CRC error in parameter handling */
    FW_ERR_PAR_CRC32_ERROR = 33915,
    /** CRC error in production data read */
    FW_ERR_PAR_CRC32_ERROR_PROD_DATA = 33916,
    /** Copy error when saving parameters */
    FW_ERR_PAR_ERROR_WHEN_MAKING_PARAMETER_COPY = 33917,
    /** No room for parameters. */
    FW_ERR_PAR_LIST_FULL = 33918,
    /** Error when trying change codesys states when unlocking password. */
    FW_ERR_PAR_ERROR_IN_COD_STATE_CHANGES = 33919,
    /** No more free space for new version infos. */
    FW_ERR_PAR_ERROR_NO_FREE_SLOT_FOR_VERSION_ID = 33920,
    /** Defined parameter set is is not found on list */
    FW_ERR_PAR_ERROR_PAR_SET_NOT_FOUND = 33921,
    /** No store handler for parameter set */
    FW_ERR_PAR_ERROR_NO_STORE_HANDLER = 33922,
    /** Parameter system is not in correct state */
    FW_ERR_PAR_ERROR_PAR_INSTANCE_NOT_IN_VALID_STATE = 33923,
    /** Parameter system id already inited */
    FW_ERR_PAR_ERROR_PAR_SET_INSTANCE_ALLREADY_INITED = 33924,
    /** No free slots for parameter system */
    FW_ERR_PAR_ERROR_NO_FREE_PAR_SET_INSTANCE = 33925,
    /** No write permission to parameter --> user level error */
    FW_ERR_PAR_ERROR_PAR_WRITE_NO_PERMISSION = 33926,
    /** No write permission to parameter --> user level error */
    FW_ERR_PAR_ERROR_PAR_READ_NO_PERMISSION = 33927,
    /** Only constant parameter set */
    FW_PAR_ERROR_NO_SAVE_POSSIBLE = 33928,
    /** Error when trying to read saved area */
    FW_PAR_ERROR_SAVED_AREA_ERROR = 33929,
    /** Both parameter area pointers are NULL */
    FW_PAR_ERROR_BOTH_AREA_HANDLES_NULL = 33930,
    /** Start tag error */
    FW_ERR_PAR_START_TAG_ERROR = 33931,
    /** End tag error */
    FW_ERR_PAR_END_TAG_ERROR = 33932,
    /** Parameter error in create. */
    FW_ERR_PAR_CREATE_ADDR_CHECK_ERROR = 33933,
    /** Parameter exists when trying to create new */
    FW_ERR_PAR_CREATE_ADDR_PARAMETER_EXISTS = 33934,
    /** Pointer compare error in removing parameter */
    FW_ERR_PAR_POINTER_COMPARE_FAIL = 33935,

   /*--------------------------------------------------------------------------
        NvRAM driver error codes
    --------------------------------------------------------------------------*/
    /** NvRAM function block has not been initialized. */
    FW_ERR_NVRAM_INSTANCE_NOT_INITIALIZED = 34000,
    /** NvRAM startup has failed permanently. NvRAM is not usable. */
    FW_ERR_NVRAM_INSTANCE_STARTUP_FAILURE = 34001,
    /** NvRAM internal configuration data is not set. */
    FW_ERR_NVRAM_INVALID_CONFIG_DATA = 34002,
    /** NVRAM write disabled.
        Possible reason is under voltage or SPI communication problem when writing data. */
    FW_ERR_NVRAM_WRITE_DISABLED = 34003,
    /** Generic address error. */
    FW_ERR_NVRAM_ADDRESS_ERROR = 34004,
    /** Address is below memory region range. */
    FW_ERR_NVRAM_TOO_LOW_ADDRESS = 34005,
    /** Address is over memory region range. */
    FW_ERR_NVRAM_TOO_HIGH_ADDRESS = 34006,
    /** Data length is zero. */
    FW_ERR_NVRAM_DATA_LENGTH_ZERO = 34007,
    /** NvRAM index is invalid. */
    FW_ERR_NVRAM_INVALID_INDEX = 34008,
    /** NvRAM is busy. Only one access allowed at a time. */
    FW_ERR_NVRAM_SESSION_BUSY = 34009,
    /** NvRAM device is invalid/not expected chip.  */
    FW_ERR_NVRAM_INVALID_DEVICE = 34010,

    /*--------------------------------------------------------------------------
        FLASH driver error codes
    --------------------------------------------------------------------------*/

    /* Reservation for Flash driver*/
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_INVALID_AREA = 34100,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_RESERVED = 34101,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_NOT_RESERVED = 34102,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_ALREADY_CLOSED = 34103,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_INVALID_LENGTH = 34104,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_INVALID_OFFSET = 34105,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLASH_NOT_IN_SAFE_STATE = 34106,

    /*--------------------------------------------------------------------------
        FLASH error codes
    --------------------------------------------------------------------------*/
    FW_ERR_FLASH_ALINGMENT = 34150,

    /*--------------------------------------------------------------------------
        DSPI driver error codes
    --------------------------------------------------------------------------*/

    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_INVALID_MODULE = 34200,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_CHN_RESERVED = 34201,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_CHN_ALREADY_CLOSED = 34202,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_BR_CALC_FAILED = 34203,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_CSSC_CALC_FAILED = 34204,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_ASC_CALC_FAILED = 34205,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_DT_CALC_FAILED = 34206,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_CHN_BUSY = 34207,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_NO_DATA = 34208,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_INT_CH_CONF_FAILED = 34209,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_HW_CH_CONF_FAILED = 34210,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_SW_TCD_CONF_FAILED = 34211,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_RX_CH_CONF_FAILED = 34212,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_DMA_NOT_SUPPORTED = 34213,
    /** Low level error. More information please contact EPEC */
    FW_ERR_DSPI_INVALID_CTAR = 34214,

    /*--------------------------------------------------------------------------
        PCU driver error codes
    --------------------------------------------------------------------------*/

    /** Platform Coherency Unit - Core0 error detail register. */
    FW_ERR_PCU_EDR0 = 34250,
    /** Platform Coherency Unit - Core0 address register. */
    FW_ERR_PCU_EAR0 = 34251,
    /** Platform Coherency Unit - Core1 error detail register. */
    FW_ERR_PCU_EDR1 = 34252,
    /** Platform Coherency Unit - Core1 address register. */
    FW_ERR_PCU_EAR1 = 34253,

    /*--------------------------------------------------------------------------
        PIT driver error codes
    --------------------------------------------------------------------------*/

    /** Low level error. More information please contact EPEC */
    FW_ERR_PIT_INVALID_CHANNEL = 34300,
    /** Low level error. More information please contact EPEC */
    FW_ERR_PIT_CHANNEL_RESERVED = 34301,

    /*--------------------------------------------------------------------------
        CANOPEN driver error codes
    --------------------------------------------------------------------------*/

    /** Message not handled by CANopen */
    FW_ERR_CANOPEN_MESSAGE_NOT_HANDLED = 34400,
    /** Handled message length is longer than maximum allowed. */
    FW_ERR_CANOPEN_TOO_LONG_CAN_MSG = 34401,
    /** GFC received */
    FW_ERR_CANOPEN_GFC_RECEIVED = 34402,
    /** Written bit rate is not correct */
    FW_ERR_CANOPEN_NOT_VALID_BIT_RATE = 34403,

    /*--------------------------------------------------------------------------
        OD error codes
    --------------------------------------------------------------------------*/

    /** No free lines available in OD */
    FW_ERR_OD_FULL = 34500,
    /** Object type doesn't match used add function */
    FW_ERR_OD_WRONG_OBJECT_TYPE = 34501,
    /** No read access to od data */
    FW_ERR_OD_NO_READ_ACCESS = 34502,
    /** No write access to od data */
    FW_ERR_OD_NO_WRITE_ACCESS = 34503,
    /** Wanted index not found. */
    FW_ERR_OD_NO_INDEX = 34504,
    /** Wanted subindex not found. */
    FW_ERR_OD_NO_SUBINDEX = 34505,
    /** Undefined object type */
    FW_ERR_OD_UNDEF_OBJ_TYPE = 34506,
    /** Unsupported object type */
    FW_ERR_OD_UNSUP_OBJ_TYPE = 34507,
    /** Data offset is too big. */
    FW_ERR_OD_INV_DATA_OFFSET = 34508,
    /** Invalid index definition. */
    FW_ERR_OD_INVALID_INDEX_DEFINITION = 34509,
    /** Wrong user level for read */
    FW_ERR_OD_WRONG_USER_LEVEL_READ_ACCESS = 34510,
    /** Wrong user level for write */
    FW_ERR_OD_WRONG_USER_LEVEL_WRITE_ACCESS = 34511,
    /** Hidden index */
    FW_ERR_OD_HIDDEN_INDEX = 34512,
    /** Undefined access type. */
    FW_ERR_OD_UNDEFINED_ACCESS_TYPE = 34513,
    /** Password given but unit is not in safe state */
    FW_ERR_OD_PASSWORD_WRITTEN_BUT_SYSTEM_IS_NOT_SAFE_STATE = 34514,
    /** OD init failure */
    FW_ERR_OD_SUB_1F50_INIT_FAIL = 34515,

    /*--------------------------------------------------------------------------
        EQADC driver error codes
    --------------------------------------------------------------------------*/
    /** eQADC CFIFO0 DMA error */
    FW_ERR_EQADC_DMA_CFIFO4 = 34600,
    /** eQADC RFIFO0 DMA error */
    FW_ERR_EQADC_DMA_RFIFO0 = 34601,
    /** eQADC CFIFO4 UPDATE DMA error */
    FW_ERR_EQADC_DMA_RFIFO4_UP = 34602,
    /** eQADC RFIFO1 DMA error */
    FW_ERR_EQADC_DMA_RFIFO1 = 34603,
    /** eQADC CFIFO5 UPDATE DMA error */
    FW_ERR_EQADC_DMA_RFIFO5_UP = 34604,
    /** eQADC CFIFO2 DMA error */
    FW_ERR_EQADC_DMA_CFIFO2 = 34605,
    /** eQADC RFIFO2 DMA error */
    FW_ERR_EQADC_DMA_RFIFO2 = 34606,
    /** eQADC RFIFO3 DMA error */
    FW_ERR_EQADC_DMA_RFIFO3 = 34607,
    /** eQADC RFIFO4 DMA error */
    FW_ERR_EQADC_DMA_RFIFO4 = 34608,
    /** eQADC RFIFO5 DMA error */
    FW_ERR_EQADC_DMA_RFIFO5 = 34609,
    /** eQADC CFIFO1 DMA error eTPU trigger. */
    FW_ERR_EQADC_DMA_ETPUTRG0 = 34610,
    /** eQADC CFIFO3 DMA error eTPU trigger. */
    FW_ERR_EQADC_DMA_ETPUTRG1 = 34611,
    /** eQADC ADC0 calibration */
    FW_ERR_EQADC_CALIB_ADC0 = 34612,
    /** eQADC ADC1 calibration */
    FW_ERR_EQADC_CALIB_ADC1 = 34613,
    /** eQADC ADC0 calibration */
    FW_ERR_EQADC_ERROR_ADC0 = 34614,
    /** eQADC ADC1 calibration */
    FW_ERR_EQADC_ERROR_ADC1 = 34615,

    FW_ERR_EQADC_CALIB_ADC1_1 = 34616,
    FW_ERR_EQADC_CALIB_ADC1_2 = 34617,
    FW_ERR_EQADC_CALIB_ADC1_3 = 34618,


    /*--------------------------------------------------------------------------
        FlexCAN driver error codes
    --------------------------------------------------------------------------*/

    /** Low level error. More information please contact EPEC */
    FW_ERR_FLEXCAN_INVALID_MODULE = 34700,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLEXCAN_INVALID_BITRATE = 34701,
    /** Low level error. More information please contact EPEC */
    FW_ERR_FLEXCAN_NOT_INITIALIZED = 34702,

    /*--------------------------------------------------------------------------
        Message buffer error codes
    --------------------------------------------------------------------------*/

    /** Low level error. More information please contact EPEC */
    FW_ERR_MESSAGEBUFFER_FULL = 34720,
    /** Low level error. More information please contact EPEC */
    FW_ERR_MESSAGEBUFFER_EMPTY = 34721,
    /** Low level error. More information please contact EPEC */
    FW_ERR_MESSAGE_ADDR_BUFFER_FULL = 34722,

    /*--------------------------------------------------------------------------
        Can interface error codes
    --------------------------------------------------------------------------*/

    /* Reservation for Can interface */
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_INVALID_CHANNEL = 34750,
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_INVALID_INVALID_PROTOCOL = 34751,
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_TIMETRIGGERED_INDEX_WRONG = 34752,
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_TIMETRIGGERED_COBID_RESERVED = 34753,
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_TIMETRIGGERED_ALL_RESERVED = 34754,
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_TIMETRIGGERED_UPDATE_NOT_READY = 34755,
    /** Low level error. More information please contact EPEC */
    FW_ERR_CAN_CONFIGURATION_ERROR = 34756,

    /*--------------------------------------------------------------------------
        Diagnostic error codes
    --------------------------------------------------------------------------*/

    /** Diagnostic startup has detected that one or more startup tests has failed.
        Info contains the error code causing startup failure. */
    FW_ERR_DIAG_STARTUP_FAIL = 34800,

    /** Diagnostic scheduling is not started and system task is not running correctly. */
    FW_ERR_DIAG_SYSTEM_TASK_FAILURE = 34801,

    /** Diagnostic asynchronous task remains executing when it should be completed. */
    FW_ERR_DIAG_ASYNCHRONOUS_TASK_HANGS = 34802,

    /** Diagnostic has detected a PIT time deviation when a full cycle of all the diagnostic tasks
        has been finished.
        Info contains the measured and deviated PIT time. */
    FW_ERR_DIAG_EXECUTION_TIME_DEVIATION = 34803,

    /** SBC reset request sent to reset the device due exception or fatal error.
         Info is one if the request comes after SBC driver has been started. */
    FW_ERR_DIAG_SBC_RESET_REQUEST = 34804,

    /** Comm cycle time deviation detected.
        Info contains the last Comm Cycle execution time in milliseconds. */
    FW_ERR_DIAG_COMM_CYCLE_TIME_DEVIATION = 34805,

    /** CRC driver spooler has no more space for calculations.
        Diagnostic startup fails since spooler is full. */
    FW_ERR_DIAG_CRC_DRIVER_SPOOLER_FULL = 34806,

    /** System Timer Module (STM) interrupt routine hangs.
        Info contains last interrupt routine counter value. */
    FW_ERR_DIAG_STM_INTERRUPT_HANGS = 34807,

    /** System task callback function registration failed. */
    FW_ERR_DIAG_CALLBACK_REGISTRATION_ERROR = 34808,

    /** Invalid/unused interrupt vector.
        Info contains the invalid/unused vector. */
    FW_ERR_DIAG_INTC_VECTOR_ERROR = 34809,

    /** Application has not been loaded.
        Info not used. */
    FW_ERR_DIAG_NO_APPLICATION = 34810,

    /** Application state error when state queried.
        Info not used. */
    FW_ERR_DIAG_APPLICATION_STATE_ERROR = 34811,

    /** Application exit and stopped.
        Info not used. */
    FW_ERR_DIAG_APPLICATION_EXIT_STOP = 34812,

    /** System maximum runtime exceeded. */
    FW_ERR_DIAG_MAX_RUNTIME_EXCEEDED = 34813,

    /*--------------------------------------------------------------------------
        Diagnostic ADC driver
    --------------------------------------------------------------------------*/

    /** ADC sampling timestamp missmatch. */
    FW_ERR_DIAG_AI_TIMESTAMP_ERROR = 34870,

    /** ADC sampling start timestamp missmatch. */
    FW_ERR_DIAG_AI_START_TIMESTAMP_ERROR = 34871,

    /** ADC sampling end timestamp missmatch. */
    FW_ERR_DIAG_AI_END_TIMESTAMP_ERROR = 34872,

    /** ADC EPU channels sampling queue "Middle" timestamp deviation.*/
    FW_ERR_DIAG_AI_ETPU_MID_TIMESTAMP_ERROR = 34873,

    /** ADC EPU channels sampling queue "End" timestamp deviation.*/
    FW_ERR_DIAG_AI_ETPU_END_TIMESTAMP_ERROR = 34874,

    FW_ERR_DIAG_AI_SAMPLING_STALLED = 34875,

    /*--------------------------------------------------------------------------
        Diagnostic Temperature error codes
    --------------------------------------------------------------------------*/

    /** MPC5777C temperature sensor resets not configured in the DCF. */
    FW_ERR_DIAG_TEMP_SENSOR_RESETS_DCF_CONFIG = 34880,
    /** ADC driver error when fetching MPC5777C temperature sensor samples.
        Info contains ADC driver error. */
    FW_ERR_DIAG_TEMP_SENSOR_ADC_ERROR = 34881,
    /** MPC5777C temperature sensor readings not yet calculated. */
    FW_ERR_DIAG_TEMP_SENSOR_READINGS_UNKNOWN = 34882,
    /** MPC5777C temperature sensor 0 value out of limits.
        Info contains calculated temperature as unsigned integer value. */
    FW_ERR_DIAG_TEMP_SENSOR_0 = 34883,
    /** MPC5777C temperature sensor 1 value out of limits.
        Info contains calculated temperature as unsigned integer value. */
    FW_ERR_DIAG_TEMP_SENSOR_1 = 34884,
    /** MPC5777C temperature sensor 0 and 1 values differ for more than 10 degrees
        from each other. Info contains the calculated temperature difference as unsigned integer value. */
    FW_ERR_DIAG_TEMP_SENSOR_READINGS_DIFFERENCE = 34885,
    /** PCB Temperature sensor value GET failed */
    FW_ERR_DIAG_TEMP_SENSOR_PCB_GET_FAIL = 34886,
    /** PCB Temperature exceeded high or low range  */
    FW_ERR_DIAG_TEMP_SENSOR_PCB_OUT_OF_RANGE = 34887,
    /** PCB Temperature and MCU temperature difference out of bounds */
    FW_ERR_DIAG_TEMP_SENSOR_PCB_MCU_TEMP_DEVIATION = 34888,
    /** PCB Temperature ADC unit and channel were not configured before initialization */
    FW_ERR_DIAG_TEMP_SENSOR_PCB_ADC_NOT_CONFIGURED = 34889,

    /*--------------------------------------------------------------------------
        Diagnostic CMU error codes
    --------------------------------------------------------------------------*/

    /** Clock Monitoring Unit Driver not initialized. */
    FW_ERR_DIAG_CMU_UNINITIALIZED = 34890,
    /**
    * Clock Monitoring Unit XOSC not enabled or system clock source is not set to XOSC.
    * Info 1 means XOSC is not enabled, 2 means clock source is not set to XOSC
    * and 3 means both conditions are true.
    */
    FW_ERR_DIAG_CMU_XOSC_OR_PLL = 34891,
    /** Clock Monitoring Unit reference frequency error.
        Info contains CMU_ISR register flags where error is set. */
    FW_ERR_DIAG_CMU_REFERENCE_FREQUENCY = 34892,
    /** Clock Monitoring Unit internal RC oscillator frequency error.
        Info contains calculated IRC OSC frequency. */
    FW_ERR_DIAG_CMU_IRC_OSC_FREQUENCY = 34893,
    /** PLL0 and/or PLL1 lock has not been acquired. */
    FW_ERR_DIAG_CMU_PLL_LOCK_ACQ = 34894,
    /** PLL0 and/or PLL1 lock has been lost during FW initialization.
        Log entry is saved to RAM and event is cleared. Safe state not activated. */
    FW_ERR_DIAG_CMU_PLL_LOCK_LOST_INIT = 34895,
    /** PLL0 and/or PLL1 lock has been lost while FW was running. */
    FW_ERR_DIAG_CMU_PLL_LOCK_LOST_RUN = 34896,

    /*--------------------------------------------------------------------------
        Diagnostic PMC error codes
    --------------------------------------------------------------------------*/

    /** Power Management Controller self tests failed. */
    FW_ERR_DIAG_PMC_SELF_TEST_ERROR = 34900,
    /** Power Management Controller configuration for resets is invalid. */
    FW_ERR_DIAG_PMC_RESETS_DCF_ERROR = 34901,
    /** Power Management Controller CRC driver error when adding registers for CRC verification. */
    FW_ERR_DIAG_PMC_CRC_DRIVER_ERROR = 34902,
    /** Power Management Controller ADC driver error when fetching samples. */
    FW_ERR_DIAG_PMC_ADC_ERROR = 34903,
    /** Power Management Controller detected bandgap voltage deviation.
        Info contains calculated bandgap voltage. */
    FW_ERR_DIAG_PMC_BANDGAP_VOLTAGE = 34904,
    /** Power Management Controller interrupt.
        Info contains PMC interrupt status. */
    FW_ERR_DIAG_PMC_INTERRUPT = 34905,
    /** PMC_LVD_HVD_EVENT_STATUS flag has changed value. Info contains
        the PMC_LVD_HVD_EVENT_STATUS register value. */
    FW_ERR_DIAG_PMC_LVD_HVD_EVENT_STATUS = 34906,

    /*--------------------------------------------------------------------------
        Diagnostic CRC driver error codes
    --------------------------------------------------------------------------*/

    /** CRC Driver timeouts, calculations have not been made. */
    FW_ERR_CRCDRV_TIMEOUT = 34910,
    /** CRC Driver CRC check fails. */
    FW_ERR_CRCDRV_CRC_CHECK_FAIL = 34911,

    /*--------------------------------------------------------------------------
        Diagnostic GPIO error codes
    --------------------------------------------------------------------------*/

    /** GPIO Online diagnostic failed, failed GPIO number stored to Info. */
    FW_ERR_DIAG_GPIO_STATE_WRONG = 34920,
    /** GPIO pad number is defined as not supported. */
    FW_ERR_GPIO_UNSUPPORTED_PAD_NBR = 34921,

    /*--------------------------------------------------------------------------
        Diagnostic CAN error codes
    --------------------------------------------------------------------------*/

    /** CAN test not yet executed */
    FW_ERR_DIAG_CAN_NOT_DONE = 34930,
    /** RX CRC startup test failed */
    FW_ERR_DIAG_CAN_RX_CRC_FAILED = 34931,
    /** TX CRC startup test failed */
    FW_ERR_DIAG_CAN_TX_CRC_FAILED = 34932,
    /** Problem in configuration of 'CAN Startup Test' */
    FW_ERR_CAN_STARTUP_TEST_CONFIGURATION_ERROR = 34933,
    /** 'CAN Startup Test' has failed */
    FW_ERR_CAN_STARTUP_TEST_FAILED = 34934,

    /*--------------------------------------------------------------------------
        Diagnostic SSCM error codes
    --------------------------------------------------------------------------*/

    /** System Status and Configuration Module detected invalid device configuration
        due DCF transfer or DCF record parity error. */
    FW_ERR_DIAG_SSCM_DEVICE_CONFIG = 34940,
    /** System Status and Configuration Module has received a notification of
        a memory configuration error. */
    FW_ERR_DIAG_SSCM_MEMORY_CONFIG = 34941,
    /** System Status and Configuration Module has detected in field life cycle
        while Nexus interface(s) enabled. */
    FW_ERR_DIAG_SSCM_IN_FIELD_NEXUS_ENABLED = 34942,
    /** System Status and Configuration Module has detected that device has
        detected disabled in field cycle. */
    FW_ERR_DIAG_SSCM_IN_FIELD_DISABLED = 34943,

    /*--------------------------------------------------------------------------
        Over voltage protection error codes
    --------------------------------------------------------------------------*/

    /** Over voltage protection - Startup test GPIO control error.
        Info contains control error code from GPIO driver. */
    FW_ERR_OVP_STARTUP_GPIO_CONTROL = 34960,
    /** Over voltage protection - Startup test failed due ADC driver error or too low supply voltage.
        Info contains either current ADC supply reading or ADC error code. */
    FW_ERR_OVP_STARTUP_TEST = 34961,
    /** Over voltage protection - Energy storage capacity test failed.
        Info contains the OVP startup test execution time in milliseconds. */
    FW_ERR_OVP_ENERGY_STORAGE_FAIL = 34962,
    /** Over voltage protection - Over voltage detected in SBC safety path test.
        Info is zero when detected before safety path test, 1 or 2 while detected during safety path test. */
    FW_ERR_OVP_DETECTED_IN_SBC_SAFETY_PATH = 34963,
    /** Logic OVP overvoltage protection detected during online diagnostics.
        Info contains latest averaged power supply voltage reading. */
    FW_ERR_OVP_DETECTED_ONLINE = 34964,

    /*--------------------------------------------------------------------------
        Diagnostic External RAM error codes
    --------------------------------------------------------------------------*/

    /** External RAM address bus stuck high error */
    FW_ERR_DIAG_EXTRAM_ADDRESS_HIGH_ERROR = 34970,
    /** External RAM address bus stuck low error */
    FW_ERR_DIAG_EXTRAM_ADDRESS_LOW_ERROR = 34971,
    /** External RAM address bus short error */
    FW_ERR_DIAG_EXTRAM_ADDRESS_SHORT_ERROR = 34972,
    /** External RAM data bus error */
    FW_ERR_DIAG_EXTRAM_DATA_ERROR = 34973,
    /** Extran RAM test start address wrong */
    FW_ERR_DIAG_EXTRAM_START_ADDRESS_ERROR = 34974,
    /** External RAM test failed. */
    FW_ERR_EXTRAM_MEMORY_FAIL = 34975,

    /*--------------------------------------------------------------------------
        Diagnostic eMIOS error codes
    --------------------------------------------------------------------------*/

    /** eMios initialization detected startup test error.
        Info contains a bit mask of the failed eMIOS channels. */
    FW_ERR_EMIOS_STARTUP_TEST = 34980,
    /** eMios startup test detected wrong state for the channel. */
    FW_ERR_EMIOS_CHANNEL_WRONG_STATE = 34981,
    /** eMios driver has not been invalid or initialization has failed. */
    FW_ERR_EMIOS_DRIVER_UNINITIALIZED = 34982,
    /** eMios channel has not been invalid or initialization has failed. */
    FW_ERR_EMIOS_CHANNEL_UNINITIALIZED = 34983,
    /** eMios channel is invalid i.e. not supported channel. */
    FW_ERR_EMIOS_INVALID_CHANNEL = 34984,
    /** eMios invalid channel mode. */
    FW_ERR_EMIOS_INVALID_CHANNEL_MODE = 34985,
    /** eMios invalid channel mode. */
    FW_ERR_EMIOS_INVALID_PRESCALER = 34986,

    /*--------------------------------------------------------------------------
        Diagnostic Safety Switch error codes
    --------------------------------------------------------------------------*/

    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_STARTUP_1 = 35000,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_STARTUP_2 = 35001,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_STARTUP_ALL = 35002,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_ANALOG_1 = 35003,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_ANALOG_2 = 35004,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_DIGITAL_1 = 35005,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_DIGITAL_2 = 35006,
    /** Undervoltage condition during startup. Triggers system restart */
    FW_ERR_DIAG_SAFETY_SWITCH_BEF_LOW = 35007,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_BEF_HIGH = 35008,
    /** Error code not in use. */
    FW_ERR_DIAG_SAFETY_SWITCH_O_AFT_LOW = 35009,

    /**
     * Safety switch diagnostic has measured too high voltage level after
     * safety switch when switch is open (outputs deactivated). This error may
     * occur during startup or online diagnostic.
     */
    FW_ERR_DIAG_SAFETY_SWITCH_O_AFT_HIGH = 35010,
    /**
     * Safety switch diagnostic has measured too low voltage level after
     * safety switch component compared to voltage level before switch.
     * Diagnostic has been done when switch was closed (outputs energized).
     */
    FW_ERR_DIAG_SAFETY_SWITCH_C_AFT_LOW = 35011,
    /**
     * Safety switch diagnostic has measured too high voltage level after safety
     * switch component compared to voltage level before switch.
     * Diagnostic has been done when switch was closed (outputs energized).
     */
    FW_ERR_DIAG_SAFETY_SWITCH_C_AFT_HIGH = 35012,
    /**
    * Safety switch analog state online test error code.
    * Cannot read voltage measurement before safety switch.
    * LogEntry Info field contains ADC-driver function error code.
    */
    FW_ERR_DIAG_SAFETY_1_ANALOG_BEFORE = 35013,
    /**
    * Safety switch analog state online test error code.
    * Cannot read voltage measurement after safety switch.
    * LogEntry Info field contains ADC-driver function error code.
    */
    FW_ERR_DIAG_SAFETY_1_ANALOG_AFTER = 35014,
    /**
    * Safety switch one online diagnostic failed because safety switch
    * number one startup diagnostic has been failed.
    */
    FW_ERR_DIAG_SAFETY_1_STARTUP_NOK = 35015,
    /** Safety switch one online diagnostic error, unexpected gpio status. */
    FW_ERR_DIAG_SAFETY_1_WRONG_STATE = 35016,
    /**
     * Safety switch online diagnostic error, discharge load error detected.
     */
    FW_ERR_DIAG_SAFETY_SWITCH_1_ONLINE_DLE = 35017,
    /**
    * Safety switch startup test error code.
    * Safety switch is closed while entering startup test.
    **/
    FW_ERR_DIAG_SAFETY_SWITCH_1_CLOSED = 35018,
    /**
    * Safety switch one first startup diagnostic error.
    * Startup diagnostic sequence error.
    * Wrong sequence variable state is set to logEntry Info field.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_1_START_1_SEQ = 35019,
    /**
    * Safety switch one second startup diagnostic error.
    * Startup diagnostic sequence error.
    * Wrong sequence variable state is set to logEntry Info field.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_1_START_2_SEQ = 35020,
    /**
    * Safety switch one third startup diagnostic error.
    * Startup diagnostic sequence error.
    * Wrong sequence variable state is set to logEntry Info field.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_1_START_3_SEQ = 35021,
    /**
    * Safety switch one fourth startup diagnostic error.
    * Startup diagnostic sequence error.
    * Wrong sequence variable state is set to logEntry Info field.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_1_START_4_SEQ = 35022,
    /**
    * Safety switch one fifth startup diagnostic error.
    * Startup diagnostic sequence error.
    * Wrong sequence variable state is set to logEntry Info field.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_1_START_5_SEQ = 35023,
    /**
     * Safety switch startup test error. Discharge load error detected.
     * Startup sequence variable state is set to logEntry Info field.
     */
     FW_ERR_DIAG_SAFETY_SWITCH_1_START_DLE = 35024,

    /**
     * Safety switch startup test failures because of internal error. Internal
     * safe state has been activated from other firmware component before
     * safety switch startup test. Original error code is stored to log message
     * Info field. Safety switch startup diagnostic first function error code.
     */
    FW_ERR_DIAG_SAFETY_S1_1_INTERNAL = 35025,

    /**
     * Safety switch startup test failures because of internal error. Internal
     * safe state has been activated from other firmware component before
     * safety switch startup test. Original error code is stored to log message
     * Info field. Safety switch startup diagnostic second function error code.
     */
    FW_ERR_DIAG_SAFETY_S1_2_INTERNAL = 35026,
    /**
     * Safety switch startup test failures because of internal error. Internal
     * safe state has been activated from other firmware component before
     * safety switch startup test. Original error code is stored to log message
     * Info field. Safety switch startup diagnostic third function error code.
     */
    FW_ERR_DIAG_SAFETY_S1_3_INTERNAL = 35027,
    /**
     * Safety switch startup test failures because of internal error. Internal
     * safe state has been activated from other firmware component before
     * safety switch startup test. Original error code is stored to log message
     * Info field. Safety switch startup diagnostic fourth function error code.
     */
    FW_ERR_DIAG_SAFETY_S1_4_INTERNAL = 35028,
    /**
     * Safety switch startup test failures because of internal error. Internal
     * safe state has been activated from other firmware component before
     * safety switch startup test. Original error code is stored to log message
     * Info field. Safety switch startup diagnostic fifth function error code.
     */
    FW_ERR_DIAG_SAFETY_S1_5_INTERNAL = 35029,
    /**
    * Safety switch startup test failures because of overvoltage has been detected.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_1_OVP_FAULT = 35030,
    /**
    * One or more safety Ouput Voltage measurements between 1. and 32. exceeds the limit.
    * Info contains 32 bit number where each channels is stored.
    * 1.bit is first voltage measurement etc.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_OUTPUT_VOLTAGE_OVER_1 = 35031,
    /**
    * One or more safety Ouput Voltage measurements between 33. and 64. exceeds the limit.
    * Info contains 32 bit number where each channels is stored.
    * 1.bit is 33.voltage measurement etc.
    */
    FW_ERR_DIAG_SAFETY_SWITCH_OUTPUT_VOLTAGE_OVER_2 = 35032,

    /**
     * Measured VIN_M and SBC VSUP voltages are different.
     */
    FW_ERR_DIAG_SAFETY_SWITCH_VIN_VSUP_MISMATCH = 35033,




    /*--------------------------------------------------------------------------
        Diagnostic FCCU error codes
    --------------------------------------------------------------------------*/

    /** Fault Collection and Control Unit operation execution did not complete in time. */
    FW_ERR_DIAG_FCCU_RUN_OPERATION = 35100,
    /** Fault Collection and Control Unit could not clear pending faults from status register 0. */
    FW_ERR_DIAG_FCCU_NCF0_CLEAR = 35101,
    /** Fault Collection and Control Unit could not clear pending faults from status register 1. */
    FW_ERR_DIAG_FCCU_NCF1_CLEAR = 35102,
    /** Fault Collection and Control Unit configuration error. */
    FW_ERR_DIAG_FCCU_STATE_CONFIG = 35103,
    /** Fault Collection and Control Unit reading status failed.
        Info contains the error code leading into failure. */
    FW_ERR_DIAG_FCCU_STATUS = 35104,
    /** Fault Collection and Control Unit interrupt execution error.
        Info contains the error code leading into failure. */
    FW_ERR_DIAG_FCCU_INTERRUPT = 35105,
    /** Fault Collection and Control Unit fault detected in input channels from 0 to 31.
        Info contains FCCU NCF_S0 register value. */
    FW_ERR_DIAG_FCCU_CHANNELS_0_31 = 35106,
    /** Fault Collection and Control Unit fault detected in input channels from 32 to 46.
        Info contains FCCU NCF_S1 register value. */
    FW_ERR_DIAG_FCCU_CHANNELS_32_46 = 35107,
    /** Fault Collection and Control Unit Crossbar Integrity error status register.
        Info contains XBIC ESR register value. */
    FW_ERR_DIAG_FCCU_XBIC_ESR_REGISTER = 35108,
    /** Fault Collection and Control Unit Crossbar Integrity error address register.
        Info contains XBIC EAR register value. */
    FW_ERR_DIAG_FCCU_XBIC_ADDR_REGISTER = 35109,
    /** Fault Collection and Control - Faults present during startup.
        Info contains FCCU status error value when system started. */
    FW_ERR_DIAG_FCCU_STARTUP_STATUS = 35110,
    /** Fault Collection and Control - Faults present during startup.
        Info contains FCCU NCF_S0 status register value when system started. */
    FW_ERR_DIAG_FCCU_STARTUP_FAULTS0 = 35111,
    /** Fault Collection and Control - Faults present during startup.
        Info contains FCCU NCF_S1 status register value when system started. */
    FW_ERR_DIAG_FCCU_STARTUP_FAULTS1 = 35112,
    /** Fault Collection and Control - Inject fake fault to test FCCU status.
        Info contains FCCU interrupt status register value. */
    FW_ERR_DIAG_FCCU_INTERRUPT_STATUS = 35113,
    /** Fault Collection and Control Unit - Uncorrectable error in M_CAN RAM Controller. */
    FW_ERR_FCCU_PER_UCE_IN_MCAN = 35114,
    /** Fault Collection and Control Unit - Uncorrectable error in FlexCAN A RAM Controller. */
    FW_ERR_FCCU_PER_UCE_IN_FLEXCAN_A = 35115,
    /** Fault Collection and Control Unit - Uncorrectable error in FlexCAN B RAM Controller. */
    FW_ERR_FCCU_PER_UCE_IN_FLEXCAN_B = 35116,
    /** Fault Collection and Control Unit - Uncorrectable error in FlexCAN C RAM Controller. */
    FW_ERR_FCCU_PER_UCE_IN_FLEXCAN_C = 35117,
    /** Fault Collection and Control Unit - Uncorrectable error in FlexCAN D RAM Controller. */
    FW_ERR_FCCU_PER_UCE_IN_FLEXCAN_D = 35118,

    /*--------------------------------------------------------------------------
        Diagnostic ERM driver error codes
    --------------------------------------------------------------------------*/

    /** ERM startup test not yet executed */
    FW_ERR_DIAG_ERM_NOT_DONE = 35150,
    /** Flash ECC error not correctly reported to ERM module */
    FW_ERR_DIAG_ERM_FLASH_ECC = 35151,
    /** Uncorrectable single-bit error on eDMA_A TCD  */
    FW_ERR_DIAG_ERM_EDMA_A_TCD_ECC = 35152,

    /** Error Reporting Module. Error Status Register 0. */
    FW_ERR_ERM_STATUS0 = 35153,

    /** Error Reporting Module. Error Status Register 1. */
    FW_ERR_ERM_STATUS1 = 35154,

    /** Error Reporting Module. Error Status Register 2. */
    FW_ERR_ERM_STATUS2 = 35155,

    /** Error Reporting Module. ERM channel 0 address */
    FW_ERR_ERM_ADDRESS0 = 35156,

    /** Error Reporting Module. ERM channel 1 address */
    FW_ERR_ERM_ADDRESS1 = 35157,

    /** Error Reporting Module. ERM channel 2 address */
    FW_ERR_ERM_ADDRESS2 = 35158,

    /** Error Reporting Module. ERM channel 3 address */
    FW_ERR_ERM_ADDRESS3 = 35159,

    /** Error Reporting Module. ERM channel 4 address */
    FW_ERR_ERM_ADDRESS4 = 35160,

    /** Error Reporting Module. ERM channel 5 address */
    FW_ERR_ERM_ADDRESS5 = 35161,

    /** Error Reporting Module. ERM channel 6 address */
    FW_ERR_ERM_ADDRESS6 = 35162,

    /** Error Reporting Module. ERM channel 7 address */
    FW_ERR_ERM_ADDRESS7 = 35163,

    /** Error Reporting Module. ERM channel 8 address */
    FW_ERR_ERM_ADDRESS8 = 35164,

    /** Error Reporting Module. ERM channel 9 address */
    FW_ERR_ERM_ADDRESS9 = 35165,

    /** Error Reporting Module. ERM channel 10 address */
    FW_ERR_ERM_ADDRESS10 = 35166,

    /** Error Reporting Module. ERM channel 11 address */
    FW_ERR_ERM_ADDRESS11 = 35167,

    /** Error Reporting Module. ERM channel 12 address */
    FW_ERR_ERM_ADDRESS12 = 35168,

    /** Error Reporting Module. ERM channel 13 address */
    FW_ERR_ERM_ADDRESS13 = 35169,

    /** Error Reporting Module. ERM channel 14 address */
    FW_ERR_ERM_ADDRESS14 = 35170,

    /** Error Reporting Module. ERM channel 15 address */
    FW_ERR_ERM_ADDRESS15 = 35171,

    /** Error Reporting Module. ERM channel 16 address */
    FW_ERR_ERM_ADDRESS16 = 35172,

    /** Error Reporting Module. ERM channel 17 address */
    FW_ERR_ERM_ADDRESS17 = 35173,

    /** Error Reporting Module. ERM channel 18 address */
    FW_ERR_ERM_ADDRESS18 = 35174,

    /** Error Reporting Module. ERM channel 19 address */
    FW_ERR_ERM_ADDRESS19 = 35175,

    /*--------------------------------------------------------------------------
        Diangostic Log error codes
    --------------------------------------------------------------------------*/

    /** Diagnostic log - RAM log header checksum fails. Occurs when diagnostic RAM log header is corrupted.
        Info contains verification checksum value. */
    FW_ERR_DIAG_LOG_HEADER_CHECKSUM = 35200,
    /** Diagnostic log - RAM log entry checksum fails. Occurs when diagnostic RAM log entry is corrupted. */
    FW_ERR_DIAG_LOG_ENTRY_CHECKSUM = 35201,
    /** Diagnostic log - Selecting and/or unlocking page for erase failed. */
    FW_ERR_DIAG_LOG_FLASH_ERASE_UNLOCK_FAILURE = 35202,
    /** Diagnostic log - Starting flash erase failed. */
    FW_ERR_DIAG_LOG_FLASH_ERASE_FAILURE = 35203,

    /*--------------------------------------------------------------------------
        System Basis Chip errors codes
    --------------------------------------------------------------------------*/

    /** System Basis Chip - INIT_INT configuration does not match in driver startup.
        Info contains INIT_INT register value. */
    FW_ERR_SBC_INIT_INT_CONFIGURATION = 35300,
    /** System Basis Chip - Safety path FS0b deactivation fails.
        Can also occur when power supply has an unstable electrical connection and voltage fluctuates.
        Info contains WD_ANSWER, and in some cases also WD_COUNTER register values for FSx, IO_FS_G and WD_err. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_FS0B_DEACTIVATION = 35301,
    /** System Basis Chip - Safety path EXT ERR / IO_4 GPIO control fails.
        Info contains either control error code from GPIO driver or
        IO_INPUT and WD_ANSWER register values for IO_4, IO_5 and IO_FS_G, or GPIO driver error code. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_SET_EXT_ERR = 35302,
    /** System Basis Chip - Safety path EXT ERR / IO_4 verification fails.
        Info contains IO_INPUT register value or both IO_INPUT and WD_ANSWER register values. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_VERIFY_EXT_ERR = 35303,
    /** System Basis Chip - Safety path EXT ERR ACK / IO_5 GPIO control fails.
        Info contains control error code from GPIO driver. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_SET_EXT_ERR_ACK = 35304,
    /** System Basis Chip - Safety path EXT ERR ACK / IO_5 verification fails.
        Info contains IO_INPUT register value. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_VERIFY_EXT_ERR_ACK = 35305,
    /** System Basis Chip - Safety path test fails to verify safety switch voltage.
        Can also occur when power supply has an unstable electrical connection and voltage fluctuates.
        Info contains the measured millivoltage value over the safety switch i.e. voltage to outputs. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_TEST_VOLTAGE = 35306,
    /** System Basis Chip - Safety path safety switch GPIO control fails.
        Info contains control error code from GPIO driver. */
    FW_ERR_SBC_STARTUP_SAFETY_PATH_TEST = 35307,

    /** System Basis Chip - Non-maskable interrupt interconnection test fails between SBC and MCU. */
    FW_ERR_SBC_STARTUP_NMI_INTERCONNECTION_TEST = 35308,

    /** System Basis Chip - SBC debug pin is enabled, SBC is not fully functional. */
    FW_ERR_SBC_DEBUG_SWITCH_ON = 35309,
    /** System Basis Chip - HW_CONFIG Vaux not used.
        Info contains HW_CONFIG register value. */
    FW_ERR_SBC_HW_CONFIG_VAUX_NOT_USED = 35310,
    /** System Basis Chip - HW_CONFIG external PNP connect mismatch.
        Info contains HW_CONFIG register value. */
    FW_ERR_SBC_HW_CONFIG_VCCA_PNP = 35311,
    /** System Basis Chip - HW_CONFIG Vcca 3.3 V / 5 V mismatch.
        Info contains HW_CONFIG register value. */
    FW_ERR_SBC_HW_CONFIG_VCCA = 35312,
    /** System Basis Chip - HW_CONFIG Vaux 3.3 V / 5 V mismatch.
        Info contains HW_CONFIG register value. */
    FW_ERR_SBC_HW_CONFIG_VAUX = 35313,
    /** System Basis Chip - HW_CONFIG Vpre Buck-boost / Buck only mismatch.
        Info contains HW_CONFIG register value. */
    FW_ERR_SBC_HW_CONFIG_VPRE = 35314,

    /** System Basis Chip - WU_SOURCE Wakeup detected when wakeups disabled.
        Info contains WU_SOURCE register value. */
    FW_ERR_SBC_WAKEUP_DETECTED = 35315,

    /** System Basis Chip - EXT ERR ACK signal low from MCU to SBC.
        Info contains IO_INPUT register value. */
    FW_ERR_SBC_IO_5_ERROR = 35316,
    /** System Basis Chip - EXT ERR signal low from MCU to SBC.
        Info contains IO_INPUT register value. */
    FW_ERR_SBC_IO_4_ERROR = 35317,
    /** System Basis Chip - IO_Others IO_2 or IO_3 indicating FCCU error.
        Info contains IO_INPUT register value. */
    FW_ERR_SBC_IO_INPUT_FCCU_ERROR = 35318,
    /** System Basis Chip - R, bridge drift monitoring (Vcore).
        Info contains IO_INPUT register value. */
    FW_ERR_SBC_IO_1_ERROR = 35319,
    /** System Basis Chip - Unused in current configuration.
        Info contains IO_INPUT register value. */
    FW_ERR_SBC_IO_0_ERROR = 35320,

    /** System Basis Chip - Status_Vreg1 input power feed forward activated.
        Info contains STATUS_VREG1 register value. */
    FW_ERR_SBC_STATUS_VREG1_IPFF_MODE_ACTIVATED = 35321,
    /** System Basis Chip - Status_Vreg1 Vpre SMPS state off.
        Info contains STATUS_VREG1 register value. */
    FW_ERR_SBC_STATUS_VREG1_VPRE_SMPS_STATE_OFF = 35322,

    /** System Basis Chip - Status_Vreg2 Vcore SMPS off.
        Info contains STATUS_VREG2 register value. */
    FW_ERR_SBC_STATUS_VREG2_VCORE_SMPS_OFF = 35323,

    /** System Basis Chip - VPRE overvoltage.
        Info contains DIAG_VREG1 register value. */
    FW_ERR_SBC_DIAG_VREG1_VPRE_OVERVOLTAGE = 35324,
    /** System Basis Chip - Vcore overvoltage.
        Info contains DIAG_VREG1 register value. */
    FW_ERR_SBC_DIAG_VREG1_VCORE_OVERVOLTAGE = 35325,
    /** System Basis Chip - Vcore undervoltage.
        Info contains DIAG_VREG1 register value. */
    FW_ERR_SBC_DIAG_VREG1_VCORE_UNDERVOLTAGE = 35326,

    /** System Basis Chip - Vaux overvoltage.
        Info contains DIAG_VREG2 register value. */
    FW_ERR_SBC_DIAG_VREG2_VAUX_OVERVOLTAGE = 35327,
    /** System Basis Chip - Vaux undervoltage.
        Info contains DIAG_VREG2 register value. */
    FW_ERR_SBC_DIAG_VREG2_VAUX_UNDERVOLTAGE = 35328,

    /** System Basis Chip - Vcca overvoltage.
        Info contains DIAG_VREG3 register value. */
    FW_ERR_SBC_DIAG_VREG3_VCCA_OVERVOLTAGE = 35329,
    /** System Basis Chip - Vcca undervoltage.
        Info contains DIAG_VREG3 register value. */
    FW_ERR_SBC_DIAG_VREG3_VCCA_UNDERVOLTAGE = 35330,

    /** System Basis Chip - CAN overvoltage. Warning only, does not foce safe state.
        Info contains DIAG_VREG2 register value. */
    FW_ERR_SBC_DIAG_VREG2_VCAN_OVERVOLTAGE = 35331,
    /** System Basis Chip - CAN undervoltage. Warning only, does not foce safe state.
        Info contains DIAG_VREG2 register value. */
    FW_ERR_SBC_DIAG_VREG2_VCAN_UNDERVOLTAGE = 35332,

    /** System Basis Chip - CANH battery short-circuit. Warning only, does not foce safe state.
        Info contains DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CANH_BATTERY_SHORT_CIRCUIT = 35333,
    /** System Basis Chip - CANH ground short-circuit. Warning only, does not foce safe state.
        Info contains DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CANH_GROUND_SHORT_CIRCUIT = 35334,
    /** System Basis Chip - CANL battery short-circuit. Warning only, does not foce safe state.
        Info contains SBC DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CANL_BATTERY_SHORT_CIRCUIT = 35335,
    /** System Basis Chip - CANL ground short-circuit. Warning only, does not foce safe state.
        Info contains DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CANL_GROUND_SHORT_CIRCUIT = 35336,

    /** System Basis Chip - CAN_LIN overcurrent detection. Warning only, does not foce safe state.
        Info contains DIAG_CAN_LIN register value. */
    FW_ERR_SBC_DIAG_CAN_LIN_CAN_OVERCURRENT = 35337,
    /** System Basis Chip - CAN_LIN overtemperature detection.
        Info contains DIAG_CAN_LIN register value. */
    FW_ERR_SBC_DIAG_CAN_LIN_CAN_OVERTEMPERATURE = 35338,

    /** System Basis Chip - CAN BUS dominant clamping. Warning only, does not foce safe state.
        Info contains DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CAN_BUS_DOMINANT = 35339,
    /** System Basis Chip - CAN RXD recessive clamping. Warning only, does not foce safe state.
        Info contains DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CAN_RXD_RECESSIVE = 35340,
    /** System Basis Chip - CAN TXD dominant clamping. Warning only, does not foce safe state.
        Info contains DIAG_CAN register value. */
    FW_ERR_SBC_DIAG_CAN_TXD_DOMINANT = 35341,

    /** System Basis Chip - Vref voltage too low.
        Info contains Vref voltage value (2.5 V) in millivolts. */
    FW_ERR_SBC_VREF_LOW_LIMIT = 35342,
    /** System Basis Chip - Vref voltage too high.
        Info contains Vref voltage value (2.5 V) in millivolts. */
    FW_ERR_SBC_VREF_HIGH_LIMIT = 35343,
    /** System Basis Chip - Temperature too low, below -40 C.
        Info contains temperature as unsigned integer value, multiplied with 10 for first decimal value. */
    FW_ERR_SBC_UNDERTEMPERATURE = 35344,
    /** System Basis Chip - Temperature too high, above 125 C.
        Info contains temperature as unsigned integer value, multiplied with 10 for first decimal value. */
    FW_ERR_SBC_OVERTEMPERATURE = 35345,

    /** System Basis Chip - CAN mode not normal operation mode.
        Info contains CAN_LIN_MODE register value. */
    FW_ERR_SBC_CAN_MODE_NOT_NORMAL = 35346,
    /** System Basis Chip - CAN automatic Tx disable active.
        Info contains CAN_LIN_MODE register value. */
    FW_ERR_SBC_CAN_AUTOMATIC_TX_DISABLE = 35347,
    /** System Basis Chip - CAN wakeup detection set.
        Info contains CAN_LIN_MODE register value. */
    FW_ERR_SBC_CAN_WRONG_WAKEUP_MODE = 35348,
    /** System Basis Chip - LIN is not disabled.
        Info contains CAN_LIN_MODE register value. */
    FW_ERR_SBC_LIN_WRONG_MODE = 35349,

    /** System Basis Chip - SPI command has invalid secure bits.
        Info contains DIAG_SPI register value. */
    FW_ERR_SBC_SPI_SECURE_BITS = 35350,
    /** System Basis Chip - SPI channel clocking error.
        Info contains DIAG_SPI register value. */
    FW_ERR_SBC_SPI_CLOCK = 35351,
    /** System Basis Chip - SPI command wrong/sent at worng time.
        Info contains DIAG_SPI register value. */
    FW_ERR_SBC_SPI_VIOLATION = 35352,
    /** System Basis Chip - SPI command parity bit error.
        Info contains DIAG_SPI register value. */
    FW_ERR_SBC_SPI_PARITY = 35353,

    /** System Basis Chip - MODE not in initialization mode i.e. reset cycle detected.
        Info contains MODE register value. */
    FW_ERR_SBC_MODE_NOT_INIT = 35354,
    /** System Basis Chip - SBC not in normal mode i.e. unexpected power-on-reset detected.
        Info contains MODE register value. */
    FW_ERR_SBC_MODE_NOT_IN_NORMAL = 35355,

    /** System Basis Chip - Vcore_en, Vcca_en, Vaux_en or Vcan_en not enabled.
        Info contains VREG_MODE register value. */
    FW_ERR_SBC_VREG_MODE_FAULTY = 35356,

    /** System Basis Chip - IO_4 configured as output.
        Info contains IO_OUT_AMUX register value. */
    FW_ERR_SBC_IO_OUT_AMUX_IO4_OUTPUT_GATE_DRIVER = 35357,
    /** System Basis Chip - IO_5 configured as output.
        Info contains IO_OUT_AMUX register value. */
    FW_ERR_SBC_IO_OUT_AMUX_IO5_OUTPUT_GATE_DRIVER = 35358,

    /** System Basis Chip - Vcore safety input configuration error.
        Info contains INIT_SUPERVISOR1 register value. */
    FW_ERR_SBC_INIT_SUPERVISOR1_VCORE_SAFETY_INPUT = 35359,
    /** System Basis Chip - Vcca safety input configuration error.
        Info contains INIT_SUPERVISOR1 register value. */
    FW_ERR_SBC_INIT_SUPERVISOR1_VCCA_SAFETY_INPUT = 35360,

    /** System Basis Chip - Vaux input configuration error.
        Info contains INIT_SUPERVISOR2 register value. */
    FW_ERR_SBC_INIT_SUPERVISOR2_VAUX_SAFETY_INPUT = 35361,
    /** System Basis Chip - Deep fail safe timer configuration error.
        Info contains INIT_SUPERVISOR2 register value. */
    FW_ERR_SBC_INIT_SUPERVISOR2_DEEP_FAIL_SAFE_TIMER = 35362,

    /** System Basis Chip - Fail Safe state machine 1 configuration does not match.
        Info contains INIT_FSSM1 register value. */
    FW_ERR_SBC_INIT_FSSM1_CONFIGURATION = 35363,

    /** System Basis Chip - Fail Safe state machine 2 configuration does not match.
        Info contains INIT_FSSM2 register value. */
    FW_ERR_SBC_INIT_FSSM2_CONFIGURATION = 35364,
    /** System Basis Chip - RSTb error counter has wrong configuration value.
        Info contains INIT_FSSM2 register value. */
    FW_ERR_SBC_INIT_FSSM2_RSTB_ERROR_COUNTER_WRONG = 35365,
    /** System Basis Chip - FCCU monitoring not enabled.
        Info contains INIT_FSSM2 register value. */
    FW_ERR_SBC_INIT_FSSM2_FCCU_MONITORING_DISABLED = 35366,
    /** System Basis Chip - Wrong FCCU polarity configured.
        Info contains INIT_FSSM2 register value. */
    FW_ERR_SBC_INIT_FSSM2_FCCU_POLARITY = 35367,

    /** System Basis Chip - Watchdog window duration is invalid.
        Info contains WD_WINDOW register value. */
    FW_ERR_SBC_WD_WINDOW_DURATION = 35368,
    /** System Basis Chip - Ivalid fail safe secure bits in watchdog window.
        Info contains WD_WINDOW register value. */
    FW_ERR_SBC_WD_WINDOW_SPI_FAIL_SAFE_SECURE_BITS = 35369,
    /** System Basis Chip - Fail safe CLK error detection in watchdog window.
        Info contains WD_WINDOW register value. */
    FW_ERR_SBC_WD_WINDOW_FAIL_SAFE_CLK_ERROR = 35370,
    /** System Basis Chip - Invalid fail safe SPI access in watchdog window.
        Info contains WD_WINDOW register value. */
    FW_ERR_SBC_WD_WINDOW_SPI_FAIL_SAFE_INVALID_ACCESS = 35371,
    /** System Basis Chip - Invalid SPI parity in watchdog window.
        Info contains WD_WINDOW register value. */
    FW_ERR_SBC_WD_WINDOW_SPI_FAIL_SAFE_INVALID_PARITY = 35372,

    /** The SBC WD ANSWER response errors indicating serious faults in SBC. */
    /** System Basis Chip - Reset event.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_RESET_EVENT_PENDING = 35373,
    /** System Basis Chip - Fail-safe event.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_FAIL_SAFE_EVENT = 35374,
    /** System Basis Chip - Watchdog refresh error.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_REFRESH_ERROR = 35375,
    /** System Basis Chip - Fail-safe output failure.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_FAIL_SAFE_OUTPUT_FAILURE = 35376,
    /** System Basis Chip - IO monitoring error detected.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_IO_MONITORING_ERROR = 35377,
    /** System Basis Chip - ECC on fail-safe state machine.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_ECC_FAIL_SAFE_SM_EVENT = 35378,
    /** System Basis Chip - ECC on fail-safe registers failed due errors which cannot be corrected.
        Info contains WD_ANSWER register value. */
    FW_ERR_SBC_WD_ANSWER_ECC_FAIL_SAFE_REGISTERS = 35379,

    /** System Basis Chip - FS_OUT deactivation error. */
    FW_ERR_SBC_FS_OUT_DEACTIVATION_FAIL = 35380,

    /** System Basis Chip - External reset. Not an error, normal event in power-on-reset. */
    FW_ERR_SBC_DIAG_FS1_EXTERNAL_RSTB = 35381,
    /** System Basis Chip - RSTb short-circuit HIGH.
        Info contains DIAG_FS1 register value. */
    FW_ERR_SBC_DIAG_FS1_RSTB_SHORT_CIRCUIT_HIGH = 35382,
    /** System Basis Chip - Fail Safe output short-circuit low/open load.
        Info contains DIAG_FS1 register value. */
    FW_ERR_SBC_DIAG_FS1_FS0B_SHORT_CIRCUIT_LOW = 35383,
    /** System Basis Chip - Fail Safe output short-circuit high.
        Info contains DIAG_FS1 register value. */
    FW_ERR_SBC_DIAG_FS1_FS0B_SHORT_CIRCUIT_HIGH = 35384,

    /** System Basis Chip - Incorrect watchdog refreshes.
        Info contains WD_COUNTER register value. */
    FW_ERR_SBC_WD_COUNTER_ERROR = 35385,

    /** System Basis Chip - Reset error counter over limits.
        Info contains DIAG_FS2 register value. */
    FW_ERR_SBC_DIAG_FS2_RSTB_ERROR_COUNTER = 35386,
    /** System Basis Chip - Error in the IO_45 i.e. external IC / FCCU error monitoring.
        Info contains DIAG_FS2 register value. */
    FW_ERR_SBC_DIAG_FS2_IO_45_PROTOCOL = 35387,
    /** System Basis Chip - Error in the FCCU protocol.
        Info contains DIAG_FS2 register value. */
    FW_ERR_SBC_DIAG_FS2_FCCU_PROTOCOL = 35388,
    /** System Basis Chip - Error in the external resistor string monitoring.
        Info contains DIAG_FS2 register value. */
    FW_ERR_SBC_DIAG_FS2_EXTERNAL_IO_1_MONITORING = 35389,

    /** System Basis Chip - Error from ADC driver when reading samples for conversion.
        Info contains ADC driver error code. */
    FW_ERR_SBC_ADC_ERROR = 35390,

    /** System Basis Chip - SBC reset cycle detected.
        Info contains SBC reset counter value. */
    FW_ERR_SBC_RESET_CYCLE_DETECTED = 35391,

    /** System Basis Chip - Error when setting AMUX.
        Info contains IO_OUT_AMUX register value. */
    FW_ERR_SBC_AMUX_ERROR = 35392,

    /** System Basis Chip - IO_01_FS safety input monitoring.
        Info contains INIT_FSSM1 register value. */
    FW_ERR_SBC_INIT_FSSM1_IO_01_MONITORING = 35393,
    /** System Basis Chip - IO_1_FS Second external resistor bridge monitoring not enabled.
        Info contains INIT_FSSM1 register value. */
    FW_ERR_SBC_INIT_FSSM1_RESISTOR_BRIDGE_MONITORING_DISABLED = 35394,
    /** System Basis Chip - IC / External error signals not enabled.
        Info contains INIT_FSSM1 register value. */
    FW_ERR_SBC_INIT_FSSM1_EXT_ERROR_SIGNALS_DISABLED = 35395,

    /** System Basis Chip - Triggered safety switch logic HW reset due undervoltage.
        Info contains the measured millivoltage value over the safety switch i.e. voltage to outputs. */
    FW_ERR_SBC_SS_RESET_IN_SAFETY_PATH_TEST = 35396,
    /** System Basis Chip - Measured supply before Safety switch logic HW is invalid.
        Info contains the measured millivoltage value over the safety switch i.e. voltage to outputs. */
    FW_ERR_SBC_SS_BEFORE_VOLTAGE_SAFETY_PATH_TEST = 35397,
    /** System Basis Chip - Measured voltage over Safety switch logic HW is invalid.
        Info contains the measured millivoltage value over the safety switch i.e. voltage to outputs. */
    FW_ERR_SBC_SS_AFTER_VOLTAGE_SAFETY_PATH_TEST = 35398,
    /** System Basis Chip - Safety path verification retry.
        Info contains the measured millivoltage value over the safety switch i.e. voltage to outputs. */
    FW_ERR_SBC_SAFETY_PATH_VERIFICATION_RETRY = 35399,

    /** System Basis Chip - Vreg1 core feedback.
        Info contains INIT_VREG1 register value. */
    FW_ERR_SBC_INIT_VREG1_CORE_FEEDBACK = 35400,
    /** System Basis Chip - Vreg1 input Power Feed Forward disabled.
        Info contains INIT_VREG1 register value. */
    FW_ERR_SBC_INIT_VREG1_IPFF_DISABLED = 35401,
    /** System Basis Chip - Warning : Voltage detected after safety switch in startup.
        Info contains the measured millivoltage value after the safety switch in startup. */
    FW_ERR_SBC_SS_AFTER_VOLTAGE_IN_STARTUP = 35402,

    /** Value fo SBC VAux is not same as configured in HW */
    FW_ERR_SBC_VAUX_VOLTAGE_HW_CONF_NOT_CORRETCT = 35403,
    /** Value fo SBC VAux is not same as configured in HW */
    FW_ERR_SBC_BUCK_BOOST_HW_CONF_NOT_CORRETCT = 35404,

    /*--------------------------------------------------------------------------
        Self-test Control unit error codes
    --------------------------------------------------------------------------*/

    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MBEH = 35450,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MBEM = 35451,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MBEL = 35452,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_LBEH = 35453,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_LBEL = 35454,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MBSH = 35455,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MBSM = 35456,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MBSL = 35457,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_LBSH = 35458,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_LBSL = 35459,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_LBE = 35460,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_LBS = 35461,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRH0 = 35462,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRH1 = 35463,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRH2 = 35464,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRH3 = 35465,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRH4 = 35466,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRH5 = 35467,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRL0 = 35468,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRL1 = 35469,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRL2 = 35470,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRL3 = 35471,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRL4 = 35472,
    /** Low level error. More information please contact EPEC */
    FW_ERR_STCU2_MISRRL5 = 35473,
    /** STCU2 run state active at boot start. */
    FW_ERR_STCU2_RUN = 35474,
    /** STCU2 selftest execution error. */
    FW_ERR_STCU2_ERROR = 35475,

    /*--------------------------------------------------------------------------
        Safety switch error codes
    --------------------------------------------------------------------------*/

    /**
     * Closing Safety switch (energize outputs) is not possible because of
     * internal error. Internal error detected by firmware de-energizes outputs
     * and safety switch close is not allowed. Power-on Reset is required.
     **/
    FW_ERR_SSWITCH_INTERNAL_ERROR = 35500,
    /**
     * Closing safety switch 1 (energize outputs) is not possible because of
     * initialization or startup diagnostic has been failed or not executed.
     **/
    FW_ERR_SSWITCH_1_STARTUP_NOT_OK = 35501,
    /**
     * Closing safety switch 1 (energize outputs) is not possible because of
     * online diagnostic error.
     **/
    FW_ERR_SSWITCH_1_NOT_OK = 35502,
    /**
     * Closing safety switch 1 (energize outputs) is not possible because this
     * output group has been de-energized after it has been energized.
     * Output energize is possible to only once after power-on.
     **/
    FW_ERR_SSWITCH_1_DE_ENERGIZED = 35503,
     /**
     * Closing safety switch 2 (energize outputs) is not possible because of
     * initialization or startup diagnostic has been failed or not executed.
     **/
    FW_ERR_SSWITCH_2_STARTUP_NOT_OK = 35504,
    /**
     * Closing safety switch 2 (energize outputs) is not possible because of
     * online diagnostic error.
     **/
    FW_ERR_SSWITCH_2_NOT_OK = 35505,
    /**
     * Closing safety switch 2 (energize outputs) is not possible because this
     * output group has been de-energized after it has been energized.
     * Output energize is possible to only once after power-on.
     **/
    FW_ERR_SSWITCH_2_DE_ENERGIZED = 35506,
    /**
     * Safety switch one undervoltage recovery failure. Cannot verify that
     * GPIO state is false.
     */
    FW_ERR_SSWITCH_1_UVR_OFF = 35507,
    /**
     * Safety switch one undervoltage recovery failure. Cannot verify that
     * GPIO state is true.
     */
    FW_ERR_SSWITCH_1_UVR_ON = 35508,
    /**
     * Safety switch two undervoltage recovery failure. Cannot verify that
     * GPIO state is false.
     */
    FW_ERR_SSWITCH_2_UVR_OFF = 35509,
    /**
     * Safety switch one undervoltage recovery failure. Cannot verify that
     * GPIO state is true.
     */
    FW_ERR_SSWITCH_2_UVR_ON = 35510,
    /**
     * Closing Safety switch (energize outputs) is not possible because
     * caller is not in SAFE_CONTEXT. This operation can be called only
     * in safe context.
     */
    FW_ERR_SSWITCH_WRONG_CALLER_CONTEXT = 35511,

    /**
     * Safety switch is tested before outputs are activated, however the
     * supply voltage level is too low.
     */
    FW_ERR_SSWITCH_SUPPLY_LOW = 35512,

    /**
     * SafetySwtich function is called with SafetySwitchNbr enumeration
     * value All, but feature is not supported with this function.
     * Call this function by defining individual switch value.
     */
    FW_ERR_SSWITCH_ALL_NOT_SUPPORTED = 35513,

   /*--------------------------------------------------------------------------
        CmpSystem error codes
    --------------------------------------------------------------------------*/

    /**
     * System component cannot close power switch because IO-Driver state is
     * not RUN state.
     */
    FW_ERR_SYSTEM_IO_DRV_NOT_RUN_STATE = 35600,
    /**
     * System component cannot close power switch because internal diagnostic
     * status is not OK.
     */
    FW_ERR_SYSTEM_DIAGNOSTIC_NOT_OK = 35601,
    /**
     * System compoment power switch manipulation function parameter that
     * indicates power switch number has invalid value. Only values 0,1 and 2
     * are valid.
     */
    FW_ERR_SYSTEM_INVALID_SWITCH_NBR = 35602,
    /**
     * System component power switch manipulation function parameter that
     * indicates wanted power switch state has invalid value. Only 0/1 allowed.
     */
    FW_ERR_SYSTEM_INVALID_STATE = 35603,
    /**
     * System component error code. GetFwLogTail function parameter
     * i_logEntryArray is null
     */
    FW_ERR_SYSTEM_LOG_ENTRY_NULL = 35604,
    /**
     * System component error code. GetFwLog Tail i_Count parameter too high.
     * Maximum tail length is 500 log entries.
     */
    FW_ERR_SYSTEM_TAIL_TOO_LONG = 35605,
    /**
     * System component error code. GetFwLog Tail i_Count parameter is zero.
     * Maximum tail length should be from 1 to  500 log entries.
     */
    FW_ERR_SYSTEM_TAIL_TOO_SHORT = 35606,
    /**
     * System compoment error. GetLastLogEvent - All logs are empty.
     * No log messages in firmware log.
     */
    FW_ERR_SYSTEM_LOG_EMPTY = 35607,
    /**
    * System component error. GetFwLogEvent function id paramter is zero.
    */
    FW_ERR_SYSTEM_LOG_ID_INVALID = 35608,
    /**
     * System compoment error. Cannot find specific log event.
     */
    FW_ERR_SYSTEM_LOG_ID_NOT_FOUND = 35609,

    /** Password has already once tried to unlock */
    FW_ERR_PASSWORD_UNLOCK_RETRY = 35610,

    /*--------------------------------------------------------------------------
        CSE driver error codes
    --------------------------------------------------------------------------*/

    /**
    * CSEDriver True random failure, try again.
    * Random values generated by the TRNG are checked with a statistical test
    * to verify proper operation of the TRNG. If the test fails, a TRNG error
    * (EC = 0x12) is returned. Due to the statistical nature of this test,
    * there is a very small probability (< 10-9) that a properly operating TRNG
    * will return an error. If an TRNG error is returned, the command can be
    * issued again.
    **/
    FW_ERR_CSEDRV_TRNG = 35700,
    /**
     * CSEDriver get true random number internal error. CSE error code will
     * be logged to firmware error log Info field.
     */
    FW_ERR_CSEDRV_GETTRND_INTERNAL = 35701,

    /** CSEDriver Get True Random Number function parameter is NULL */
    FW_ERR_CSEDRV_GETTRDN_NULL_PARAM = 35702,

    /**
     * CSEDriver get true random number error. True random number generator
     * is not initialized.
     */
    FW_ERR_CSEDRV_TRNG_NOT_INITIALIZED = 35703,

    /**
     * CSEDriver initialization function error. True random number generator
     * is not initialized.
     */
    FW_ERR_CSEDRV_INITIALIZATION = 35704,

    /**
     * CSEDriver initialization failed because CSE module is busy and
     * initialization command cannot performed.
     */
    FW_ERR_CSEDRV_INIT_BUSY = 35705,
    /**
     * CSEDriver initilization failure because processing the initialization
     * command takes too long time.
     */
    FW_ERR_CSEDRV_INIT_TIMEOUT = 35706,
    /**
     * CSEDriver Generate true random number command execution takes too long
     * time.
     */
    FW_ERR_CSEDRV_TRNG_TIMEOUT = 35707,
    /**
     * CSEDriver get true random number failure. CSE is busy and new random
     * number generation command cannot performed.
     */
    FW_ERR_CSEDRV_TRNG_BUSY = 35708,

    /*--------------------------------------------------------------------------
        LOG error codes
    --------------------------------------------------------------------------*/

    /** Log handler error no free space in log */
    FW_ERR_LOG_NO_FREE_ENTRY = 35800,
    /** No free instance find in log instance */
    FW_ERR_LOG_NO_FREE_INSTANCE = 35801,
    /** No log instance wiht correct Log Id find */
    FW_ERR_LOG_NO_MATCH_ID_FIND = 35802,
    /** Address definitions for log instance are not valid */
    FW_ERR_LOG_ADDRESS_MISSMATCH = 35803,
    /** Log interface not in correct state */
    FW_ERR_LOG_NO_READY = 35804,
    /** Error in finding free entry for log */
    FW_ERR_LOG_NO_FREE_ENTRY_FIND = 35805,
    /** Instance type is not same as requested */
    FW_ERR_LOG_ENTRY_TYPE_MISSMATCH = 35806,
    /** Log is empty even it is wanted to find entry  */
    FW_ERR_LOG_IS_EMTPY = 35807,
    /** Not a valid log id */
    FW_ERR_NOT_VALID_LOG_ID = 35808,
    /** Requested log id is too big compared logged ids */
    FW_ERR_LOG_NOT_VALID_ENTRY_ID = 35809,

    /*--------------------------------------------------------------------------
        GPIO Driver error codes
    --------------------------------------------------------------------------*/

    /** GPIO state return parameter is null. */
    FW_ERR_GPIO_GET_STATE_NULL_PTR = 35900,
    /** GPIO Get/Set operation for invalid GPIO number. */
    FW_ERR_GPIO_INVALID_NBR = 35901,
    /** GPIO Set verification failed. */
    FW_ERR_GPIO_SET_VERIFICATION = 35902,
    /** GPIO_DRIVER Failed to verify Safety Switch one value that was set. */
    FW_ERR_GPIO_SET_SS1_VERIFICATION = 35903,
    /** GPIO_DRIVER Failed to verify Safety Switch two value that was set. */
    FW_ERR_GPIO_SET_SS2_VERIFICATION = 35904,
    /** GPIO_DRIVER Failed to verify some GPO state when setting all GPOs to off state. */
    FW_ERR_GPIO_OFF_VERIFICATION = 35905,
    /** GPIO Driver failed to verify Testpoint GPO state after setting state. */
    FW_ERR_GPIO_TESTPOINT_VERIFICATION = 35906,
    /** GPIO Driver failed to verify REF 5V Off GPO state after setting state.*/
    FW_ERR_GPIO_5V_REF_VERIFICATION = 35907,
    /** GPIO Driver failed to verify REF 10V Off GPO state after setting state.*/
    FW_ERR_GPIO_10V_REF_VERIFICATION = 35908,
    /** GPIO Driver failed to verify FRAM 1 WP GPO state after setting state.*/
    FW_ERR_GPIO_FRAM1WP_VERIFICATION = 35909,
    /** GPIO Driver failed to verify FRAM 2 WP GPO state after setting state.*/
    FW_ERR_GPIO_FRAM2WP_VERIFICATION = 35910,
    /** GPIO Driver failed to verify EXT ERR ACK state after setting.*/
    FW_ERR_GPIO_EXTERRACK_VERIFICATION = 35911,
    /** GPIO Driver failed to verify EXT ERR OUT state after setting.*/
    FW_ERR_GPIO_EXTERROUT_VERIFICATION = 35912,
    /** GPO configuration lock failed because configuration already locked. */
    FW_ERR_GPIO_CONF_ALREADY_LOCKED = 35913,
    /** GPIO driver function SetCanSTB module parameter is invalid. */
    FW_ERR_GPIO_CAN_MODULE = 35914,
    /** GPIO Driver failed to verify CanSTB GPO state. */
    FW_ERR_GPIO_CANSTB_VERIFICATION = 35915,
    /** GPIO Driver failed to verify Logic OVP shutdown GPO state. */
    FW_ERR_GPIO_LOGIC_OVP_SHDN_VERIFICATION = 35916,
    /** GPIO Driver selected power group index is not supported in this
     * control unit*/
    FW_ERR_GPIO_INVALID_PG_INDEX = 35917,
    /** GPIO Driver selected voltage output index index is not supported in this
     * control unit*/
    FW_ERR_GPIO_INVALID_VOLTAGE_INDEX = 35918,
    /**
     * GPIO Driver, selected ref out voltage index is not supported in this
     * control unit.
     */
    FW_ERR_GPIO_INVALID_REFOUT_INDEX = 35919,
    /**
     * GPIO driver, Sleep function is not supported in this control unit.
     */
    FW_ERR_GPIO_SLEEP_NOT_SUPPORTED = 35920,
    /**
     * GPIO driver, this control unit does not have memory chip with given index.
     */
    FW_ERR_GPIO_INVALID_MEMORY_INDEX = 35921,
    /**
     * Given GPIO number is not valid
     */
    FW_ERR_GPIO_FUNC_NOT_SUPPORTED = 35922,

    /*--------------------------------------------------------------------------
        Ext GPO Driver error codes
    --------------------------------------------------------------------------*/

    /** GPIO state return parameter is null. */
    FW_ERR_GPO_VERIFICATION = 35950,

    /*--------------------------------------------------------------------------
        SIU driver errors codes
    --------------------------------------------------------------------------*/

    /** SIU pad configuration failed, pad state verification error. */
    FW_ERR_SIU_PAD_CONFIGURATION = 36000,
    FW_ERR_SIU_SET_GPIO_INPUT_DISABLED = 36001,
    FW_ERR_SIU_SET_GPIO_VERIFICATION_FAILED = 36002,
    FW_ERR_SIU_SET_GPIO_OUTPUT_DISABLED = 36003,
    FW_ERR_SIU_SET_GPIO_PAD_NOT_GPIO_MODE = 36004,
    FW_ERR_SIU_GET_GPIO_INPUT_DISABLED = 36005,
    FW_ERR_SIU_GET_GPIO_PAD_NOT_GPIO_MODE = 36006,
    FW_ERR_SIU_GET_GPIO_NULL = 36010,
    FW_ERR_SIU_CHECK_GPIO_NUMBER_NOT_VALID = 36011,
    /** SIU PAD is used to control output and pin state is wrong in startup test */
    FW_ERR_SIU_OUTPUT_PIN_START_UP_ERROR = 36012,
    /** 5V reference pin has voltage in startup */
    FW_ERR_5V_REF_START_UP_ERROR = 36013,

    /*--------------------------------------------------------------------------
    CAN message fifo error codes
    --------------------------------------------------------------------------*/

    /** New message was copied. */
    FW_ERR_CANMSGFIFO_NEW_MESSAGE = 36100,
    /** No new messages. */
    FW_ERR_CANMSGFIFO_OVER_EMPTY = 36101,
    /** Fifo overflow. */
    FW_ERR_CANMSGFIFO_OVER_FLOW = 36102,
    /** Can message fifo initializing. */
    FW_ERR_CANMSGFIFO_INITIALIZING = 36103,

    /*--------------------------------------------------------------------------
    Shared memory error codes
    --------------------------------------------------------------------------*/

    /** Shared memory outof memory, reserved size too small */
    FW_ERR_SHM_OUTOF_MEMORY = 36200,
    /** Shared memory block size missmatch */
    FW_ERR_SHM_SIZE_MISSMATCH = 36201,
    /** Shared memory ID error -> corrupted or not initialized */
    FW_ERR_SHM_INIT_OR_ID_ERROR = 36202,


    /*--------------------------------------------------------------------------
        Comm cycle monitoring errors
    --------------------------------------------------------------------------*/

    /** One of the components is not registered comm cycle correctly */
    FW_ERR_COMM_CYCLE_COUNTER_ERROR = 37000,

    /** Invalid component number used when registering comm cycle */
    FW_ERR_COMM_CYCLE_WRONG_CMP_NUMBER = 37001,

    /*--------------------------------------------------------------------------
        System monitor errors
    --------------------------------------------------------------------------*/

    /** No defined vars in debug list */
    FW_ERR_SYS_MON_DBG_NO_DEFINED_VARS = 37200,
    /** No defined vars in debug list */
    FW_ERR_SYS_MON_DBG_TX_DATA_OVERFLoW = 37201,
    /** Not valid address for debugging var  */
    FW_ERR_SYS_MON_DBG_NOT_VALID_ADDRESS = 37202,

    /*--------------------------------------------------------------------------
        Dynamic libraries
    --------------------------------------------------------------------------*/

    /** Function id missmatch */
    FW_ERR_DYN_LIB_ID_MISSMATCH = 37300,
    FW_ERR_DYN_LIB_FUN_PTR_ADDR_INVALID = 37301,
    FW_ERR_DYN_LIB_NOT_INITED = 37302,
    /** Error when checking input parameter size of pointer */
    FW_ERR_DYN_LIB_INPUT_ERROR = 37303,
    /** Error when checking output parameter size of pointer */
    FW_ERR_DYN_LIB_OUTPUT_ERROR = 37304,
    /** Header TAG error */
    FW_ERR_DYN_LIB_INTERFACE_TAG_ERROR = 37305,

    /*--------------------------------------------------------------------------
       Memory handler 37400 ->
    --------------------------------------------------------------------------*/

    /** Not valid memory handler instance */
    FW_ERR_MEM_HANDLER_NOT_VALID_INSTANCE = 37400,
    FW_ERR_MEM_HANDLER_NULL_POINTER = 37401,
    FW_ERR_MEM_HANDLER_INS_ALLREADY_IN_USE = 37402,
    /** Memory area not found */
    FW_ERR_MEM_HANDLER_AREA_NOT_FOUND = 37403,

   /*--------------------------------------------------------------------------
      User management 37500 ->
    --------------------------------------------------------------------------*/

    /** NULL pointer in parameters */
    FW_ERR_USER_MANAGEMENT_NULL_POINTER = 37500,
    /** At least one user/password combination must be defined in image */
    FW_ERR_USER_MANAGEMENT_INIT_IMAGE_SIZE_ERROR = 37501,
    /** User management is already inited */
    FW_ERR_USER_MANAGEMENT_INIT_ALLREADY_DONE = 37502,
    /** User management is already inited */
    FW_ERR_USER_MANAGEMENT_STATIC = 37503,
    /** Encryption not implemented */
    FW_ERR_USER_MANAGEMENT_NO_ENCRYPPTION_SUPPORT = 37504,
    /** Image read size error */
    FW_ERR_USER_MANAGEMENT_IMAGE_READ_SIZE_ERROR = 37505,
    /** Image read TAG error */
    FW_ERR_USER_MANAGEMENT_IMAGE_READ_TAG_ERROR = 37506,
    /** Image read CRC error */
    FW_ERR_USER_MANAGEMENT_IMAGE_READ_CRC_ERROR = 37507,
    /** User number error */
    FW_ERR_USER_MANAGEMENT_USER_COUNT_TOO_HIGH = 37508,
    /** User management not initialised */
    FW_ERR_USER_MANAGEMENT_SYSTEM_NOT_INITIALIZED = 37509,
    /** User not found */
    FW_ERR_USER_MANAGEMENT_USER_NOT_FOUND = 37510,
    /** Not valid user level  */
    FW_ERR_USER_MANAGEMENT_INVALID_USER_LEVEL= 37511,
    /** Password too short */
    FW_ERR_USER_MNGT_PASS_TOO_SHORT= 37512,
    /** Password not match */
    FW_ERR_USER_MNGT_PASS_NOT_MATCH= 37513,
    /** User level invalid */
    FW_ERR_USER_MNGT_USR_LEV_INV= 37514,
    /** User level invalid */
    FW_ERR_USER_MNGT_PASS_MISSMATCH= 37515,

    /*--------------------------------------------------------------------------
      Inertial Measurement Unit 37600 ->
    --------------------------------------------------------------------------*/
    /* SCC433T/SCR410T failed to initialize. */
    FW_ERR_IMU_INITIALIZATION_FAILED = 37600,
    /* Null pointer was provided. */
    FW_ERR_IMU_NULL_POINTER = 37601,
    /* Invalid parameter value was provided. */
    FW_ERR_IMU_INVALID_PARAMETER = 37602,
    /* Sensor has detected saturation. */
    FW_ERR_IMU_SATURATION = 37603,
    /* Sensor reading failed */
    FW_ERR_IMU_READ_FAILED = 37604,

    /*--------------------------------------------------------------------------
      RTOS related error codes, 37700 ->
    --------------------------------------------------------------------------*/
    /* OS detected a safety critical exception. */
    FW_ERR_OS_SAFETY_CRITICAL_EXCEPTION = 37700,
    /* A task has returned from it's loop. */
    FW_ERR_OS_TASK_RETURNED = 37701,
    /* A task has caused an access fault. */
    FW_ERR_OS_TASK_ACCESS_FAULT = 37702,
    /* A task has tried to access a peripheral it has no access to. */
    FW_ERR_OS_TASK_PERIPH_ACCESS_FAULT = 37703,
    /* A tasks stack has under/overflowed. */
    FW_ERR_OS_TASK_STACK_OVERFLOW = 37704,
    /* A tasks Logical Program Flow Monitoring did not match excepted value. */
    FW_ERR_OS_PFM_ERROR = 37720,
    /* A tasks Temporal Program Flow Monitoring did not match expected value. */
    FW_ERR_OS_TBW_ERROR = 37730,

    /*--------------------------------------------------------------------------
      Ethernet related error codes, 37800 ->
    --------------------------------------------------------------------------*/

    FW_ERR_ETH_PHY_INIT = 37800,
    FW_ERR_ETH_MAC_INIT = 37801,

    /** Ethernet transmission has timed out. */
    FW_ERR_ETH_TRANSMISSION_TIMEOUT = 37802,

    /*--------------------------------------------------------------------------
      SENT Driver error codes, 37900 ->
    --------------------------------------------------------------------------*/
    /** SENT Driver is not initialised */
    FW_ERR_SENT_NOT_INIT = 37900,

    /** SENT Driver is already initialised */
    FW_ERR_SENT_ALREADY_INIT = 37901,

    /** SW CRC check failed during SENT message read */
    FW_ERR_SENT_CRC_FAIL = 37902,

    /** SENT Channel Read: Channel index was out of range or invalid */
    FW_ERR_SENT_IDX_OUT_OF_RANGE = 37903,

    /** SENT Channel was not configured for DMA FIFO reading */
    FW_ERR_SENT_FIFO_NOT_CONFIGURED = 37904,

    /** SENT message type input was invalid */
    FW_ERR_SENT_INVALID_MSG_TYPE = 37905,


    /*--------------------------------------------------------------------------
        Boot error codes
    --------------------------------------------------------------------------*/

    /** SIU reset cycle, reset source illegal. */
    FW_ERR_RESET_CYCLE = 40000,
     /** Error in AI driver update. */
    FW_ERR_UPDATE = 40001,
    /** Safe firmware updated ok.*/
    FW_ERR_UPDATED_SAFE = 40002,
    /** Non-safe firmware updated ok.*/
    FW_ERR_UPDATED_NONSAFE = 40003,
    /** eTPU firmware updated ok.*/
    FW_ERR_UPDATED_ETPU = 40004,
    /** Power supply over or under voltage deviation detected. */
    FW_ERR_POWER_SUPPLY_VOLTAGE_DEVIATION = 40005,
    /** Safe firmware update failed. */
    FW_ERR_UPDATE_SAFE_FAIL = 40006,
    /** Safe update image CRC is wrong. */
    FW_ERR_UPDATE_SAFE_IMAGE_CRC = 40007,
    /** Non-safe firmware update failed. */
    FW_ERR_UPDATE_NONSAFE_FAIL = 40008,
    /** Non-safe update image CRC is wrong. */
    FW_ERR_UPDATE_NONSAFE_IMAGE_CRC = 40009,
    /** eTPU firmware update failed. */
    FW_ERR_UPDATE_ETPU_FAIL = 40010,
    /** eTPU update image CRC is wrong. */
    FW_ERR_UPDATE_ETPU_IMAGE_CRC = 40011,
    /** Production data missing or CRC error. */
    FW_ERR_PRODUCTION_DATA = 40012,
    /** MCU revision is not correct. */
    FW_ERR_MCU_REVISION = 40013,
    /** Safe executable image CRC is wrong. */
    FW_ERR_SAFE_EXE_IMAGE_CRC = 40014,
    /** Nonsafe executable image CRC is wrong. */
    FW_ERR_NONSAFE_EXE_IMAGE_CRC = 40015,
    /** eTPU executable image CRC is wrong. */
    FW_ERR_ETPU_EXE_IMAGE_CRC = 40016,
    /** Safe update image flash is incompatible. */
    FW_ERR_UPDATE_SAFE_IMAGE_INCOMPATIBLE = 40017,
    /** Non-safe firmware image flash is incompatible. */
    FW_ERR_UPDATE_NONSAFE_IMAGE_INCOMPATIBLE = 40018,
    /** eTPU update image flash is incompatible. */
    FW_ERR_UPDATE_ETPU_IMAGE_INCOMPATIBLE = 40019,
    /** Error in programming flash. */
    FW_ERR_FLASH_PROGRAM = 40020,
     /** Error when system is erasing flash. */
    FW_ERR_FLASH_ERASE = 40021,
    /** Error flash locks. */
    FW_ERR_FLASH_LOCK = 40022,
    /** CORE0 at wrong state. */
    FW_ERR_CORE0_STATE= 40023,
    /** Safe firmware is same, no update. */
    FW_ERR_UPDATE_SAFE_IMAGE_SAME = 40024,
    /** ETPU firmware is same, no update. */
    FW_ERR_UPDATE_ETPU_IMAGE_SAME = 40025,
    /** Non-Safe firmware is same, no update. */
    FW_ERR_UPDATE_NONSAFE_IMAGE_SAME = 40026,
    /** UDS mode activated. */
    FW_ERR_UDS_MODE = 40027,
    /** UDS binary invalid. */
    FW_ERR_UDS_INVALID = 40028,

    /*--------------------------------------------------------------------------
        Range for errors that are system exceptions,
        failures and other that can cause system reset cycles.
    --------------------------------------------------------------------------*/

    /** Exception detected.
        Info contains the instruction address value or exception code. */
    FW_ERR_DIAG_EXCEPTION_HANDLER = 57005,

    /** System has experienced a reset in the previous execution and has restarted from the reset. */
    FW_ERR_DIAG_SYSTEM_RESET = 57006,

    /** SysExceptMPC57xx has detected exception.
        Info contains the instruction address value in the exception handler. */
    FW_ERR_DIAG_SYSTEM_EXCEPTION_HANDLER = 57007,

    /** 3S runtime exception detected.
        Info contains the exception code. */
    FW_ERR_DIAG_EXCEPTION_CODE = 57008,

    /** Application startup failed when 3S runtime started the application. */
    FW_ERR_RUNTIME_INIT_FAIL = 57009,

    /** Diagnostic forces safe state when set. */
    FW_ERR_CRITICAL = 57010,

    /** Low level error. Contact EPEC for more information.
        GHS runtime check code */
    FW_ERR_GHS_RUNTIME_CHECK_CODE = 57011,

    /** Low level error. Contact EPEC for more information.
        GHS runtime check address. */
    FW_ERR_GHS_RUNTIME_CHECK_ADDRESS = 57012,

    /** Low level error. Contact EPEC for more information.
        GHS runtime check line. */
    FW_ERR_GHS_RUNTIME_CHECK_LINE = 57013,

    /** Memory Protection Unit exception leading into reset.
        Error Detail Register for MPU 0 slave port 0. */
    FW_ERR_MPU0_EDR0 = 57014,
        /** Memory Protection Unit exception leading into reset.
        Error Address Register for MPU 0 slave port 0. */
    FW_ERR_MPU0_EAR0 = 57015,
    /** Memory Protection Unit exception leading into reset.
        Error Detail Register for MPU 0 slave port 1. */
    FW_ERR_MPU0_EDR1 = 57016,
        /** Memory Protection Unit exception leading into reset.
        Error Address Register for MPU 0 slave port 1. */
    FW_ERR_MPU0_EAR1 = 57017,
    /** Memory Protection Unit exception leading into reset.
        Error Detail Register for MPU 0 slave port 2. */
    FW_ERR_MPU0_EDR2 = 57018,
        /** Memory Protection Unit exception leading into reset.
        Error Address Register for MPU 0 slave port 2. */
    FW_ERR_MPU0_EAR2 = 57019,
    /** Memory Protection Unit exception leading into reset.
        Error Detail Register for MPU 1 slave port 1. */
    FW_ERR_MPU1_EDR1 = 57020,
        /** Memory Protection Unit exception leading into reset.
        Error Address Register for MPU 1 slave port 1. */
    FW_ERR_MPU1_EAR1 = 57021,
    /** Memory Protection Unit exception leading into reset.
        Error Detail Register for MPU 1 slave port 2. */
    FW_ERR_MPU1_EDR2 = 57022,
    /** Memory Protection Unit exception leading into reset.
        Error Address Register for MPU 1 slave port 2. */
    FW_ERR_MPU1_EAR2 = 57023,
    /** Memory Protection Unit was disabled during runtime.
        Info contains the number of the MPU unit that was disabled.*/
    FW_ERR_MPU_RUNTIME_DISABLED = 57024,
    /** SysExceptMPC57xx has detected exception.
        Info contains the return address value in the exception handler i.e.
        function/address which possibly caused the exception to occur.
        This error provides additional information with other exception errors.
        Address can be in application or in firmware.
        Address can be related to
        - floating point calculation exception,
        - memory access violation,
        - memory protection error etc. */
    FW_ERR_DIAG_SYSTEM_EXCEPTION_HANDLER_RETURN_IP = 57025,

    /*--------------------------------------------------------------------------
        Range for errors that relate to 3S runtime application requirements.
    --------------------------------------------------------------------------*/

    /** Firmware has detected a reset cycle and evaluated possible reset reason.
        The info field indicates possible reset source (MCU, FW, application...). */
    FW_ERR_RESET_REASON = 57030,

    /** Firmware has forced a sleep request. */
    FW_RESET_ERROR_SLEEP_REQ = 57031,

    /** Firmware has detected unexpected wakeup signals while sleep should be activated.
        The info field contains bit mask of KL15, RTC and Charger wakeup signals. */
    FW_ERR_KL15_OR_CHG_ACTIVE_BEFORE_SLEEP = 57032,

    /** Firmware has cleared RTC wakeup interrupt and configured new wakeup time. */
    FW_ERR_CLEAR_RTC_BEFORE_SLEEP = 57033,

    /** Firmware has cleared RTC wakeup interrupt and configured new wakeup time.
        The info field indicates error code from RTC handling. */
    FW_ERR_RTC_FAILURE_BEFORE_SLEEP = 57034,

    /*--------------------------------------------------------------------------
        Range for errors that relate to 3S runtime control and application loading.
    --------------------------------------------------------------------------*/

    /** 3S runtime debug mode has been activated.
        Indication when the debug mode has been activated for example to load a new application. */
    FW_ERR_RUNTIME_DEBUG_MODE = 57100,

    /** 3S runtime application download event.
        Indication when the application download has been started. */
    FW_ERR_RUNTIME_NEW_APP_LOADING = 57101,

    /** 3S runtime errors when exiting runtime application(s). */
    FW_ERR_RUNTIME_APP_EXIT = 57102,

    /*--------------------------------------------------------------------------
        SBC FS8x
    --------------------------------------------------------------------------*/

    /** Failure during FS8x init function.
     * Info field contains first error code during init. */
    FW_ERR_FS8X_INIT_FAILURE = 57200,

    /** SBC reset cycle detected.
    Info contains SBC reset counter value stored in MEMORY1. */
    FW_ERR_FS8X_RESET_CYCLE_DETECTED = 57201,

    /* FS8X SPI SCLK error detection */
    FW_ERR_FS8X_SPI_FS_CLK = 57202,

    /* FS8X Invalid fail-safe SPI access */
    FW_ERR_FS8X_SPI_FS_REQ = 57203,

    /* FS8X Fail-safe SPI communication CRC issue */
    FW_ERR_FS8X_SPI_FS_CRC = 57204,

    /* FS8X Fail-safe I2C communication CRC issue */
    FW_ERR_FS8X_I2C_FS_CRC = 57205,

    /* FS8X Invalid fail-safe I2C access */
    FW_ERR_FS8X_I2C_FS_REQ = 57206,

    /* FS8X Main domain SPI SCLK error detection */
    FW_ERR_FS8X_SPI_M_CLK = 57207,

    /* FS8X Invalid main domain SPI access */
    FW_ERR_FS8X_SPI_M_REQ = 57208,

    /* FS8X Main domain SPI communication CRC issue */
    FW_ERR_FS8X_SPI_M_CRC = 57209,

    /* FS8X Main domain I2C communication CRC issue */
    FW_ERR_FS8X_I2C_M_CRC = 57210,

    /* FS8X Invalid main domain I2C access */
    FW_ERR_FS8X_I2C_M_REQ = 57211,

    /** FS8X Bad WD refresh, error in the DATA */
    FW_ERR_FS8X_BAD_WD_DATA = 57212,

    /** FS8X Bad WD refresh, wrong window or in timeout */
    FW_ERR_FS8X_BAD_WD_TIMING = 57213,

    /** Report OTP bit corruption detection or INIT register corruption detection.
    Info contains FS_STATES register value. */
    FW_ERR_FS8X_DATA_CORRUPT = 57214,

    /** SPI read register operation failure.
    Info contains address that was tried to read. */
    FW_ERR_FS8X_SPI_READ = 57215,

    /** SPI write register operation failure.
    Info contains address that was tried to write. */
    FW_ERR_FS8X_SPI_WRITE = 57216,

    /** FS8x debug mode active. Info contains FS_STATES register value. */
    FW_ERR_FS8X_DEBUG_MODE = 57217,

    /** FS8X Error from ADC driver when reading samples for conversion.
        Info contains ADC driver error code. */
    FW_ERR_FS8X_ADC_ERROR = 57218,

    /** Amux channel switch error. Info contains measurement array index
    that caused the error. */
    FW_ERR_FS8X_AMUX = 57219,

    /** Test write error during init */
    FW_ERR_FS8X_TEST_WRITE = 57220,

    /** Error in watchdog refresh function */
    FW_ERR_FS8X_WD_REFRESH = 57221,

    /** Error during init watchdog startup refresh sequence */
    FW_ERR_FS8X_WD_INIT_SEQUENCE = 57222,

    /** FS8X RSTB requested */
    FW_ERR_FS8X_RSTB_REQ = 57223,

    /** FS8X FS0B release request failure. Info contains error counter value. */
    FW_ERR_FS8X_FS0B_REL_FAIL = 57224,

    /** FS8X VPRE_FB_OV event */
    FW_ERR_FS8X_VPRE_FB_OV = 57225,

    /** FS8X VSUP_UV7 event */
    FW_ERR_FS8X_VSUP_UV7 = 57226,

    /** FS8X VPREUVL event */
    FW_ERR_FS8X_VPREUVL = 57227,

    /** FS8X VPREUVH event */
    FW_ERR_FS8X_VPREUVH = 57228,

    /** FS8X VSUPUVL event */
    FW_ERR_FS8X_VSUPUVL = 57229,

    /** FS8X VSUPUVH event */
    FW_ERR_FS8X_VSUPUVH = 57230,

    /** FS8X FCCU12, FCCU1 or FCCU2 error. Info contains FS_DIAG_SAFETY register value. */
    FW_ERR_FS8X_FCCU = 57231,

    /** FS8X error in the ERRMON input. Info contains FS_DIAG_SAFETY register value. */
    FW_ERR_FS8X_ERRMON = 57232,

    /** FS8X Analog BIST1 FAIL. Info contains FS_DIAG_SAFETY register value. */
    FW_ERR_FS8X_ABIST1 = 57233,

    /** FS8X Analog BIST2 FAIL. Info contains FS_DIAG_SAFETY register value. */
    FW_ERR_FS8X_ABIST2 = 57234,

    /** FS8X Logical BIST FAIL. Info contains FS_DIAG_SAFETY register value. */
    FW_ERR_FS8X_LBIST = 57235,

    /** FS8X general purpose error for debugging */
    FW_ERR_FS8X_DEBUG = 57236,

    /** FS8X PGOOD pad sensed low. Info contains FS_SAFE_IOS register value. */
    FW_ERR_FS8X_PGOOD_SNS_LOW = 57237,

    /** FS8X PGOOD short to high */
    FW_ERR_FS8X_PGOOD_DIAG = 57238,

    /** FS8X RSTB short to high */
    FW_ERR_FS8X_RSTB_DIAG = 57239,

    /** FS8X Failure on FS0B */
    FW_ERR_FS8X_FS0B_DIAG = 57240,

    /** FS8X Overvoltage reported on VCOREMON */
    FW_ERR_FS8X_VCOREMON_OV = 57241,

    /** FS8X Undervoltage reported on VCOREMON */
    FW_ERR_FS8X_VCOREMON_UV = 57242,

    /** FS8X Overvoltage reported on VDDIO */
    FW_ERR_FS8X_VDDIO_OV = 57243,

    /** FS8X Undervoltage reported on VDDIO */
    FW_ERR_FS8X_VDDIO_UV = 57244,

    /** FS8X Overvoltage reported on VMON4 */
    FW_ERR_FS8X_VMON4_OV = 57245,

    /** FS8X Undervoltage reported on VMON4 */
    FW_ERR_FS8X_VMON4_UV = 57246,

    /** FS8X Overvoltage reported on VMON3 */
    FW_ERR_FS8X_VMON3_OV = 57247,

    /** FS8X Undervoltage reported on VMON3 */
    FW_ERR_FS8X_VMON3_UV = 57248,

    /** FS8X Overvoltage reported on VMON2 */
    FW_ERR_FS8X_VMON2_OV = 57249,

    /** FS8X Undervoltage reported on VMON2 */
    FW_ERR_FS8X_VMON2_UV = 57250,

    /** FS8X Overvoltage reported on VMON1 */
    FW_ERR_FS8X_VMON1_OV = 57251,

    /** FS8X Undervoltage reported on VMON1 */
    FW_ERR_FS8X_VMON1_UV = 57252,

    /** FS8X Digital fail-safe reference overvoltage */
    FW_ERR_FS8X_FS_DIG_REF_OV = 57253,

    /** FS8X Drift of the fail-safe OSC */
    FW_ERR_FS8X_FS_OSC_DRIFT = 57254,

    /** FS8X VBOS undervoltage high event */
    FW_ERR_FS8X_VBOSUVH = 57255,

    /** FS8X VBOOST undervoltage high event */
    FW_ERR_FS8X_VBOOSTUVH = 57256,

    /** FS8X VPRE overcurrent event */
    FW_ERR_FS8X_VPREOC = 57257,

    /** FS8X BUCK1 overcurrent event */
    FW_ERR_FS8X_BUCK1OC = 57258,

    /** FS8X BUCK2 overcurrent event */
    FW_ERR_FS8X_BUCK2OC = 57259,

    /** FS8X BUCK3 overcurrent */
    FW_ERR_FS8X_BUCK3OC = 57260,

    /** FS8X LDO1 overcurrent */
    FW_ERR_FS8X_LDO1OC = 57261,

    /** FS8X LDO2 overcurrent */
    FW_ERR_FS8X_LDO2OC = 57262,

    /** FS8X CLK_FIN_DIV monitoring */
    FW_ERR_FS8X_CLK_FIN_DIV = 57263,

    /** FS8X VBOOST overvoltage protection event */
    FW_ERR_FS8X_VBOOSTOV = 57264,

    /** FS8X VBOOST overtemperature shutdown event */
    FW_ERR_FS8X_VBOOSTOT = 57265,

    /** FS8X BUCK1 overtemperature shutdown event */
    FW_ERR_FS8X_BUCK1OT = 57266,

    /** FS8X BUCK2 overtemperature shutdown event */
    FW_ERR_FS8X_BUCK2OT = 57267,

    /** FS8X BUCK3 overtemperature shutdown event */
    FW_ERR_FS8X_BUCK3OT = 57268,

    /** FS8X LDO1 overtemperature shutdown event */
    FW_ERR_FS8X_LDO1OT = 57269,

    /** FS8X LDO2 overtemperature shutdown event */
    FW_ERR_FS8X_LDO2OT = 57270,

    /** FS8X ERRMON test failed. ERRMON_STATUS did not update as expected. Info:
     * 0=ERRMON pin initial value high. 1=ERRMON pin level did not change.
     * >1=SPI error code. */
    FW_ERR_FS8X_ERRMON_TEST = 57271,

    /** FS8X FS0B test failed. FS0B status did not update as expected. Info:
     * 0=SNS initially high. 1=FS0B release fail. 2=SNS low after release.
     * 3=FS0B req fail. >3=SPI error code. */
    FW_ERR_FS8X_FS0B_TEST = 57272,

    /** FS8X RSTB request failed. MCU reset requested. */
    FW_ERR_FS8X_MCU_RESET_AFTER_RSTB_FAIL = 57273,

    /** FS8X interrupt test failed. Info: 0=INT handler not called.
     * >0 SPI operation error code. */
    FW_ERR_FS8X_INTB_TEST_FAIL = 57274,

    /** FS8X safe reaction register1 read back failure.
     * Info: Read register value. */
    FW_ERR_SAFEREACTION1_FAIL = 57275,

    /** FS8X safe reaction register2 read back failure.
     * Info: Read register value. */
    FW_ERR_SAFEREACTION2_FAIL = 57276,

    /*--------------------------------------------------------------------------
        Reference outputs
    --------------------------------------------------------------------------*/

    /** Ref out switch init failure. Info contains detailed error code. */
    FW_ERR_REF_SWITCH_INIT = 57300,

    /** Ref out init failure. Info contains detailed error code. */
    FW_ERR_REF_OUT_INIT = 57301,

    /** External voltage in at least one reference output measurement
    when setting reference output switch control on */
    FW_ERR_REF_SWITCH_EXTERNAL_VOLTAGE = 57302,

    /** External voltage detected in refout pin. Info: ref out id (bits 20-23),
    measurement id (bits 16-19), measurement value in mV (bits 0-15). */
    FW_ERR_REF_OUT_EXTERNAL_VOLTAGE = 57303,

    /** Shortcut detected in refout pin. Info: ref out id (bits 20-23),
    measurement id (bits 16-19), measurement value in mV (bits 0-15). */
    FW_ERR_REF_OUT_SHORTCUT = 57304,

    /** Overvoltage detected in refout pin. Info: ref out id (bits 20-23),
    measurement id (bits 16-19), measurement value in mV (bits 0-15). */
    FW_ERR_REF_OUT_OVERVOLTAGE = 57305,

    /** Overvoltage detected in refout pin and refout control is off. Info: ref out id
    (bits 20-23), measurement id (bits 16-19), measurement value in mV (bits 0-15). */
    FW_ERR_REF_OUT_PERSISTING_OVERVOLTAGE = 57306,

    /** Redundant measurement mismatch. Info contains lowest 16 bits
    of both measurements m1|m0 in mV. */
    FW_ERR_REF_OUT_MEASUREMENT_MISMATCH = 57307,

    /** Supply voltage under reference output specific limit. Info: ref out id
     * (bits 20-23), supply voltage in mV (bits 0-15). */
    FW_ERR_REF_OUT_SUPPLY_UNDERVOLTAGE = 57308,

    /** Supply voltage over reference output specific limit. Info: ref out id
     * (bits 20-23), supply voltage in mV (bits 0-15). */
    FW_ERR_REF_OUT_SUPPLY_OVERVOLTAGE = 57309,

    /** Reference output retry max count exceeded. */
    FW_ERR_REF_OUT_RETRY_COUNT = 57310,

    /** Reference output cooling time not elapsed. */
    FW_ERR_REF_OUT_COOLING = 57311,

    /** Invalid reference output id. */
    FW_ERR_REF_OUT_INVALID_ID = 57312,

    /** Requested reference output id not found in data structures. */
    FW_ERR_REF_OUT_ID_NOT_FOUND = 57313,

    /*--------------------------------------------------------------------------
        Cable detection
    --------------------------------------------------------------------------*/

    /** Reading cable detection parameters failed */
    FW_ERR_CD_PARAM_READ_FAILED = 57350,

    /** Cable detection indicates invalid BSL voltage */
    FW_ERR_CD_INVALID_VOLTAGE = 57351,

    /** Cable detection monitoring indicates invalid BSL voltage */
    FW_ERR_CD_MONITORING = 57352,

    /** Cable detection detects invalid reference voltage */
    FW_ERR_CD_INVALID_REF_VOLTAGE = 57353,

    /*--------------------------------------------------------------------------
        Measurement monitor
    --------------------------------------------------------------------------*/

    /** Generic measurement monitor low error. Info bits 0-23 measurement value,
    bits 24-31 measurement id. */
    FW_ERR_MEAS_MONITOR_LOW = 57370,

    /** Generic measurement monitor high error. Info bits 0-23 measurement value,
    bits 24-31 measurement id. */
    FW_ERR_MEAS_MONITOR_HIGH = 57371,

    /** 5V_2 voltage out of allowed range. Info contains measurement value. */
    FW_ERR_MEAS_5V_2_VOLTAGE = 57372,

    /** VBAT_3V3 voltage out of allowed range. Info contains measurement value. */
    FW_ERR_MEAS_VBAT_3V3_VOLTAGE = 57373,

    /* 5V_2-LDO2 voltage out of range. Info contains signed difference. */
    FW_ERR_MEAS_5V_2_DIFF_AMUX_LDO2 = 57374,

    /*--------------------------------------------------------------------------
        HS/LS pin shortcut prevention
    --------------------------------------------------------------------------*/

    /** An attempt was made to activate both the HS and the LS channels of a
    single pin which would lead to shortcut. */
    FW_ERR_HSLS_INVALID_STATE = 57400,

    /*--------------------------------------------------------------------------
        FwCmd
    --------------------------------------------------------------------------*/

    /** Invalid cmd id  */
    FW_ERR_FW_CMD_ID = 57500,

    /** Invalid parameter provided */
    FW_ERR_FW_CMD_PARAM = 57501,

    /** Invalid parameter alignment */
    FW_ERR_FW_CMD_PARAM_ALIGN = 57502,

    /** Invalid cmd  */
    FW_ERR_FW_CMD_INV = 57503,

    /** FwCmd internal error */
    FW_ERR_FW_CMD_INT = 57504,

    FW_ERR_MAX = 0x4000FFFF

 } Err_t;

#endif  /* FW_ERROR_H */
