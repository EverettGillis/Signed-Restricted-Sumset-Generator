# signed restricted sumset generator
# Everett Gillis


from itertools import product
from itertools import combinations


def isprime(n): # returns 1 if n is prime or 0 if n is not
    isprime = 1
    if n<2 or (n%2 == 0 and n!=2):
        isprime = 0
        return isprime
    else:
        for i in range(2,n-1,2):
            if n%(i+1)==0:
                isprime = 0 #no
                return isprime
    return isprime

def sumset(n, m, h, A): # generates sumset

    # elements in G
    elements_in_G = []
    for i in range(0, n):
        elements_in_G.append(i)

    # sumset element calculator
    sumset = []
    def calculate_element(cf_set, subset):
        running_term_sum = 0
        for i in range(0, len(subset)):
            #print(cf_set[i], 'x', subset[i])
            term_sum = (int(cf_set[i]) * int(subset[i]))
            running_term_sum += term_sum
            running_term_sum = running_term_sum%n
        #print(running_term_sum)
        sumset.append(running_term_sum)
        running_term_sum = 0


    # coefficients
    cf_lambda = [-1,0,1]

    for layout in product(cf_lambda, repeat=m):
        #print(layout)

        # does sum of cfs = h?
        running_cf_sum = 0
        for cf in layout:
            running_cf_sum+=abs(cf)
        if running_cf_sum == h:
            #print(layout)
            calculate_element(layout, A)
        running_cf_sum = 0

    # sumset output
    sumset = [*set(sumset)]
    return(sumset)


# data
print('n\tm\th\tnu^+/-\trho^+/-\t\trho^+/->=m\tprime n\n')

for n in range(2, 100): # group orders
    
    primeorder = ''
    if isprime(n) == 0:
        primeorder = 'FALSE'
    else:
        primeorder = 'TRUE'
        
    group = []
    for i in range(0, n):
        group.append(i)
        
    for m in range(1,n+1): # m values
        
        for h in range(1,m+1): # h values (1,m+1)
            sumset_sizes = []

            for A in list(combinations(group, m)): # subsets
                #print('n=' + str(n) + ', m=' + str(m) + ', h=' + str(h) + ', A=' + str(A))
                #print(len(sumset(n, m, h, A)))
                sumset_sizes.append(len(sumset(n, m, h, A)))

            sumset_sizes.sort()


            # START CONDITIONS TO CHECK FOR WHILE DATA IS GENERATING
            
            # m vs rho (lower bounds)
            m_leq_min = ''
            if sumset_sizes[0] >= m:
                m_leq_min = 'TRUE'
            elif sumset_sizes[0] < m:
                m_leq_min = 'FALSE'

            # END CONDITIONS TO CHECK FOR WHILE DATA IS GENERATING
            
            # n, m, h, nu, rho, rho>=m
            print(str(n)+'\t'+str(m)+'\t'+str(h)+'\t'+str(sumset_sizes[-1])+'\t'+str(sumset_sizes[0])+'\t\t'+str(m_leq_min)+'\t\t'+str(primeorder))
            sumset_sizes = []































