'''takes the raw cell count and calculates percentage out of total cells
 (3 lines of code not 5)'''
def raw_to_percentage(raw, total_cells):
    calculation = (raw/total_cells) * 100
    return round(calculation, 2)
