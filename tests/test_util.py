#!/usr/bin/env python

"""Tests for 'education_math_homework_generator.util' package."""

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
