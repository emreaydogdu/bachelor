import timeit

# Define the code to be benchmarked
code_to_test = """
print('hello world')
"""

# Run the benchmark
execution_time = timeit.timeit(code_to_test, number=10000000)

print(f"Execution time: {execution_time} seconds")