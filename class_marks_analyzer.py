import numpy as np


# =====================================
# CLASS MARKS ANALYZER
# =====================================

# Step 1: Function to take student marks
def get_marks():

    print("\n===== CLASS MARKS ANALYZER =====")

    user_input = input(
        "Enter student marks separated by spaces: "
    )

    marks = []

    # Step 2: Validate marks
    for value in user_input.split():

        try:
            mark = float(value)

        except ValueError:
            print(f"Invalid marks '{value}'. Enter numbers only.")
            return None

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return None

        marks.append(mark)

    if len(marks) == 0:
        print("Please enter at least one student's marks.")
        return None

    return np.array(marks)


# Step 3: Analyze student marks
def analyze_marks(marks):

    mean = np.mean(marks)
    median = np.median(marks)
    maximum = np.max(marks)
    minimum = np.min(marks)
    std_dev = np.std(marks)

    # Step 4: Count passed and failed students
    passed = np.sum(marks >= 40)
    failed = len(marks) - passed

    # Step 5: Calculate pass percentage
    pass_percentage = (passed / len(marks)) * 100

    # Step 6: Count students above average
    above_average = np.sum(marks > mean)

    # Step 7: Display results
    print("\n========== ANALYSIS RESULT ==========")

    print(f"Total Students: {len(marks)}")

    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")

    print(f"Max: {maximum:g}")
    print(f"Min: {minimum:g}")

    print(f"Std Dev: {std_dev:.2f}")

    print(f"Passed: {passed} of {len(marks)}")
    print(f"Failed: {failed}")

    print(f"Pass Percentage: {pass_percentage:.2f}%")

    print(f"Above Average: {above_average} students")

    print("=====================================")


# Step 8: Main function
def main():

    marks = get_marks()

    if marks is not None:
        analyze_marks(marks)


# Step 9: Run program
if __name__ == "__main__":
    main()