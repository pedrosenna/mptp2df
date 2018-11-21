import numpy as np
import urllib2
data = open('mPTP_output.txt','r')
svarr = np.array([])
ct = 0
line_count = 1
svarr = np.append(svarr,np.array([" ", "gr", "labels"]))
for line in data:
    if line.split(' ')[0] == 'Species':
        ct+=1
    elif line.strip():
        svarr = np.append(svarr,np.array([line_count, 'mptp'+str(ct), line.split('\n')[0]]))
        line_count += 1        
svarr = svarr.reshape((svarr.size/3,3))
np.savetxt('mPTParray.txt',svarr,fmt='%.128s', delimiter='\t')
