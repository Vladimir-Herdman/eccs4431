"""OF NOTE:
Essentially, this program defines nodes that act as 'states,' which
contain a dict of string values and output states acting as the
transition functions for each state on an input. The methods then
handle calling the initial values, printing, and returning.
"""
from sys import argv
from dataclasses import dataclass, fields


#Global string set in base case for return reason. Get's printed after
#all states are ran through as success/failure reason.
result: str = ""

success_str = "\033[32m\u001b[1mACCEPTED\033[0m"
failure_str = "\033[31m\u001b[1mFAILURE\033[0m"


@dataclass
class Transition:
    input: list[str]
    destination: "State"

class State:
    def __init__(self, name: str):
        self.name = name
        self.transitions = dict() #dict of transition str -> destination

    def set_transitions(self, t_list: list[Transition]):
        for t in t_list:
            for input in t.input:
                self.transitions[input] = t.destination

    def handle_input(self, input: list[str]):
        global result

        print(f"{self.name}", end=" -> " if len(input) != 0 else "")
        if (len(input) == 0):
            result = f"{success_str if self.name == "bread" else failure_str}: "\
                     f"ending node is '{self.name}'"\
                     f"{", the acceptance state" if self.name == "bread" else ", not the acceptance state 'bread'"}.\n"
            return
        if input[0] not in self.transitions:
            result = f"{failure_str}: Transition {input[0]} for state {self.name} not found."
            return
        next_node = self.transitions[input[0]]
        input = input[1:]
        next_node.handle_input(input)


starter = State("starter")
levain = State("levain")
clumpy = State("clumpy")
dough = State("dough")
trash = State("trash")
shaped = State("shaped")
bread = State("bread")

starter.set_transitions([
    Transition(input=["feed", "rise"], destination=levain),
])
levain.set_transitions([
    Transition(input=["falls"], destination=starter),
    Transition(input=["mix"], destination=clumpy)
])
clumpy.set_transitions([
    Transition(input=["mold"], destination=trash),
    Transition(input=["mix"], destination=dough)
])
dough.set_transitions([
    Transition(input=["cold-proof"], destination=shaped),
    Transition(input=["mold"], destination=trash),
    Transition(input=["rise"], destination=dough),
    Transition(input=["sticky"], destination=clumpy),
])
shaped.set_transitions([
    Transition(input=["bake"], destination=bread),
    Transition(input=["falls", "mold"], destination=trash),
    Transition(input=["sticky"], destination=dough),
])
trash.set_transitions([
    Transition(input=["bake", "cold-proof", "falls", "mix", "mold", "rise", "sticky", "feed"], destination=trash)
])


def handle_input(input: list[str]) -> None:
    print("--------------------------------------------")
    print(f"Input is: '{" ".join(input)}'")
    print("States, in order, are:", end="\n  -> ")
    starter.handle_input(input)
    print(f"\n{result}")


def main() -> int:
    passedargs = argv[1:]
    if (len(passedargs) < 1):
        print("ERROR: No input was passed to program.")
        return 1

    if (passedargs[0] == "testcases"):
        handle_input(["feed", "mix", "mix", "cold-proof", "bake"])
        handle_input(["feed", "mix", "mix", "cold-proof", "bake"])
        handle_input(["feed", "mix", "mix", "mold", "mix", "mold", "bake", "rise", "falls"])
        handle_input(["feed", "falls", "feed", "falls", "feed", "mix", "mix", "rise", "rise", "cold-proof", "sticky", "cold-proof", "bake"])
        handle_input(["feed", "mix", "mix", "cold-proof"])
    else:
        handle_input(passedargs)

    return 0


if __name__ == "__main__":
    main()
