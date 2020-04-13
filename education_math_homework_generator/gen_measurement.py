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
    radius = random.randint(15, 35) / 10
    radius_line = r'\draw ' + '({},{}) -- ({},{});'.format('0', '0', '0', str(radius))
    diameter_line = r'\draw ' + '({},{}) -- ({},{});'.format(str(-1 * radius), '0', str(radius), '0')
    circle_line = r'\draw (0,0) circle (' + str(radius) + r');'
    return '\n'.join([circle_line, diameter_line, radius_line])


def gen_block_rectangle():
    length = random.randint(1, 8)
    width = random.randint(1, 8)
    if width > length:
        length, width = width, length
    grid = r'\draw[step=1cm,gray,very thin] ' + '(0,0) grid ({},{});'.format(length, width)
    return grid


def generate_measurement_problems(shape='lines', number_of_problems=10):
    lines = [r'\documentclass[letterpaper]{article}',
             r'\usepackage{amsmath}',
             r'\usepackage{amsfonts}',
             r'\usepackage{amssymb}',
             r'\usepackage{multicol}',
             r'\usepackage{geometry}',
             r'\geometry{portrait,a4paper,total={170mm,257mm},left=10mm,right=10mm,top=30mm}',
             r'\usepackage{tikz}',
             r'\begin{document}', r'{\Large Measuring ' + shape + r' practice version 0.3\par}',
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
        if shape == 'rectangles-blocks':
            lines.append(gen_block_rectangle())
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

    print('\n'.join(lines))
    return '\n'.join(lines)


def parse_arguments():
    """
    Parse user arguments to modify how the document is generated for tables
    :return: parsed args passed by the user or defaults defined below
    """
    shapes = ('lines', 'rectangles', 'circles', 'mixed', 'rectangles-blocks')

    parser = argparse.ArgumentParser(description='Generate shapes to practice measuring')
    parser.add_argument('--number_of_problems', default=10, type=int, help='Number of problems to generate')
    parser.add_argument('--shape', default='mixed', help='Type of shape to measure')
    parser.add_argument('--filename', default='measurements_01.tex', help='filename to generate')
    parser.add_argument('--use_blocks', default=False, help='Use generic blocks so no ruler is required - only rectangles')
    args = parser.parse_args()

    if args.use_blocks:
        assert args.shape == 'rectangles', 'Only rectangles are available in block mode'
        args.shape = 'rectangles-blocks'
    assert args.shape in shapes, '{} not a valid table_type, only {}'.format(args.table_type, ', '.join([x for x in shapes]))
    return args


def generate_measurement_problems_pdf(args):
    """
    Takes the parsed arguments, generates appropriate latex, converts it a pdf, and cleans up any temporary files
    Blocks option allows the generation of simple blocks to generate rectangles to be able to measure without a ruler.
    This option will also extend to multiplication and area concepts easily going forward.
    :param args: parsed arguments that define how to generate the document
    """
    contents = generate_measurement_problems(shape=args.shape, number_of_problems=args.number_of_problems)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_measurement_problems_pdf(parse_arguments())
