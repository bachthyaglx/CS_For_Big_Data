
class Expressions:
    """"
    Fill in one-line expressions (no own functions) to initialize attributes
    self.b .. self.k with specified values.

    Use Python built-in functions, list expressions and list comprehension,
    but NOT own functions.

    Complete tasks one after another. Once you are done with one task,
    uncomment test cases in test_expressions.py. Remove comments for
      # Test_case_b = Test_case
      # Test_case_c = Test_case
      # Test_case_d = Test_case
      # ...
    Run tests in IDE and in a terminal:
      python test_expressions.py
      python -m unittest
    """

    default_numbers=[4, 12, 3, 8, 17, 12, 1, 8, 7]

    def __init__(self, _numbers=default_numbers):
        """
        Constructor to initialize member variables.
        """
        self.numbers = _numbers

        # a) initialize with number of numbers: 9
        self.a = len(self.numbers)    # <-- given solution, insert one-line expressions below

        # b) initialize with first three numbers: [4, 12, 3]
        self.b = self.numbers[:3]     # <-- write expression here

        # c) initialize with last three numbers: [1, 8, 7]
        self.c = self.numbers[-3:] 

        # d) initialize with last three numbers reverse: [7, 8, 1]
        self.d = list(reversed(self.c))

        # e) initialize with odd numbers: [3, 17, 1, 7]
        self.e = [i for i in self.numbers if i%2 != 0]

        # f) initialize with number of odd numbers: 4
        self.f = len(self.e)

        # g) initialize with sum_ of odd numbers: 28
        self.g = sum(self.e)

        # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
        self.h = [value for key,value in enumerate(self.numbers) if value not in self.numbers[:key]] #enumerate: convert list to tuple (key, value)

        # i) number of duplicate numbers: 2 
        self.i = len(self.numbers) - len(self.h)

        # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
        self.j = [i*i for i in list(set(self.numbers))]

        # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
        self.k = "EVEN_LIST" if len(self.numbers) and len(self.numbers)%2 == 0 else ("ODD_LIST" if len(self.numbers)%2 != 0 else "EMPTY_LIST")


        # attempt to load solution module (ignore)
        try:
            sol_module = (__file__.split("\\")[-1:])[0].split(".")[0] + "_sol"
            mod = __import__(sol_module, globals(), locals(), [], 0)
            mod.set_solution(self)  # replace empty values with solutions
        #
        except ImportError:
            pass


    def print_results(self):
        print(f'\nnumbers: {self.numbers}\n#')
        fmt = {
            # key: (value, output string)
            'a': (self.a, 'number of numbers'),
            'b': (self.b, 'first three numbers'),
            'c': (self.c, 'last three numbers'),
            'd': (self.d, 'last three numbers reverse'),
            'e': (self.e, 'odd numbers'),
            'f': (self.f, 'number of odd numbers'),
            'g': (self.g, 'sum of odd numbers'),
            'h': (self.h, 'duplicate numbers removed'),
            'i': (self.i, 'number of duplicate numbers'),
            'j': (self.j, 'ascending, de-dup (n^2) numbers'),
            'k': (self.k, 'length'),
        }
        # format output, e.g.: "b) first three numbers: [1, 4, 6]"
        for k in sorted(fmt.keys()):
            print(f'{k}) {fmt[k][1]}: {fmt[k][0]}')


if __name__ == '__main__':
    '''
    Driver code that runs when this file is directly executed.
    '''
    #
    n1 = Expressions()  # use default list
    #
    # 2nd object with different list
    n2 = Expressions([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67,
        6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
    #
    n1.print_results()
    # n2.print_results()     # try also other list
