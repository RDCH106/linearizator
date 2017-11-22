# -*- coding: utf-8 -*-

from __future__ import division


class Linearizator(object):

    def __init__(self, x1=None, y1=None, x2=None, y2=None, unknown=None, equation=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__unknown = unknown
        self.__known = None
        if (self.__unknown == "y"):
            self.__known = "x"
        if(self.__unknown == "x"):
            self.__known = "y"
        self.__equation = equation

    @property
    def x1(self):
        return self.__x1

    @property
    def x2(self):
        return self.__x2

    @property
    def y1(self):
        return self.__y1

    @property
    def y2(self):
        return self.__y2

    @property
    def unknown(self):
        return self.__unknown

    @property
    def equation(self):
        return self.__equation

    @x1.setter
    def x1(self, value):
        self.__x1 = value

    @x2.setter
    def x2(self, value):
        self.__x2 = value

    @y1.setter
    def y1(self, value):
        self.__y1 = value

    @y2.setter
    def y2(self, value):
        self.__y2 = value

    @unknown.setter
    def unknown(self, value):
        if(value == "x" or value == "y"):
            self.__unknown = value
            if value == "x":
                self.__known = "y"
            if value == "y":
                self.__known = "x"
        else:
            print("Allowed values x and y")

    @equation.setter
    def equation(self, equation):
        mvalue, cvalue = equation
        self.__equation = (mvalue, cvalue)

    def linearize(self):

        # y = mx + n
        # x = my + n
        # http://www.vitutor.com/geo/rec/d_7.html
        # http://www.vitutor.com/geo/rec/d_4.html

        if self.check_values():

            v_x2x1 = self.__x2 - self.__x1
            #print(v_x2x1)
            v_y2y1 = self.__y2 - self.__y1
            #print(v_y2y1)

            mx = v_y2y1/v_x2x1
            #print(mx)
            vx1 = -(self.__x1 * v_y2y1)/v_x2x1
            #print(vx1)
            vc = vx1+self.__y1
            #print(vc)

            if(self.__unknown == "y"):
                self.__equation = (mx, vc)
            else:
                self.__equation = (1/mx, vc/mx)

    def inverse(self):
        if self.check_values():
            modified = False
            if self.__unknown == "y":
                self.__known = "y"
                self.__unknown = "x"
                modified = True
            if self.__unknown == "x" and not modified:
                self.__known = "x"
                self.__unknown = "y"
            self.__equation = (1/self.__equation[0], -(self.__equation[1]/self.__equation[0]))

    def pretty_equation(self):
        if self.check_values():
            return self.__unknown + " = " + str(self.__equation[0]) + self.__known + " + (" + str(self.__equation[1]) + ")"

    def calculate(self, value):

        result = None

        if self.check_values():
            result = self.__equation[0] * value + self.__equation[1]
            print(self.__unknown+" = "+str(result))
            return result

    def check_values(self):
        if self.__unknown == None or (self.__unknown != "x" and self.__unknown != "y"):
            print("Undefined Unknown! Set x o y as unknown")
            return False

        if self.__x1 is None:
            print("Undefined value of  x1")
            return False
        else:
            if self.__x2 is None:
                print("Undefined value of  x2")
                return False
            else:
                if self.__x2 - self.__x1 == 0:
                    print("Not linearizable!: x2-x1=0 --> x2 = x1")
                    return False

        if self.__y1 is None:
            print("Undefined value of  y1")
            return False
        else:
            if self.__y2 is None:
                print("Undefined value of  y2")
                return False
            else:
                if self.__y2 - self.__y1 == 0:
                    print("Not linearizable!: y2-y1=0 --> y2 = y1")
                    return False
        return True
