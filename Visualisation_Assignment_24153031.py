# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 02:23:17 2026

@author: pb25aap
"""

# PRINCE BOBEBE 24153031

# Each package that will be used in this script is imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The functions to be used are defined


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
    # Figure is used to create an environment for the figure and figsize
    # specifies the resolution of the figure which is 12x6
    plt.figure(figsize=(12, 6))

    plt.bar(identifier, values, width=0.8)

    # The x and y axis are labled and the x axis labes are tilted at 20degrees
    plt.xlabel('Years')
    plt.xticks(rotation=20)
    plt.ylabel('Number of people without electricity per 1 000 000')

    # The chart is given a title which will also be used as the filename
    # when saved
    plt.title(title)
    plt.savefig(title)

    # To print out the created figure
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
    # Figure is used to create an environment for the figure
    plt.figure()

    plt.pie(values, labels=identifier)

    # The chart is given a title which will also be used as the filename
    # when saved
    plt.title(title)

    plt.savefig(title)

    # To print out the created figure
    plt.show()


# The main code begins


# The data is extracted into an array using pandas package and inspected
df_electricity = pd.read_csv(
    "Number of people without access to electricity.csv")
print(df_electricity)

# the countries colums is extracted into an array and inspected
countries = df_electricity["Country"]
print(countries)

# the 2023 column is extracted and inspected
year_2023 = df_electricity["2023"]
print(year_2023)

# Extracting the each country row and inspecting it
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

# An array of the years is created since these values are not present within
# the dataframe but as column headers
years = np.array(np.linspace(2000, 2022, 23))

# using the function and the variables to plot both defined graphs
plot_bar_chart(countries, year_2023,
               "People without electricity per 1 000 000")
plot_pie_chart(countries, year_2023,
               "People without Electricity per 1 000 000")

# plotting the line graph
# The argument of figure specifies the image should be a 12x6 inches
plt.figure(figsize=(12, 6))

# plotting each line using an array of the years and the number of people
# and labeling each using the country name
plt.plot(years, Brazil_numbers, label=countries[0])
plt.plot(years, DRC_numbers, label=countries[1])
plt.plot(years, EAP_numbers, label=countries[2])
plt.plot(years, Ethiopia_numbers, label=countries[3])
plt.plot(years, India_numbers, label=countries[4])
plt.plot(years, Nigeria_numbers, label=countries[5])
plt.plot(years, SA_numbers, label=countries[6])

# labeling the x axis and the y axis then producing a legend showing
# which line represents which country
plt.xlabel('Years')
plt.ylabel('Number of people without electricity per 1 000 000')
plt.legend()

# The title of the line graph is specified and the figure is saved
plt.title("line graph")

plt.savefig("line graph")

# To produce the figure
plt.show()
