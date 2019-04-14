#!/usr/bin/python
#-*-coding UTF-8 -*-
import os
import sys
import struct

def crateHDCPKeyArray(inputfilename,output_filename):
	print "source file is :"+inputfilename
	print "target file is :"+output_filename
	HDCPkeydata=[]
	if(os.path.exists(inputfilename)):
		print "file exits, we will change the file"
		file_object=open(inputfilename,'rb')
		#index=0
		try:
			while True:
				byte=file_object.read(1)
				if byte == '':
					break
				else:
					hexstr="%s" % byte.encode('hex')
					intdecvalue=int(hexstr,16)
					hexvalue=hex(intdecvalue)
					HDCPkeydata.append(hexvalue)
					#sys.stdout.write('index:')
					#print index
					#print hexvalue
					#index=index+1
		finally:
			file_object.close()
	else:
		print "file is not exits!!!"
		exit(1)
	target_file_object=open(output_filename,'w')
	try:
		target_file_object.truncate()
                target_file_object.write("#define CC_HDCP_KEY_CONTENT_SIZE "+len(HDCPkeydata)+"\n");
		target_file_object.write("mDefHDCPKeyContentBuf[CC_HDCP_KEY_CONTENT_SIZE] = {")
		for x in xrange(len(HDCPkeydata)):
			if (x%10 == 0):
				target_file_object.writelines("\n")
			if(len(HDCPkeydata[x]) < 4):
				target_file_object.write(" ")
			target_file_object.write(str(HDCPkeydata[x])+", ");
		target_file_object.writelines("\n")
		target_file_object.write("};")
	finally:
		target_file_object.close()

if __name__ == '__main__':
	print "__main__"

	if len(sys.argv) !=3:
		print "Usage: python input_name output_name"
		exit(1)
	input_filename=sys.argv[1]
	output_filename=sys.argv[2]
	crateHDCPKeyArray(input_filename,output_filename)
