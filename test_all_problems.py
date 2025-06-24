#!/usr/bin/env python3
import subprocess
import sys
import glob
import re
import time

# Expected answers for Project Euler problems 1-78
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
    10: "142913828922",
    11: "70600674",
    12: "76576500",
    13: "5537376230",
    14: "837799",
    15: "137846528820",
    16: "1366",
    17: "21124",
    18: "1074",
    19: "171",
    20: "648",
    21: "31626",
    22: "871198282",
    23: "4179871",
    24: "2783915460",
    25: "4782",
    26: "983",
    27: "-59231",
    28: "669171001",
    29: "9183",
    30: "443839",
    31: "73682",
    32: "45228",
    33: "100",
    34: "40730",
    35: "55",
    36: "872187",
    37: "748317",
    38: "932718654",
    39: "840",
    40: "210",
    41: "7652413",
    42: "162",
    43: "16695334890",
    44: "5482660",
    45: "1533776805",
    46: "5777",
    47: "134043",
    48: "9110846700",
    49: "296962999629",
    50: "997651",
    51: "121313",
    52: "142857",
    53: "4075",
    54: "376",
    55: "249",
    56: "972",
    57: "153",
    58: "26241",
    59: "129448",
    60: "26033",
    61: "28684",
    62: "127035954683",
    63: "49",
    64: "1322",
    65: "272",
    66: "661",
    67: "7273",
    68: "6531031914842725",
    69: "510510",
    70: "8319823",
    71: "428570",
    72: "303963552391",
    73: "7295372",
    74: "402",
    75: "161667",
    76: "190569291",
    77: "71",
    78: "55374"
}

def get_problem_files():
    """Get all problem*.py files sorted by problem number"""
    files = glob.glob("problem*.py")
    # Sort by problem number
    def extract_number(filename):
        match = re.search(r'problem(\d+)\.py', filename)
        return int(match.group(1)) if match else 0
    
    return sorted(files, key=extract_number)

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
    print("Testing Project Euler Solutions")
    print("=" * 50)
    
    problem_files = get_problem_files()
    total_tests = len(problem_files)
    passed = 0
    failed = 0
    
    for filename in problem_files:
        # Extract problem number
        match = re.search(r'problem(\d+)\.py', filename)
        if not match:
            continue
            
        problem_num = int(match.group(1))
        
        print(f"Testing {filename}...", end=" ")
        
        if problem_num not in EXPECTED_ANSWERS:
            print("SKIP (no expected answer)")
            continue
            
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
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed, {total_tests} total")
    
    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed!")

if __name__ == "__main__":
    main()