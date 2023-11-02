def is_solution_valid(mapping, words, result):
    num_words = len(words)
    num_result = len(result)
    
    # Convert words and result to numbers using the given mapping
    num_values = []
    for word in words + [result]:
        num = 0
        for letter in word:
            num = num * 10 + mapping[letter]
        num_values.append(num)
    
    # Check if the sum of words is equal to the result
    return sum(num_values[:-1]) == num_values[-1]

def solve_cryptarithmetic(words, result):
    # Extract unique letters from words and result
    letters = set(''.join(words) + result)
    
    # Check if the number of unique letters is greater than 10 (0-9 digits)
    if len(letters) > 10:
        return None
    
    # Generate all possible permutations of digits for the letters
    from itertools import permutations
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        if is_solution_valid(mapping, words, result):
            return mapping
    
    return None

# Example usage
words = ["send", "more"]
result = "money"
solution = solve_cryptarithmetic(words, result)

if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
