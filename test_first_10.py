#!/usr/bin/env python3
import subprocess
import sys
import time

# Expected answers for first 10 Project Euler problems
EXPECTED_ANSWERS = {
    1: "233168",
    2: "4613732", 
    3: "6857",
    4: "906609",
    5: "232792560",
    6: "25164150",
    7: "104743",
    8: "23514624000",
    9: "31875000",
    10: "142913828922"
}

def run_problem(filename):
    """Run a problem file and capture its output"""
    try:
        result = subprocess.run(
            [sys.executable, filename], 
            capture_output=True, 
            text=True, 
            timeout=30
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
        return None, "Timeout (30s exceeded)"
    except Exception as e:
        return None, f"Exception: {str(e)}"

def main():
    print("Testing First 10 Project Euler Solutions")
    print("=" * 45)
    
    passed = 0
    failed = 0
    
    for problem_num in range(1, 11):
        filename = f"problem{problem_num}.py"
        
        print(f"Testing {filename}...", end=" ")
        
        start_time = time.time()
        actual_output, error = run_problem(filename)
        elapsed = time.time() - start_time
        
        if error:
            print(f"FAIL ({error})")
            failed += 1
            continue
            
        expected = EXPECTED_ANSWERS[problem_num]
        
        if actual_output == expected:
            print(f"PASS ({elapsed:.2f}s)")
            passed += 1
        else:
            print(f"FAIL (expected: {expected}, got: {actual_output})")
            failed += 1
    
    print("\n" + "=" * 45)
    print(f"Results: {passed} passed, {failed} failed")

if __name__ == "__main__":
    main()