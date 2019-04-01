import pandas as pd
import numpy as np

def new_sheet(wb, wbname, ta, row_count):
    wb.create_sheet(title=wbname)
    active_sheet = wb[wbname]
    active_sheet['B1'] = 'Tau(ms)'
    active_sheet['A2'] = 'Number of molecules [G(0)]'
    active_sheet['A3'] = 'Ignore value'
    active_sheet['A4'] = 'Amplitude'
    '''active_sheet['A5'] = 'Number of molecules2 [G(0)]'
    active_sheet['A6'] = 'Tau(td)2'
    active_sheet['A7'] = 'Alpha2'
    active_sheet['A8'] = 'Triplet Tau(Tt)'
    active_sheet['A9'] = 'Number of triplet (T)'
    active_sheet['A10'] = 'Normalized residual'''
    active_sheet['A11'] = 0
    active_sheet['A'+str(np.size(ta)+3)] = 'Y axis offset'
    for i in range(0, np.size(ta)):
        active_sheet.cell(row=row_count+2+i, column=2).value = ta[i]


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

def export(active_sheet, fit_parameters, wbname, row_count, Nmol, ta):
    
    active_sheet.cell(row=row_count+10, column=1).value = active_sheet.cell(row=row_count+10, column=1).value + 1
    column_count = active_sheet.cell(row=row_count+10, column=1).value
    active_sheet.cell(row=row_count, column=column_count+2).value = wbname
    active_sheet.cell(row=row_count+1, column=column_count+2).value = Nmol
    for i in range(0, np.size(ta)+1):
        active_sheet.cell(row=row_count+2+i, column=column_count+2).value = fit_parameters[i]

    
    
    
