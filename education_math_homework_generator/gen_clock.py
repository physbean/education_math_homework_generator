import argparse
import random

from education_math_homework_generator.pdflatex_functions import convert_latex_to_pdf
from education_math_homework_generator.pdflatex_functions import remove_temporary_files


#
# Clock code example taken from stackexchange:
# https://tex.stackexchange.com/questions/132321/generate-analog-clock-with-numbered-face/


def gen_clock(hour, minute):
    # 1-12 -- 360/12 = 30
    # 0-59 -- 360/60 = 6
    hour_degree = 90.0 - hour * 30
    minute_degree = 90.0 - minute * 6
    print(hour, minute)
    lines = [r'\begin{tikzpicture}[line cap = rect, line width = 3 pt]',
             r'\filldraw[fill = white] (0, 0) circle[radius = 2 cm];',
             r'\foreach \angle[count =\xi] in {60, 30, ..., -270}',
             r'{',
             r'  \draw[line width = 1 pt] (\angle:1.8cm) - - (\angle:2cm);',
             r'  \node[font =\large] at(\angle: 1.36 cm) {\textsf{\xi}};',
             r'}',
             r'\foreach \angle in {0, 90, 180, 270}',
             r'\draw[line width = 2 pt] (\angle:1.6cm) - - (\angle:2cm);',
             r'\draw[->][color=black, line width = 3 pt](0, 0) -- (' + str(hour_degree) + ':0.75cm);',
             r'\draw[->][color=blue,line width = 2 pt](0, 0) -- (' + str(minute_degree) + ':1cm);',
             r'\end{tikzpicture}']
    return lines


def generate_clock_problems(problem_type='analog', number_of_problems=10):
    lines = [r'\documentclass[letterpaper]{article}',
             r'\usepackage{amsmath}',
             r'\usepackage{amsfonts}',
             r'\usepackage{amssymb}',
             r'\usepackage{multicol}',
             r'\usepackage{geometry}',
             r'\geometry{portrait,a4paper,total={170mm,257mm},left=10mm,right=10mm,top=30mm}',
             r'\usepackage{tikz}',
             r'\begin{document}', r'{\Large Telling time (type=' + problem_type + r') practice version 0.1\par}',
             r'\vspace*{10px}',
             r'\begin{large}',
             r'\pagenumbering{gobble}',
             r'\begin{multicols}{2}',
             r'\begin{enumerate}']

    for i in range(number_of_problems):
        lines.append(r'\item')
        for line in gen_clock(random.choice(range(0, 12, 1)), random.choice(range(0, 60, 5))):
            lines.append(line)
        lines.append(r'\vspace*{5px}')

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
    problem_types = ('analog')

    parser = argparse.ArgumentParser(description='Generate shapes to practice measuring')
    parser.add_argument('--number_of_problems', default=10, type=int, help='Number of problems to generate')
    parser.add_argument('--problem_type', default='analog', help='Type of shape to measure')
    parser.add_argument('--filename', default='clock_01.tex', help='filename to generate')
    args = parser.parse_args()

    assert args.problem_type in problem_types, '{} not a valid table_type, only {}'.format(args.table_type, ', '.join([x for x in problem_types]))
    return args


def generate_clock_problems_pdf(args):
    """
    Takes the parsed arguments, generates appropriate latex, converts it a pdf, and cleans up any temporary files
    :param args: parsed arguments that define how to generate the document
    """
    contents = generate_clock_problems(problem_type=args.problem_type, number_of_problems=args.number_of_problems)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_clock_problems_pdf(parse_arguments())
