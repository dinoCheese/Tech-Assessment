'''
PLAN FOR TABLE
# TASK: Make a results table using the dictionary
1. Print a header to help visualise the placements
2. Loop through the medalResults data structure and pull the first entry
3. Get the Value (sport) from the first entry and place that at the start of each line
4. Get the Value (country) from the second entry
5. Then take off the first 2 chars and place all three country entries after the sport
5. Repeat for all values until complete
- In future adapt the code so that it scales better by making the array values (arr and arr2) dependent on input
- Also did not use results object, this can be improved
'''

'''
PLAN FOR SCORES
# TASK: Calculate points for each country based on podium position, then sort and print
1. Loop through the data structure only looking at the "podium" value  
2. Take this value and split chars into two - the first: position - the second: country 
3. Use an empty dictionary and check if country entry already exists
4. If it does not, create a new entry for that country
5. If it does, check which placement that country has won and award the corresponding points 
6. Once finished, sort in value order descending
7. Then print out the results in the same style as the test case 
'''

medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]


def createMedalTable():

    print("\n ------- Results Table: ------- \n")
    print("	     | 1st place | 2nd place | 3rd place ")

    # arrays to hold data representing the number of items in medalResults
    arr = [0, 1, 2, 3]
    arr2 = [0, 1, 2]

    # Looping through the medalResults dict to extract sport and podium position
    for x in arr:
        print("\n" + medalResults[x]["sport"] + " | ", end='')
        for y in arr2:
            medinput = medalResults[x]["podium"][y][2:]
            # takes values after the initial two chars
            print(medinput, end='' + " | ")

    print("\n")
    print("\n ------- Points Table: ------- \n")

    table = {}

    for x in arr:
        for y in arr2:
            # looping through medalResults dict to extract country and podium position
            Position = medalResults[x]["podium"][y][0:1]
            # gets the first char from value
            Country = medalResults[x]["podium"][y][2:9]
            # gets remaining chars after 2nd position from value

            if Country in table == False:
                table.append(Country)
                # add country if it doesn't exist in table already
                # then allocates points
            elif Position == "1":
                table[Country] = table.get(Country, 0) + 3
            elif Position == "2":
                table[Country] = table.get(Country, 0) + 2
            elif Position == "3":
                table[Country] = table.get(Country, 0) + 1

    # sort table descending order, now called a
    #sortedtable = sorted(table.items(), key=lambda x: x[1], reverse=True)
    #print(sortedtable)

    sortedtable = sorted(table.items(), key=lambda t: t[::-1], reverse=True)

    # prints the results nicely
    for i, j in sortedtable:
        print(i, j)

    return

def test_function():
    # This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

# Main
createMedalTable()


#### NOTES ####
'''
FINAL POINTS
- the results table doesn't match the test table in terms of the order given but is still valid 
- there is a typo (unsure if on purpose) in the medalResults data structure for High Jump for Qatar (says 1 should be 2)
the typo will impact the results especially for the points 
- Could be improved for scalability by making the data structures more dynamically linked to input
- Could also use the test function and throw some exceptions if outside the scope to make more stable
'''





