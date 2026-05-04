"""
Real-Time Sequence Library
=================

A Robot Framework library for running real-time sequences in National Instruments VeriStand.
"""
from niveristand import run_py_as_rtseq, nivs_rt_sequence, NivsParam
from niveristand.clientapi import ChannelReference, DoubleValue, I64Value
from niveristand.library import wait_until_next_ms_multiple, ramp, square_wave
from robot.api import logger as robot_logger


@NivsParam("ramp_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("init_value", DoubleValue(0), NivsParam.BY_VALUE)
@NivsParam("final_value", DoubleValue(0), NivsParam.BY_VALUE)
@NivsParam("step_value", DoubleValue(0), NivsParam.BY_VALUE)
@NivsParam("step_duration_ms", I64Value(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def step_ramp(ramp_out, init_value, final_value, step_value, step_duration_ms):
    """Basic step-ramp function. Changes channel value from initial value to final value by defined steps.

    Args:
        - `ramp_out`: Channel reference to which the value is written
        - `init_value`: Initial start value for steps
        - `final_value`: Final value for steps to stop
        - `step_value`: Value of each step
        - `step_duration_ms`: Waits defined amount of time before next step in milliseconds
    """
    current_value = DoubleValue(0)
    current_value.value = init_value.value

    while current_value.value <= final_value.value:
        ramp_out.value = current_value.value
        wait_until_next_ms_multiple(step_duration_ms)
        current_value.value = current_value.value + step_value.value


class real_time_sequences:
    """Robot Framework library for wrapping NI VeriStand Real-Time Sequences.
    https://niveristand-python.readthedocs.io/en/v3.1.0/basic_rt_sequence_examples.html
    """

    ROBOT_LIBRARY_SCOPE: str = 'GLOBAL'

    def ramp(self, ramp_out_ch: str, *, init_value: DoubleValue,
             final_value: DoubleValue, duration: DoubleValue) -> int:
        """Basic ramp function. Changes channel value from initial value to final value.

        Calls NI VeriStand library function called 'ramp'.

        Args:
        - `ramp_out`: Channel reference to which the value is written
        - `init_value`: Initial start value for steps
        - `final_value`: Final value for steps to stop
        - `duration`: Time, in seconds, the ramp to take.
        """
        rt_seq_params = {
            'ramp_out': ChannelReference(ramp_out_ch),
            'init_value': DoubleValue(init_value),
            'final_value': DoubleValue(final_value),
            'duration': DoubleValue(duration)
        }
        robot_logger.info("Call Real-time sequence")
        run_py_as_rtseq(ramp, rtseq_params=rt_seq_params)
        robot_logger.info("Real-time sequence executed")
        return 0

    def step_ramp(self, ramp_out_ch: str, *, init_value: DoubleValue,
                  final_value: DoubleValue, step_value: DoubleValue, step_duration: DoubleValue) -> int:
        """Basic step-ramp function. Changes channel value from initial value to final value by defined steps.

        Args:
        - `ramp_out`: Channel reference to which the value is written
        - `init_value`: Initial start value for steps
        - `final_value`: Final value for steps to stop
        - `step_value`: Value of each step
        - `step_duration`: Waits defined amount of time before next step in seconds
        """
        step_duration_ms = I64Value(step_duration*1000)
        rt_seq_params = {
            'ramp_out': ChannelReference(ramp_out_ch),
            'init_value': DoubleValue(init_value),
            'final_value': DoubleValue(final_value),
            'step_value': DoubleValue(step_value),
            'step_duration_ms': I64Value(step_duration_ms)
        }
        robot_logger.info("Call Real-time sequence")
        run_py_as_rtseq(step_ramp, rtseq_params=rt_seq_params)
        robot_logger.info("Real-time sequence executed")
        return 0

    def square_wave(self, wave_out_ch: str, *, amplitude: DoubleValue,
                    freq: DoubleValue, phase: DoubleValue, bias: DoubleValue, duty_cycle: DoubleValue, duration: DoubleValue) -> int:
        """Basic square wave function. Plays a square wave with the parameters specified.

        Args:
        - `wave_out`: Variable onto which the square wave plays.
        - `amplitude`: Amplitude of the square wave.
        - `freq`: Frequency, in Hz, of the square wave.
        - `phase`: Phase, in degrees, of the square wave.
        - `bias`: Offset to add to the square wave.
        - `duty_cycle`: Percentage of time the square wave remains high versus low over one period.
        - `duration`: Time, in seconds, to play the square wave.
        """
        rt_seq_params = {
            'wave_out': ChannelReference(wave_out_ch),
            'amplitude': DoubleValue(amplitude),
            'freq': DoubleValue(freq),
            'phase': DoubleValue(phase),
            'bias': DoubleValue(bias),
            'duty_cycle': DoubleValue(duty_cycle),
            'duration': DoubleValue(duration)
        }
        robot_logger.info("Call Real-time sequence")
        run_py_as_rtseq(square_wave, rtseq_params=rt_seq_params)
        robot_logger.info("Real-time sequence executed")
        return 0
