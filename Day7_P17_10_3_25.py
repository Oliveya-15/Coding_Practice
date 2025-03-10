#Find out the Maximum product value
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))

# Step 2: Handle small array sizes
if len(a) == 1:
    print("The Maximum product value is:", a[0])
elif len(a) == 2:
    print("The Maximum product value is:", a[0] * a[1])
else:
    # Step 3: Sort the array
    a.sort()

    # Step 4: Find two possible maximum products
    max_product = max(a[-1] * a[-2] * a[-3], a[0] * a[1] * a[-1])                                      

    # Step 5: Print the result
    print("The Maximum product value is:", max_product)



"""
a = [1,2,-3,0,-4,-5] => 40 
                                          -6   -5  -4 -3  -2  -1
Sorted a: [-5, -4, -3, 0, 1, 2]          | -5| -4| -3| 0 | 1 | 2 |
                                           0    1   2  3   4   5

max(    a[-1]    *   a[-2]    * a[-3]   ,    a[0]   *   a[1]    *    a[-1]) 
        last(2)    2nd(1)      3rd(0)       1'st(-5)   2nd(-4)       last(2)

( 2  *  1  *  0) = 0  ,   ((-5  *  -4)  *  2) = 20 * 2 = 40 

max( 0 * 40 ) => 40

"""


"""
input : 1,2,-3,0,-4,-5  => 40
input : 1 2 3 4 5    => 120
All Positive => Simple Multiplication among all
Zero exist => no effect simple multiply with 0
Some Negative Some Positive => Add the highest 2 negative value as (negative * negative = positive)[(-5) * (-4) = 20]

For implying this formula :-

Performing sorting a.sort() to get ascending order [-5,-4,-3,0,1,2]
it have the highest and lowest
divide the array in 2 part most highest[0,1,2] mose lowest[-5,-4,-3]
-1 carry the most highest value[2]
0 carry the most lowest value[-5]
perform multiplication on the most highest values[2*1*0] = 0
We can't multiply 3 negative[-5*-4*-3] so taking the most highest[-5 * -4] and multiply it with most highest positive(2) = 40
performing max operation on this 2 ( 0 * 40) => 40 this is the result

"""