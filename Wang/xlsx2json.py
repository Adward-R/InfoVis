#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import xlrd
import xlwt

def parse_sheet(sheet, filename, root):
  '''Parse the sheet and tranfer it to a json file'''

  output = file(filename, 'w')
  header = []
  data = []
  for col in range(sheet.ncols):
    header.append(sheet.cell_value(0, col))
  for row in range(1, sheet.nrows):
    line = []
    for col in range(sheet.ncols):
      cell = sheet.cell(row, col)
      pair = (header[col], cell)
      line.append(pair)
    data.append(line)

  cnt = 0
  output.write('{ "' + root + '" : [\n')
  pattern = re.compile(r'Date')
  for line in data[:-1]:
    output.write('\t{\n')
    for it in range(len(line)):
      name = line[it][0]
      value = line[it][1]
      output.write('\t\t"' + name + '" : ')
      if value is xlrd.empty_cell or value.value == '':
        output.write('"",\n')
      elif pattern.search(name) is not None:
        date = xlrd.xldate_as_tuple(value.value, sheet.book.datemode)
        output.write('"' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + '",\n')
      elif isinstance(value.value, unicode):
        output.write('"' + value.value + '",\n')
      else:
        output.write('"' + str(value.value) + '",\n')
    else:
      number = cnt
      cnt = cnt + 1
      output.write('\t\t"Number" : "' + str(number) + '"\n')
      output.write('\t},\n')
      '''
      name = line[-1][0]
      value = line[-1][1]
      output.write('\t\t"' + name + '" : ')
      if value is xlrd.empty_cell or value.value == '':
        output.write('""\n')
      elif pattern.search(name) is not None:
        date = xlrd.xldate_as_tuple(value.value, sheet.book.datemode)
        output.write('"' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + '"\n')
      elif isinstance(value.value, unicode):
        output.write('"' + value.value + '"\n')
      else:
        output.write('"' + str(value.value) + '"\n')
    output.write('\t},\n')
    '''
  else:
    output.write('\t{\n')
    for it in range(len(line)):
      name = line[it][0]
      value = line[it][1]
      output.write('\t\t"' + name + '" : ')
      if value is xlrd.empty_cell or value.value == '':
        output.write('"",\n')
      elif pattern.search(name) is not None:
        date = xlrd.xldate_as_tuple(value.value, sheet.book.datemode)
        output.write('"' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + '",\n')
      elif isinstance(value.value, unicode):
        output.write('"' + value.value + '",\n')
      else:
        output.write('"' + str(value.value) + '",\n')
    else:
      number = cnt
      cnt = cnt + 1
      output.write('\t\t"Number" : "' + str(number) + '"\n')
      output.write('\t}\n')
      '''
      name = line[-1][0]
      value = line[-1][1]
      output.write('\t\t"' + name + '" : ')
      if value is xlrd.empty_cell or value.value == '':
        output.write('""\n')
      elif pattern.search(name) is not None:
        date = xlrd.xldate_as_tuple(value.value, sheet.book.datemode)
        output.write('"' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + '"\n')
      elif isinstance(value.value, unicode):
        output.write('"' + value.value + '"\n')
      else:
        output.write('"' + str(value.value) + '"\n')
      '''

  output.write(']}\n')
  output.close()

filename = sys.argv[1]
workbook = xlrd.open_workbook(filename)
workbook.sheet_names()

# Parse the first sheet 'Employee Records'
sheet = workbook.sheet_by_index(0)
outputname = workbook.sheet_names()[0]
outputname += '.json'
parse_sheet(sheet, outputname, 'nodes')
