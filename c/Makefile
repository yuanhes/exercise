CFLAGS=-Wall -g
SHELL := /bin/bash

all: clean setup ex

clean: 
	rm -rf ex$(N)/ex$(N).$(M)
	rm -rf ex$(N)/ex$(N).$(M).c

setup:
	mkdir -p ex$(N)
	touch ex$(N)/ex$(N).c
	
ex:
	cp -rf ex$(N)/ex$(N).c ex$(N)/ex$(N).$(M).c
	cc $(CFLAGS)  ex$(N)/ex$(N).$(M).c -o ex$(N)/ex$(N).$(M)
