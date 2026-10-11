Project 2
---------

This project implements a mini lexical analyzer for the Simple Code called
Wizard language. It acts as Project 2 for our Theory of Computation course.

## Running the Program
I'm using a Unix-based system, but for most systems, it'll be about the same: Use
a Python interpreter to run the `src/main.py` file. An example from the terminal
is given below:
```bash
python3 main.py <file file file...>
```

In <file file file..." you can pass in your files to test through the analyzer.
These files should not be passed as *one* string, so another example
with expected, simple success, is given:
```bash
python3 main.py test1_basic.txt test2_token_coverage.txt
```

### Example Test Cases
Some example test files have been made and can be ran as the above example showed.
Simply call the python program with the text file in src, or multiple files at once.

A visual will be presented showing what file was given, the tokens found, and
any errors/warnings from each line of the file.

# Video Guide
Here's a link to a video presenting this specific state diagram and project:
- https://youtu.be/60k7ILrvjRo
