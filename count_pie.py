import xlrd
book = xlrd.open_workbook("a.xlsx")
book2 = xlrd.open_workbook("b.xlsx")
book3 = xlrd.open_workbook("c.xlsx")
book4 = xlrd.open_workbook("d.xlsx")
book5 = xlrd.open_workbook("e.xlsx")
sheet = book.sheet_by_index(0)
sheet2 = book2.sheet_by_index(0)
sheet3 = book3.sheet_by_index(0)
sheet4 = book4.sheet_by_index(0)
sheet5 = book5.sheet_by_index(0)
file = open("count_pie.csv","w")
file.write("y16,y15,y14,y13,y12\n")
count_certified16=0
count_denied16=0
count_cwithdrawn16=0
count_withdrawn16=0
count_certified15=0
count_denied15=0
count_cwithdrawn15=0
count_withdrawn15=0
count_certified14=0
count_denied14=0
count_cwithdrawn14=0
count_withdrawn14=0
count_certified13=0
count_denied13=0
count_cwithdrawn13=0
count_withdrawn13=0
count_certified12=0
count_denied12=0
count_cwithdrawn12=0
count_withdrawn12=0
for rx in range(sheet.nrows):
    tmp = sheet.cell_value(rowx=rx,colx=1)
    stat = sheet.cell_value(rowx=rx,colx=4)
    if (stat=="H-1B" and tmp =="CERTIFIED"):
        count_certified16+=1
    elif (stat=="H-1B" and tmp =="DENIED"):
        count_denied16+=1
    elif (stat == "H-1B" and tmp == "WITHDRAWN"):
        count_withdrawn16+=1
    elif (stat == "H-1B" and tmp =="CERTIFIED-WITHDRAWN"):
        count_cwithdrawn16+=1    
for rx in range(sheet2.nrows):
    tmp2 = sheet2.cell_value(rowx=rx,colx=1)
    stat2 = sheet2.cell_value(rowx=rx,colx=4)
    if (stat2=="H-1B" and tmp2 =="CERTIFIED"):
        count_certified15+=1
    elif (stat2=="H-1B" and tmp2 =="DENIED"):
        count_denied15+=1
    elif (stat2 == "H-1B" and tmp2 == "WITHDRAWN"):
        count_withdrawn15+=1
    elif (stat2 == "H-1B" and tmp2 =="CERTIFIED-WITHDRAWN"):
        count_cwithdrawn15+=1    
for rx in range(sheet3.nrows):
    tmp3 = sheet3.cell_value(rowx=rx,colx=1)
    stat3 = sheet3.cell_value(rowx=rx,colx=4)
    if (stat3=="H-1B" and tmp3 =="CERTIFIED"):
        count_certified14+=1
    elif (stat3=="H-1B" and tmp3 =="DENIED"):
        count_denied14+=1
    elif (stat3 == "H-1B" and tmp3 == "WITHDRAWN"):
        count_withdrawn14+=1
    elif (stat3 == "H-1B" and tmp3 =="CERTIFIED-WITHDRAWN"):
        count_cwithdrawn14+=1
for rx in range(sheet4.nrows):
    tmp4 = sheet4.cell_value(rowx=rx,colx=1)
    stat4 = sheet4.cell_value(rowx=rx,colx=4)
    if (stat4=="H-1B" and tmp4 =="CERTIFIED"):
        count_certified13+=1
    elif (stat4=="H-1B" and tmp4 =="DENIED"):
        count_denied13+=1
    elif (stat4 == "H-1B" and tmp4 == "WITHDRAWN"):
        count_withdrawn13+=1
    elif (stat4 == "H-1B" and tmp4 =="CERTIFIED-WITHDRAWN"):
        count_cwithdrawn13+=1
for rx in range(sheet5.nrows):
    tmp5 = sheet5.cell_value(rowx=rx,colx=1)
    stat5 = sheet5.cell_value(rowx=rx,colx=4)
    if (stat5=="H-1B" and tmp5 =="CERTIFIED"):
        count_certified12+=1
    elif (stat5=="H-1B" and tmp5 =="DENIED"):
        count_denied12+=1
    elif (stat5 == "H-1B" and tmp5 == "WITHDRAWN"):
        count_withdrawn12+=1
    elif (stat5 == "H-1B" and tmp5 =="CERTIFIED-WITHDRAWN"):
        count_cwithdrawn12+=1
file.write( str(count_certified16) + "," + str(count_certified15) + "," + str(count_certified14) + "," + str(count_certified13) + "," + str(count_certified12) + "\n")
file.write( str(count_denied16) + "," + str(count_denied15) + "," + str(count_denied14) + "," + str(count_denied13) + "," + str(count_denied12) + "\n" )
file.write( str(count_withdrawn16) + "," + str(count_withdrawn15) + "," + str(count_withdrawn14) + "," + str(count_withdrawn13) + "," + str(count_withdrawn12) + "\n")
file.write( str(count_cwithdrawn16) + "," + str(count_cwithdrawn15) + "," + str(count_cwithdrawn14) + "," + str(count_cwithdrawn13) + "," + str(count_cwithdrawn12) + "\n")
print "yay"
file.close();
