INPUT_FILE_NAME = "reports.dat"
OUTPUT_FILE_NAME = "correct-reports.dat"


def read_file(filename):
    """Read the input file and return a list of integer reports."""
    reports = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            numbers = line.split()
            reports.append([int(num) for num in numbers])

    return reports


def is_valid_report(report):
    """Check whether a report is valid based on ordering and step differences."""
    if report == sorted(report):
        ordered = True
    elif report == sorted(report, reverse=True):
        ordered = True
    else:
        ordered = False

    if not ordered:
        return False

    differences = []
    for i in range(len(report) - 1):
        differences.append(abs(report[i] - report[i + 1]))

    return 0 < min(differences) and max(differences) < 4


def find_correct_reports(reports):
    """Filter and return only valid reports."""
    correct_reports = []

    for report in reports:
        if is_valid_report(report):
            correct_reports.append(report)

    return correct_reports


def write_file(filename, reports):
    """Write valid reports to the output file."""
    with open(filename, "w", encoding="utf-8") as file:
        for report in reports:
            line = " ".join(str(num) for num in report)
            file.write(line + "\n")


def display_statistics(total_reports, correct_reports_count):
    """Print summary statistics."""
    percentage = (correct_reports_count / total_reports) * 100
    print(f"I read {total_reports} reports: {percentage:.2f}% were correct.")


def main():
    reports = read_file(INPUT_FILE_NAME)
    correct_reports = find_correct_reports(reports)

    display_statistics(len(reports), len(correct_reports))
    write_file(OUTPUT_FILE_NAME, correct_reports)

    print("Program finished successfully.")


if __name__ == "__main__":
    main()