#!/usr/bin/env python3
from random import randint
# if from CGG import *, import only 'get_color'
__all__ = ['get_color']
__module__ = "CGG"
class ColorGammaGenerator:
    # @author Hamid Abdul
 
    
    # Quantity of colors in gamma
    __COLOR_QUANTITY = 5
    # minimum indexing value through predefined gammas
    __MIN_BASE = 2
    # list offset, when indxing list
    __LIST_OFFSET = 1
    # Those values are hardcoded into list comprahension, because it would not work otherwise.
    # this generates a new gamma of colors on a random basis.
    __BASE_OTHER = ["#%s%s"%("0"*(6-len(str(hex(color))[2:])),str(hex(color))[2:]) for quantity in range(__COLOR_QUANTITY) for color in [randint(0,16777215)]]
    # this are predefined gammas of colors:
    __PREDEFINED_GAMMAS =(["#2b275a","#792654","#a20800","#db4705","#ffb80e"],["#63afae","#f9654a","#ff733e","#ff9c3e","#ffc75a"],
                          ["#fb9090","#ffbb82","#aef279","#a2fffd","#b67dff"],["#007dc3","#1369c1","#13ab2d","#ee7d31","#aaaaaa"],
                          ["#d9f9b3","#d3ff9f","#c4ff7e","#b2ff56","#9cff25"],["#fd8313","#f56546","#eb463f","#e81854","#b80b6d"],
                          ["#136a9b","#fcc914","#2284b9","#36a0ce","#3d3d3d"],["#93c52f","#200c91","#241ca7","#385aba","#4e7fd5"],
                          ["#ff66cc","#ccff66","#66ccff","#ffd97f","#ff8383"],["#df9c9c","#57b0c3","#5475bd","#9791d6","#6fd49f"])
    # this is a qunatity of predefined gammas
    __PREDEFINED_GAMMAS_QTY = len(__PREDEFINED_GAMMAS)
    def __init__(self,base):
        base=int(base)
        # if there is no predefined gamma for the base, use generated one
        if base > (ColorGammaGenerator.__PREDEFINED_GAMMAS_QTY) or base < ColorGammaGenerator.__MIN_BASE:
            self.__set_base_gamma(ColorGammaGenerator.__BASE_OTHER)
        # else use predefined one
        else:
            self.__set_base_gamma(ColorGammaGenerator.__PREDEFINED_GAMMAS[base-ColorGammaGenerator.__LIST_OFFSET])
        
    def __str__(self):
        # this is a string representation of gamma
        return str(self.get_gamma())

    def __set_base_gamma(self,base_gamma):
        # this is a setter for base gamma
        self.__base_gamma = base_gamma

    def get_gamma(self):
        # this is a getter for base gamma
        return self.__base_gamma

def get_color(base):
    # this is a function for quick getting of gamma.
    gamma = ColorGammaGenerator(base)
    return gamma.get_gamma()

	
