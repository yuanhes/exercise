CFLAGS=-Wall -g
SHELL := /bin/bash

all: clean setup ex

clean: 
	rm -rf ex$(N)/ex$(N).$(M)

setup:
	mkdir -p ex$(N)
	touch ex$(N)/ex$(N).c
	
ex:
	cp -rf ex$(N)/ex$(N).c ex$(N)/ex$(N).$(M).c
	cc -Wall -g ex$(N)/ex$(N).$(M).c -o ex$(N)/ex$(N).$(M)
