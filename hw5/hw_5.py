'''
This code fetches 365 imf files(1 file contains to 1 day  of data) and 1 DST file from
http://www-personal.umich.edu/%7Edwelling/imf_2003/.
The files are then downloaded and written into a text file of the desired formatting.

Author: Tre'Shunda James
'''

# import the needed modules
import urllib.request
import re

# define the general web address
url = r'http://www-personal.umich.edu/%7Edwelling/imf_2003/'
# specify the files to be downloaded
with urllib.request.urlopen(url) as response:
    raw_filelist = re.findall('imf2003\d+\.dat', str(response.read())) # now list of file for each day (repeated
                                                                        # 3 times)
filelist= raw_filelist[::3] # now list of files for each day (no repeates)


# now to download the files
download_files=[] # empty array to store the complete urls of the files we want to download
# for-loop to iterate through each file in the filelist
for file in filelist:
    data_url= url + file # add the strings together to get the full download url
    download_files.append(data_url) # add the complete urls to the array download_files
#print(download_files) # for debugging

# download DST file and write into its own file
with open('dstfile.dat', 'wb') as data:
    response = urllib.request.urlopen(url+'Dst_2003_Format1.txt')  # Open website...
    data.write(response.read()) # downloads all the data in the file and writes it into a file called dstfile.dat

# download each imf file and write it to one data file
with open('imffile.dat', 'wb') as data:
    for i in download_files:
        response = urllib.request.urlopen(i)  # Open website...
        data.write(response.read())# "read" reads whole file, "write" saves it to file called imffile.dat.

# now for formatting purposes, we write a new file.
with open('imffile.dat') as f, open('imf.dat', 'w') as k:
    k.write('#START\n') # again, for formatting purposes
    # for-loop to iterate through eachline in imffile.dat
    for line in f.readlines():
        # check each line for the conditions below. If these conditions are not met, write the line to the new file.
        if not line.startswith('F') and not line.startswith('#') and line.strip():
            k.write(line)




