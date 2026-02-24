# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 02:23:17 2026

@author: pb25aap
"""

#PRINCE BOBEBE 24153031

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def plot_line_graph(xarray, yarray, identifier, title):
    """
    The function creates a line graph using two arrays to plot the coordintes
    and an identifier and title for the graph.

    Parameters
    ----------
    xarray : array
        an array of values that will be used to plot the x-axis graph 
        coordinates.
    yarray : array
        an array of values that will be used to plot the y-axis graph 
        coordinates.
    identifier : string
        a string of character that will be given as the name of the line that 
        is plotted.
    title : string
        a string of characters to give the graph a title and the filename of 
        the graph image produced.

    Returns 
    -------
    a line graph.

    """
    plt.figure()

    plt.plot(xarray, yarray, label=identifier)


    plt.xlabel('Years')
    plt.ylabel('Number of people without electricity per 1000000')
    plt.legend()
    plt.title(title)

    plt.savefig(title)

    plt.show()
    
def plot_bar_chart():
    
    
    
    plt.figure()
    
    plt.bar()