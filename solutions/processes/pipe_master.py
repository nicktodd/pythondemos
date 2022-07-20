import subprocess

#echo = subprocess.Popen(['echo','one','two','three'],\
#                        shell=True, stdout = subprocess.PIPE)
echo = subprocess.Popen(['echo','jo bo mo'],shell=True,stdout=subprocess.PIPE)
catupper = subprocess.Popen(['python','make_upper.py','pipe'],shell=True, \
                            stdout=subprocess.PIPE,stdin=echo.stdout)
dosort=subprocess.Popen(['python','do_sort.py'],stdin=catupper.stdout , stdout=subprocess.PIPE)
for line in dosort.stdout.readlines():
    print (line.decode('utf-8').rstrip())
