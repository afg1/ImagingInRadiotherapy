# In this assignment we will finish off the manual registration code you started
# yesterday, before adding in automatic registration using scipy.optimize.
#
# Everything you need shuld be imported below.


from scipy.ndimage import interpolation, rotate
from scipy.optimize import minimize, basinhopping, brute, differential_evolution
import matplotlib.pyplot as plt
from scipy import misc
import numpy as np
import dicom


# Implement your cost function here
def costFunction(image1, image2):
    pass

# Load the two lung images from dicom files here

# Hint: use the pydicom module like in the first practical
lung1 = #...
lung2 = #...

# Tip: run your script after every stage. So run it now!

# Now diplay the images here

# Remember: you will need to keep hold of your figure and plot objects to do the
# manual registration

# Tip: Think about how you can split out the bit of code that handles the events
# and the bit of code that handles the shifting of the image.
# If you do it right, you can re-use a big chunk of your code!


# You can probably paste some code from yesterday's practical here
fig = ...

# Run your script to make sure it still works!

# Add your event handler function(s)
def manualRegister(event):
    pass


# Now we can try to automate the registration.
# You should have imported some optimiser functions from the scipy.optimize
# library. Try them out here - I have written the brute force one for you.
#                                       These are the limits over which we move
res = brute(<Your image shift function>, ((-100, 100),(-100, 100)))



# Some of the other methods need an initial guess for the best shift. Specify it
# like this:
init = [0.0, 0.0] # Add more if you include rotation
