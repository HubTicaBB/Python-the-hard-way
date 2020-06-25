keywords = {
    "and": "Logical and",
    "as": "Part of the with-as statement",
    "assert": "Assert (ensure) that something is true",
    "break": "Stop the loop right now",
    "class": "Define a class",
    "continue": "Don't process more of the loop, do it again",
    "def": "Define a function",
    "del": "Delete from dictionary",
    "elif": "Else if condition",
    "else": "Else condition",
    "except": "If an exception happens, do this",
    "exec": "Run a string as Python",
    "finally": "Exceptions or not, finally do this no matter what",
    "for": "Loop over a collection of things",
    "from": "Import specific parts of a module",
    "global": "Declare that you want a global variable",
    "if": "If condition",
    "import": "Import a module into this one to use",
    "in": "Part of for-loops, also a test of X in Y",
    "is": "Like == to test equality",
    "lambda": "Create a short anonimous function",
    "not": "Logical not",
    "or": "Logical or",
    "pass": "This block is empty",
    "print": "Print this string",
    "raise": "Raise an exception when things go wrong",
    "return": "Exit the function with a return value",
    "try": "Try this block, and if exception, go to except",
    "while": "While loop",
    "with": "With a expression as a variable do",
    "yield": "Pause here and return to caller"
}

points = 0

for keyword, description in list(keywords.items()):
    print(f"{description}:", end=' ')
    answer = input()
    if answer == keyword:
        points += 1
    else:
        print("WRONG")
        print(f"Correct answer is: '{keyword}''")
        print("Press ENTER to continue...")
        input()

print(f"Your score: {points}/{len(keywords)}")