import argparse
import random

from education_math_homework_generator.pdflatex_functions import convert_latex_to_pdf
from education_math_homework_generator.pdflatex_functions import remove_temporary_files


# Credits:
# latex formatting adopted from stackexchange
# https://tex.stackexchange.com/questions/11702/how-to-present-a-vertical-multiplication-addition

def generate_problems(number_of_problems=2, maximum_integer=50, problem_type='Addition', number_of_pages=1):
    """
    Generates random example math problems in latex format for practicing Addition, Subtraction, or Multiplication
    :param number_of_problems: defines how many problems to generate
    :param maximum_integer: defines the maximum integer possible during the generation of problems
    :param problem_type: type of problems to generate. options are Addition, Subtraction, or Multiplication
    :return: contents of the latex document as a string
    """
    operator = {'Addition': '+',
                'Subtraction': '-',
                'Multiplication': '*'}

    lines = [r'\documentclass{article}',
             r'\usepackage{amsmath}',
             r'\usepackage{amsfonts}',
             r'\usepackage{amssymb}',
             r'\usepackage{multicol}',
             r'\begin{document}']

    for index, page in enumerate(range(number_of_pages)):
        lines.append(r'{\Large ' + problem_type + r' practice version 0.1\par}')
        lines.append(r'{\large using max integer = ' + str(maximum_integer) + r'\par}')
        lines.append(r'\begin{multicols}{2}')
        lines.append(r'\begin{large}')
        lines.append(r'\begin{enumerate}')

        for _ in range(number_of_problems):
            lines.append(r'\item')
            lines.append(r'\begin{tabular}{lr}')
            int_1 = random.randint(1, maximum_integer)
            int_2 = random.randint(1, maximum_integer)
            if int_1 < int_2:
                int_2, int_1 = int_1, int_2
            int_1_string = ' '.join(iter(str(int_1)))
            int_2_string = ' '.join(iter(str(int_2)))
            lines.append(r' & ' + int_1_string + r'\\')
            lines.append(operator[problem_type] + r'& ' + int_2_string + r'\\')
            lines.append(r'\hline')
            lines.append(r' &    \\')
            lines.append(r'\end{tabular}')
            lines.append(r'\vspace*{50px}')

        lines.append(r'\end{enumerate}')
        lines.append(r'\end{large}')
        lines.append(r'\end{multicols}')

        # generate the next set of problems on a new page for student i
        if index != number_of_pages:
            lines.append(r'\newpage')

    lines.append(r'\end{document}')

    return '\n'.join(lines)


def parse_arguments():
    """
    Parse user arguments to modify how the document is generated for problem generation
    :return: parsed args passed by the user or defaults defined below
    """
    operators = ('Addition',
                 'Subtraction',
                 'Mixed')

    parser = argparse.ArgumentParser(description='Generate a numberline to practice Addition/Subtraction')
    parser.add_argument('--maximum_integer', default=10, type=int, help='maximum integer to use in generation')
    parser.add_argument('--numproblems', default=10, type=int, help='number of problems to generate')
    parser.add_argument('--problemtype', default='Addition', help='number of lines to generate')
    parser.add_argument('--filename', default='math_homework_01.tex', help='filename to generate')
    parser.add_argument('--numpages', default=10, help='Generate multiple pages for entire class or for extra practice')
    args = parser.parse_args()

    assert args.problemtype in operators, '{} not a valid problemtype, only {}'.format(args.problemtype, ', '.join([x for x in operators]))
    return args


def generate_problems_pdf(args):
    """
    Takes the parsed arguments, generates appropriate latex, converts it a pdf, and cleans up any temporary files
    :param args: parsed arguments that define how to generate the document
    """
    contents = generate_problems(number_of_problems=args.numproblems, maximum_integer=args.maximum_integer, problem_type=args.problemtype, number_of_pages=args.numpages)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_problems_pdf(parse_arguments())
