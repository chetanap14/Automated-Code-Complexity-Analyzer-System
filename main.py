"""

file = open("input_code/sample_code.py", "r")

lines = file.readlines()

for line in lines:
    print(line.strip())
"""
"""
from analyzer.loop_detector import detect_loops

file = open("input_code/sample_code.py", "r")

lines = file.readlines()

loop_count = detect_loops(lines)

print("Loops detected:", loop_count)
"""


"""
from analyzer.loop_detector import detect_loop_depth

file = open("input_code/sample_code.py", "r")

lines = file.readlines()

#depth = detect_loop_depth(lines)
depth = detect_loop_depth("".join(lines))

print("Maximum Loop Depth:", depth)
"""
"////////////////////////////////////////////////////////////////////////"
"""

#from analyzer.complexity_estimator import estimate_complexity
import sys
import os
from analyzer.style_checker import check_pep8
from analyzer.infinite_loop_detector import detect_infinite_loops
from analyzer.recursion_detector import detect_recursion
from analyzer.loop_detector import detect_loop_depth
from analyzer.complexity_estimator import estimate_complexity
from analyzer.loop_counter import count_loops
from analyzer.unused_variable_detector import detect_unused_variables
from analyzer.cyclomatic_complexity import calculate_cyclomatic_complexity
from analyzer.function_complexity import function_complexity
from analyzer.code_smell_detector import detect_code_smells
from analyzer.space_complexity import estimate_space_complexity
from analyzer.html_report import generate_html_report

def read_code(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def main():

    # sample file to analyze
    #file_path = os.path.join("samples", "sample1.py")
    #file_path = os.path.join("samples", "sample2.py")
    file_path = os.path.join("samples", "sample3.py")

    # read code
    lines = read_code(file_path)

    # convert list → string for AST parser
    code = "".join(lines)

    # detect loop nesting
    depth = detect_loop_depth(code)

    total_loops = count_loops(code)

    # estimate complexity
    complexity = estimate_complexity(depth)

    recursion_found, functions = detect_recursion(code)

    unused_vars = detect_unused_variables(file_path)

    infinite_loops = detect_infinite_loops(code)
    complexity_score = calculate_cyclomatic_complexity(file_path)
    func_complexity = function_complexity(file_path)
    code_smells = detect_code_smells(file_path)
    space_complexity = estimate_space_complexity(file_path)

    report_html = False
    if len(sys.argv) > 2 and sys.argv[2] == "--report" and sys.argv[3] == "html":
        report_html = True
    # Collect metrics into dictionary
    results = {
        "loop_depth": depth,
        "time_complexity": f"O(n^{depth})",
        "total_loops": total_loops,
        "cyclomatic_complexity": complexity_score,
        "recursion": recursion,
        "infinite_loop": infinite_loop,
        "unused_vars": unused_vars,
        "func_complexity": func_complexity,
        "code_smells": code_smells,
        "space_complexity": space_complexity,
        "style_warnings": check_pep8(file_path)
    }
        # If HTML requested
    """
"""
    if report_html:
        generate_html_report(file_path, results)
"""
"""
    
    if len(sys.argv) > 2 and sys.argv[2] == "--report" and sys.argv[3] == "html":
        generate_html_report(file_path, results)

    else:
        # Print text report
        print("\n===== Code Analysis Report =====")
        print(f"Maximum Loop Depth: {depth}")
        print(f"Estimated Time Complexity: O(n^{depth})")
        print(f"Total Loops Found: {total_loops}")
        print(f"Cyclomatic Complexity: {complexity_score}")
        print(f"Recursion Detected: {'Yes' if recursion else 'No'}")
        print(f"Infinite Loop Risk: {'Yes' if infinite_loop else 'No'}")
        print(f"Unused Variables: {unused_vars}")
        print("\nFunction Complexity:")
        for func, score in func_complexity.items():
            print(f" - {func}: {score}")
        print("\nCode Smells Detected:")
        for smell in code_smells:
            print(f"⚠ {smell}")
        print("\nSpace Complexity:", space_complexity)
        print("\nPEP8 / Style Warnings:")
        for style in results["style_warnings"]:
            print(f"⚠ {style}")
    

        



    print("\n===== Code Analysis Report =====")
    print("Maximum Loop Depth:", depth)
    print("Estimated Time Complexity:", complexity)
    print("Total Loops Found:", total_loops)
    print("Unused Variables:", unused_vars)
    print("Cyclomatic Complexity:", complexity_score)

    print("\nFunction Complexity:")
    for func, score in func_complexity.items():
        print(f" - {func}: {score}")

    print("\nCode Smells Detected:")
    for smell in code_smells:
        print(f"⚠ {smell}")

    print("\nEstimated Space Complexity:", space_complexity)



    
    if recursion_found:
        print("Recursion Detected: Yes")
        print("Recursive Functions:", functions)
    else:
        print("Recursion Detected: No")
        
    if infinite_loops:
        print("Infinite Loop Risk: Yes")
        
        for loop in infinite_loops:
            print("Warning:", loop)
    else:
        print("Infinite Loop Risk: No")
    
    


if __name__ == "__main__":
    main()
"""
"""
import sys
import os
from analyzer.loop_detector import detect_loop_depth
from analyzer.loop_counter import count_loops
from analyzer.time_complexity import estimate_time_complexity
from analyzer.cyclomatic_complexity import calculate_cyclomatic_complexity
from analyzer.recursion_detector import detect_recursion
from analyzer.infinite_loop_detector import detect_infinite_loop
from analyzer.unused_variable_detector import detect_unused_variables
from analyzer.function_complexity import function_complexity
from analyzer.code_smell_detector import detect_code_smells
from analyzer.space_complexity import estimate_space_complexity
from analyzer.style_checker import check_pep8
from analyzer.html_report import generate_html_report

def read_code(file_path):

#Read file and return content as string

    with open(file_path, "r") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path> [--report html]")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: file '{file_path}' not found")
        sys.exit(1)

    code = read_code(file_path)
    lines = code.splitlines()

    # --- Analysis ---
    try:
        depth = detect_loop_depth(lines)
    except:
        depth = 0

    try:
        total_loops = count_loops(code)
    except:
        total_loops = 0

    try:
        complexity_score = calculate_cyclomatic_complexity(file_path)
    except:
        complexity_score = 0

    try:
        recursion = detect_recursion(code)
    except:
        recursion = False

    try:
        infinite_loop = detect_infinite_loop(code)
    except:
        infinite_loop = False

    try:
        unused_vars = detect_unused_variables(file_path)
    except:
        unused_vars = []

    try:
        func_complexity = function_complexity(file_path)
    except:
        func_complexity = {}

    try:
        code_smells = detect_code_smells(file_path)
    except:
        code_smells = []

    try:
        space_complexity = estimate_space_complexity(file_path)
    except:
        space_complexity = "O(1)"

    try:
        style_warnings = check_pep8(file_path)
    except:
        style_warnings = []

    # --- Collect results ---
    complexity = estimate_time_complexity(depth)


    results = {
        "max_loop_depth": depth,
        "time_complexity": complexity,
        "total_loops": loop_count,
        "cyclomatic_complexity": cyclomatic,
        "recursion": recursion,
        "infinite_loop": infinite_loop,
        "unused_variables": unused_vars
    }
    

    # --- Check CLI for HTML report ---
    if len(sys.argv) > 2 and sys.argv[2] == "--report" and len(sys.argv) > 3 and sys.argv[3] == "html":
        generate_html_report(file_path, results)
    else:
        # --- Print text report ---
        print("\n===== Code Analysis Report =====")
        print(f"Maximum Loop Depth: {depth}")
        print(f"Estimated Time Complexity: O(n^{depth})")
        print(f"Total Loops Found: {total_loops}")
        print(f"Unused Variables: {unused_vars}")
        print(f"Cyclomatic Complexity: {complexity_score}")
        print(f"Recursion Detected: {'Yes' if recursion else 'No'}")
        print(f"Infinite Loop Risk: {'Yes' if infinite_loop else 'No'}")
        if infinite_loop:
            print("Warning: while True loop detected")
        print("\nFunction Complexity:")
        for func, score in func_complexity.items():
            print(f" - {func}: {score}")
        print("\nCode Smells Detected:")
        for smell in code_smells:
            print(f"⚠ {smell}")
        print("\nSpace Complexity:", space_complexity)
        print("\nPEP8 / Style Warnings:")
        for style in style_warnings:
            print(f"⚠ {style}")

if __name__ == "__main__":
    main()
"""
"""

import argparse
import os

from analyzer.loop_detector import detect_loop_depth
from analyzer.loop_counter import count_loops
from analyzer.time_complexity import estimate_time_complexity
from analyzer.recursion_detector import detect_recursion
from analyzer.infinite_loop_detector import detect_infinite_loop
from analyzer.unused_variable_detector import detect_unused_variables
from analyzer.cyclomatic_complexity import calculate_cyclomatic_complexity
from analyzer.html_report_generator import generate_html_report
from analyzer.ai_bug_detector import detect_ai_bugs

def read_code(file_path):
    with open(file_path, "r") as file:
        return file.read()


def get_python_files(path):

    python_files = []

    if os.path.isfile(path):
        python_files.append(path)

    elif os.path.isdir(path):

        for root, dirs, files in os.walk(path):

            for file in files:

                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

    return python_files




def main():

    parser = argparse.ArgumentParser(description="Code Complexity Analyzer")

    parser.add_argument("file", help="Python file to analyze")

    parser.add_argument(
        "--report",
        choices=["html"],
        help="Generate HTML report"
    )

    args = parser.parse_args()

    file_path = args.file

    if not os.path.exists(file_path):
        print("File not found.")
        return

    code = read_code(file_path)

    lines = code.split("\n")

    # ---- ANALYSIS ----

    depth = detect_loop_depth(lines)

    complexity = estimate_time_complexity(depth)

    loop_count = count_loops(file_path)

    cyclomatic = calculate_cyclomatic_complexity(file_path)

    recursion = detect_recursion(file_path)

    infinite_loop = detect_infinite_loop(file_path)

    unused_vars = detect_unused_variables(file_path)

    bugs = detect_ai_bugs(file_path)

    file_path = args.file

    files = get_python_files(file_path)

    # ---- RESULTS ----

    results = {
        "max_loop_depth": depth,
        "time_complexity": complexity,
        "total_loops": loop_count,
        "cyclomatic_complexity": cyclomatic,
        "recursion": recursion,
        "infinite_loop": infinite_loop,
        "unused_variables": unused_vars,
        "ai_bugs": bugs
    }

    # ---- PRINT REPORT ----

    print("\n===== Code Analysis Report =====")

    print("Maximum Loop Depth:", depth)

    print("Estimated Time Complexity:", complexity)

    print("Total Loops Found:", loop_count)

    print("Cyclomatic Complexity:", cyclomatic)

    print("Recursion Detected:", "Yes" if recursion else "No")

    print("Infinite Loop Risk:", "Yes" if infinite_loop else "No")

    print("Unused Variables:", unused_vars)

    print("\nAI Bug Detection:")

    if bugs:
        for bug in bugs:
            print("-", bug)
    else:
        print("No AI bugs detected")

    # ---- HTML REPORT ----

    if args.report == "html":

        generate_html_report(results, file_path)

        print("\nHTML report generated successfully: report.html")


if __name__ == "__main__":
    main()
"""

import argparse
import os

from analyzer.loop_detector import detect_loop_depth
from analyzer.loop_counter import count_loops
from analyzer.time_complexity import estimate_time_complexity
from analyzer.recursion_detector import detect_recursion
from analyzer.infinite_loop_detector import detect_infinite_loop
from analyzer.unused_variable_detector import detect_unused_variables
from analyzer.cyclomatic_complexity import calculate_cyclomatic_complexity
from analyzer.html_report_generator import generate_html_report
from analyzer.ai_bug_detector import detect_ai_bugs


def read_code(file_path):
    with open(file_path, "r") as file:
        return file.read()


def get_python_files(path):

    python_files = []

    if os.path.isfile(path):
        python_files.append(path)

    elif os.path.isdir(path):

        for root, dirs, files in os.walk(path):

            for file in files:

                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

    return python_files


def main():

    parser = argparse.ArgumentParser(description="Code Complexity Analyzer")

    parser.add_argument("file", help="Python file to analyze")

    parser.add_argument(
        "--report",
        choices=["html"],
        help="Generate HTML report"
    )

    args = parser.parse_args()

    file_path = args.file

    if not os.path.exists(file_path):
        print("File not found.")
        return

    # ---- READ CODE ----

    code = read_code(file_path)

    lines = code.split("\n")

    # ---- ANALYSIS ----

    depth = detect_loop_depth(lines)

    complexity = estimate_time_complexity(depth)

    loop_count = count_loops(file_path)

    cyclomatic = calculate_cyclomatic_complexity(file_path)

    recursion = detect_recursion(file_path)

    infinite_loop = detect_infinite_loop(file_path)

    unused_vars = detect_unused_variables(file_path)

    bugs = detect_ai_bugs(file_path)

    files = get_python_files(file_path)

    # ---- RESULTS ----

    results = {
        "max_loop_depth": depth,
        "time_complexity": complexity,
        "total_loops": loop_count,
        "cyclomatic_complexity": cyclomatic,
        "recursion": recursion,
        "infinite_loop": infinite_loop,
        "unused_variables": unused_vars,
        "ai_bugs": bugs
    }

    # ---- PRINT REPORT ----

    print("\n===== Code Analysis Report =====")

    print("Maximum Loop Depth:", depth)

    print("Estimated Time Complexity:", complexity)

    print("Total Loops Found:", loop_count)

    print("Cyclomatic Complexity:", cyclomatic)

    print("Recursion Detected:", "Yes" if recursion else "No")

    print("Infinite Loop Risk:", "Yes" if infinite_loop else "No")

    print("Unused Variables:", unused_vars)

    print("\nAI Bug Detection:")

    if bugs:
        for bug in bugs:
            print("-", bug)
    else:
        print("No AI bugs detected")

    # ---- HTML REPORT ----

    if args.report == "html":

        generate_html_report(results, file_path)

        print("\nHTML report generated successfully: report.html")


if __name__ == "__main__":
    main()































    
