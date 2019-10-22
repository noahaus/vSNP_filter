import xlsxwriter
import csv

def excelwriter(filename):
    orginal_name = filename
    filename = filename.replace(".csv", ".xlsx")
    wb = xlsxwriter.Workbook(filename)
    ws = wb.add_worksheet("Sheet1")
    with open(orginal_name, 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in table:
            ws.write_row(i, 0, row)
            i += 1

    col = len(row)
    col = col + 1
    #print(i, "x", col)

    formatA = wb.add_format({'bg_color': '#58FA82'})
    formatG = wb.add_format({'bg_color': '#F7FE2E'})
    formatC = wb.add_format({'bg_color': '#0000FF'})
    formatT = wb.add_format({'bg_color': '#FF0000'})
    formatnormal = wb.add_format({'bg_color': '#FDFEFE'})
    formatlowqual = wb.add_format({'font_color': '#C70039', 'bg_color': '#E2CFDD'})
    formathighqual = wb.add_format({'font_color': '#000000', 'bg_color': '#FDFEFE'})
    formatambigous = wb.add_format({'font_color': '#C70039', 'bg_color': '#E2CFDD'})
    formatN = wb.add_format({'bg_color': '#E2CFDD'})

    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 60, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 59, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 58, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 57, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 56, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 55, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 54, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 53, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 52, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 51, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 50, 'format': formathighqual})
    ws.conditional_format(i - 2, 1, i - 2, col - 2, {'type': 'text', 'criteria': 'not containing', 'value': 100, 'format': formatlowqual})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'cell', 'criteria': '==', 'value': 'B$2', 'format': formatnormal})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'A', 'format': formatA})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'G', 'format': formatG})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'C', 'format': formatC})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'T', 'format': formatT})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'S', 'format': formatambigous})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'Y', 'format': formatambigous})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'R', 'format': formatambigous})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'W', 'format': formatambigous})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'K', 'format': formatambigous})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'M', 'format': formatambigous})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': 'N', 'format': formatN})
    ws.conditional_format(2, 1, i - 3, col - 2, {'type': 'text', 'criteria': 'containing', 'value': '-', 'format': formatN})

    ws.set_column(0, 0, 30)
    ws.set_column(1, col - 2, 2)
    ws.freeze_panes(2, 1)
    format_rotation = wb.add_format({'rotation': '90'})
    ws.set_row(0, 140, format_rotation)
    formatannotation = wb.add_format({'font_color': '#0A028C', 'rotation': '-90', 'align': 'top'})
    #set last row
    ws.set_row(i - 1, 400, formatannotation)

    wb.close()

excelwriter("excel_writer_examp.csv")
