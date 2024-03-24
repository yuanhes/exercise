## **Intro**
A repo for programming exercise.

## **Log**
* 2024/03/09
  - Start `c` programming exercise based on [Learn C The Hard Way (Chiniese Version)](https://www.cntofu.com/book/25/index.html) .
  - c/ex1: Compile an example for printing "hello world".
  - c/ex2: Simple example of `make` and Makefile
  - c/ex3: Print with format, and try to make it error/crash, through methods like: not initializing varialbes, not specifying variables in the print command.
* 2024/03/10
  - c/ex4: Install `valgrind` and use it for printing errors of exeutable.
    - Use `curl -O <link>` download the compressed `.tar.bz2` file. Failed to uncompress with `tar xvzf <file>` at first with message `bzip2: (stdin) is not a bzip2 file...`. Root cause is found to be file is broken during downloading, which could be checked by `md5sum` comparison with that in the download page. Re-downloaded and then fixed.
    - How to change shell of `make`: By default, `make` use the [POSIX](## "Portable Operating System Interface") shell (`/bin/sh`), need to add `SHELL := /bin/bash` on the top of Makefile to let it use bash. ([Ref.](https://stackoverflow.com/questions/589276/how-can-i-use-bash-syntax-in-makefile-targets))
    - How to pass args to `make`: ([Ref.](https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run))
        -  Makefile: 
           ```
           run:
               @echo $(ARGS)
           ```
           run: `make run ARGS="Hello"`, 
           output: `Hello`
  - c/ex5: Read a simple c script line by line to know the basic code structure.
  - c/ex6: A script containning multiple variables of different data types. Print them with `printf`.
  - c/ex7: A simple code for knowing different types of data. 
    - 'long' type integer:
        - printf with %ld
        - limit: -2^63 ~ +2^63 - 1
    - printf special char `'\0'` (null_byte) with:
        - %c -> (empty) 
        - %s -> (null)
        - %d -> 0
    - printf char of number zero `'0'` with %s -> Segmentation fault
    - 'unsigned long' type integer:
        - printf with %lu
        - limit: 0 ~ +2^64 - 1
* 2024/03/23
  - c/ex8: Play with array of numbers, array of chars and string by `printf` / `sizeof`
    - string is array of chars ending with `null` character, i.e. `'\0'`.
    - `sizeof()` returns the allocated memory for the operand, so, for a string, it will take the ending `null` into count, then usually looks 1 more than the number of characters of the string. ([Ref.](https://www.quora.com/What-is-the-difference-between-strlen-and-sizeof-in-C-programming-language))
  - c/ex9: Involve something like array initialization, assigning string with pointer ... (Not really know what the author wants readers to know....just go through 😅:)
  - c/ex10: Array of strings and loop
    - `argv[0]` is the command/executable itself.
    - Format of a `for` loop:
        ```
        for(INITIALIZER; TEST; INCREMENTER) {
            CODE;
        }
        ```
      Executing order: INITIALIZER, TEST, CODE, INCREMENTER, TEST, CODE, INCREMENTER, ... until TEST being false.
* 2024/03/24
  - c/ex11: While loop
    - Format of a `while` loop:
        ```
        while (TEST) {
            CODE;
        }
        ```
    - Usually `for` loop is more robust, since it has INITIALIZER and INCREMENTER that help avoiding errors.
    - Way to print the memory address of a variable:
        ```
        int var = 0;
        printf("Mem addr of var: %p \n" &var);
        ```
        output example: ```Mem addr of var: 0x7ffe2333ce7c ```

        
