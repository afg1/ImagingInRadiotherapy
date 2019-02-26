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
    """
    Return the sum of square differences
    """
    return np.mean((image1 - image2)**2)
    return np.sum((image1 - image2)**2)

# Load the two lung images from dicom files here

# Hint: use the pydicom module like in the first practical
# lung1 = misc.imread("/Users/agreen/Dropbox/IMG-0003-00001.bmp", flatten=True).astype(np.int32)#dicom.read_file("image1.dcm")
# lung2 = misc.imread("/Users/agreen/Dropbox/IMG-0003-00004.bmp", flatten=True).astype(np.int32)#dicom.read_file("image2.dcm")

lung1 = dicom.read_file("/Users/agreen/Dropbox/IMG-0004-00001.dcm").pixel_array
lung2 = dicom.read_file("/Users/agreen/Dropbox/IMG-0004-00002.dcm").pixel_array
lung3 = dicom.read_file("/Users/agreen/Dropbox/IMG-0004-00001.dcm").pixel_array
lung4 = dicom.read_file("/Users/agreen/Dropbox/IMG-0004-00002.dcm").pixel_array

# lung1 = dicom.read_file("/Users/agreen/Dropbox/IMG-0003-00001.dcm", force=True).pixel_array#.mean(axis=0)#.swapaxes(1, 0)

print(lung2.dtype)

print(lung1.shape)

lung3 = dicom.read_file("test.dcm").pixel_array
print(lung3.shape)





# Tip: run your script after every stage. So run it now!

# Now diplay the images here
# You can probably paste some code from yesterday's practical here
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)

fixed = ax.imshow(lung1, cmap="Greens_r", alpha=0.5)
# fixed = ax.imshow(lung3, cmap="Greys_r")
floating = ax.imshow(lung2, cmap="Purples_r", alpha=0.5)


# For now, do manual registration:
manual = False

# Remember: you will need to keep hold of your figure and plot objects to do the
# manual registration

# Tip: Think about how you can split out the bit of code that handles the events
# and the bit of code that handles the shifting of the image.
# If you do it right, you can re-use a big chunk of your code!

# separate out the user interface and shift functions
def eventHandler(event, fig=fig, floating=floating, ax=ax):
    """
    This function handles deciphering what the user wants us to do,
    the event knows which key has been pressed. I've implemented shifts and
    and rotations using the arrow keys.
    """
    UD = 0
    LR = 0
    CW = 0
    whichKey = event.key
    if whichKey == "up":
        UD -= 1
    elif whichKey == "down":
        UD += 1
    elif whichKey == "left":
        LR -= 1
    elif whichKey == "right":
        LR += 1
    elif whichKey == "alt+left":
        CW += 1
    elif whichKey == "alt+right":
        CW -= 1

    shiftImages([UD,LR,CW], True, fig, floating, ax)


def shiftImages(shifts, manual=True, fig=None, floating=None, axes=None):
    """
    This function interpolates the image into its shifted position.
    """
    # If no rotations are given, we have to skip them here
    if len(shifts) == 3:
        UD, LR, CW = shifts
    else:
        UD, LR = shifts


    global lung2
    global lung1

    # Note: we work on a temporary copy - if we don't want to update the plot
    # we can skip resetting the global variable to the shifted one
    tmp = interpolation.shift(lung2, (UD,LR), mode='nearest', order=1)
    if len(shifts) == 3:
        tmp = rotate(tmp, CW, reshape=False)
    else:
        pass

    # calculate the cost function now
    cf = costFunction(lung1, tmp)


    if not floating is None and not fig is None:
        axes.set_title("Cost Function: {0}".format(cf))
        floating.set_data(tmp)

        if manual:
            lung2 = tmp

        fig.canvas.draw()
        plt.pause(0.001)

    # We return the cost function because we will re-use this function in the
    # automatic registration bit
    return cf

# Connect the event handler to the plot
cid = fig.canvas.mpl_connect('key_press_event', eventHandler)

# This switches off the plot waiting for you
if not manual:
    plt.ion()


plt.show()

# Run your script to make sure it still works!

# Add your event handler function(s)
def manualRegister(event):
    pass


# Now we can try to automate the registration.
# You should have imported some optimiser functions from the scipy.optimize
# library. Try them out here - I have written the brute force one for you.
#                                       These are the limits over which we move
res = brute(shiftImages, ((-100, 100),(-100, 100)), args=(False, fig, floating, ax))

# Note - if you don't want the figure to update, don't pass anything for args=



# Some of the other methods need an initial guess for the best shift. Specify it
# like this:
init = [0.0, 0.0] # Add more if you include rotation
# You may also need to implement a "callback" function to update the plot

def updatePlot(x, cf, accept, fig=fig, floating=floating, axes=ax):
    shiftImages(x, False, fig, floating, axes)

# res = basinhopping(shiftImages, init, stepsize=10.0)#, callback=updatePlot)


shiftImages(res, True, fig, floating, ax)
# Add this line to keep the plot open at the end
plt.pause(10)


# subreg = [404, 464, 218, 278]
#
# plt.ioff()
# plt.figure()
# plt.imshow(lung1[subreg[2]:subreg[3], subreg[0]:subreg[1]], cmap="Greys_r", interpolation='none')
#
# plt.figure()
#
# # shiftImages(res.x, True)
#
# plt.imshow(lung2[subreg[2]:subreg[3], subreg[0]:subreg[1]], cmap="Greys_r", interpolation='none')
# plt.show()
