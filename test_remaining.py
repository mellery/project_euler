#!/usr/bin/env python3
import subprocess
import sys
import time
import os

# Expected answers for remaining Project Euler problems
EXPECTED_ANSWERS = {
    26: "983", 27: "-59231", 28: "669171001", 29: "9183", 30: "443839",
    31: "73682", 32: "45228", 33: "100", 34: "40730", 35: "55",
    36: "872187", 37: "748317", 38: "932718654", 39: "840", 40: "210",
    41: "7652413", 42: "162", 43: "16695334890", 44: "5482660", 45: "1533776805",
    46: "5777", 47: "134043", 48: "9110846700", 49: "296962999629", 50: "997651",
    51: "121313", 52: "142857", 53: "4075", 54: "376", 55: "249",
    56: "972", 57: "153", 58: "26241", 59: "129448", 60: "26033",
    61: "28684", 62: "127035954683", 63: "49", 64: "1322", 65: "272",
    66: "661", 67: "7273", 68: "6531031914842725", 69: "510510", 70: "8319823",
    71: "428570", 72: "303963552391", 73: "7295372", 74: "402", 75: "161667",
    76: "190569291", 77: "71", 78: "55374"
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
    print("Testing Project Euler Solutions (Problems 26-78)")
    print("=" * 55)
    
    passed = 0
    failed = 0
    failures = []
    
    for problem_num in range(26, 79):
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
    
    print("\n" + "=" * 55)
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