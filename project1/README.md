Project 1
---------

<!-- NOTE:
Briefly explain the real-world system, what you chose to model, how to run your
program, and anything else I need to know to understand your implementation.
-->

The real-world system being modeled here is the set of steps required to take
sourdough starter from a starter to a baked loaf of bread. Specifically, the
states are physical "states" the dough mixture goes through on its way to
becoming bread, with the input at each state being a physical change you or the
world can make to the bread, such as feeding, mixing, or cold-proofing the dough.

## Running the Program
I'm using a Unix-based system, but for most systems, it'll be about the same: Use
a Python interpreter to run the `src/main.py` file. An example from the terminal
is given below:
```bash
python3 main.py <input input input...>
```

In <input input input..." you can pass in your input values to test through the
model. These input values should not be passed as *one* string, so another example
with expected, simple success is given:
```bash
python3 main.py feed, mix, mix, cold-proof, bake
```

### Example Test Cases
Some example test cases have been implemented and can be ran with:
```bash
python3 main.py testcases
```

A visual will be presented showing what input was given, the states traversed, and
whether the input has been accepted or denied.

# Video Guide
Here's a link to a video presenting this specific state diagram and project:
- https://youtu.be/SlZw3Np2W9E?si=pL8Fys2h8uvY5uAx
