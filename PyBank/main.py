import os
import csv

#path to collect data from the Resources folder, file budget_data.csv
budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# open csv file
with open(budget_csv, encoding='utf') as budgetcsv:
    #csv reader to specify delimiter and variables
    budgetcsvr = csv.reader(budgetcsv, delimiter =",")
    #account for the header row
    header = next(budgetcsvr, None)
    #set the variables
    number_of_months = 0
    total_profitslosses = 0
    preprofitlosseschange = 0
    totalprofitlosseschange = 0
    numberofchanges = 0
    largestincrease = 0
    largestincreasedate = "" #setting variable as empty string
    largestdecrease = 0
    largestdecreasedate = "" #setting variable as empty string
    averageprofitslosseschangerounded = 0


    for row in budgetcsvr:
        #count the number of months
        number_of_months+=1
        #sum the total of profits and losses
        total_profitslosses +=int(row[1])
        #calculate the profits and losses changes
        profitloss = int(row[1])
        if number_of_months > 1:
            profitlosseschange =profitloss-preprofitlosseschange
            totalprofitlosseschange+=profitlosseschange
            numberofchanges +=1
            #look for largest increase
            if profitlosseschange > largestincrease:
                largestincrease = profitlosseschange
                largestincreasedate = (row[0])

            #look for largest decrease
            if profitlosseschange < largestdecrease:
                largestdecrease = profitlosseschange
                largestdecreasedate = (row[0])

        #restart the preprofitlosseschange variable
        preprofitlosseschange = profitloss

    #average of profits an losses changes
    averageprofitslosseschange = (totalprofitlosseschange/numberofchanges)
    

#print the total of months
print ("Total Months:" + " " + str(number_of_months))
#print the total of profits and losses
print ("Total:" + " " + "$" + str(total_profitslosses))
#print the average change of profits and losses rounded to 2 decimals
averageprofitslosseschangerounded = round(averageprofitslosseschange, 2)
print ("Average Change:" + " " + str(averageprofitslosseschangerounded))
#print the max and min of the changes in profit/losses
print ("Greatest Increase in Profits:" + " " + str(largestincreasedate) + " " + "(" + "$" + str(largestincrease) + ")")
print ("Greatest Decrease in Profits:" + " " + str(largestdecreasedate) + " " + "(" + "$" + str(largestdecrease) + ")")


#create a single string variable containing all the results to export to a txt file.  Documentation researched to include different variables and information in one sinle string:
#https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/#:~:text=If%20you%20have%20multiple%20variables,%7D%20and%20%7Bvar_name%7D.%22
budget_singlestring = f"""
Total Months: {str(number_of_months)}
Total: ${str(total_profitslosses)}
Average Change: {str(averageprofitslosseschangerounded)}
Greatest Increase in Profits: {str(largestincreasedate)} (${str(largestincrease)})
Greatest Decrease in Profits: {str(largestdecreasedate)} (${str(largestdecrease)})
"""
budgettxt_path = "analysis/budgetresults.txt"
with open(budgettxt_path,"w") as file:
    file.write(budget_singlestring)

