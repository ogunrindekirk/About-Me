#created by kirk ogunrinde on Jun 5 2023

#import argparse library
import argparse

#function calc that does the counting down of the "Hello World {INT}" based on parameter x
def calc(x):
    msg = "Hello World {"
    
    for i in range (x + 1):
        print(msg + str(i) + "} ")
        
#this is technically the "main" function, renamed accrodingly so we can use argparse to enter commands in the terminal
def main(num):
    rem = num - 1
    calc(rem)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Use Command Line Arguments For function")
    parser.add_argument("main", type=int, help="Enter an Integer number")
    args = parser.parse_args()
    
    num = args.main
    main(num)
    
    