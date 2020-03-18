import argparse
import random

from education_math_homework_generator.util import convert_latex_to_pdf
from education_math_homework_generator.util import remove_temporary_files


def generate_problems(number_of_problems=2, maximum_integer=50, problem_type='Addition'):
    lines = [r'\documentclass{article}',
             r'\usepackage{amsmath}',
             r'\usepackage{amsfonts}',
             r'\usepackage{amssymb}',
             r'\usepackage{multicol}',
             r'\begin{document}', r'{\Large ' + problem_type + r' practice version 0.1\par}',
             r'{\large using max integer = ' + str(maximum_integer) + r'\par}',
             r'\begin{multicols}{2}',
             r'\begin{large}',
             r'\begin{enumerate}']

    operator = {'Addition': '+',
                'Subtraction': '-',
                'Multiplication': '*'}

    for i in range(number_of_problems):
        lines.append(r'\item')
        lines.append(r'\begin{tabular}{lr}')
        int_1 = random.randint(1, maximum_integer)
        int_2 = random.randint(1, maximum_integer)
        if int_1 < int_2:
            int_2, int_1 = int_1, int_2
        int_1_string = ' '.join(x for x in str(int_1))
        int_2_string = ' '.join(x for x in str(int_2))
        lines.append(r' & ' + int_1_string + r'\\')
        lines.append(operator[problem_type] + r'& ' + int_2_string + r'\\')
        lines.append(r'\hline')
        lines.append(r' &    \\')
        lines.append(r'\end{tabular}')
        lines.append(r'\vspace*{50px}')

    lines.append(r'\end{enumerate}')
    lines.append(r'\end{large}')
    lines.append(r'\end{multicols}')
    lines.append(r'\end{document}')

    return '\n'.join(lines)


def parse_arguments():
    operators = ('Addition',
                 'Subtraction',
                 'Mixed')

    parser = argparse.ArgumentParser(description='Generate a numberline to practice Addition/Subtraction')
    parser.add_argument('--maximum_integer', default=10, type=int, help='maximum integer to use in generation')
    parser.add_argument('--numproblems', default=10, type=int, help='number of problems to generate')
    parser.add_argument('--problemtype', default='Addition', help='number of lines to generate')
    parser.add_argument('--filename', default='math_homework_01.tex', help='filename to generate')
    args = parser.parse_args()

    assert args.problemtype in operators, '{} not a valid problemtype, only {}'.format(args.problemtype, ', '.join([x for x in operators]))
    return args


def generate_problems_pdf(args):
    contents = generate_problems(number_of_problems=args.numproblems, maximum_integer=args.maximum_integer, problem_type=args.problemtype)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_problems_pdf(parse_arguments())
