'''
In this problem, you are asked to find the amount of radiation a person is exposed to during some period of time by completing the following function:

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
To complete this function you'll need to know what the value of the radioactive decay curve is at various points. There is a function f that will be defined for you that you can call from within your function that describes the radioactive decay curve for the problem. Do not define f in your code.

You should implement this function on your own machine. Open a new Canopy Python file and title it "radiationExposure.py". Complete your work inside this file. Test your code well in Canopy, and when you are convinced it is correct, cut and paste your definition into this tutor window.
'''

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    values = [x for x in range(0, int((stop-start)/step))]
    for i in range(len(values)):
        values[i] = start + i * step
    
    values = map(f,values)
    return sum(values)*step