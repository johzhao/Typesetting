#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)

class Typesetting(object):

	def __init__(self):
		self.logger = logging.getLogger('Typesetting')
		self.leadingIndent = True
		self.emptyLineBetweenLines = True
		self.useFullWidth = True

	def ConvertFile(self, srcFile, desFile, lowMemoryMode=False):
		try:
			with open(srcFile, 'r') as srcF:
				if lowMemoryMode:
					# Open the destination file. Read one line from source file and save one line to destionation file.
					# Not support for now.
					pass
				else:
					# Read all lines from source file. Save to destination file after convert all data.
					srcData = srcF.readlines()
					desData = self.ConvertData(srcData)
					with open(desFile, 'w') as desF:
						desF.writelines(desData)
		except IOError as e:
			self.logger.critical('IO Error: %s' % e)

	def ConvertData(self, srcData):
		resultData = None
		for line in srcData:
			line = self.ConvertOneLine(line)
			if line != None:
				if resultData != None:
					resultData = resultData + self.HandleNewLine(line)
				else:
					resultData = line + '\n'
		return resultData

	def ConvertOneLine(self, srcLine):
		# Handle single line string.
		srcLine = self.HandleStringStrip(srcLine)
		if srcLine == '':
			return None

		srcLine = self.HandleLeadingIndent(srcLine)

		if self.useFullWidth:
			srcLine = self.UseFullWidthChar(srcLine)
		return srcLine

	def HandleLeadingIndent(self, srcData):
		# Add leading indent if the option was True
		if srcData != None:
			if self.leadingIndent:
				return '　　' + srcData
			else:
				return srcData
		else:
			return None

	def HandleStringStrip(self, srcData):
		# Strip the string
		if srcData != None:
			srcData = srcData.replace('　', '')
			srcData = srcData.strip()
		return srcData

	def HandleNewLine(self, srcData):
		# Insert \n at the begin of string if the new line option was True
		# Append \n at the tail of string
		if srcData != None:
			if self.emptyLineBetweenLines:
				srcData = '\n' + srcData + '\n'
			else:
				srcData = srcData + '\n'
		return srcData

	def UseFullWidthChar(self, srcData):
		# Replace the character with the full width version
		if srcData != None:
			srcData = srcData.replace(',', '，')
			srcData = srcData.replace('.', '。')
			srcData = srcData.replace(':', '：')
			srcData = srcData.replace('?', '？')
		return srcData


def main():
	#t = Typesetting()
	#t.ConvertFile('example3.txt', 'result.txt')
	with open('example_ansi.txt', 'r') as f:
		data = f.readlines()
		for line in data:
			line = line.decode('gbk')
			#line = line.encode('utf-8')
			logging.debug(line)

if __name__ == '__main__':
	main()
