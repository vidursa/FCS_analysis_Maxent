import pandas as pd
import numpy as np

def new_sheet(wb, wbname, row_count):
    wb.create_sheet(title=wbname)
    active_sheet = wb[wbname]
    active_sheet['A2']  = 'Number of molecules [G(0)]'
    active_sheet['A3'] = 'Tau(td)1'
    active_sheet['A4'] = 'Alpha1'
    active_sheet['A5']  = 'Fraction of molecules in tau1'
    active_sheet['A6'] = 'Tau(td)2'
    active_sheet['A7'] = 'Alpha2'
    active_sheet['A8'] = 'Triplet Tau(Tt)'
    active_sheet['A9'] = 'Number of triplet (T)'
    active_sheet['A10'] = 'Normalized residual'
    active_sheet['A11'] = 'Offset'
    active_sheet['A12'] = 0
    


def analyzed(active_sheet, wbname, fileiter, Analyzed_counter, row_count):
    for column in active_sheet.iter_cols(min_row=row_count,
                                         max_row=row_count,
                                         min_col=active_sheet.min_column,
                                         max_col=active_sheet.max_column):
        for cell in column:
            if cell.value == wbname:
                Analyzed_counter = 1
                print('file already analyzed ')
                fileiter += 1
                break
        else:
            continue
        break
    return Analyzed_counter, fileiter

def export(active_sheet, params, wbname, row_count,G,modelGt):
    Nmol = float(params['N'])
    Td = float(params['td'])
    NA = float(params['Alpha1'])
    Nmol2 = float(params['N2'])
    Td2 = float(params['td2'])
    NA2 = float(params['Alpha2'])
    Tt = float(params['tT'])
    T = float(params['T'])
    Offset = float(params['Offset'])
    active_sheet.cell(row=row_count+11, column=1).value = active_sheet.cell(row=row_count+11, column=1).value + 1
    column_count = active_sheet.cell(row=row_count+11, column=1).value
    active_sheet.cell(row=row_count, column=column_count+1).value = wbname
    active_sheet.cell(row = row_count+1, column = column_count+1).value = Nmol
    active_sheet.cell(row = row_count+2, column = column_count+1).value = Td
    active_sheet.cell(row = row_count+3, column = column_count+1).value = NA
    active_sheet.cell(row = row_count+4, column = column_count+1).value = Nmol2
    active_sheet.cell(row = row_count+5, column = column_count+1).value = Td2
    active_sheet.cell(row = row_count+6, column = column_count+1).value = NA2
    active_sheet.cell(row = row_count+7, column = column_count+1).value = Tt
    active_sheet.cell(row = row_count+8, column = column_count+1).value = T
    active_sheet.cell(row = row_count+9, column = column_count+1).value = np.mean(G-modelGt)/np.max(G)
    active_sheet.cell(row = row_count+10, column = column_count+1).value = Offset




    
