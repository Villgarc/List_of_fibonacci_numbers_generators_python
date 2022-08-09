import time
import sys

def fibonacci(index : int) :
    if index == 0: return 0
    if index == 1: return 1
    return fibonacci(index-1) + fibonacci(index-2)


def fib_list(number_of_terms : str , verbose : str):
    try:
        if number_of_terms:
            result = []
            number_of_terms = int(number_of_terms)
            time.perf_counter()
            for i in range(int(number_of_terms)+1):
                fib = fibonacci(i)
                if verbose == '1' : print("For index {} the fibonacci number is {}".format(i,fib))
                result.append(fib)

            if verbose == '1':
                print("")
                print("It took {}s to calculate {} fibonacci terms".format(time.perf_counter(),number_of_terms))
                print("")
            return result

    except ValueError:
        print("The number of terms parameter must be an integer",file=sys.stderr)


if __name__ == "__main__":
    try:
        number_of_terms ,verbose = [sys.argv[1],sys.argv[2]]
        result = fib_list(number_of_terms,verbose)
        print(result)
    except IndexError:
        print("These program uses two arguments :\nThe number of terms parameter must be an integer and the verbose can be either 0 or 1",file=sys.stderr)