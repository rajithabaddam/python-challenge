import os

# Module for reading CSV files
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

csvpath = os.path.join("..", "Resources", "election_data.csv") 


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    Total_voter_count = 0
    khan_per = 0
    candidates_lst = []
    unique_candidates_lst = []
    member1_cnt = 0
    member2_cnt = 0
    member3_cnt = 0
    member4_cnt = 0
    member1_percent =0
    member2_percent =0
    member3_percent =0
    member4_percent =0
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        Total_voter_count = Total_voter_count + 1
        candidates_lst.append(row[2])
    for x in candidates_lst:
        if x not in unique_candidates_lst: 
            unique_candidates_lst.append(x) 

    #print (unique_candidates_lst)  
    # Find the voters list count by member  

    for i in range(len(candidates_lst)):
        if candidates_lst[i] ==  unique_candidates_lst[0] :
            member1_cnt = member1_cnt +1
        if candidates_lst[i] ==  unique_candidates_lst[1] :
            member2_cnt = member2_cnt +1
        if candidates_lst[i] ==  unique_candidates_lst[2] :
            member3_cnt = member3_cnt +1
        if candidates_lst[i] ==  unique_candidates_lst[3] :
            member4_cnt = member4_cnt +1
    #Calcualte Percent for each candidate
    member1_percent = member1_cnt/Total_voter_count
    member2_percent = member2_cnt/Total_voter_count
    member3_percent = member3_cnt/Total_voter_count
    member4_percent = member4_cnt/Total_voter_count

    member_percent_lst = [member1_percent,member2_percent,member3_percent,member4_percent]
    max_percent_pos = max_pos = member_percent_lst.index(max(member_percent_lst))
  
    #Print all results

    print ("Election Results")
    print ("--------------------------------------------")
    print("Total Votes : "+str(Total_voter_count) )
    print ("--------------------------------------------")
    print(unique_candidates_lst[0] +": " +"{:.3%}".format(member1_percent)+ "  (" +str(member1_cnt)+ ")")
    print(unique_candidates_lst[1] +": " +"{:.3%}".format(member2_percent)+ "  (" +str(member2_cnt)+ ")")
    print(unique_candidates_lst[2] +": " +"{:.3%}".format(member3_percent)+ "  (" +str(member3_cnt)+ ")")
    print(unique_candidates_lst[3] +": " +"{:.3%}".format(member4_percent)+ "  (" +str(member4_cnt)+ ")")
    print ("--------------------------------------------")
    print ("Winner : " +str(unique_candidates_lst[int(max_percent_pos)]))
    print ("--------------------------------------------")

    #print output to text file
    #  
    file1 = open("output.txt","w")
    file1.write("Election Results \n")
    file1.write("--------------------------------------------\n")
    file1.write("Total Votes : "+str(Total_voter_count) + "\n" )
    file1.write("--------------------------------------------\n")
    file1.write (unique_candidates_lst[0] +": " +"{:.3%}".format(member1_percent)+ "  (" +str(member1_cnt)+ ") \n") 
    file1.write(unique_candidates_lst[1] +": " +"{:.3%}".format(member2_percent)+ "  (" +str(member2_cnt)+ ") \n")
    file1.write(unique_candidates_lst[2] +": " +"{:.3%}".format(member3_percent)+ "  (" +str(member3_cnt)+ ") \n")
    file1.write(unique_candidates_lst[3] +": " +"{:.3%}".format(member4_percent)+ "  (" +str(member4_cnt)+ ") \n")
    file1.write("--------------------------------------------\n")
    file1.write("Winner : " +str(unique_candidates_lst[int(max_percent_pos)]) +"\n")
    file1.write("--------------------------------------------\n")
   
   
   