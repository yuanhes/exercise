CFLAGS=-Wall -g

all: clean ex

clean:
	date=`date +%Y%m%d_%H%M%S`
	rm -rf ex3.${COUNT}.c

ex: SHELL:=/bin/bash
ex:
	cp -rf ex3.c ex3.${COUNT}.c
	cc ex3.${COUNT}.c -o ex3.${COUNT}
	export COUNT=$$((COUNT+1))

