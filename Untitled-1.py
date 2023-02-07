import xlsxwriter
import json
f = open('json_test.json')
data = json.load(f)
workbook=xlsxwriter.Workbook("test.xlsx")
row=0
col=0
ws = workbook.add_worksheet('Data')
#ws.write(0,0,'metric')
#ws.write(0,1,'total_hits')
#ws = workbook.add_worksheet('Data')
for i in data:
	#print('{} : {}'.format(i['metric'] ,i['total_hits']))
    ws.write(row,col,i['metric'])
    ws.write(row,col+1,i['total_hits'])
    row+=1
workbook.close()
f.close()

