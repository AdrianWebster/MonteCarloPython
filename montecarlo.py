

import random
import statistics as stats

n = 10
lst = [random.random() for x in range(n)]


def carloloop(nums):
   if nums <= 0.05:
##            print("nine")
       nine.append(1)
       result = 9
   elif 0.05 < nums <= .15:
##            print('ten')
       ten.append(1)
       result = 10
   elif .15 < nums <= .3:
##            print('eleven')
       eleven.append(1)
       result = 11
   elif .3 < nums <= .5:
##            print('twelve')
       twelve.append(1)
       result = 12
   elif .5 < nums <= .6:
##            print('thirteen')
       thirt.append(1)
       result = 13
   elif .6 < nums <= .7:
##            print('fourteen')
       fourt.append(1)
       result = 14
   elif .7 < nums <= .8:
##            print('fifteen')
       fift.append(1)
       result = 15
   elif .8 < nums <= .9:
##            print('sixteen')
       sixt.append(1)
       result = 16
   elif .9 < nums <= .95:
##            print('seventen')
       sevt.append(1)
       result = 17
   else:
##            print('eighteen')
       eigt.append(1)
       result = 18
   return result



def profit(pre,last):
     return (pre*4000)+(last*10000)


def cprofit(pre,last,total):
     salvage = total-pre-last
     return (pre*4000)+(last*10000)+(salvage*2500)



def simulate(seed):
     avgrevs =[]
     stds = []
     revs = []
     stds = []
     varz = []
     for i in range(0,26):
          
          print('\n \n')
          print('----------------------')
          print(str(i)+' slots presold')
          print('----------------------')
          presoldrevs= []
          for n in range(0,len(seed)):
               seedval = seed[n]
               last = carloloop(seedval)

               if last + i > 25:
                    last = 25-i

                    
               print(str(last) +' simulated last minute sales')
               rev =  profit(i,last)
               revs.append(rev)
               presoldrevs.append(rev)
               print('revenue '+str(rev)+'\n')
          x = sum(revs)/len(revs)

          print('----------------------')    
          print('avg rev ' + str(x))
          std = stats.stdev(revs)
          print('std ' + str(std))
          var = (1.984*std)/10
          print('var ' + str(var))
          print('----------------------')
          
          avgrevs.append(x)
          stds.append(std)
          varz.append(var)
     return [avgrevs,stds,varz]
               
          
def csimulate(seed):
     avgrevs =[]
     stds = []
     revs = []
     stds = []
     varz = []
     for i in range(0,26):
          
          print('\n \n')
          print('----------------------')
          print(str(i)+' slots presold')
          print('----------------------')
          presoldrevs= []
          for n in range(0,len(seed)):
               seedval = seed[n]
               last = carloloop(seedval)

               if last + i > 25:
                    last = 25-i

                    
               print(str(last) +' simulated last minute sales')
               rev =  cprofit(i,last,25)
               revs.append(rev)
               presoldrevs.append(rev)
               print('revenue '+str(rev)+'\n')
          x = sum(revs)/len(revs)

          print('----------------------')    
          print('avg rev ' + str(x))
          std = stats.stdev(revs)
          print('std ' + str(std))
          var = (1.984*std)/10
          print('var ' + str(var))
          print('----------------------')
          
          avgrevs.append(x)
          stds.append(std)
          varz.append(var)
     return [avgrevs,stds,varz]
               

def test():

    print(len(nine)/n)
    print(len(ten)/n)
    print(len(eleven)/n)
    print(len(twelve)/n)
    print(len(thirt)/n)
    print(len(fift)/n)
    print(len(sixt)/n)
    print(len(sevt)/n)
    print(len(eigt)/n)
    print(len(eigt)+len(sevt)+len(sixt)+len(fift)+len(fourt)+len(thirt)+len(twelve)+len(eleven)+len(ten)+len(nine))



            
nine = []
ten = []
eleven = []
twelve = []
thirt = []
fourt = []
fift = []
sixt = []
sevt = []
eigt = []

sim = [nine,ten,eleven,twelve,thirt,fourt,fift,sixt,sevt,eigt]
sim1 = simulate(lst)
sim2 = csimulate(lst)

