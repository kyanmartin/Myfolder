"""Simple calculator with a Gooey-based graphical user interface.

Instead of text prompts, the user can choose an operation and
enter two numbers in a polished GUI powered by gooey.  The result
is printed back to the console (and the GUI).

To run:

    python calculator.py

If gooey is not installed, install it with ``pip install Gooey``.
"""

from gooey import Gooey, GooeyParser


@Gooey(program_name="Calculator",
       default_size=(400, 300),
       progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)")
def main():
    parser = GooeyParser(description="Perform a basic arithmetic operation")
    parser.add_argument('operation',
                        choices=['*', '/', '+', '-'],
                        help='Operation to perform: multiply (*), divide (/), add (+) or subtract (-)')
    parser.add_argument('first', type=float, help='First number')
    parser.add_argument('second', type=float, help='Second number')

    args = parser.parse_args()

    # compute result
    if args.operation == '/' and args.second == 0:
        result = None
        message = "Error: Division by zero is not allowed."
    else:
        if args.operation == '*':
            result = args.first * args.second
        elif args.operation == '/':
            result = args.first / args.second
        elif args.operation == '+':
            result = args.first + args.second
        elif args.operation == '-':
            result = args.first - args.second
        message = f"The answer is: {result}"

    # print result; Gooey will display it in output panel as well
    print(message)


if __name__ == '__main__':
    main()