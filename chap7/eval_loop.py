# Exercise 7.2

def eval_loop():
    """Evaluate code input by user until they enter 'done'
    """
    input_prompt = "Enter a piece of code to be run, or 'done' to stop.\n:"
    while True:
        code = input(input_prompt)
        if code=='done':
            break
        print(eval(code))

eval_loop()
