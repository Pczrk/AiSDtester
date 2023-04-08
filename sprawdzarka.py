import os

passed = 0
input_dir = './in'
output_dir = './out'
program = 'solver.py'
tests = 200  # ilosc testow

input_files = ["in" + str(num) for num in range(1, tests+1)]
output_files = ["out" + str(num) for num in range(1, tests+1)]

for input_file in input_files:
    input_path = os.path.join(input_dir, input_file)

    expected_output_file = input_file.replace('in', 'out')
    expected_output_path = os.path.join(output_dir, expected_output_file)

    temp_output_path = 'temp.txt'
    command = f'python {program} < {input_path} > {temp_output_path}'
    os.system(command)

    try:
        with open(temp_output_path, 'r') as f1, open(expected_output_path, 'r') as f2:
            if f1.read() == f2.read():
                print(f'{input_file} PASSED')
                passed += 1
            else:
                print(f'{input_file} FAILED')
    except FileNotFoundError:
        print(f'{expected_output_path} not found')

    os.remove(temp_output_path)
print(f"\n{passed}/{tests} PASSED")