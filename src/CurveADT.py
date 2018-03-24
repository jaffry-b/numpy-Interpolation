## @file CurveADT.py
#  @title CurveADT
#  @author Bilal Jaffry
#  @date 1/22/2018

## @brief Imports the abstract data type SeqT as well as all of numpy library.
from SeqADT import SeqT
from numpy import *

## @brief This class represents curves.
#  @details This class represents as (x,y) sequence of coordinates for interpolation of a 1,2 or nth degree function.
class CurveT:

    ## @brief Constructor for CurveT
    #  @details Constructor accepts no parameters. Creates to instances of SeqT for x and y-coordinates.
    def __init__(self):
        ## @brief x-value sequence initialized.
        self.x_state = SeqT()
        ## @brief y-value sequence initialized.
        self.y_state = SeqT()

    ## @brief Reads a file and adds elements to x,y sequence.
    #  @details strips the newline characters as well as splits the list at ',', allowing to properly assign x,y values to given sequence.
    #  @param s input for filename [yourtextfile.txt]
    def CurveT(self, s):
        fileRead = open(s, 'r')
        for i in fileRead.readlines():
            index1 = i.strip()
            index = index1.split(',')
            self.x_state.add(self.x_state.size(), int(index[0]))
            self.y_state.add(self.y_state.size(), int(index[1]))
        fileRead.close()

    ## @brief Interpolates values with a linear approximation.
    #  @param x the value being approximated.
    #  @return returns the approximated interpolation at given x-value.
    def linVal(self, x):
        index = self.x_state.indexInSeq(x)
        x0 = self.x_state.get(index)
        y0 = self.y_state.get(index)
        x1 = self.x_state.get(index + 1)
        y1 = self.y_state.get(index + 1)

        yVal = ((y1 - y0) / (x1 - x0)) * (x - x0) + y0
        return yVal

    ## @brief Interpolates values with a quadratic approximation.
    #  @param x the value being approximated.
    #  @return returns the approximated interpolation at given x-value.
    def quadVal(self, x):
        index = self.x_state.indexInSeq(x)
        x0 = self.x_state.get(index)
        y0 = self.y_state.get(index)
        x1 = self.x_state.get(index+1)
        y1 = self.y_state.get(index+1)
        x2 = self.x_state.get(index+2)
        y2 = self.y_state.get(index+2)

        yVal = y1 +((y2 - y0)/(x2 - x0))*(x - x1) + ((y2 - 2*y1 + y0)/2*(x2 - x1)**2)*(x - x1)**2
        return yVal

    ## @brief Interpolates values with a nth order approximation.
    #  @param n the nth order polynomial approxmiation.
    #  @param x the value being approximated.
    #  @return returns the approximated interpolation at given x-value.
    def npolyval(self, n, x):
        if n >= 3:
            coeffs = polyfit(self.x_state.initList,self.y_state.initList,n)
            y = polyval(coeffs, x)
            return y


