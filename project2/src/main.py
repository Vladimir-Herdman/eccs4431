"""main.py file for Project 3. Implements a mini lexical analyzer for
the Simple Code called Wizard language.
"""
import pathlib
import re
from sys import argv


def usage():
    print("ERROR")
    print("Pass in a file (or list of files) to the command to start"
          "lexically analyzing them, for example:")
    print("\tpython3 main.py file1")
    print("\tpython3 main.py file1 file2 file3...")


def lexically_analyze(file):
    keyword_pattern =    r"\b(IF|ELSE|WHILE|PRINT|INTEGER|FLOAT|GET)\b"
    operator_pattern =   r"[+\-\*]|[<>=!]?[=](?!=)|[<>]|(?:&&)|(?:\|\|)|[!]"
    identifier_pattern = r"[a-zA-Z][a-zA-Z_0-9]*"
    number_pattern =     r"[0-9]+(?:\.[0-9]+)?" #?: makes a capturing group in () not a capture group. Means re.findall returns whole match, instead of capture group when printing.
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

    with open(file, "r") as f:
        token_list: list[tuple] = list()

        for line in f:
            for token_type, pattern in patterns:
                tokens = re.findall(pattern, line)
                for token in tokens:
                    token_list.append((token_type, token))

                #comment_pattern should be first each time
                if pattern is comment_pattern:
                    line = line.split("//")[0]

            #numbers = re.findall(number_pattern, line)
            # here, put a for to check for values that look like '44.' and remove them
        #print(token_list)
        for ttype, tval in token_list:
            print(f"Token: {tval}, Type: {ttype}")


def main() -> None:
    if len(argv) < 2:
        usage()
        return
    
    files = argv[1:]
    for file in files:
        if not pathlib.Path(file).is_file():
            print("ERROR")
            print(f"passed in string '{file}' is not a proper file. Ending program.")
            return

    for file in files:
        lexically_analyze(file)


if __name__ == "__main__":
    main()
