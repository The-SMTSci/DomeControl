#############################################################################
# Makefile -- /home/git/external/DomeControl/GUI/Makefile
#############################################################################

SHELL=/bin/bash

UNAME := $(shell uname)
ifeq ($(UNAME),Darwin)
INCFILES     = -I/opt/local/include/ -I/var/local/cfitsio/include
prefix       = /opt/local
else
INCFILES     = 
prefix       = $(pwd)
SHARLIB      = g++ -shared -Wl,-soname,libfoo.so.$(LIBVERSION) -o libfoo.so.$(LIBVERSION)
endif

bindir       = $(prefix)/bin
incdir       = $(prefix)/include
libdir       = $(prefix)/lib
mandir       = $(prefix)/man/manl

CC           = gcc
CPP          = g++
DEBUG        = -g
SHARED       = -fPIC
# Command to make a shared library.
SHARLIB      = g++ -shared -Wl,-soname,libfoo.so.$(LIBVERSION) -o libfoo.so.$(LIBVERSION)
INCFILES     =
LIB          =
WILDCARDS    =
SRCS         =
INCS         =
DOCS         = 
BINS         =
NROFFS       =
OBJS         = $(SRCS:.cpp=.o)
MANS         = $(NROFFS:.nroff=.l)
PYSIDE6      = pyside6-uic

%o:%cpp
	$(CPP) $(DEBUG) -c $<
%o:%c
	$(C) $(DEBUG) -c $<
%py:%ui
	$(PYSIDE6) $< -o $*py


all: ComPortDialogUI.py MainWindowUI.py NetworkDialogUI.py

ComPortDialogUI.py : ComPortDialogUI.ui  
MainWindowUI.py    : MainWindowUI.ui
NetworkDialogUI.py : NetworkDialogUI.ui

clean : ComPortDialogUI.py MainWindowUI.py NetworkDialogUI.py
	echo rm $^

uninstall:
	-(for i in $(MANS); do  rm -v $(mandir)/$$i; done)

#LaTeX support
pdfclean:
	-rm *.ent *.out *.idx *.log *.dvi *.aux *.bbl *.blg *.ilg *.ind *.lot *.lof *.toc *.nav *.snm 


# change foo to shared library.
# copy lib..so.files to a location specified in /etc/ld.so.conf.d files.
# ln -s libblah.so.1.2.3 libblah.so
# sudo /sbin/ldconfig
#
install: all
	-cp -p $(INCS) $(incdir)
	-cp -p $(LIBS) $(libdir)
	-cp -p $(DOCS) $(mandir)
	-cp -p $(BINS) $(bindir)
	-(if [[ -e libwgutility.so.$(LIBVERSION) ]]; then       cp libfoo.so.$(LIBVERSION) $(libdir) ;       ln -sf $(libs)/libfoo.so.$(LIBVERSION) $(libs)/libfoo.so ;    fi)
