
class multiplication(object):
    '''use to multiplication
        as:  a = multiplication(b,c) means a = b * c 
        b,c must be string'''
    def __init__(self, num1='', num2=''):
        if num1.isdigit() and num2.isdigit():
            pass
        else:
            print 'input must be 0-9'
            raise  IOError
        num_1,zero_num_1 = self.zero_count(num1)
        num_2,zero_num_2 = self.zero_count(num2)
        if len(num_1) > len(num_2):
            self.num1 = num_1
            self.num2 = num_2
        else:
            self.num1 = num_2
            self.num2 = num_1
        self.zero_num_1 = zero_num_1
        self.zero_num_2 = zero_num_2
            
    def zero_count(self,num):
        '''zero_count(num)
            return num0(without zero), num1(zero number)
            like:
                a,b=zero_count('123000')
                a--->'123'
                b--->3
        '''
        if num[-1] == '0':
            for i in range(len(num)):
                if num[0-i-1] == '0':
                    pass
                else:
                    zero_count_1 = i
                    num_1 = num[0:0-i]
                    break
            return num_1, zero_count_1
        else:
            return num, 0
    
    def multiplication(self):
        '''multiplication()
           return string
           like :   123
                   x 99
                   ----
                   1107
                  1107
                  -----
                  12177
        '''
        if self.num1 and self.num2:
            num_1_len = len(self.num1)
            num_2_len = len(self.num2)
            num2_tr = self.num2[::-1]
            num1_tr = self.num1[::-1]
            num = []
            for i in range(num_2_len):
                a = 0
                b = ''
                for j in range(num_1_len):
                    c = int(num1_tr[j])
                    d = int(num2_tr[i])
                    e =  d * c +  a
                    f = str(e)
                    if len(f) > 1:
                        b = b + f[-1]
                        a = int(f[0])
                    else:
                        b = b + f[-1]
                b = '0' * i + b + str(a)
                num.append(b)
            number_1 = self.mul_add(num)
            number_1 = number_1 + '0' * self.zero_num_1 + '0' * self.zero_num_2
            return number_1
        else:
            return '0'
    
    def mul_add(self, num):
        '''just use for add the result
             return string
        '''
        a = 0
        b = ''
        for i in range(len(num[-1])):
            for j in range(len(num)):
                try:
                    c = int(num[j][i])
                except:
                    c = 0
                a = a + c
            b = b + str(a % 10) 
            a = a / 10
        if a == 0:
            pass
        else:
            e = str(a)
            e = e[::-1]
            b = b + e
        d = b[::-1]
        for i in range(len(d)):
            if d[0] == '0':
                d = d[1:]
            else:
                break
        return d
