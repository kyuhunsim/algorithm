def process_input(input_string):
    # Two stacks representing characters to the left and right of the cursor.
    left = []
    right = []

    # Process each character in the input string.
    for char in input_string:
        if char == '<':
            # Move cursor to the left.
            if left:
                right.append(left.pop())
        elif char == '>':
            # Move cursor to the right.
            if right:
                left.append(right.pop())
        elif char == '-':
            # Backspace.
            if left:
                left.pop()
        else:
            # Regular character.
            left.append(char)

    # Build the result from the two stacks.
    return ''.join(left + right[::-1])


n=int(input())

for i in range(n):
    a=input()
    print(process_input(a))
