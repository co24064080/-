# coding: utf-8
#input polynomial
polynomial = input("Input a polynomials(it is OK whether you enter '*', but it is not support without '^'): ")
#cut from right_brackets
right_brackets = polynomial.split(")")
right_brackets[0][1:]

#remove brackets
no_brackets = []
for i in (right_brackets[:-1]) :
    no_brackets.append(i[1:])
#split by + and -
Allbrackets_cut_by_sign = []

for j in range(len(no_brackets)):
    inAbracket = no_brackets[j]
    a = 0
    negative = False
    cut_by_sign = []
    for i in inAbracket:
        if i == '+':
            cut_by_sign.append(inAbracket[a:(inAbracket.find('+',a))])
            a = a + len(inAbracket[a:inAbracket.find('+',a)]) + 1
            if negative == True:
                cut_by_sign[-1] = "-" + cut_by_sign[-1]
                negative = False
        if i == "-":
            cut_by_sign.append(inAbracket[a:(inAbracket.find('-',a))])
            a = a + len(inAbracket[a:inAbracket.find('-',a)]) + 1
            if negative == True:
                cut_by_sign[-1] = "-" + cut_by_sign[-1] 
                negative = False
            
            negative = True
    cut_by_sign.append(inAbracket[a:])
    if negative == True:
        cut_by_sign[-1] = "-" + cut_by_sign[-1] 
        negative = False
    
    Allbrackets_cut_by_sign.append(cut_by_sign)
#split coefficient and variables
Allbrackets_cut_by_sign_ = Allbrackets_cut_by_sign

Allbrackets_coefficient = []
Allbrackets_variables = []


for aBracket in Allbrackets_cut_by_sign:
    
    coefficient = []
    variables = []
    have_variable = False
    
    for one_in_aBracket in aBracket:
        no_multi = one_in_aBracket.replace('*','')
        
        for t in no_multi:
            try:
                int(t)
                continue
            except:
                if t == '-':
                    continue
                else:
                    variable_start = no_multi.find(t)
                    have_variable = True
                    break
        
        if have_variable == False:
            coefficient.append(int(no_multi))
            variables.append('')
        else:
            try:
                coefficient.append(int(no_multi[0:variable_start]))
                variables.append(no_multi[variable_start:])
            except:
                if no_multi[no_multi.find(t)-1] == '-':
                    coefficient.append(-1)
                    variables.append(no_multi[(variable_start):])
                else:
                    coefficient.append(1)
                    variables.append(no_multi[variable_start:])                    

    Allbrackets_coefficient.append(coefficient)
    Allbrackets_variables.append(variables)
#compute coefficient part
compute = True
while compute == True :
    first_bracket_coefficient = []
    for c in Allbrackets_coefficient[0] :
        for d in Allbrackets_coefficient[1] :
            first_bracket_coefficient.append(c * d)
            
    if len(Allbrackets_coefficient) > 2 :
        new_coefficient = []
        new_coefficient.append(first_bracket_coefficient)
        new_coefficient.extend(Allbrackets_coefficient[2:])
        Allbrackets_coefficient = new_coefficient
    else :
        res_coefficient = first_bracket_coefficient
        compute = False
#compute variable part
compute = True
while compute == True :
    first_bracket_variables= []
    for c in Allbrackets_variables[0] :
        for d in Allbrackets_variables[1] :
            #first bracket
            pure_variables = []
            variable_exponent = []

            for c_ in range(len(c)):
                try:
                    int(c[c_])
                except:
                    if c[c_] == '^':
                        count = True
                        exponent_place = 2
                        while count == True:
                            try:
                                int(c[(c_ + 1):(c_ + exponent_place)])
                                exponent_place += 1                    
                            except:
                                variable_exponent[pure_variables.index(c[c_-1])] += (int(c[(c_ + 1):(c_ + exponent_place - 1)]) - 1)
                                count = False
                            else:
                                if exponent_place > len(c):
                                    variable_exponent[pure_variables.index(c[c_-1])] += (int(c[(c_ + 1):(c_ + exponent_place - 1)]) - 1)
                                    count = False
                    
                    elif c[c_] not in pure_variables :
                        pure_variables.append(c[c_])
                        variable_exponent.append(1)
                    elif c[(c_ + 1)] != '^':
                        variable_exponent[pure_variables.index(c[c_-1])] += (int(c[(c_ + 1):(c_ + exponent_place - 1)]) - 1)

            pure_variables_c = pure_variables
            variable_exponent_c = variable_exponent

            #second bracket
            pure_variables = []
            variable_exponent = []

            for d_ in range(len(d)):
                try:
                    int(d[d_])
                except:
                    if d[d_] == '^':
                        count = True
                        exponent_place = 2
                        while count == True:
                            try:
                                int(d[(d_ + 1):(d_ + exponent_place)])
                                exponent_place += 1                    
                            except:
                                variable_exponent[pure_variables.index(d[d_-1])] += (int(d[(d_ + 1):(d_ + exponent_place - 1)]) - 1)
                                count = False
                            else:
                                if exponent_place > len(d):
                                    variable_exponent[pure_variables.index(d[d_-1])] += (int(d[(d_ + 1):(d_ + exponent_place - 1)]) - 1)
                                    count = False
                    
                    elif d[d_] not in pure_variables :
                        pure_variables.append(d[d_])
                        variable_exponent.append(1)
                    elif d[(d_ + 1)] != '^':
                        variable_exponent[pure_variables.index(d[d_-1])] += (int(d[(d_ + 1):(d_ + exponent_place - 1)]) - 1)

            pure_variables_d = pure_variables
            variable_exponent_d = variable_exponent

            #compute
            temp = pure_variables_c + pure_variables_d
            temp_exponent = variable_exponent_c + variable_exponent_d    
            temp_no_same = []
            temp_no_same_exponent = []    

            for t in range(len(temp)):
                if temp[t] in temp_no_same:
                    temp_no_same_exponent[temp_no_same.index(temp[t])] += temp_exponent[t]

                else:
                    temp_no_same.append(temp[t])
                    temp_no_same_exponent.append(temp_exponent[t])
                            
            #sort
            sort_temp = sorted(temp_no_same)
            sort_temp_exponent = []
            for s in sort_temp:
                sort_temp_exponent.append(temp_no_same_exponent[temp_no_same.index(s)])
    
            #combine
            combine = []
            for e in range(len(sort_temp)):
                if sort_temp_exponent[e] == 1 :
                    combine.append(sort_temp[e])
                else:
                    combine.append(str(sort_temp[e]) + '^' + str(sort_temp_exponent[e]))
        
            new_variable = ''.join(combine)       
            first_bracket_variables.append(new_variable)
            
    if len(Allbrackets_variables) > 2 :
        new_variables = []
        new_variables.append(first_bracket_variables)
        new_variables.extend(Allbrackets_variables[2:])
        Allbrackets_variables = new_variables
    else :
        res_variables = first_bracket_variables
        compute = False
#compute
final_variables = []
final_coefficient = []    

for f in range(len(res_variables)):
    if res_variables[f] in final_variables:
        final_coefficient[final_variables.index(res_variables[f])] += res_coefficient[f]

    else:
        final_variables.append(res_variables[f])
        final_coefficient.append(res_coefficient[f])
        
#combine
final_combine = []
for v in range(len(final_variables)):
    if final_coefficient[v] < 0 :
        plus_minus = '-'
    else:
        plus_minus = '+'
    
    if v == 0 :
        if abs(final_coefficient[v]) == 1 :        
            final_combine.append(final_variables[v])
        else:
            final_combine.append(str(abs(final_coefficient[v])) + '*' + str(final_variables[v]))
    else:
        if abs(final_coefficient[v]) == 1 :        
            final_combine.append(plus_minus + final_variables[v])
        else:
            final_combine.append(plus_minus + str(abs(final_coefficient[v])) + '*' + str(final_variables[v]))

output = ''.join(final_combine) 
print('Output Result: ' + output)
