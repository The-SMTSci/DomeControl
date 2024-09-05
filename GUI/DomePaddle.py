#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# /usr2/git/external/DomeControl/Code/py3.12/env/src/DomePaddle.py
#
#
# (compile (format "python3 -m py_compile %s" (buffer-file-name)))
# (compile (format "pydoc3 %s" (buffer-file-name)))
#
# Todo:  Fix the statusbar spacing.
#
#
#############################################################################
### HEREHEREHERE

import os
import optparse
import sys
import platform
import re
import math
#import numpy as np
#import pandas as pd
#from astropy.io import fits
from  PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtWidgets import QApplication, QLabel

from MainWindowUI      import Ui_MainWindow
from ComPortDialogUI   import Ui_ComPortDialog
from NetworkDialogUI   import Ui_DomeNetwork

__author__  = 'Wayne Green'
__version__ = '0.1'
__all__     = ['']                                        # list of quoted items to export

__FSDEBUG = [False,True][os.getenv('FSDEBUG') == '']

# to handle the Unicode filenames from Win1X
_encoding   = 'utf-8'                                     # deal with nt's UTF issues.
__oursystem = os.name
__ourplatform = platform.platform()
print(f"{__oursystem}")
if(__oursystem == 'nt'):
    _encoding = 'utf-16'
# with io.open(listname,'r',encoding=_encoding) as f:

# (wg-python-types)
#############################################################################
#
#
#  /usr2/git/external/DomeControl/Code/py3.12/env/src/DomePaddle.py
# (wg-python-emacs-help)
#
#   self.One_pushButton
#   self.Two_pushButton
#   self.Three_pushButton
#   self.Four_pushButton
#   self.Five_pushButton
#   self.Six_pushButton
#   self.Seven_pushButton
#   self.Eight_pushButton
#   self.Nine_pushButton
#   self.Zero_pushButton
#   self.Decimal_pushButton
#
#   self.JogCW_pushButton
#   self.JogCCW_pushButton
#
#   self.Entry_lineEdit
#   self.Clear_pushButton
#   self.Home_pushButton
#   self.Go_pushButton
#   self.CurrentPosition
#
#    case 'H':   - Home
#    case 'h':
#    case 'P':   - Park
#    case 'p':
#    default:  a number to achieve.
#
#
# (wg-python-toc)
#
# __author__  = 'Wayne Green'
# __version__ = '0.1'
# __all__     = ['']                                        # list of quoted items to export
# __doc__ = """
# class NetworkDialogException(Exception):
#     def __init__(self,message,errors=None):
#     @staticmethod
#     def __format__(e):
# class NetworkDialog(Ui_DomeNetwork):
#     #__slots__ = [''] # add legal instance variables
#     def __init__(self):                                   # NetworkDialog::__init__()
#     def gethostname(self):                                # NetworkDialog.gethostname()
#     def port(self):                                       # NetworkDialog.port()
#     def debug(self,msg="",skip=[],os=sys.stderr):         # NetworkDialog::debug()
# class ComDialogException(Exception):
#     def __init__(self,message,errors=None):
#     @staticmethod
#     def __format__(e):
# class ComDialog(QtWidgets.QDialog, Ui_ComPortDialog):
#     #__slots__ = [''] # add legal instance variables
#     def __init__(self):                                   # ComDialog::__init__()
#     def debug(self,msg="",skip=[],os=sys.stderr):         # ComDialog::debug()
# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self,options):                           # MainWindow.__init__()
#     def usenetwork(self):                                 #  MainWindow.usenetwork()
#     def useserial(self):                                  #  MainWindow.useserial()
#     def statusmsg(self,msg):                              # MainWindow.statusmsg()
#     def valupdate(self,value):                            # MainWindow.valupdate()
#     def numberbutton_clicked(self,value):                 # MainWindow.numberbutton()
#     def Clear_pushButton_clicked(self):                   # MainWindow.Clear_pushButton_clicked()
#     def Home_pushButton_clicked(self):                    # MainWindow.Home_pushButton_clicked()
#     def Go_pushButton_clicked(self):                      # MainWindow.Go_pushButton_clicked()
#     def JogCCW_pushbutton_clicked(self):                  # MainWindow.JogCW_pushbutton_clicked()
#     def JogCW_pushbutton_clicked(self):                   # MainWindow.JogCCW_pushbutton_clicked()
#     def validposition(self,val):                          # MainWindow.validposition()
#     def debug(self,msg="",skip=[],os=sys.stderr):         # MainWindow.debug()
# if __name__ == "__main__":
#
#
#
#
#############################################################################

__doc__ = """

/usr2/git/external/DomeControl/Code/py3.12/env/src/DomePaddle.py

Allow a user to interface with an Arduino based dome controller,
using simple single letter commands and optional arguments.
Move the dome to various positions. The dome may be
  1 ) sent to a position with the keypad and Go buttons
  2 ) Homed
  3 ) Jogged CW or CCW with button for an optional step size.

A Comm dialog helps to change default communication parameters from
/dev/ttyACM0, 9600 baud, one stop, no parity.

2024-09-03T10:46:02-0600 wlg - initial work.

Questions:
   Do we add a park button?

"""


##############################################################################
# NetworkDialogException
#
##############################################################################
class NetworkDialogException(Exception):
    """Special exception to allow differentiated capture of exceptions"""
    def __init__(self,message,errors=None):
        super(NetworkDialogException,self).__init__("NetworkDialog "+ message)
        self.errors = errors
    @staticmethod
    def __format__(e):
        return f" NetworkDialog: {e.__str__()}\n"
# NetworkDialogException

##############################################################################
# NetworkDialog
#
##############################################################################
class NetworkDialog(QtWidgets.QDialog, Ui_DomeNetwork):
    """ Put up a dialog that gets hostname and port for a network connection
        instead of Serial port connection.

    self.Hostname      QLineEdit
    self.Port          QLineEdit
    self.Username      QLineEdit
    self.Password      QLineEdit  echo=Password
    

    """
    #__slots__ = [''] # add legal instance variables
    # (setq properties `("" ""))
    def __init__(self,parent=None):                       # NetworkDialog::__init__()
        """Initialize this class."""
        super(NetworkDialog,self).__init__()
        self.setupUi(self)
        # (wg-python-property-variables)
        self.username         = None
        self.password         = None
        self.hostname         = None
        self.port             = None


    ### NetworkDialog.__init__()

    def get_username(self):                                # NetworkDialog.gethostname()
        """Get the hostname from the dialog and check for valid"""
        pass
    ### NetworkDialog.gethostname()

    def get_password(self):                                # NetworkDialog.gethostname()
        """Get the hostname from the dialog and check for valid"""
        pass
    ### NetworkDialog.gethostname()

    def get_hostname(self):                                # NetworkDialog.gethostname()
        """Get the hostname from the dialog and check for valid"""
        pass
    ### NetworkDialog.gethostname()

    def get_port(self):                                       # NetworkDialog.port()
        """Get the port from the dialog and check for valid"""
        pass
    ### NetworkDialog.port()

    def debug(self,msg="",skip=[],os=sys.stderr):         # NetworkDialog::debug()
        """Help with momentary debugging, file to fit.
           msg  -- special tag for this call
           skip -- the member variables to ignore
           os   -- output stream: may be IOStream etc.
        """
        import pprint
        print("NetworkDialog - %s " % msg, file=os)
        for key,value in self.__dict__.items():
            if(key in skip):
               continue
            print(f'{key:20s} =',file=os,end='')
            pprint.pprint(value,stream=os,indent=4)
        return self

    ### NetworkDialog.debug()

# class NetworkDialog

##############################################################################
# ComDialogException
#
##############################################################################
class ComDialogException(Exception):
    """Special exception to allow differentiated capture of exceptions"""
    def __init__(self,message,errors=None):
        super(ComDialogException,self).__init__("ComDialog "+ message)
        self.errors = errors
    @staticmethod
    def __format__(e):
        return f" ComDialog: {e.__str__()}\n"
# ComDialogException

##############################################################################
# ComDialog
#
##############################################################################
class ComDialog(QtWidgets.QDialog, Ui_ComPortDialog):
    """ Tune up the Com port dialog:

    Defaults are first in the lists.

    Systems: Linux (posix), WinX (nt) , MacOS (darwin)

    Baud Choices:

         9600,    110,   300,     600,   1200,  2400, 4800,
        14400,  19200,  28800,  31250,  38400, 51200,
        56000,  57600,  76800, 115200, 128000,
       230400, 256000, 921600

    Bit Choices:
       8 bit, 5 bit, 6 bit, 7 bit

    Start/Stop Choices:
       1,     1.5,   2,     None

    Parity Choices:
       None,  Even,  Odd,   Space, Mark

    """
    #__slots__ = [''] # add legal instance variables
    # (setq properties `("" ""))
    def __init__(self,parent=None):                       # ComDialog::__init__()
        """Initialize this class."""
        super(ComDialog,self).__init__()
        self.setupUi(self)
        
        # (wg-python-property-variables)
        self.systems        = {'Linux'   : ['/dev/ttyACM0','/dev/ttyS4'],
                               'Windows' : ['COM4'],
                               'MacOS'   : ['/dev/ttyACM0']
                              }

        self.default_port   = '/dev/ttyACM0'
        self.PortItems      = [self.default_port,'/dev/devACM0']
        self.BaudItems      = [   '9600',    '110'   , '300',    '600',   '1200',  '2400', '4800',
                                 '14400',  '19200' , '28800',  '31250',  '38400', '51200',
                                 '56000',  '57600' , '76800', '115200', '128000',
                                '230400', '256000', '921600'
                              ]
        self.BitsItems      = ['8 bit', '5 bit', '6 bit', '7 bit'          ]
        self.StartStopItems = ['1',     '1.5',   '2',     'None'           ]
        self.ParityItems    = ['None',  'Even',  'Odd',   'Space', 'Mark'  ]

        # add action text choices to values
        self.PortValue   .addItems(self.PortItems      )
        self.BaudValue   .addItems(self.BaudItems      )
        self.BitsValue   .addItems(self.BitsItems      )
        self.ParityValue .addItems(self.ParityItems    )
        self.StartValue  .addItems(self.StartStopItems )
        self.StopValue   .addItems(self.StartStopItems )

        # tie actions to values
        self.PortValue   .currentIndexChanged.connect(lambda : self.get_PortValue()   )
        self.BaudValue   .currentIndexChanged.connect(lambda : self.get_BaudValue()   )
        self.StartValue  .currentIndexChanged.connect(lambda : self.get_StartValue()  )
        self.StopValue   .currentIndexChanged.connect(lambda : self.get_StopValue()   )
        self.ParityValue .currentIndexChanged.connect(lambda : self.get_ParityValue() )
        self.BitsValue   .currentIndexChanged.connect(lambda : self.get_BitsValue()   )

    ### ComDialog.__init__()

    def get_PortValue(self):                              # ComDialog.get_PortValue()
        """Get the  value, validate"""
        txt = self.PortValue.currentText()
        print(f"get_PortValue {txt}")
    ### ComDialog.get_PortValue()

    def get_BaudValue(self):                              # ComDialog.get_BaudValue()
        """Get the  value, validate"""
        pass
    ### ComDialog.get_BaudValue()

    def get_StartValue(self):                             # ComDialog.get_StartValue()
        """Get the  value, validate"""
        pass
    ### ComDialog.get_StartValue()

    def get_StopValue(self):                              # ComDialog.get_StopValue()
        """Get the  value, validate"""
        pass
    ### ComDialog.get_StopValue()

    def get_ParityValue(self):                            # ComDialog.get_ParityValue()
        """Get the  value, validate"""
        pass
    ### ComDialog.get_ParityValue()

    def get_BitsValue(self):                              # ComDialog.get_BitsValue()
        """Get the  value, validate"""
        pass
    ### ComDialog.get_BitsValue()

    def debug(self,msg="",skip=[],os=sys.stderr):         # ComDialog::debug()
        """Help with momentary debugging, file to fit.
           msg  -- special tag for this call
           skip -- the member variables to ignore
           os   -- output stream: may be IOStream etc.
        """
        import pprint
        print("ComDialog - %s " % msg, file=os)
        for key,value in self.__dict__.items():
            if(key in skip):
               continue
            print(f'{key:20s} =',file=os,end='')
            pprint.pprint(value,stream=os,indent=4)
        return self

    ### ComDialog.debug()

    __ComDialog_debug = debug  # really preserve our debug name if we're inherited

   # (wg-python-properties properties)

# class ComDialog

##############################################################################
# class MainWindow - a PySide6 main window, inherit the pyside6-designer
# layout ui.
# uses a comm dialog
##############################################################################
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Window for the Dome Controller"""
    __validposre = re.compile(r'[0-9]{1}[0-9]*|[0-9]{1}[0-9]*[.]{1}[0-9]*')
    __posintre   = re.compile(r'[0-9]+')
    __posfloatre = re.compile(r'[0-9]{1}[0-9]*[.]{1}[0-9]*')


    def __init__(self,options):                           # MainWindow.__init__()
        super(MainWindow,self).__init__()
        self.setupUi(self)

        self.port                  =        options.port
        self.bits                  = int  ( options.bits    )
        self.baud                  = int  ( options.baud    )
        self.parity                =        options.parity
        self.start                 = int  ( options.start   )
        self.stop                  = int  ( options.stop    )
        self.step                  = float( options.step    )

        self.serialflag            = False
        self.networkflag           = False
        self.connected             = False
        self.network_username      = None
        self.network_password      = None
        self.network_hostname      = None
        self.network_port          = None

        self.currentposition       = None
        self.accumulator           = 0

        self.domestate             = "unknown"

        self.msg                   = ""

        self.One_pushButton        .clicked.connect(lambda : self.numberbutton_clicked('1'))
        self.Two_pushButton        .clicked.connect(lambda : self.numberbutton_clicked('2'))
        self.Three_pushButton      .clicked.connect(lambda : self.numberbutton_clicked('3'))
        self.Four_pushButton       .clicked.connect(lambda : self.numberbutton_clicked('4'))
        self.Five_pushButton       .clicked.connect(lambda : self.numberbutton_clicked('5'))
        self.Six_pushButton        .clicked.connect(lambda : self.numberbutton_clicked('6'))
        self.Seven_pushButton      .clicked.connect(lambda : self.numberbutton_clicked('7'))
        self.Eight_pushButton      .clicked.connect(lambda : self.numberbutton_clicked('8'))
        self.Nine_pushButton       .clicked.connect(lambda : self.numberbutton_clicked('9'))
        self.Zero_pushButton       .clicked.connect(lambda : self.numberbutton_clicked('0'))
        self.Decimal_pushButton    .clicked.connect(lambda : self.numberbutton_clicked('.'))

        self.JogCW_pushButton      .clicked.connect(lambda : self.JogCW_pushbutton_clicked())
        self.JogCCW_pushButton     .clicked.connect(lambda : self.JogCCW_pushbutton_clicked())

        self.Clear_pushButton      .clicked.connect(lambda : self.Clear_pushButton_clicked())
        self.Home_pushButton       .clicked.connect(lambda : self.Home_pushButton_clicked())
        self.Go_pushButton         .clicked.connect(lambda : self.Go_pushButton_clicked())
        self.action_Network        .triggered.connect(self.usenetwork)
        self.action_Serial         .triggered.connect(self.useserial)

        self.serialdialog  = ComDialog(self)                         # use a basic dialog
        self.networkdialog = NetworkDialog(self)


    ### MainWindow.__init__()

    def usenetwork(self):                                 #  MainWindow.usenetwork()
        """Use the network"""
        res = self.networkdialog.exec()
        if(res == 1):
            self.networkflag = True
            self.serialflag  = False
            try:
                self.network_username  = self.networkdialog  .Username .text()
                self.network_password  = self.networkdialog  .Password .text()
                self.network_hostname  = self.networkdialog  .Hostname .text()
                self.network_port      = self.networkdialog  .Port     .text()
            except Exception as e:
                print(f"MainWindow.usenetwork(): {e.__str__()}")
    ###  MainWindow.usenetwork()

    def useserial(self):                                  #  MainWindow.useserial()
        """Use the eseria"""
        res = self.serialdialog.exec()
        if(res == 1):
            self.networkflag = False
            self.serialflag  = True
            try:
                self.port    = self.serialdialog  .PortValue   . currentText()
                self.bits    = self.serialdialog  .BitsValue   . currentText()
                self.baud    = self.serialdialog  .BaudValue   . currentText()
                self.parity  = self.serialdialog  .ParityValue . currentText()
                self.start   = self.serialdialog  .StartValue  . currentText()
                self.stop    = self.serialdialog  .StopValue   . currentText()
            except Exception as e:
                print(f"MainWindow.usenetwork(): {e.__str__()}")
    ###  MainWindow.useserial()

    def statusmsg(self,msg):                              # MainWindow.statusmsg()
        """Put message on the status bar. Make them short"""
        self.messageArea.setText(f"{msg}")
     ### MainWindow.statusmsg()

    def valupdate(self,value):                            # MainWindow.valupdate()
        """Add the value into the emerging value.
           If the value is negative or goes > 360
           raise the alarm.
        """
        str = self.Entry_lineEdit.text()
        if( value in {"0","1","2","3","4","5","6","7","8","9","."} ):
            str += value
            self.Entry_lineEdit.setText(str)
        else:
            self.msg = f"Error value {value} not a legal character."
        self.statusmsg(f"value for valueupdate {str}")
    ### MainWindow.valupdate()

    def numberbutton_clicked(self,value):                 # MainWindow.numberbutton()
        """Handle the value of each button
        verify a decent number >0 <= 360.
        """
        self.valupdate(value)
    ### MainWindow.numberbutton()

    def Clear_pushButton_clicked(self):                   # MainWindow.Clear_pushButton_clicked()
       """Clear the accumulator.
       """
       self.Entry_lineEdit.setText("")
    ### MainWindow.Clear_pushButton_clicked()

    def Home_pushButton_clicked(self):                    # MainWindow.Home_pushButton_clicked()
       """Send Home command to the interface.
       """
       self.statusmsg("Home")
    ### MainWindow.Home_pushButton_clicked()

    def Go_pushButton_clicked(self):                      # MainWindow.Go_pushButton_clicked()
        """Send Rotate command to the interface.
        """
        newpos = self.Entry_lineEdit.text()
        if(newpos != ""):
            if(self.validposition(newpos)):
                self.statusmsg(self.tr(f"Go {newpos}"))
                self.CurrentPosition_label.setText(newpos)
                self.Entry_lineEdit.setText("")
            else:
                self.Entry_lineEdit.setText("")
                self.statusmsg(f"Bad txt '{newpos}'")
    ### MainWindow.Go_pushButton_clicked()

    def JogCW_pushbutton_clicked(self):                   # MainWindow.JogCW_pushbutton_clicked()
        """Subtract stepsize from the accumulator
        and send a move command
        """
        newpos = self.CurrentPosition_label.text()
        if(self.validposition(newpos)):
            if(MainWindow.__posintre.fullmatch(newpos)):  # integer value
                v = int(newpos) - int(self.step)
                if(v < 0 or v >= 360):
                    v = (360 + v) % 360
                newpos = f"{v:d}"
            if(MainWindow.__posfloatre.fullmatch(newpos)):
                v = float(newpos) - float(self.step)
                if(v < 0 or v >= 360):
                    v = math.fmod((360.0 + v),360.0)
                newpos = f"{v:.1f}"
            self.Entry_lineEdit.setText(newpos)
            self.Go_pushButton_clicked()
        else:
            msg = f"Bad value {newpos}"
            self.Entry_lineEdit.setText("")
    ### MainWindow.JogCW_pushbutton_clicked()

    def JogCCW_pushbutton_clicked(self):                  # MainWindow.JogCCW_pushbutton_clicked()
        """Subtract stepsize from the accumulator
        and send a move commandstr
        """
        newpos = self.CurrentPosition_label.text()
        if(self.validposition(newpos)):
            if(MainWindow.__posintre.fullmatch(newpos)):
                v = int(newpos) + int(self.step)
                if(v < 0 or v >= 360):
                    v = (360 + v) % 360
                newpos = f"{v:d}"
            if(MainWindow.__posfloatre.fullmatch(newpos)):
                v = float(newpos) + float(self.step)
                if(v < 0.0 or v >= 360.0):
                    v = math.fmod((360.0 + v),360.0)
                newpos = f"{v:.1f}"
            self.Entry_lineEdit.setText(newpos)
            self.Go_pushButton_clicked()
        else:
            msg = f"Bad value {newpos}"
            self.Entry_lineEdit.setText("")
    ### MainWindow.JogCCW_pushbutton_clicked()

    def validposition(self,val):                          # MainWindow.validposition()
        """Get the current Entry_lineEdit value and make sure
        it is a valid number.
        [0-9]{1}[0-9]*|[0-9]{1}[0-9]*[.]{1}[0-9]*
        """
        return MainWindow.__validposre.fullmatch(val)
    ### MainWindow.validposition()

    def debug(self,msg="",skip=[],os=sys.stderr):         # MainWindow.debug()
        """Help with momentary debugging, file to fit.
           msg  -- special tag for this call
           skip -- the member variables to ignore
           os   -- output stream: may be IOStream etc.
        """
        import pprint
        print("MainWindow - %s " % msg, file=os)
        for key,value in self.__dict__.items():
            if(key in skip):
               continue
            print(f'{key:20s} =',file=os,end='')
            pprint.pprint(value,stream=os,indent=4)
        return self
    ### MainWindow.debug()

# class MainWindow

##############################################################################
#                                    Main
#                               Regression Tests
##############################################################################
# HEREHEREHERE
if __name__ == "__main__":
    opts = optparse.OptionParser(usage="%prog "+__doc__)

    opts.add_option("-v", "--verbose", action="store_true", dest="verboseflag",
                   default="",
                   help="<bool>     be verbose about work.")

    #import optparse

    # SERIAL_8N2: 1 start bit, 8 data bits, 2 stop bits

    opts.add_option("-p", "--port",    action="store",  dest="port",
                    default='/dev/ttyACM0',
                    help="<string>       port name        ")

    opts.add_option("--bits",    action="store_true",   dest="bits",
                    default='8',
                    help="<int>        bits: default 8.")

    opts.add_option("--baud",    action="store_true",   dest="baud",
                    default='9600',
                    help="<int>        baudrate.")

    opts.add_option("--start",    action="store_true",  dest="start",
                    default='1',
                    help="<int>         stop bits.")

    opts.add_option("--stop",    action="store_true",   dest="stop",
                    default='2',
                    help="<int>         stop bits.")

    opts.add_option("--parity",    action="store_true", dest="parity",
                    default='No',
                    help="<string>      parity.")

    opts.add_option("--step",    action="store_true",   dest="step",
                    default='1.5',
                    help="<float>      step size for jogging.")

    (options, args) = opts.parse_args()

    app    = QtWidgets.QApplication(sys.argv)

    window = MainWindow(options)                          # class MainWindow
    window.show()
    app.exec()

