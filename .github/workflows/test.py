def unsafe_code(user_input):
    eval(user_input)  # BAD: unsafe use of eval
