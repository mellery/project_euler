#!/usr/bin/env python3
from test_all_problems import run_problem, EXPECTED_ANSWERS

# Test just a few problems to demonstrate functionality
test_problems = ['problem1.py', 'problem2.py', 'problem3.py', 'problem4.py', 'problem5.py']

print("Testing Sample Project Euler Solutions")
print("=" * 40)

for filename in test_problems:
    problem_num = int(filename.replace('problem', '').replace('.py', ''))
    
    print(f"Testing {filename}...", end=" ")
    
    actual_output, error = run_problem(filename)
    
    if error:
        print(f"FAIL ({error})")
        continue
        
    expected = EXPECTED_ANSWERS[problem_num]
    
    if actual_output == expected:
        print("PASS")
    else:
        print(f"FAIL (expected: {expected}, got: {actual_output})")

print("\nTo test all problems, run: python test_all_problems.py")
print("Note: Some problems may take longer to execute.")