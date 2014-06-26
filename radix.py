class Radix(object):
    '''
    for now this class only caclulate for bases between 2 to 10
    in the future, it will go to 16.
    '''
    def __init__(self):
        pass
    
    def string_to_number(self, string, base):
        
        self.string = string
        self.base = base
        #print 'converting string "%s" to number of base = %d' % (string, base)

        s = []
        self.number = 0
        n = len(self.string)
        self.coeffs = []
        self.exps = []
        
        for digit in self.string:
            n-=1
            self.exps.append(n)
            self.coeffs.append(int(digit))
            self.number += int(digit)*self.base**n
        
        return self.number

    def number_to_string(self, number, base):
        self.number = number
        self.base = base        
        #print 'converting number %d to string of base = %d' % (number, base)
        
        n = 0
        self.coeffs = []
        self.exps = []
        r = self.number
        
        while self.base**n <= self.number:
            self.exps.append(n)
            n+=1
        
        self.exps.reverse()
        
        for n in self.exps:
            # use python integer division trick to get
            # argest coeff as an int, no remainder
            c = r/self.base**n 
            r -= c*self.base**n
            self.coeffs.append(str(c))
        
        self.string = ('').join(self.coeffs)
        
        return self.string
    
    def equation(self):
        eq = []
        for i in range(0,len(self.exps)):
            eq.append('%d(%d^%d)' % (int(self.coeffs[i]), self.base, self.exps[i]))
        return (' + ').join(eq) + ' = %d' % self.number
    

def sample():
    base = 7
    number = 666
    
    print "\nSample using base %d and number %d\n" % (base,number)
    
    test1 = Radix()
    string = test1.number_to_string(number, base)
    print "string: %s" % string
    print "equation: %s" %  test1.equation()
    
    test2 = Radix()
    number = test2.string_to_number(string, base)
    print "number: %d" % number
    print "equation: %s" %  test2.equation()
    raw_input("\nSample complete.\nReady to test? (hit enter to continue...)")
  

def test():

    bases = []          # numeric bases that produce integers (which are strings) as results
    times = []          # 0 to 59 seconds, or minutes
    
    iterations = 0
    errors = 0
    
    for i in range(2,11):
        bases.append(i)
    
    for i in range(0,60):
        times.append(i)

    print '\n'   
    print 'bases to test:\n', bases
    print 'times to test:\n', times    
    
    for time in times:
        
        for base in bases:
            
            test1 = Radix()
            string = test1.number_to_string(time, base)
            
            test2 = Radix()
            number = test2.string_to_number(string, base)
            
            iterations+=1 
            
            if number != time or test1.equation() != test2.equation():
                errors+=1
                print 'time= %d; base= %d; string= %s, test1.eq = %s; test2.eq = %s' % (time, base, string, test1.equation(), test2.equation())
          
    print '%d errors out of %d iterations.' % (errors, iterations)
    print 'test complete'
    
    
if __name__ == '__main__':
    sample()
    test()