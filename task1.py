# Task2
# Calculator
# I made a calculator by python object-oriented programming which is based on classes and objects

# import abstract method to make a abstract class
from abc import ABCMeta, abstractmethod, ABC


# classes for basic mathematical operation
class Operation(metaclass=ABCMeta):

    def input_operands(self):
        self.operand_1 = int(input('Enter your First operand:'))
        self.operand_2 = int(input('Enter your second operand:'))

    @abstractmethod
    def mathematical_operation(self):
        pass


class Addition_operation(Operation):

    def mathematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nAddition:', self.operand_1 + self.operand_2)
        print()


class Subtraction_operation(Operation, ABC):

    def mathematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nSubtraction:', self.operand_1 - self.operand_2)
        print()


class Multiplication_operation(Operation):

    def mathematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nMultiplication:', self.operand_1 * self.operand_2)
        print()


class Division_operation(Operation):

    def mathematical_operation(self):
        self.input_operands()
        print('\nRESULT:\nDivision:', round((self.operand_1 / self.operand_2),4))
        print()


# main interface
print('**** HELLO PYTHON CALCULATOR ****')
print()

try:
    while True:
        print("Here's your basic operation:")
        print('PRESS[1] FOR ADDITION \nPRESS[2] FOR SUBTRACTION \nPRESS[3] FOR MULTIPLICATION \nPRESS[4] FOR DIVISION')
        print('PRESS[5] FOR EXIT\n')
        choice = int(input('Which operation do you want to perform:'))

        if choice == 1:
            a1 = Addition_operation()
            a1.mathematical_operation()

        elif choice == 2:
            s1 = Subtraction_operation()
            s1.mathematical_operation()

        elif choice == 3:
            m1 = Multiplication_operation()
            m1.mathematical_operation()

        elif choice == 4:
            d1 = Division_operation()
            d1.mathematical_operation()

        elif choice == 5:
            print("Thankyou for using.\nHave a good day!")
            exit()

        else:
            print('Invalid Choice!!\nPLS choose a given numbers')

except ValueError:
    print("Invalid number!! Please enter a valid number")