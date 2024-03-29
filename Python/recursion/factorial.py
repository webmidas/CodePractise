"""
Write a program to print factorial of a number using recursion.
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


num = 10
print(factorial(num))



#**************************************************************************
#* (C) Copyright 2020-2023 by Ashish Jha and                              *
#* Outshine Labs. All Rights Reserved.                                    *
#*                                                                        *
#* DISCLAIMER: The authors and publisher of this book have used their     *
#* best efforts in preparing the book. These efforts include the          *
#* development, research, and testing of the theories and programs        *
#* to determine their effectiveness. The authors and publisher make       *
#* no warranty of any kind, expressed or implied, with regard to these    *
#* programs or to the documentation contained in these books. The authors *
#* and publisher shall not be liable in any event for incidental or       *
#* consequential damages in connection with, or arising out of, the       *
#* furnishing, performance, or use of these programs.                     *
#**************************************************************************