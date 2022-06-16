iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

"""Questions for code one:
        1. What is the value of the variable count that is printed out (at the print statement) 
           on iteration 0?
        2. What is the value of the variable count that is printed out (at the print statement) 
           on iteration 1?
        3. What is the value of the variable count that is printed out (at the print statement)
           on iteration 2?
        4. What is the value of the variable count that is printed out (at the print statement) 
           on iteration 3?
        5. What is the value of the variable count that is printed out (at the print statement)
           on iteration 4?
"""
