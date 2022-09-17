import sys
import math 

def get_coef(index, prompt):
    a = False;
    while a == False:
        print(prompt)
        coef_str = input()
        try: 
            coef = float(coef_str)
            a = True
        except ValueError: 
            print('Try again!\n')
            a = False
            pass  
    return coef


def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)

        if root1 == 0.0:
            result.append(root1)
        elif root1 > 0.0: 
            root11 = math.sqrt(root1)
            root12 = - math.sqrt(root1)
            result.append(root11)
            result.append(root12)

        if root2 == 0.0:
            result.append(root2)
        elif root2 > 0.0: 
            root21 = math.sqrt(root2)
            root22 = - math.sqrt(root2)
            result.append(root21)
            result.append(root22)
   
    return result


def main():
    a = get_coef(1, 'Enter ratio A:')
    b = get_coef(2, 'Enter ratio B:')
    c = get_coef(3, 'Enter ratio C:')
    roots = get_roots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Haven`t roots!')
    elif len_roots == 1:
        print('One root: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Two roots: {} & {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Three root: {}, {} & {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Four roots: {}, {}, {} & {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
