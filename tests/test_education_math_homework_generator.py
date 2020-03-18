#!/usr/bin/env python

"""Tests for `education_math_homework_generator` package."""

from education_math_homework_generator.gen_add_subtract import generate_problems
from education_math_homework_generator.gen_number_line import generate_number_lines
from education_math_homework_generator.util import convert_latex_to_pdf
from education_math_homework_generator.util import remove_temporary_files
from education_math_homework_generator.util import write_latex_data_to_file


def test_write_latex_data_to_file():
    filename = 'test_write.tex'
    contents = r"""
    \documentclass{article}
    \begin{document}
    Test page
    \end{document}
    """
    write_latex_data_to_file(filename=filename, contents=contents)
    with open(filename) as fileio:
        assert fileio.read() == contents
    remove_temporary_files(filename)


def test_convert_latex_to_pdf():
    filename = 'test_convert.tex'
    contents = r"""
    \documentclass{article}
    \begin{document}
    Test page
    \end{document}
    """
    convert_latex_to_pdf(filename=filename, contents=contents)
    remove_temporary_files(filename)


def test_generate_problems_addition():
    contents = generate_problems(number_of_problems=10, maximum_integer=50, problem_type='Addition')
    assert contents.count('+') == 10


def test_generate_problems_addition_large_int():
    contents = generate_problems(number_of_problems=10, maximum_integer=1000, problem_type='Addition')
    assert contents.count('+') == 10


def test_generate_problems_subtraction():
    contents = generate_problems(number_of_problems=10, maximum_integer=50, problem_type='Subtraction')
    assert contents.count('-') == 10


def test_generate_problems_to_pdf():
    filename = 'test_generate_problems_and_convert.tex'
    contents = generate_problems(number_of_problems=10, maximum_integer=10, problem_type='Addition')
    convert_latex_to_pdf(filename=filename, contents=contents, view=True)
    remove_temporary_files(filename)


def test_gen_number_line():
    contents = generate_number_lines(number_of_lines=5, start=0, end=20)
    assert contents is not None


def test_gen_number_line_to_pdf():
    filename = 'test_numberline.tex'
    contents = generate_number_lines(number_of_lines=5, start=0, end=20)
    convert_latex_to_pdf(filename=filename, contents=contents, view=True)
    remove_temporary_files(filename)
