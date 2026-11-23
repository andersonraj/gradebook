import pytest

from gradebook.grades import GradeBook


@pytest.fixture
def book():
    b = GradeBook()
    b.add_student("Ana")
    b.add_grade("Ana", 90)
    b.add_grade("Ana", 80)
    return b


def test_add_duplicate_student_raises(book):
    with pytest.raises(ValueError):
        book.add_student("Ana")


def test_add_grade_unknown_student_raises(book):
    with pytest.raises(KeyError):
        book.add_grade("Bob", 50)


def test_add_grade_out_of_range_raises(book):
    with pytest.raises(ValueError):
        book.add_grade("Ana", 101)


def test_average(book):
    assert book.average("Ana") == 85


def test_average_no_grades():
    b = GradeBook()
    b.add_student("Cy")
    assert b.average("Cy") == 0


def test_letter_grade(book):
    assert book.letter_grade("Ana") == "B"


def test_report_with_grades(book):
    assert book.report("Ana") == "Ana: 85.0 (Passing)"


def test_report_unknown_student(book):
    assert book.report("Zed") == "Student not found"


def test_class_statistics(book):
    book.add_student("Ben")
    book.add_grade("Ben", 60)
    stats = book.class_statistics()
    assert stats["highest"] == 85
    assert stats["lowest"] == 60