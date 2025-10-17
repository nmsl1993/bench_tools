#! /usr/bin/python3
import pps2320a
import math
VOLTAGE_SETPOINT = 5.1
CURRENT_SETPOINT = 1.0
VOLTAGE_TOLERANCE = 0.11
CURRENT_TOLERANCE = 0.02
ps = pps2320a.pps()
ps.output(False)

ps.voltage(VOLTAGE_SETPOINT, channel=1)
voltage_readback = ps.voltage(channel=1)
pps2320a.logging.info(f'voltage setpoint: {VOLTAGE_SETPOINT}, voltage_readback: {voltage_readback}')
assert math.isclose(a=VOLTAGE_SETPOINT, b=voltage_readback, rel_tol=0, abs_tol=VOLTAGE_TOLERANCE)
ps.current(1.0, channel=1)
current_readback = ps.current(channel=1)
pps2320a.logging.info(f'current setpoint: {CURRENT_SETPOINT}, current_readback: {current_readback}')
assert math.isclose(a=CURRENT_SETPOINT, b=current_readback, rel_tol=0, abs_tol=CURRENT_TOLERANCE)
ps.output(True)
