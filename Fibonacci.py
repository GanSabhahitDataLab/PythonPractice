# Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to
# that many decimal places. Keep a limit to how far the program will go

def fibonaccisequence_upton():
    askForInput()


def askForInput():
        n = int(input("Enter number of Fibonnacci sequence"))
        fibgenerated = fibonaccialgorithm(n)
        for i in fibgenerated:
            print(i)


def fibonaccialgorithm(n):
    generated_fib = []
    for i in range(0, n):
        if i > 1:
            generated_fib.append(generated_fib[i - 1] + generated_fib[i - 2])
        else:
            generated_fib.append(i)
    return generated_fib
