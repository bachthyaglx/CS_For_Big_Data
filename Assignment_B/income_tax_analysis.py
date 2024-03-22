'''
Code for Assignment B: Explore Python
 - Challenge 4: Income Analysis
 - Challenge 5: Code Income Analysis

Based on 2020 tax returns, income distribution in Madera County, CA
with (postal) ZIP code 93636 was:
#
income brackets:        number of tax returns
                        filed in brackets:
[$1 to under $25,000]             1,800
[$25,000 to under $50,000]        1,380
[$50,000 to under $75,000]          980
[$75,000 to under $100,000]         830
[$100,000 to under $200,000]      1,660
[$200,000 or more, up to $10M>]     550
'''

# design a data structure that stores information about a ZIP area
# that is relevant for mean/median tax analysis
zip_93636 = {
    'name': 'Madera County, CA',
    (1, 25000): 1800, 
    (25000, 50000): 1380, 
    (50000,75000): 980, 
    (75000,100000): 830, 
    (100000,200000): 1660, 
    (200000,10000000): 550
}

zip_94040 = {
    'name': 'Mountain View, CA',
    (1, 25000): 2830, 
    (25000, 50000): 2150, 
    (50000,75000): 1680, 
    (75000,100000): 1290, 
    (100000,200000): 3340, 
    (200000,10000000): 5600
}

zip_94304 = {
    'name': 'Palo Alto, CA',
    (1, 25000): 140, 
    (25000, 50000): 160, 
    (50000,75000): 220, 
    (75000,100000): 180, 
    (100000,200000): 410, 
    (200000,10000000): 730
}

zip_94027 = {
    'name': 'Atherton, CA',
    (1, 25000): 540, 
    (25000, 50000): 240, 
    (50000,75000): 190, 
    (75000,100000): 150, 
    (100000,200000): 420, 
    (200000,10000000): 1590
}

zip_50860 = {
    'name': 'Redding, IA',
    (1, 25000): 50, 
    (25000, 50000): 40, 
    (50000,75000): 30, 
    (75000,100000): 0, 
    (100000,200000): 0, 
    (200000,10000000): 0
}

zip_10023 = {
    'name': 'New York City, NY U West',
    (1, 25000): 5490, 
    (25000, 50000): 3840, 
    (50000,75000): 3520, 
    (75000,100000): 3130, 
    (100000,200000): 7120, 
    (200000,10000000):9540
}

# implement a function that calculates the mean income for a ZIP area
def mean_income(_zip) -> int:
    sum_income = 0
    sum_fre=0

    for key in _zip: 
        if(key!='name'):
            #Calculate total income of each group
            sum_income = sum_income + ((key[0] + key[1])/2)*_zip[key]
            #Calculate total frequency from all group
            sum_fre = sum_fre + _zip[key]

    #Calculate average (mean)
    mean = sum_income/sum_fre
    
    return round(mean)


# implement a function that calculates the median income for a ZIP area
def median_income(_zip) -> int:
    n=0
    #Calculate number of observations
    for key in _zip:
        if(key!='name'):
            n = n + _zip[key]
    l = 0
    c_f = 0
    c = 0
    f = 0
    h = 0
    temp = 0
    
    for key in _zip:
        if(key!='name'):
            #Calculate cummulative frequency
            c_f = c_f + _zip[key]
            
            if(n/2 < c_f):
                temp = temp + 1
                if(temp == 1):
                    #Calculate preceeding cummulative frequency
                    c = c_f - _zip[key]
                    #Calculate frequency
                    f = _zip[key]
                    #Calculate lower limit
                    l = key[0]
                    #Difference between upper and lower limit
                    h = key[1] - key[0]
                    
    #Calculate median 
    median = l + ((n/2 - c)/f)*h
    
    return round(median)


# use this function to print results for a ZIP area
def print_analysis(_zip):
    _country = _zip["name"]
    print(
        f'mean_income in {_country:26} is: {mean_income(_zip):10,} - ' +
        f'median_income is: {median_income(_zip):8,}'
    )


# attempt to load solution module (ignore)
try:
    solution_module = 'income_tax_analysis_sol'
    mod = __import__(solution_module, globals(), locals(), [], 0)
    mean_income, median_income, print_analysis = mod.mean_income, mod.median_income, mod.print_analysis
    zip_93636, zip_94040, zip_94304, zip_94027, zip_50860, zip_10023 = \
        mod.zip_93636, mod.zip_94040, mod.zip_94304, mod.zip_94027, mod.zip_50860, mod.zip_10023
#
except ImportError:
    pass


if __name__ == '__main__':
    '''
    driver code that runs when file is directly executed
    '''
    print_analysis(zip_93636)
    print_analysis(zip_94040)
    print_analysis(zip_94304)
    print_analysis(zip_94027)
    print_analysis(zip_50860)
    print_analysis(zip_10023)
