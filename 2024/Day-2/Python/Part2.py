from Util import read_input
from Part1 import is_safe


# Part Two:
# The Problem Dampener allows the reactor safety systems to tolerate a single bad level.
# If removing a single level from an unsafe report makes it safe, the report counts as safe.

# Given the same input as Part 1, count the number of reports that are safe after removing a single level.

def count_safe_reports_with_level_remove(reports):
    # Define the count of safe reports
    safe_reports = 0
    # Iterate through the reports
    for report in reports:
        # Check if the report is safe
        if is_safe_with_level_remove(report):
            # Increment the count of safe reports
            safe_reports += 1
    # Return the count of safe reports
    return safe_reports


def convert_report_to_differences(report):
    # convert the report to a list of differences between consecutive elements
    return [report[i] - report[i - 1] for i in range(1, len(report))]

def check_if_increasing_or_decreasing(differences):
    # check if the differences all have the same sign
    return all(difference > 0 for difference in differences) or all(difference < 0 for difference in differences)

def check_if_differences_are_valid(differences):
    # check if the differences are between 1 and 3
    return all(abs(difference) >= 1 and abs(difference) <= 3 for difference in differences)

def is_safe_with_level_remove(report):
    # convert the report to a list of differences
    differences = convert_report_to_differences(report)
    # check if the differences are valid and increasing or decreasing
    if check_if_differences_are_valid(differences) and check_if_increasing_or_decreasing(differences):
        return True
    # iterate through the differences
    for i in range(len(report)):
        # remove the i-th report level and create a new list of differences
        new_differences = convert_report_to_differences(report[:i] + report[i + 1:])
        # check if the new differences are valid
        if check_if_differences_are_valid(new_differences) and check_if_increasing_or_decreasing(new_differences):
            return True
    return False




def main():
    # read the input
    reports = read_input()
    # count the safe reports
    safe_reports = count_safe_reports_with_level_remove(reports)
    # print the number of safe reports
    print(safe_reports)

main()
