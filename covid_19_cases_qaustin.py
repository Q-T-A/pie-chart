"""
Author: Quinton Austin, qaustin@purdue.edu
Assignment: 10.3 - covid 19 cases
Date: 4/10/2023

Description:
This program is designed to read data from a file and create a chart showing covid cases

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

    # Read the data from the file
    filename = "indiana_covid-19_data_spring_2023.txt"
    with open(filename) as f:
        lines = f.readlines()

    dates = []
    new_cases = []
    total_cases = []

    # Calculate the total number of cases for each week
    total_cases_so_far = 0
    for line in lines:
        start_date, end_date, cases, deaths = line.split()
        dates.append(start_date)
        total_cases_so_far += float(cases)
        total_cases.append(total_cases_so_far / 1000)

    # Create a bar chart using matplotlib
    plt.bar(dates, total_cases, width=7)

    # Customize the chart
    plt.xlabel("Date")
    plt.ylabel("Number of Cases (in thousands)")
    plt.title("Weekly Positive COVID-19 Cases in Indiana")
    plt.xticks(rotation = 12)
    plt.savefig("covid_19_cases_qaustin.pdf", bbox_inches="tight")
    plt.show()

if __name__ == '__main__':
    main()