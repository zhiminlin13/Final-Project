def unsafe_code(user_input):
    eval(user_input)  # This will be flagged by Bandit
