#######################################################
# Author:   Quinn Trate
# Date:     September 10, 2023
# Class:    CMPSC 441 Artificial Intelligence
# Language: Python
# Purpose:  Goes Over the Basics of Python With
#	          Lists, List Comprehension, Generators,
#	          and Classes.
#######################################################



#######################################################
# 1. Sequences
#######################################################


def list_add(l1, l2):
    return list(set(l1) | set(l2))

def dict_extend(dict1, dict2):
    temp = dict()
    for key, value in dict1.items():
        if (key in temp):
            lst = temp[key]
            lst.append(value)
            temp[key] = lst
        else:
            temp[key] = [value]
    for key, value in dict2.items():
       if (key in temp):
           lst = temp[key]
           lst.append(value)
           temp[key] = lst
       else:
           temp[key] = [value]
    return temp

def dict_invert(dct):
    temp = dict()
    for key, value in dct.items():
        temp.setdefault(value, list()).append(key)
    return temp

def dict_nested(lst):
    lst.reverse()
    temp = dict()
    for i in lst:
        temp = dict([(i, temp)])
    return temp


#######################################################
# 2. List Comprehension
#######################################################


def list_product(l1, l2):
    return [(i, j) for i in l1 for j in l2]

def list_flatten(list_of_seqs):
    return [i for j in list_of_seqs for i in j]

def dict_to_table(dct):
    return [tuple(dct.keys()), *(tuple(dct[key][value] for key in dct) for value in range(len(next(iter(dct.values())))))]

def nlargest(dct, n):
    return dict(sorted(dct.items(), key = lambda x: x[1], reverse = True)[:n])

def unique_values(list_of_dicts):
    return list(set(val for dic in list_of_dicts for val in dic.values()))


#######################################################
# 3. Generators
#######################################################


def prefixes(seq):
     for i in range(len(seq) + 1):
        yield seq[:i]

def suffixes(seq):
    i = 0
    while i <= len(seq):
        yield seq[i:len(seq)]
        i += 1


#######################################################
# 4. Other algorithms
#######################################################


def encode(input):
    temp = ''
    while input:
        i = 0
        while i < len(input) and input[0] == input[i]:
            i += 1
        temp += str(i) + input[0]
        input = input[i:]
    return temp

def decode(input):
    temp = ''
    for i in range(0, len(input), 2):
        num = input[i:i+1]
        char = input[i+1:i+2]
        temp += (char * int(num))
    return temp

def camel_case(var_name):
    temp = var_name.split('_')
    return temp[0].lower() + ''.join(ele.title() for ele in temp[1:])


#######################################################
# 5. Fraction class
#######################################################


class Fraction():
    
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError('{0}/{1}'.format(numerator, denominator))
        self.numerator = numerator
        self.denominator = denominator

    def get_fraction(self):
        return (self.numerator, self.denominator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __add__(self, other):
        if self.denominator != other.denominator:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        else:
            return Fraction(self.numerator + other.numerator, self.denominator)

    def __sub__(self, other):
        if self.denominator != other.denominator:
            return self + -other
        else:
            return Fraction(self.numerator - other.numerator, self.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        temp1 = self.numerator * other.denominator
        temp2 = other.numerator * self.denominator
        return temp1 == temp2

    def __lt__(self, other):
        temp1 = self.numerator * other.denominator
        temp2 = other.numerator * self.denominator
        return temp1 < temp2

    def __call__(self):
        return self.numerator / self.denominator

    def simplify(self):
        if self.numerator < 0 and self.denominator < 0:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)
        gcd = 2
        while gcd < min(self.numerator, self.denominator) + 1:
            if self.numerator % gcd == 0 and self.denominator % gcd == 0:
                self.numerator = self.numerator / gcd
                self.denominator = self.denominator / gcd
            else:
                gcd += 1
                
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
