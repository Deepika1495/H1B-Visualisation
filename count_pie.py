import xlrd
book = xlrd.open_workbook("a.xlsx")
book2 = xlrd.open_workbook("b.xlsx")
book3 = xlrd.open_workbook("c.xlsx")
sheet = book.sheet_by_index(0)
sheet2 = book2.sheet_by_index(0)
sheet3 = book3.sheet_by_index(0)
file = open("count_pie.csv","w")
file.write("y1,y2,y3\n")
count_certified16=0
count_denied16=0
count_withdrawn16=0
count_certified15=0
count_denied15=0
count_withdrawn15=0
count_certified14=0
count_denied14=0
count_withdrawn14=0
for rx in range(sheet.nrows):
    tmp = sheet.cell_value(rowx=rx,colx=1)
    stat = sheet.cell_value(rowx=rx,colx=4)
    if (stat=="H-1B" and tmp =="CERTIFIED"):
        count_certified16+=1
    elif (stat=="H-1B" and tmp =="DENIED"):
        count_denied16+=1
    elif (stat == "H-1B" and (tmp =="CERTIFIED-WITHDRAWN" or tmp == "WITHDRAWN")):
        count_withdrawn16+=1
for rx in range(sheet2.nrows):
    tmp2 = sheet2.cell_value(rowx=rx,colx=1)
    stat2 = sheet2.cell_value(rowx=rx,colx=4)
    if (stat2=="H-1B" and tmp2 =="CERTIFIED"):
        count_certified15+=1
    elif (stat2=="H-1B" and tmp2 =="DENIED"):
        count_denied15+=1
    elif (stat2 == "H-1B" and (tmp2 =="CERTIFIED-WITHDRAWN" or tmp2 == "WITHDRAWN")):
        count_withdrawn15+=1
for rx in range(sheet3.nrows):
    tmp3 = sheet3.cell_value(rowx=rx,colx=1)
    stat3 = sheet3.cell_value(rowx=rx,colx=4)
    if (stat3=="H-1B" and tmp3 =="CERTIFIED"):
        count_certified14+=1
    elif (stat3=="H-1B" and tmp3 =="DENIED"):
        count_denied14+=1
    elif (stat3 == "H-1B" and (tmp3 =="CERTIFIED-WITHDRAWN" or tmp3 == "WITHDRAWN")):
        count_withdrawn14+=1
file.write( str(count_certified16) + "," + str(count_certified15) + "," + str(count_certified14) + "\n")
file.write( str(count_denied16) + "," + str(count_denied15) + "," + str(count_denied14) + "\n" )
file.write( str(count_withdrawn16) + "," + str(count_withdrawn15) + "," + str(count_withdrawn14) +"\n")
print "yay"
file.close();
