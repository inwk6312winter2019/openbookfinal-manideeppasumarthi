
file1=open("book1.txt","r")
file2=open("book2.txt","r")
file3=open("Overlap_compound1_2","w")
list1=file1.readlines()
list2=file2.readlines()

for line1 in list1:
  for line2 in list2:
    if line1.strip() in line2.strip().split(' '):
      print line2
      file3.write(line2)
