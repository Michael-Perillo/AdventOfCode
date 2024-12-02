from Util import read_input

# Problem Statement: Count the "safe" reports
# input: a list of reports
# a report is a list of integers

# a report only counts as safe if both of the following are true:
# The integers are either all increasing or all decreasing.
# Any two adjacent integers differ by at least one and at most three.

def count_safe_reports(reports):
    # Define the count of safe reports
    safe_reports = 0
    print(len(reports))
    # Iterate through the reports
    for report in reports:
        # Check if the report is safe
        if is_safe(report):
            # Increment the count of safe reports
            safe_reports += 1
    # Return the count of safe reports
    return safe_reports

def is_safe(report):
    """
    Determines if a given report is "safe" based on specific criteria.

    A report is considered "safe" if the differences between consecutive
    elements are either all increasing or all decreasing, and each difference
    is between 1 and 3 (inclusive).

    Args:
        report (list of int): A list of integers representing the report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    increasing = True
    decreasing = True
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        if difference < 0:
            increasing = False
        if difference > 0:
            decreasing = False
    return increasing or decreasing


def main():
    # read the input
    reports = read_input()
    # count the safe reports
    safe_reports = count_safe_reports(reports)
    # print the number of safe reports
    print(safe_reports)

main()
