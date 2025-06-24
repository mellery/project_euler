#!/usr/bin/env python3
import subprocess
import sys
import time
import os

# Expected answers for Project Euler problems
EXPECTED_ANSWERS = {
    1: "233168", 2: "4613732", 3: "6857", 4: "906609", 5: "232792560",
    6: "25164150", 7: "104743", 8: "23514624000", 9: "31875000", 10: "142913828922",
    11: "70600674", 12: "76576500", 13: "5537376230", 14: "837799", 15: "137846528820",
    16: "1366", 17: "21124", 18: "1074", 19: "171", 20: "648",
    21: "31626", 22: "871198282", 23: "4179871", 24: "2783915460", 25: "4782"
}

def run_problem(filename):
    """Run a problem file and capture its output"""
    try:
        result = subprocess.run(
            [sys.executable, filename], 
            capture_output=True, 
            text=True, 
            timeout=60
        )
        if result.returncode != 0:
            return None, f"Error: {result.stderr.strip()}"
        
        # Get the last line of output (the answer)
        lines = result.stdout.strip().split('\n')
        if lines:
            return lines[-1].strip(), None
        else:
            return None, "No output"
            
    except subprocess.TimeoutExpired:
        return None, "Timeout (60s exceeded)"
    except Exception as e:
        return None, f"Exception: {str(e)}"

def main():
    print("Testing Project Euler Solutions (Batch 1-25)")
    print("=" * 50)
    
    passed = 0
    failed = 0
    failures = []
    
    for problem_num in range(1, 26):
        filename = f"problem{problem_num}.py"
        
        if not os.path.exists(filename):
            continue
            
        print(f"Testing {filename}...", end=" ")
        
        start_time = time.time()
        actual_output, error = run_problem(filename)
        elapsed = time.time() - start_time
        
        if error:
            print(f"FAIL ({error})")
            failed += 1
            failures.append((problem_num, error, None, None))
            continue
            
        expected = EXPECTED_ANSWERS.get(problem_num)
        if not expected:
            print("SKIP (no expected answer)")
            continue
        
        if actual_output == expected:
            print(f"PASS ({elapsed:.2f}s)")
            passed += 1
        else:
            print(f"FAIL (expected: {expected}, got: {actual_output})")
            failed += 1
            failures.append((problem_num, None, expected, actual_output))
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    
    if failures:
        print("\nFailures:")
        for problem_num, error, expected, actual in failures:
            if error:
                print(f"  Problem {problem_num}: {error}")
            else:
                print(f"  Problem {problem_num}: expected {expected}, got {actual}")

if __name__ == "__main__":
    main()