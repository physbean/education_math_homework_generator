=================================
education_math_homework_generator
=================================


.. image:: https://img.shields.io/pypi/v/education_math_homework_generator.svg
        :target: https://pypi.python.org/pypi/education_math_homework_generator

.. image:: https://img.shields.io/travis/physbean/education_math_homework_generator.svg
        :target: https://travis-ci.com/physbean/education_math_homework_generator

.. image:: https://pyup.io/repos/github/physbean/education_math_homework_generator/shield.svg
     :target: https://pyup.io/repos/github/physbean/education_math_homework_generator/
     :alt: Updates

.. image:: https://readthedocs.org/projects/education-math-homework-generator/badge/?version=latest
        :target: https://education-math-homework-generator.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/physbean/education_math_homework_generator/python-3-shield.svg
     :target: https://pyup.io/repos/github/physbean/education_math_homework_generator/
     :alt: Python 3

A repository of simple, scalable mathematics homework generator using python and latex to create pdfs for early childhood education.
Customizable tools are also included to be used as an aid, including customizable number lines and tables. 
This project was started for self-learning on common distribution tools and utilities, but given the number of families now homeschooling their children because of SARS-CoV-2, this seemed like the most useful side project to put out there for the world. Any feedback or requests are welcome as I continue to learn project structure and all the other tools defined in this template (link below).

Recently added gen_measurement code that allows the practice of measurements of common shapes: lines, rectangles, and circles. These are intended to be used with a ruler of some sort (or you can use the blocks variant for younger learners). This generator will probably be extended to younger age ranges by generating pairs to work on comparisons (larger/smaller) and extended to older age ranges by inclusion of area computation and/or 3d shapes. 
I am working on adding problem generators that include working with time, money, and ratios currently (reading up on the standards of a few states currently for ideas/guidance).
I would also like to add generating N pages of a problem type as an user optioni (complete for gen_add_subtract) as well as more mixed mode types to work on attention and identification of the operators/shapes/etc as a progression option. 

Proper credits to latex examples used in this repo have been added below as well as at the top of each respective source file. Apologies for not doing this from the start.

* Free software: MIT license
* Documentation: https://education-math-homework-generator.readthedocs.io.

[ ~ Dependencies scanned by PyUp.io ~ ]

Features
--------

* Generation of problems for learning addition, subtraction, and multiplication
* Tools to aid the student such as customizable number lines and tables.


Credits
-------

* SARS-CoV-2 
* latex formating addition/subtraction alignment examples https://tex.stackexchange.com/questions/132321/generate-analog-clock-with-numbered-face/
* latex formating shape examples: https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ:_A_Tutorial_for_Beginners_(Part_1)%E2%80%94Basic_Drawing
* latex formating number line: https://tex.stackexchange.com/questions/148252/help-drawing-a-very-simple-number-line-using-tikz
* latex formating tables: https://tex.stackexchange.com/questions/210670/addition-and-multiplication-tables
* latex formating clocks: https://tex.stackexchange.com/questions/132321/generate-analog-clock-with-numbered-face (NYI) 

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
