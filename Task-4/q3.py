Matrix = [
    ['Roll_no', '  Name', '  Marks'],
    ['1', '        Abc', '    90'],
    ['2', '        Def', '    95'],
    ['3', '        Ghi', '    85']
]

for x in Matrix:    #For loop to print Every list without ' '
    print(*x, sep='')

print(*Matrix[2])   #printing second record/row that contains '2      Def      95'