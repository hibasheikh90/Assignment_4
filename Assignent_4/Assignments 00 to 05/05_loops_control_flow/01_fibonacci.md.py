# Define the maximum value for Fibonacci sequence terms
MAX_TERM_VALUE = 10000

def main():
    curr_term = 0  # The 0th Fibonacci number
    next_term = 1  # The 1st Fibonacci number

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print on the same line with space separator
        term_after_next = curr_term + next_term  # Calculate next term
        curr_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()
