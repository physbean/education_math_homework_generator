import argparse
import math
import random

from education_math_homework_generator.util import convert_latex_to_pdf
from education_math_homework_generator.util import remove_temporary_files


# Credits:
# Code to generate lines and shapes from overleaf:
# https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ:_A_Tutorial_for_Beginners_(Part_1)%E2%80%94Basic_Drawing


def gen_line():
    length = random.randint(30, 70) / 10
    angle = random.choice([0.0, 30.0, 45.0, 60.0, 90.0])
    x = str(math.sin(math.radians(angle)) * length)
    y = str(math.cos(math.radians(angle)) * length)
    return r'\draw (0,0) -- ' + '({},{})'.format(x, y) + r';'


def gen_rectangle():
    length = str(random.randint(10, 60) / 10)
    width = str(random.randint(10, 60) / 10)
    if width > length:
        length, width = width, length
    return r'\draw (0,0) -- (' + length + r',0) -- ' + '({},{})'.format(length, width) + r' -- (0,' + width + r') -- (0,0);'


def gen_circle():
    radius = str(random.randint(10, 40) / 10)
    return r'\draw (0,0) circle (' + radius + r'cm);'


def generate_measurement_problems(shape='lines', number_of_problems=10):
    lines = [r'\documentclass[letterpaper]{article}',
             r'\usepackage{amsmath}',
             r'\usepackage{amsfonts}',
             r'\usepackage{amssymb}',
             r'\usepackage{multicol}',
             r'\usepackage{geometry}',
             r'\geometry{portrait,a4paper,total={170mm,257mm},left=10mm,right=10mm,top=30mm}',
             r'\usepackage{tikz}',
             r'\begin{document}', r'{\Large Measuring ' + shape + r' practice version 0.1\par}',
             r'\vspace*{50px}',
             r'\begin{large}',
             r'\begin{multicols}{2}',
             r'\begin{enumerate}']

    for i in range(number_of_problems):
        lines.append(r'\item')
        lines.append(r'\begin{tikzpicture}')
        if shape == 'lines':
            lines.append(gen_line())
        if shape == 'rectangles':
            lines.append(gen_rectangle())
        if shape == 'circles':
            lines.append(gen_circle())
        if shape == 'mixed':
            lines.append(random.choice([gen_line(), gen_rectangle(), gen_circle()]))
        lines.append(r'\end{tikzpicture}')
        lines.append(r'\vspace*{10px}')

    lines.append(r'\end{enumerate}')
    lines.append(r'\end{multicols}')
    lines.append(r'\end{large}')
    lines.append(r'\end{document}')

    return '\n'.join(lines)


def parse_arguments():
    """
    Parse user arguments to modify how the document is generated for tables
    :return: parsed args passed by the user or defaults defined below
    """
    shapes = ('lines', 'rectangles', 'circles', 'mixed')

    parser = argparse.ArgumentParser(description='Generate shapes to practice measuring')
    parser.add_argument('--number_of_problems', default=10, type=int, help='Number of problems to generate')
    parser.add_argument('--shape', default='mixed', help='Type of shape to measure')
    parser.add_argument('--filename', default='measurements_01.tex', help='filename to generate')
    args = parser.parse_args()

    assert args.shape in shapes, '{} not a valid table_type, only {}'.format(args.table_type, ', '.join([x for x in shapes]))
    return args


def generate_measurement_problems_pdf(args):
    """
    Takes the parsed arguments, generates appropriate latex, converts it a pdf, and cleans up any temporary files
    :param args: parsed arguments that define how to generate the document
    """
    contents = generate_measurement_problems(shape=args.shape, number_of_problems=args.number_of_problems)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_measurement_problems_pdf(parse_arguments())
