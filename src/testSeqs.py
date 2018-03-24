from CurveADT import CurveT
from SeqADT import *



def program():
    testCurve = CurveT()

    testCurve.CurveT('input.txt')
    n = input("Enter the order of polynomial function: ")
    x = input("Enter x value you wish to know y value for: ")

    if (n == 1):
        linTest = testCurve.linVal(x)
        print("linVal: {}".format(linTest))
    elif (n == 2):
        polyTest = testCurve.quadVal(x)
        print("polyVal results : {}".format(polyTest))
    else:
        y = testCurve.npolyval(n, x)
        print("The y value of %f is %f" % (x, y))

def testSeqADT():
    initList = SeqT()
    initList.add(0, 0)
    initList.add(1, 7)
    initList.add(2, 15)
    initList.add(3, 99)
    count = 0
    if (initList.get(3) == 99):
        print("Add function: pass")
        count+=1
    else:
        print("Add function: failed")

    initList.rm(2)
    if initList.size() == 3:
        print("RM function: pass")
        count+=1
    else:
        print("RM function: failed...")

    initList.set(1, 10)
    if (initList.get(1) == 10):
        print("Set function: pass")
        count+=1
    else:
        print("Set function:  failed")

    if(initList.get(0) == 0):
        print("Get function: pass")
        count+=1
    else:
        print("Get function: Failed!")

    if (initList.size() == 3):
        print("Size function:  Pass")
        count+=1
    else:
        print("Size function:  Failed!")

    if(initList.indexInSeq(10) == 0):
        print("indexInSeq function: Pass")
        count+=1
    else:
        print("indexInSeq: Failed")
    if(count == 6):
        print("\n{} of 6 passed\n".format(count))
        print("SeqADT is good to go!")
    else:
        print("\n{} of 6 passed\n".format(count))
        print("SeqADT is no good :( Try fixing it!")

def testCurveADT():
    testQuad = CurveT()
    quadVal_T = "testQuad.txt"
    if quadVal_T == None:
        raise LookupError("Cannot find file 'testQuad.txt'")
        exit()

    testLin = CurveT()
    linVal_T = "testLin.txt"
    if linVal_T == None:
        raise LookupError("Cannot find file 'testLin.txt'")
        exit()

    testnPoly = CurveT()
    nPolyVal_T = "testnplyv.txt"
    if nPolyVal_T == None:
        raise LookupError("Cannot find file 'testnplyv.txt'")
        exit()

    testQuad.CurveT(quadVal_T)
    testnPoly.CurveT(nPolyVal_T)
    testLin.CurveT(linVal_T)


    count = 0

    x_Lin = 8
    linVal = testLin.linVal(x_Lin)
    if (linVal == 16):
        print("linVal: Pass")
        count+=1
    else:
        print("linVal: Failed")

    x_Quad = 5
    quadVal = testQuad.quadVal(x_Quad)

    if(quadVal == 25):
        print("quadVal: Pass")
        count+=1
    else:
        print("quadVal: Failed")

    n_Poly = 3
    x_Poly = 5.5
    nPolyVal = testnPoly.npolyval(n_Poly,x_Poly)
    if(round(nPolyVal,3) == 166.375):
        print("nPolyVal: Pass")
        count+=1
    else:

        print("nPolyVal: Failed")

    if(count == 3):
        print("\n{} of 3 passed\nCurveADT is good to go!".format(count))
    else:
        print("\n{} of 3 passed\nCurveADT is no good :( Try fixing it!".format(count))

while(True):
    inv = input("Test SeqADT(1), Test CurvADT(2), Test ALL (3) or Run the Program (4): ")
    if inv == 1:
        print("\n-----------------\nTesting SeqADT....\n-----------------\n")
        testSeqADT()
        break
    elif inv == 4:
        program()
        break
    elif inv == 2:
        print("\n-----------------\nTesting CurveADT...\n-----------------\n")
        testCurveADT()
        break
    elif inv == 3:

        print("\n-----------------\nTesting SeqADT....\n-----------------\n")
        testSeqADT()
        print("\n-----------------\nTesting CurveADT...\n-----------------\n")
        testCurveADT()
        break
    else:
        print("That isn't an option. Please try again. \n")
