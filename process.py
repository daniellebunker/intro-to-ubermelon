#My answers:

log_file = open("um-server-01.txt")
#opens log_file which contains sales report info

def sales_reports(log_file):
    """Displays sales report for Mondays"""

    for line in log_file:
    #iterate over each line in log_file
        line = line.rstrip()
        #strips trailing characters of line and stores in 'line' variable
        day = line[0:3]
        #displays the first three characters of a line and stores it in 'date' variable
        if day == "Mon":
        #if value is equal to Monday
            print(line)
        #print the line of information for 'date' 

sales_reports(log_file)
#function call


#HB Solution:
# # Create a file object from um-server-01.txt so we can access its
# # contents via Python
# log_file = open("um-server-01.txt")

# # Function definition
# def sales_reports(log_file):
#     """Print sales info for Monday."""

#     # Get each line in `log_file`
#     for line in log_file:
#         line = line.rstrip()  # Remove extra whitespace to the right

#         # Get the first 3 characters in `line` --- that's where we can get the
#         # day of the week from `line`
#         day = line[0:3]

#         # Change "Tue" to "Mon" (since we only want to print Mondays' logs)
#         if day == "Mon":
#             print(line)


# # Call `sales_reports` and pass in the `log_file` defined on line 3
# sales_reports(log_file)