## **Intro**
A repo for programming exercise.

## **Log**
* 2024/03/09
  - Start `c` programming exercise based on [Learn C The Hard Way (Chiniese Version)](https://www.cntofu.com/book/25/index.html)
  - c/ex1: compile an example for printing "hello world".
  - c/ex2: simple example of make and Makefile
  - c/ex3: print with format, and try to make it error/crash, through methods like: not initializing varialbes, not specifying variables in the print command.
* 2024/03/10
  - c/ex4: install valgrind and use it for print errors of exeutable.
    - Use `curl -O <link>` download the compressed `.tar.bz2` file. failed to uncompress at the first with message `bzip2: (stdin) is not a bzip2 file...`. Root cause is file is broken, which could be check by `md5sum` comparison with that in the download page. Re-downloaded and then fixed.
    - How to change shell of make: By default, make use the POSIX shell (`/bin/sh`), need to add `SHELL := /bin/bash` on the top to let it use bash. 
    - How to pass args to make: ([Ref](https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run))
        -  Makefile: 
           ```
           run:
               @echo $(ARGS)
           ```
           run: `make run ARGS="Hello"`
           output: `Hello`

