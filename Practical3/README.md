# Practical 3 - 2D rigid image registration

In this practical you will take the code you wrote yesterday and modify it to do automatic registration. To do this you will 
need to choose a metric to calculate, and modify the way your shift and rotate functions work so that they will do the right 
thing when we use an optimiser.

Once you have finished the main parts of the code, play around with the different optimisers available in scipy and see if you can 
make your registration better (or worse!) by using a different one. You could also try implementing different image similarity 
metrics and see how much effect that has on the registration.
