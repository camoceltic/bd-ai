from functions.get_files_info import get_files_info

test_cases = [".", "pkg", "/bin", ".."]

for i in test_cases:
    print(f"Result for {i}")
    print(get_files_info("calculator", i))
