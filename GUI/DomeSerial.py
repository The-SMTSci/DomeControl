#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# /home/git/external/DomeControl/GUI/DomeSerial.py
#
# (wg-astroconda-pdb)
# (wg-python-fix-pdbrc)
#
#
# (compile (format "python -m py_compile %s" (buffer-file-name)))
# (compile (format "pydoc3 %s" (buffer-file-name)))
#
#############################################################################
### HEREHEREHERE

import os
import optparse
import sys
import re
from enum import Enum                                     # fancy state tracking

# to handle the Unicode filenames from Win1X
_encoding = 'utf-8'                         # deal with nt's UTF issues.
if(os.name == 'nt'):
    _encoding = 'utf-16'
# with io.open(listname,'r',encoding=_encoding) as f:

# (wg-python-types)
#############################################################################
#
#
#  /home/git/external/DomeControl/GUI/DomeSerial.py
# (wg-python-emacs-help)
#
# (wg-python-toc)
#
#
#############################################################################

__doc__ = """

/home/git/external/DomeControl/GUI/DomeSerial.py
[options] files...

WinX  windows manager

Linux   lsusb for 

"""

##############################################################################
# DomeSerialException
#
##############################################################################
class DomeSerialException(Exception):
    """Special exception to allow differentiated capture of exceptions"""
    def __init__(self,message,errors=None):
        super(DomeSerialException,self).__init__("DomeSerial "+ message)
        self.errors = errors
    @staticmethod
    def __format__(e):
        return f" DomeSerial: {e.__str__()}\n"
# DomeSerialException

##############################################################################
# DomeSerial
#
##############################################################################
class DomeSerial(object):
    """ A serial interface with the DomeController.
    """
    #__slots__ = [''] # add legal instance variables
    # (setq properties `("" ""))

    # DomeSerialState has  rich meaning for messages.
    comstate = Enum('DomeSerialState',['INDETERMINATE','OPEN','CLOSED'])

    def __init__(self,portrequirements):                  # DomeSerial::__init__()
        """portrequirements json string with:
        port          - platform dependent /dev/ COM... etc.
        bits          - string with integer number of bits default 8
        baud          - string with the integer baud rate
        start         - string with the startbits (may appear floating)
        stop          - string with the stopbits  (may appear floating)
        parity        - Parity default None
        {"port" : "" , "bits" : "" , "baud" : "" , "start" : "" , "stop" : "" , "parity" : "" }

        PySide6 QSerialPort
        baudRate          - The data baud rate for the desired direction
        dataBits          - The data bits in a frame
        parity            - The parity checking mode
        breakEnabled      - The state of the transmission line in break
        stopBits          - The number of stop bits in a frame
                          
        dataTerminalReady - The state (high or low) of the line signal DTR
        error             - The error status of the serial port
        flowControl       - The desired flow control mode
        requestToSend     - The state (high or low) of the line signal RTS
        
        Use QSerialPort in asynchronous mode: The pacing is controlled by the
        main control loop.

Related stuff
Socket read/write using QThread
https://forum.qt.io/topic/155413/socket-and-serial-read-and-write-using-qthread





        """
        #super().__init__()
        # (wg-python-property-variables)

        self.port       = portrequirements["port"]
        self.baudrate   = portrequirements["bits"]

        self.connection = None

        self.msg        = ""                              # messages as needed
        self.validp     = False                           # Not opened yet.
        self.state      = DomeSerial.comstate.OPEN        # The state of affairs.

    ### DomeSerial.__init__()

    def open(self):                                       # DomeSerial.open()
        """Connect to the port.
        serial.serialutil.SerialException will be raised if the connection is dropped."""
        try:
            self.connection = serial.Serial(self.port, self.baudrate)
            if(self.connection == None):
                self.validp = False
            else:
                self.validp = True
        except Exception as e:
            self.msg += f" : {e.__str__()}"

    ### DomeSerial.open()

    def read():                                           # DomeSerial.read()
        """read some data if available"""
        pass
    ### DomeSerial.read()

    def write():                                          # DomeSerial.write()
        """write data to the device"""
        pass
    ### DomeSerial.write()

    def close():                                          # DomeSerial.close()
        """close the device connection"""
        pass
    ### DomeSerial.close()

    def status():                                         # DomeSerial.status()
        """status return string with status."""
        pass
    ### DomeSerial.status()

    def debug(self,msg="",skip=[],os=sys.stderr):           # DomeSerial::debug()
        """Help with momentary debugging, file to fit.
           msg  -- special tag for this call
           skip -- the member variables to ignore
           os   -- output stream: may be IOStream etc.
        """
        import pprint
        print("DomeSerial - %s " % msg, file=os)
        for key,value in self.__dict__.items():
            if(key in skip):
               continue
            print(f'{key:20s} =',file=os,end='')
            pprint.pprint(value,stream=os,indent=4)
        return self

    ### DomeSerial.debug()

    __DomeSerial_debug = debug  # really preserve our debug name if we're inherited

   # (wg-python-properties properties)

# class DomeSerial


__author__  = 'Wayne Green'
__version__ = '0.1'
__all__     = ['DomeSerial']                              # of quoted items to export

##############################################################################
#                                    Main
#                               Regression Tests
##############################################################################
# HEREHEREHERE
if __name__ == "__main__":
    opts = optparse.OptionParser(usage="%prog "+__doc__)

    opts.add_option("-v", "--verbose", action="store_true", dest="verboseflag",
                   default=False,
                   help="<bool>     be verbose about work.")

    (options, args) = opts.parse_args()

    # (wg-python-atfiles)
    for filename in args:
        with open(filename,'r') if filename else sys.stdin as f:
            for l in f:
                if('#' in l):
                    continue
                parts = map(str.strip,l.split())

