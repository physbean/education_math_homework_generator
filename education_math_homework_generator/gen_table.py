import argparse

from education_math_homework_generator.pdflatex_functions import convert_latex_to_pdf
from education_math_homework_generator.pdflatex_functions import remove_temporary_files


# Credits:
# latex table example code adopted from stackexchange
# https://tex.stackexchange.com/questions/210670/addition-and-multiplication-tables

def generate_table(start_int=0, end_int=10, table_type='Addition'):
    """
    Generates reference tables for learning early childhood mathematics
    :param start_int: start value for the table as an integer
    :param end_int: end value for the table as an integer
    :param table_type: type of table to generate. options are Addition, Subtraction, or Multiplication
    :return:
    """
    lines = [r'\documentclass{article}',
             r'\usepackage{geometry}',
             r'\geometry{landscape,a4paper,total={170mm,257mm},left=10mm,right=10mm,top=10mm}',
             r'\usepackage{amsmath}',
             r'\usepackage{amsfonts}',
             r'\usepackage{amssymb}',
             r'\usepackage{dcolumn}',
             r'\newcolumntype{2}{D{.}{}{2.0}}',
             r'\begin{document}',
             r'\begin{large}',
             r'\begin{center}',
             r'{\Large ' + table_type + r' Table version 0.1\par}',
             r'\vspace*{25px}',
             r'\renewcommand\arraystretch{1.3}',
             r'\setlength\doublerulesep{0pt}',
             r'\begin{tabular}{r||*{' + str(end_int - start_int + 1) + '}{3|}}']

    operator = {'Addition': r'$+$',
                'Subtraction': r'$-$',
                'Multiplication': r'$\times$'}

    lines.append(operator[table_type] + ''.join([' & {} '.format(x) for x in range(start_int, end_int + 1)]) + r'\\')
    lines.append('\hline\hline')
    for i in range(start_int, end_int + 1):
        if table_type == 'Addition':
            lines.append(str(i) + ''.join([' & {} '.format(x + i) for x in range(start_int, end_int + 1)]) + r'\\')
        if table_type == 'Subtraction':
            lines.append(str(i) + ''.join([' & {} '.format(x - i) for x in range(start_int, end_int + 1)]) + r'\\')
        if table_type == 'Multiplication':
            lines.append(str(i) + ''.join([' & {} '.format(x * i) for x in range(start_int, end_int + 1)]) + r'\\')
        lines.append('\hline')

    lines.append(r'\end{tabular}')
    lines.append(r'\end{center}')
    lines.append(r'\end{large}')
    lines.append(r'\end{document}')

    return '\n'.join(lines)


def parse_arguments():
    """
    Parse user arguments to modify how the document is generated for tables
    :return: parsed args passed by the user or defaults defined below
    """
    operators = ('Addition',
                 'Subtraction',
                 'Multiplication')

    parser = argparse.ArgumentParser(description='Generate a numberline to practice Addition/Subtraction')
    parser.add_argument('--start_int', default=1, type=int, help='starting integer')
    parser.add_argument('--end_int', default=10, type=int, help='ending integer')
    parser.add_argument('--table_type', default='Multiplication', help='table type')
    parser.add_argument('--filename', default='table_01.tex', help='filename to generate')
    args = parser.parse_args()

    max_int = 26
    assert args.table_type in operators, '{} not a valid table_type, only {}'.format(args.table_type, ', '.join([x for x in operators]))
    assert args.end_int > args.start_int, 'start_int must be less than end_int'
    assert args.end_int - args.start_int < max_int, 'number of columns [end_int - start_int] must be less than {} to fit on the page'.format(max_int)
    return args


def generate_problems_pdf(args):
    """
    Takes the parsed arguments, generates appropriate latex, converts it a pdf, and cleans up any temporary files
    :param args: parsed arguments that define how to generate the document
    """
    contents = generate_table(start_int=args.start_int, end_int=args.end_int, table_type=args.table_type)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_problems_pdf(parse_arguments())
