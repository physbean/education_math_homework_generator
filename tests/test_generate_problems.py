#!/usr/bin/env python

"""Tests for 'education_math_homework_generator.gen_add_subtract' package."""

from education_math_homework_generator.gen_add_subtract import generate_problems
from education_math_homework_generator.pdflatex_functions import convert_latex_to_pdf
from education_math_homework_generator.pdflatex_functions import remove_temporary_files


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
