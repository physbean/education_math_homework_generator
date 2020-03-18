import argparse

from education_math_homework_generator.util import convert_latex_to_pdf
from education_math_homework_generator.util import remove_temporary_files


def generate_number_lines(number_of_lines=6, start=0, end=20):
    lines = [r'\documentclass[letterpaper]{article}',
             r'\usepackage{geometry}',
             r'\geometry{landscape,a4paper,total={170mm,257mm},left=10mm,right=10mm,top=30mm}',
             r'\usepackage{tikz}',
             r'\usepackage{amsmath}',
             r'\usetikzlibrary{arrows}',
             r'\begin{document}',
             r'\begin{LARGE}',
             r'']

    numbers = ','.join([str(x) for x in range(start, end + 1)])
    for i in range(number_of_lines):
        lines.append(r'')
        lines.append(r'{\Large $-$}')
        lines.append(r'\begin{tikzpicture}')
        lines.append(r'\draw[latex-latex, thick] ' + '({},0) -- ({},0) ;'.format(start - 1, end + 1))
        lines.append(r'\foreach \x in  {' + numbers + '}')
        lines.append(r'\draw[shift={(\x,0)},color=black, thick] (0pt,3pt) -- (0pt,-3pt);')
        lines.append(r'\foreach \x in  {' + numbers + '}')
        lines.append(r'\draw[shift={(\x,0)},color=black, thick] (0pt,0pt) -- (0pt,-3pt) node[below] ')
        lines.append(r'{\textbf{\x}};')
        lines.append(r'\end{tikzpicture}')
        lines.append(r'{\Large $+$}')
        lines.append(r'\\')
        lines.append(r'\vspace*{50px}')
        lines.append(r'')

    lines.append(r'\end{LARGE}')
    lines.append(r'\end{document}')

    return '\n'.join(lines)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate a numberline to practice Addition/Subtraction')
    parser.add_argument('--start', default=0, type=int, help='integer to start the number line')
    parser.add_argument('--end', default=20, type=int, help='integer to end the number line')
    parser.add_argument('--numlines', default=5, metavar='N', type=int, help='number of lines to generate')
    parser.add_argument('--filename', default='numberline_01.tex', help='filename to generate')
    return parser.parse_args()


def generate_number_lines_pdf(args):
    contents = generate_number_lines(number_of_lines=args.numlines, start=args.start, end=args.end)
    convert_latex_to_pdf(args.filename, contents=contents, view=True)
    remove_temporary_files(args.filename)


if __name__ == "__main__":
    generate_number_lines_pdf(parse_arguments())
