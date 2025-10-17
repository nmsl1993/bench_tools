import serial
from serial.tools import list_ports
import time
import logging
import sys
from retrying import retry

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class pps(object):

    @staticmethod
    def check_ok(s):
        """
        For whatever reason, PSU sometimes sends back "k\no" instead of "ok\n"
        """
        if (len(s) <= 4) and 'k' in s and 'o' in s:
            return True
        return False

    def __init__(self, port = None):

        # Automatically detect serial port
        
        if port == None:
            candidate_ports = []
            logging.info('Automatically Detecting Port...')
            comports = list_ports.comports()
            candidate_ports = [cp for cp in comports if 'CP210' in cp.description]
            if len(candidate_ports) == 0:
                raise RuntimeError(f'Could not find a CP210x driver among {comports}')
            elif len(candidate_ports) == 1:
                port = candidate_ports[0].device
            else:
                raise RuntimeError(f'Multiple CP210x drivers found... please specify among {comports}')
        logging.info('Initializing Serial Port')
        if port == None:
            logging.info('Could not identify com Port')
        self.ser = serial.Serial(port, baudrate = 9600, timeout = 0.2)
        logging.info('Done.')
    

    def send_command(self, command, bytes_to_read = 3):
        '''
        '''

        if command[-1] != '\n':
            command += '\n'

        self.ser.write(command.encode('utf-8'))

        data = self.ser.read(bytes_to_read).decode('utf-8')

        return data

    @retry(stop_max_attempt_number=3)
    def voltage(self, value = None, channel = 1):
        ''' Set power supply voltage

            Args:
                value (int, float): Voltage value to set in volts
                channel (int): Power supply channel to set

            Returns:
                data (float): If value is None, power supply voltage in volts
        '''

        if channel not in (1,2):
            raise ValueError('Channel not valid')

        if value is not None:
            if channel == 1:
                command = 'su'
            elif channel == 2:
                command = 'sa'
        else:
            if channel == 1:
                command = 'ru'
            elif channel == 2:
                command = 'rk'

        if value is not None:
            value = int(value * 100)
            if (value > 3200) or (value < 0):
                raise ValueError('Value out of range')

            command += '%04i'%value

        data = self.send_command(command)

        if value is not None:
            if not self.check_ok(data):
                raise ValueError('Communication fail')

        else:
            output = float(data.strip())/100.
            return output

    @retry(stop_max_attempt_number=3)
    def current(self, value = None, channel = 1):
        ''' Set power supply voltage

            Args:
                value (int, float): Voltage value to set in volts
                channel (int): Power supply channel to set
                
            Returns:
                data (float): If value is None, returns power supply current value in Amps

        '''

        if channel not in (1,2): #NOTE FIX this
            raise ValueError('channel %s not valid'%str(channel))

        if value is not None:
            if channel == 1:
                command = 'si'
            elif channel == 2:
                command = 'sd'
        else:
            if channel == 1:
                command = 'ri'
            elif channel == 2:
                command = 'rq'

        if value is not None:
            value = int(value * 1000)
            if (value > 3100) or (value < 0):
                raise ValueError('Value out of range')

            command += '%04i'%value

        data = self.send_command(command)

        if value is not None:
            if not self.check_ok(data):
                raise ValueError('Communication fail')

        else:
            output = float(data.strip())/1000.
            return output

    @retry(stop_max_attempt_number=3)
    def output(self, enabled):
        ''' Enable or disable power supply output

            enable (bool): True to enable, False to disable
        '''

        if enabled:
            data = self.send_command('o1')
        else:
            data = self.send_command('o0')

        logging.info(data)
        logging.info(len(data))
        if not self.check_ok(data):
            raise ValueError('Communication fail')

