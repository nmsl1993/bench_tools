#! /usr/bin/python3
import pps2320a

ps = pps2320a.pps()
ps.output(False)
ps.voltage(5.1, channel=1)
ps.current(1.0, channel=1)
ps.output(True)
