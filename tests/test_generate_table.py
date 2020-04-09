#!/usr/bin/env python

"""Tests for 'education_math_homework_generator.gen_table' package."""

from education_math_homework_generator.gen_table import generate_table
from education_math_homework_generator.util import convert_latex_to_pdf
from education_math_homework_generator.util import remove_temporary_files


def test_generate_table():
    contents = generate_table(start_int=0, end_int=10, table_type='Addition')
    assert contents is not None


def test_generate_addition_table_to_pdf():
    filename = 'test_generate_addition_table_to_pdf.tex'
    contents = generate_table(start_int=0, end_int=10, table_type='Addition')
    convert_latex_to_pdf(filename=filename, contents=contents, view=True)
    remove_temporary_files(filename)


def test_generate_subtraction_table_to_pdf():
    filename = 'test_generate_subtraction_table_to_pdf.tex'
    contents = generate_table(start_int=0, end_int=10, table_type='Subtraction')
    convert_latex_to_pdf(filename=filename, contents=contents, view=True)
    remove_temporary_files(filename)


def test_generate_multiplication_table_to_pdf():
    filename = 'test_generate_multiplication_table_to_pdf.tex'
    contents = generate_table(start_int=0, end_int=10, table_type='Multiplication')
    convert_latex_to_pdf(filename=filename, contents=contents, view=True)
    remove_temporary_files(filename)
