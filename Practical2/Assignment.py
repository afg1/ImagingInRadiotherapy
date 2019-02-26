"""
Your task for this practical is to implement a simple manual registration engine.

To do this, we will be looking at some images of lung CT. These are just standard jpeg files, so can be loaded with imread.

lungs1 is your reference image, lungs2 has been shifted by some amount, and lungs3 has been shifted and rotated.


Write code to load and display the images with transparency so that they can be registered. We will write an event handler function
that will be linked up to the display to handle keyboard input.

After you have written everything, try to register all the images together and record the shifts/rotations you need.

Suggested steps:
- Display two images overlaid on each other with transparency
- Write a function to shift images given, play around with it to figure out how it works.
- Write event handler function and link it with one of the images to move it around (up, down, left, right)
- Extend the event handler to include rotations
- Register lungs1 <-- lungs2 and lungs1 <-- lungs3, record the required shifts/rotations

"""
## Import some libraries here
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import 


# Load all of the images, don't forget to make them single channel!
lungs1 = misc.imread(...)
lungs2 = misc.imread(...)
lungs3 = misc.imread(...)


## Display your two images with an appropriate transparency setting and colour maps.
fig = plt.figure(1)
fixed = plt.imshow(...)
floating = plt.imshow(...)

global totalShift
totalShift = np.array([0,0])

def shiftImages(shift):
    global lungs2
    lungs2 = interpolation.shift(...)
    return lungs2

def eventHandler(event):
    # Read keypress
    whichKey = event.key
    shift = (0,0)
    # Map keypress to the appropriate shift or rotation
    if whichKey == "up":
        pass
    elif whichKey == "down":
        pass
    elif whichKey == "right":
        pass
    elif whichKey == "left":
        pass

    global totalShift
    totalShift += np.array(shift)
    ## Now you should have a shift, do something with it!
    shifted = shiftImages(shift)
    floating.set_data(...)
    fig.canvas.draw()

## This line links up the keyboard to the event handler function we will write in a minute
fig.canvas.mpl_connect('key_press_event', ...)


## Make sure you see what you expect to!
plt.show()

print(totalShift)
## Early exit here to separate the two parts of the assignment. Delete or comment this line!
exit()

# Display the images
fig2 = plt.figure(2)
fixed2 = plt.imshow(...)
floating2 = plt.imshow(...)

global totalShiftRotation
totalShiftRotation = np.array([0,0, 0])

# Write a function that shifts and rotates your third image

# Convention: rotate first, then shift

def shiftRotateImages(shift, angle):
	global lungs3
	lungs3 = rotate(lungs3, angle,reshape=False)
	lungs3 = interpolation.shift(lungs3, shift)
	return lungs3

def eventHandler2(event):
    # Read keypress
    whichKey = event.key
    angle = 0
    shift = (0,0)
    # Map keypress to the appropriate shift or rotation
    if whichKey == "up":
        pass
    elif whichKey == "down":
        pass
    elif whichKey == "right":
        pass
    elif whichKey == "left":
        pass
    elif whichKey == "ctrl+left":
        pass
    elif whichKey == "ctrl+right":
        pass

    global totalShiftRotation
    totalShiftRotation += np.array([*shift, angle])

    ## Now you should have a shift, do something with it!
    shifted = shiftRotateImages(...)
    floating2.set_data(...)
    fig2.canvas.draw()

## Again, link up your event handler to the figure
fig2.canvas.mpl_connect('key_press_event', ...)

plt.show()

print(totalShiftRotation)