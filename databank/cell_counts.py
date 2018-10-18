'''takes the raw cell count and calculates percentage out of total cells
 (3 lines of code not 5)'''

def raw_to_percentage(raw, total_cells):
    calculation = (raw/total_cells) * 100
    return round(calculation, 2)


'''Calculates the cell count values entered in the results form and checks if the sum is equal to the total cells
counted. If total is not equal to total cells then it returns Boolean False which is captured by the clean_total_cells function
in forms.py and generated a ValidationError printing the error essage specified'''

def are_sum_cell_counts_equal_total(neut, mac, eos, epi, lym, total_cells):
    total = neut + mac + eos + epi + lym
    if total != total_cells:
        return False
    else:
        return True
