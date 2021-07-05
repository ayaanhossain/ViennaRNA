# -*- sh -*-

.PHONY: all build install demo clean

DEFS=-DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DLINUX=1 -DDO_PS=1 -DDO_FIG=1 -DDO_X11=1 -DDO_XDBE=1 -DDO_GD=1 -DDO_GIF=1 -DHAVE_STDIO_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_STRINGS_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_UNISTD_H=1 -DSTDC_HEADERS=1 -DHAVE_LIMITS_H=1
LIBS= -L/usr/local/lib -lm -lX11 -lXext -lgd
LDSHARED=ld

# either ../libg2.so or ../libg2.a must be there
# to make libg2.so the default, uncomment the next line and the three lines below DEPENDENCY=
#ifeq ("$(LDSHARED)","")
DEPENDENCY= libg2.a
#else
#DEPENDENCY= libg2.so
#endif

all: build

build: ../$(DEPENDENCY)
	python setup.py "$(DEFS)" "$(LIBS)" build_ext

../$(DEPENDENCY):
	cd ..; make $(DEPENDENCY)

# must be root
install: build
	python setup.py "$(DEFS)" "$(LIBS)" install

demo:
	ln -f -s $(shell find build -name g2.so) .
	python g2_test.py

clean:
	-rm -fr build
	-rm -f g2.so g2.map g2_test{_clip.eps,.{eps,ps,png,jpg,fig}} penguin.pyc

