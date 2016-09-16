# Exercise 1.1:
# Write a command that finds the 10 most popular words in a file.

# let test.txt be the file
# make sure u have navigated to the right directory
# transform uppercase to lowercase
# transform into a list of words, one per line
# removes empty rows
# sort the list
# uniq -c will count the number of times each word occurs
# sort -nr  will sort numerically in reverse order so the most popular will appear at the top
# output in shell the first 10 words 
tr '[:upper:]' '[:lower:]' < test.txt| tr -c '[:alpha:]' '\n' | awk -F'\t' '$1!=""' | sort | uniq -c | sort -nr | head  -10


# Exercise 1.2:
# Put this data (https://www.dropbox.com/s/d5c4x905w4jelbu/cars.txt?dl=0) into a file and write a command that removes all rows where the price is more than 10,000$.

# data is put into cars.txt
# column 5 is the price of the cars
awk '($5 < 10000)' cars.txt

# Exercise 1.3:
# Using this file (https://www.dropbox.com/s/tjv9pyfrd9ztx8r/dict?dl=0) as a dictionary, write a simple spellchecker that takes input from stdin or a file and outputs a list of words not in the dictionary. One solution gets 721 misspelled words in this Shakespeare file (https://www.dropbox.com/s/bnku7grfycm8ii6/shakespeare.txt?dl=0).
# Consider using the command “comm”.

# shakespeare.txt contains shakespeare file and dict contains the dictionary
# transfrom to lower and one word per line
# sort and only leave unique terms and insert it into new_shakespeare.txt
tr '[:upper:]' '[:lower:]' < shakespeare.txt | tr -c '[:alpha:]' '\n' | sort | uniq > new_shakespeare.txt

# lowercase transformation 
# sort and only leave unique terms and insert it into new_dict.txt
tr '[:upper:]' '[:lower:]' < dict | sort | uniq > new_dict.txt

# compare the two files
# first col of comm output is terms in new_shakespeare that is not in new_dict
# remove first col that are blank and extract the col
comm new_shakespeare.txt new_dict.txt | awk -F'\t' '$1!=""'| awk '($1)'

# Exercise 1.4:
# Launch a t2.micro instance on Amazon EC2. Log onto the instance, create some files and install some software (for example git).
# (You have to enter your credit card to make an Amazon account. If you want to make sure you do not spend any money, you can remove your account when you are finished with the exercises. If you really don’t want to do this, you can use the GBar instead of Amazon.)

# Exercise 1.5:
# Create a few files locally on your computer. Create a new repository on Github and push your files to this repository. Log on to a t2.micro instance on Amazon EC2 and clone your repository there. Make some changes to the files, push them again and pull the changes on your local machine.
# (If you did not make an Amazon EC2 account in Exercise 1.4, then you should push your files and pull them on the gbar.)



