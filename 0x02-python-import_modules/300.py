#!/usr/bin/python3
if __name__ != "__main__":
    exit(1)                                                                                                                           
                                                                                                                                      
from calculator_1 import add, sub, mul, div                                                                                           
from sys import argv                                                                                                                  
                                                                                                                                      
argc = len(argv)                                                                                                                      
                                                                                                                                      
if argc != 4:                                                                                                                         
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")                                                                         
    exit(1)                                                                                                                           
if argv[2] == "+":                                                                                                                    
    outcome = add(int(argv[1]), int(argv[3]))                                                                                         
elif argv[2] == "-":                                                                                                                  
    outcome = sub(int(argv[1]), int(argv[3]))                                                                                         
elif argv[2] == '*':                                                                                                                  
    outcome = mul(int(argv[1]), int(argv[3]))                                                                                         
elif argv[2] == "/":                                                                                                                  
    outcome = div(int(argv[1]), int(argv[3]))                                                                                        
else:                                                                                                                                
    print("Unknown operator. Available operators: +, -, * and /")                                                                    
    exit(1)                                                            
print("{:s} {:s} {:s} = {:d}".format(argv[1], argv[2], argv[3], outcome)
