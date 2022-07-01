#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction: No argument so returns default of 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction: prints either 'Error' or 5, feel like its an Error though

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction: Returns 5 as functions stop after a return is hit.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction: Prints 5 as functions stop after a return is hit.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction: A little tricky but I'll say prints 5. 
# Follow up: I don't understand fully the 'None' printed on the 2nd line.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Follow up: I feel like that has worked doing something similar during Web Fundamentals class.
# Comparing it to question 9, there was no return which caused the error.

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Prediction: prints'25' since its turning both numbers into strings.

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction: prints 100 and prints 10
# Follow up: the red lines would definitely hint at errors in the code,
# but I didn't think it would reach the 2nd return in the else statement. This one is confusing.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction: print 1) 7, print 2) 14, print 3) seems like an error, so possible error on entire thing?
# Follow up: after reviewing this and number 6, I see now why this one worked and number 6 had error. This has return values so the function can calculate properly.


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction: prints 8 as it stops after the first return statement.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Prediction: prints 500, 500, 300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Prediction: prints 500, 500, 300, 300, 500? It reads like it would print twice when calling the function.
# Follow up: I see now why only 1 300 was printed. Print was only called once. When it returned 300, nothing was done with that after.


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Prediction: prints 500, 500, 300
# Follow up: Because it has print inside the function and you are calling 'b' to print as well,
# There will be two prints in that entire process. Hence the 2 300 prints.


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: Man this is whack. It looks like we are calling function 'foo' which after running,
# would print 1,3,2. Just weird code to me.


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction: It prints 1, 3, 5, 10. Haha got it! Weird, but was able to follow the rabbit trail.