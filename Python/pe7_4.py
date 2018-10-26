outfile = open('Hardlopers.txt', 'a')
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
t = vandaag.strftime(' %H:%M:%S')
name = input('naam van loper: ')
outfile.write(s +', '+ t +', '+name + '\n')
outfile.close()

