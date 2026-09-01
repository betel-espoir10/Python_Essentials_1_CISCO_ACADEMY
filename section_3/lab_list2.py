#step 1: create an empty list named beatles;
beatles = [ ]
#step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("List of Beatles members:", beatles)

#step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
for i in range(2):
    beatles.append(input("Enter a band member to add: "))

print("List of Beatles members after adding Stu Sutcliffe and Pete Best:", beatles)

#step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[-1]  # Remove Pete Best
del beatles[-1]  # Remove Stu Sutcliffe

print("List of Beatles members after removing :", beatles)

#step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, "Ringo Starr")

print("Final list of Beatles members after adding Ringo Starr:", beatles)