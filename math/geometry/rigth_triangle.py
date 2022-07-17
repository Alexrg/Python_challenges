#Create a class called RightTriangle. RightTriangle should
#have two attributes (instance variables): opposite and
#adjacent. Make sure the variable names match those words.
#Both will be floats.
#
#RightTriangle should have a constructor with two required
#parameters, one for each of those attributes (opposite and
#adjacent, in that order).
#
#RightTriangle should also have a method called
#find_hypotenuse. find_hypotenuse should calculate the
#hypotenuse of the triangle based on the current values for
#opposite and adjacent.
#
#hypotenuse should NOT be an attribute of the class;
#instead, hypotenuse should be calculated and returned live
#when the method find_hypotenuse is called.
#
#The find_hypotenuse method should have NO parameters
#besides self. Instead, it should calculate the hypotenuse
#based on the current values for the opposite and adjacent
#attributes.
#
#Hint: The formula for hypotenuse is the square root of
#opposite squared plus adjacent squared. The easiest way to
#find the square root is to use the exponent operator to
#raise the sum to the 0.5 power (e.g. sum**0.5).