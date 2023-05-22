"""
Author: Quinton Austin, qaustin@purdue.edu
Assignment: 10.1 - monthly sales
Date: 4/5/2023

Description:
This is a program that takes data from the user and creates a pie chart

Contributors:
    Quinton Austin, qaustin@purdue.edu

My contributor(s) helped me:
    [x ] understand the assignment expectations without
        telling me how they will approach it.
    [ x] understand different ways to think about a solution
        without helping me plan my solution.
    [x ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import matplotlib.pyplot as plt    

"""Write new functions below this line (starting with unit 4)."""
def main():

# Define the colors using Purdue's secondary color palette
    colors = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11',
          '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']

# Define the labels for the months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

# Ask the user for monthly sales data and store it in a list
    sales = []
    for i in range(12):
        sales.append(int(input(f"Enter the sales for {months[i]}: ")))

# Plot the pie chart
    plt.pie(sales, labels=months, colors=colors, autopct='%1.1f%%')
    plt.title('Monthly Sales Values')
    plt.axis('equal')

# Save the figure as a PDF file
    plt.savefig('monthly_sales_qaustin.pdf')

# running the main function
if __name__ == '__main__':
    main()

