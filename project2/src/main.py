#!/usr/bin/env python3
"""main.py file for Project 3. Implements a mini lexical analyzer for
the Simple Code called Wizard language.
"""
import pathlib
import re
from sys import argv


error_str = "\033[38;2;255;80;80mERROR\033[0m"
token_str = "\033[38;2;35;133;250mToken\033[0m"


def usage():
    print(error_str)
    print("Pass in a file (or list of files) to the command to start"
          "lexically analyzing them, for example:")
    print("\tpython3 main.py file1")
    print("\tpython3 main.py file1 file2 file3...")


def is_float(v: str) -> bool:
    try:
        vf = float(v)
        if "." in v:
            return True
    except:
        return False
    return False


def perror(nline, estr):
    print(f"{error_str}: Line {nline}. {estr}")


keyword_pattern =    r"\b(IF|ELSE|WHILE|PRINT|INTEGER|FLOAT|GET)\b"
operator_pattern =   r"[+\-\*]|[<>=!]?[=](?!=)|[<>]|(?:&&)|(?:\|\|)|[!]"
identifier_pattern = r"[a-zA-Z][a-zA-Z_0-9]*"
number_pattern =     r"[0-9]+(?:\.[0-9]+)?" #?: makes a capturing group in () not a capture group. Means re.findall returns whole match, instead of capture group when printing. Annoying problem for a while.
symbol_pattern =     r"[(){};]"
comment_pattern =    r"//.*" #Don't include in final token count.
patterns = [
    ("Comment", comment_pattern),
    ("Keyword", keyword_pattern),
    ("Operator", operator_pattern),
    ("Identifier", identifier_pattern),
    ("Number", number_pattern),
    ("Symbol", symbol_pattern),
]
def lexically_analyze(file):
    with open(file, "r") as f:
        token_list: list[tuple] = list()
        variables = set()
        nline = 0

        for line in f:
            line = line.strip("\n")
            nline += 1
            tokens_found = set()
            for token_type, pattern in patterns:
                tokens = re.findall(pattern, line)
                for token in tokens:
                    if token in tokens_found and (token_type, token) not in token_list:
                        continue
                    token_list.append((token_type, token))
                    tokens_found.add(token)

                #comment_pattern should be first each time so we
                #don't read comments for tokens.
                if token_type == "Comment":
                    line = line.split("//")[0]

                #Here, we're gonna check if the variable already
                #exists and has been assigned. If you reference a
                #variable that hasn't been assigned, that should
                #be an error.
                #There should also be an error for if you say
                #INTEGER data type, but then that's not an integer
                #value that's been passed.
                if token_type == "Identifier":
                    assignments = re.findall(fr"\b(FLOAT|INTEGER) ({identifier_pattern})[ ]*=[ ]*(.*?);", line)
                    if len(assignments) > 1:
                        perror(nline, f"Multiple assignments: '{line}")
                    elif len(assignments) == 1:
                        vartype, varname, varval = assignments[0]
                        if varname in variables:
                            perror(nline, f"Variable name '{varname}' already in use, can't redeclare: '{line}")
                        else:
                            variables.add(varname)

                        if vartype == "INTEGER" and is_float(varval):
                            perror(nline, f"Can't assign float to integer type variable: '{line}'")
                        if vartype == "FLOAT" and not is_float(varval):
                            perror(nline, f"Improper assignment to FLOAT var '{varname}' with val {varval}: '{line}'")
                        if len(varval) == 0:
                            perror(nline, f"Variable assignment with empty value: '{line}'")

            token_list.append(("newline", ""))

        type_count = dict()
        for ttype, tval in token_list:
            if ttype == "newline":
                print()
                continue

            print(f"{token_str}: {tval}, Type: {ttype}")

            if ttype in type_count:
                type_count[ttype] += 1
            else:
                type_count[ttype] = 1

        print(type_count)


def main() -> None:
    if len(argv) < 2:
        usage()
        return
    
    files = argv[1:]
    for file in files:
        if not pathlib.Path(file).is_file():
            print(error_str)
            print(f"passed in string '{file}' is not a proper file. Ending program.")
            return

    for file in files:
        lexically_analyze(file)


if __name__ == "__main__":
    main()
