#!/usr/bin/env python

"""Tests for 'education_math_homework_generator.util' package."""

from education_math_homework_generator.gen_number_line import generate_number_lines
from education_math_homework_generator.pdflatex_functions import convert_latex_to_pdf
from education_math_homework_generator.pdflatex_functions import remove_temporary_files


def test_gen_number_line():
    contents = generate_number_lines(number_of_lines=5, start=0, end=20)
    assert contents is not None


def test_gen_number_line_to_pdf():
    filename = 'test_numberline.tex'
    contents = generate_number_lines(number_of_lines=5, start=0, end=20)
    convert_latex_to_pdf(filename=filename, contents=contents, view=True)
    remove_temporary_files(filename)
