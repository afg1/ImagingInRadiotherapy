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
from scipy.ndimage import interpolation, rotate


# Load all of the images, don't forget to make them single channel!
lungs1 = misc.imread("lungs.jpg", flatten=True)
lungs2 = misc.imread("lungs2.jpg", flatten=True)
lungs3 = misc.imread("lungs3.jpg", flatten=True)


## Display your two images with an appropriate transparency setting and colour maps.
fig = plt.figure(1)
fixed = plt.imshow(lungs1,cmap="Greens_r")
floating = plt.imshow(lungs2,cmap="Purples_r", alpha=0.5)

global totalShift
totalShift = np.array([0,0])

def shiftImages(shift):
    global lungs2
    lungs2 = interpolation.shift(lungs2, shift)
    return lungs2

def eventHandler(event):
    # Read keypress
    whichKey = event.key

    # Map keypress to the appropriate shift or rotation
    if whichKey == "up":
        shift = (-1,0)
    elif whichKey == "down":
        shift = (1,0)
    elif whichKey == "right":
        shift = (0, 1)
    elif whichKey == "left":
        shift = (0,-1)

    global totalShift
    totalShift += np.array(shift)
    ## Now you should have a shift, do something with it!
    shifted = shiftImages(shift)
    floating.set_data(shifted)
    fig.canvas.draw()

## This line links up the keyboard to the event handler function we will write in a minute
fig.canvas.mpl_connect('key_press_event', eventHandler)


## Make sure you see what you expect to!
plt.show()

print(totalShift)
## Early exit here to separate the two parts of the assignment. Delete or comment this line!
# exit()


## Now load the rotated image
lungs3 = misc.imread("lungs3.jpg", flatten=True)

# Display the image

fig2 = plt.figure(2)
fixed2 = plt.imshow(lungs1, cmap="Greens_r")
floating2 = plt.imshow(lungs3, cmap="Purples_r", alpha=0.5)

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
        shift = (-1,0)
    elif whichKey == "down":
        shift = (1,0)
    elif whichKey == "right":
        shift = (0, 1)
    elif whichKey == "left":
        shift = (0,-1)
    elif whichKey == "ctrl+left":
        angle = 1
    elif whichKey == "ctrl+right":
        angle = -1

    global totalShiftRotation
    totalShiftRotation += np.array([*shift, angle])

    ## Now you should have a shift, do something with it!
    shifted = shiftRotateImages(shift, angle)
    floating2.set_data(shifted)
    fig2.canvas.draw()

## Again, link up your event handler to the figure
fig2.canvas.mpl_connect('key_press_event', eventHandler2)

plt.show()

print(totalShiftRotation)