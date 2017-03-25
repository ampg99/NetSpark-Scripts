#Global imports
from datetime import datetime
import csv, os.path


# Begin timing the script
start_time = datetime.now()

# Define the primary function (to be moved to a separate module some day...)
def bParse(filename):
    with open(filename, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        row1 = next(reader)
        # This is the first variable that you said something about "making the new
        # doc name" or something
        docName = row1[0]
        # Test to see if it prints the right thing
        print docName
        # Skip some lines
        next(reader)
        next(reader)
        # This is the mfg and model row
        row4 = next(reader)
        # Assign the 3rd variable to Manufacturer from this row
        mfg = row4[2]
        # Assign the 4th variable to Model from this row
        model = row4[3]
        # Print shit to make sure it works
        print "Manufacturer is " + mfg
        print "Model is " + model
        # Skip a row
        next(reader)
        # Now, we're on row 6, so I just plopped everything else from here into
        # a list. Each line is a tuple we can reference
        that_damn_data = list(reader)
        # Print tests to make sure it works
        print that_damn_data[0][1]
        print that_damn_data[1][1]

# Grab the filename to edit into data
# In the end you'll get this variable from your os.path thing
# filename = raw_input('What is the file name, like "nameoffile.csv": ')
filename = "example.csv"
# Run the primary function in this program
bParse(filename)


end_time = datetime.now()
# How long did it run?
total_time = end_time - start_time
print "\nTotal time for script: \n" + str(total_time)
