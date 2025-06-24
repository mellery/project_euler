#!/usr/bin/env python3
import subprocess
import sys
import time

# Test the slowest problems we've seen
SLOW_PROBLEMS = [12, 14, 21, 34, 44, 43, 47]

EXPECTED_ANSWERS = {
    12: "76576500", 14: "837799", 21: "31626", 34: "40730", 
    44: "5482660", 43: "16695334890", 47: "134043"
}

def run_problem(filename):
    try:
        start_time = time.time()
        result = subprocess.run(
            [sys.executable, filename], 
            capture_output=True, 
            text=True, 
            timeout=60
        )
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            return None, f"Error: {result.stderr.strip()}", elapsed
        
        lines = result.stdout.strip().split('\n')
        if lines:
            return lines[-1].strip(), None, elapsed
        else:
            return None, "No output", elapsed
            
    except subprocess.TimeoutExpired:
        return None, "Timeout (60s exceeded)", 60
    except Exception as e:
        return None, f"Exception: {str(e)}", 0

def main():
    print("Testing Slow Problems")
    print("=" * 30)
    
    for problem_num in SLOW_PROBLEMS:
        filename = f"problem{problem_num}.py"
        print(f"Testing {filename}...", end=" ")
        
        actual_output, error, elapsed = run_problem(filename)
        
        if error:
            print(f"FAIL ({error}) - {elapsed:.2f}s")
            continue
            
        expected = EXPECTED_ANSWERS.get(problem_num)
        if actual_output == expected:
            print(f"PASS - {elapsed:.2f}s")
        else:
            print(f"FAIL (expected: {expected}, got: {actual_output}) - {elapsed:.2f}s")

if __name__ == "__main__":
    main()