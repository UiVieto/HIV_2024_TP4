
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade
def test_numerical_letter_grade():# pragma: no cover
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']# pragma: no cover
    assert numerical_letter_grade([1.2]) == ['D+']# pragma: no cover

    # Tests zero shot générés par Salesforce/codet5-large-ntp-py
    # numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.3, 0.0, 0.0, 4.0]) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']  # pragma: no cover

    # Q2.4. Inputs 1 - Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5, 0.75, 0.1, 0.0])  # pragma: no cover

    # Q2.4. Inputs 2 - Tests few shot générés par Salesforce/codet5-large-ntp-py
    # assert numerical_letter_grade([0.75, 0.1, 0.0]) == ['D', 'D-', 'E']  # pragma: no cover

    # Q2.4. Inputs 3 - Tests few shot générés par Salesforce/codet5-large-ntp-py
    assert numerical_letter_grade([4.0, 3, 3.5, 0.75, 0.1, 0.0]) == ['A+', 'B', 'A-', 'D', 'D-', 'E']  # pragma: no cover

    # Test générés avec Qwen2.5-Coder-0.5B-Instruct
    # assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'] # pragma: no cover
