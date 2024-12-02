
input_file_path = "2024\Day-2\Input.txt"

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# This example data contains six reports each containing five levels.

def read_input():
    # Read the input file
    with open(input_file_path, "r") as file:
        reports = []
        for line in file:
            # Read the report
            report = [int(elem) for elem in line.split()]
            # Add the report to the list
            reports.append(report)
        # Return the list of reports
        return reports
