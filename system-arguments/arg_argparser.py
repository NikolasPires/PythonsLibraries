from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--basic',
                    help="print hello world in screen",
                    #type=str, argument tyep
                    metavar='STRING',
                    #default='Hello World', #default value
                    required=False,
                    action='append',
                    #nargs="+" #list of arguments
                    )
args = parser.parse_args()

if args.basic is None:
    print("You haven't passed the argument -b")
else:
    print(args.basic)