# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 02:23:17 2026

@author: pb25aap
"""

#PRINCE BOBEBE 24153031

#Each package that will be used in this script is imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
#The functions to be used are defined 
def plot_line_graph(xarray, yarray, identifier, title):
    """
    The function creates a line graph using two variables to plot the 
    coordintes and an identifier and title for the graph.

    Parameters
    ----------
    xarray : float
        a variable containing values that will be used to plot the x-axis 
        graph coordinates.
    yarray : float
        a variable containing values that will be used to plot the y-axis 
        graph coordinates.
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
    # number = 0
    # while number < 1:
    #     number = int(input("How many line plot do you want? "))
    
    plt.figure()
    
    # if number != 1 :
    #     for i in range(number):
    #         name = str(input("Enter the name of the line "))
    #         y_array = input("Enter y axis array ")
    #         plt.plot(xarray, y_array, label=name)
    # else:
    #     plt.plot(xarray, yarray, label=identifier)
    
    plt.plot(xarray[], yarray[i], label=identifier[i])

    plt.xlabel('Years')
    plt.ylabel('Number of people without electricity per 1000000')
    plt.legend()
    plt.title(title)

    plt.savefig(title)

    plt.show()


def plot_bar_chart(identifier, values, title):
    """
    The function creates a bar chart using two variables to generate the chart
    and makes use of an identifier and title.

    Parameters
    ----------
    identifier : string
        a variable containing a string(s) to identify each tick.
    values : float
        a variable containing a value(s) to give the height of each tick.
    title : string
        a string variable that will be used as the title of the chart and the 
        filename of the chart when it is saved.

    Returns
    -------
    a bar chart.

    """
    #Figure is used to create an environment for the figure and figsize 
    #specifies the resolution of the figure which is 12x6
    plt.figure(figsize=(12,6))
    
    plt.bar(identifier, values, width=0.8)
    
    #The x and y axis are labled and the x axis labes are tilted at 20degrees
    plt.xlabel('Years')
    plt.xticks(rotation=20)
    plt.ylabel('Number of people without electricity per 1000000')
    
    #The chart is given a title which will also be used as the filename 
    #when saved
    plt.title(title)
    plt.savefig(title)
    
    #To print out the created figure
    plt.show()
    
    
def plot_pie_chart(identifier, values, title):
    """
    The function creates a pie chart using two variables to generate the chart
    and makes use of a title.

    Parameters
    ----------
    identifier : string
        a variable containing a string(s) to identify each section name.
    values : float
        a variable containing a value(s) to give the size of each section.
    title : string
        a string variable that will be used as the title of the chart and the 
        filename of the chart when it is saved.

    Returns
    -------
    a pie chart.

    """    
    #Figure is used to create an environment for the figure
    plt.figure()
    
    plt.pie(values, labels=identifier)
    
    #The chart is given a title which will also be used as the filename 
    #when saved    
    plt.title(title)

    plt.savefig(title)
    
    #To print out the created figure
    plt.show()    


#The main code begins


#The data is extracted into an array using pandas package and inspected
df_electricity = pd.read_csv("Number of \
                             people without access to electricity.csv")
print(df_electricity)

#the countries colums is extracted into an array and inspected
countries = df_electricity["Country"]
print(countries)

#the 2023 column is extracted and inspected
year_2023 = df_electricity["2023"]
print(year_2023)

#Extracting the each country row and inspecting it
Brazil_numbers = df_electricity.iloc[0, 1:-1]
print(Brazil_numbers) 

DRC_numbers = df_electricity.iloc[1, 1:-1]
print(DRC_numbers) 

EAP_numbers = df_electricity.iloc[2, 1:-1]
print(EAP_numbers) 

Ethiopia_numbers = df_electricity.iloc[3, 1:-1]
print(Ethiopia_numbers) 

India_numbers = df_electricity.iloc[4, 1:-1]
print(India_numbers) 

Nigeria_numbers = df_electricity.iloc[5, 1:-1]
print(Nigeria_numbers) 

SA_numbers = df_electricity.iloc[6, 1:-1]
print(SA_numbers) 

years = np.array(np.linspace(2000, 2022, 23))
 
plot_bar_chart(countries, year_2023, \
               "People without electricity per 1 000 000")
plot_pie_chart(countries, year_2023,\
               "People without Electricity per 1 000 000")
plot_line_graph(years, Brazil_numbers, countries, "line graph")

