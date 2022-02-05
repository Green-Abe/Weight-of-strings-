some=input('enter first word :')
d=[]
c=[]
weight= {
    'a':int('1'),
    'b':int('2'),
    'c':int('3'),
    'd':int('4'),
    'e':int('5'),
    'f':int('6'), 
    'g':int('7'),
    'h':int('8'),
    'i':int('9'),
    'j':int('10'),
    'k':int('11'),
    'l':int('12'),
          'm':int('13'), 
          'n':int('14'),
           'o':int('15'),
            'p':int('16'),
             'q':int('17'),
              'r':int('18'),
               's':int('19'),
                't':int('20'),
                 'u':int('21'),
                  'v':int('22'),
                   'w':int('23'),
                    'x':int('24'),
                     'y':int('25'), 
                     'z':int('26'),
                   
    }
for i in some:
    if i in weight:
        by=weight[i]
        
        d.append(by)
    xl=0
    for f in d:
        xl=xl+f
        #print('fist is : ' + str(xl))
        
somee=input('enter second sentence:')
for i in somee:
    if i in weight:
        by=weight[i]
        
        c.append(by)
    xll=0
    for f in c:
        xll=xll+f
        #print('fist is : ' + str(xl))
print(xl-xll) 
#print(d)
#print(c)
