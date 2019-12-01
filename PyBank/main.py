import os

# Module for reading CSV files
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

csvpath = os.path.join("..", "Resources", "budget_data.csv") 


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    count = 0
    total_pl = 0
    profloss_lst = []
    profloss_month_lst = []
    profloss_change_lst = []
    pl_dic =[]
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        count = count + 1
        total_pl = int(row[1])+ total_pl
        profloss_month_lst .append(row[0])
        profloss_lst.append(row[1])
      
    for i in range(len(profloss_lst)-1):
      profloss_change_lst.append(int(profloss_lst[i + 1]) - int(profloss_lst[i]))
    #print(profloss_change_lst)

    #average value
    avg_pl = round((sum(profloss_change_lst))/len(profloss_change_lst), 2)
    max_pl = max(profloss_change_lst)
    min_pl = min(profloss_change_lst)
    max_pos = profloss_change_lst.index(max(profloss_change_lst))
    min_pos = profloss_change_lst.index(min(profloss_change_lst)) 

    #Print results

    print("Finacial Analysis")  
    print(" ------------------------")  
    print("Total Months :" +str(count))
    print("Total :$" +str(total_pl))
    print("Average  Change : $"+str(avg_pl))
    print("Greatest Increase in Profits: " + profloss_month_lst[int(max_pos)+1]+ " ($" +str(max_pl) + ")")
    print("Greatest Decrease in Profits: " + profloss_month_lst[int(min_pos)+1]+ " ($" +str(min_pl) + ")")
   
    #Print output to text file
    
    file1 = open("output.txt","w")
    file1.write("Finacial Analysis \n")
    file1.write("--------------------------------------------\n")
    file1.write("Total Months: " +str(count)+ "\n" )
    file1.write("Total: $" +str(total_pl) + "\n" )
    file1.write("Average  Change: $"+str(avg_pl)+ "\n" )
    file1.write("Greatest Increase in Profits: " + profloss_month_lst[int(max_pos)+1]+ " ($" +str(max_pl) + ") \n")
    file1.write("Greatest Decrease in Profits: " + profloss_month_lst[int(min_pos)+1]+ " ($" +str(min_pl) + ") \n")