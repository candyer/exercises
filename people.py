# Given a list of people with their birth and death years (all between 1900-2000), 
# find the year with the most number of people alive
# if there are several years, choose the first one 

def people1(l): 
    alive_every_year = []
    birth = sorted([m[0] for m in l])
    new_l = sorted([range(n[0], n[1]) for n in l])

    if l == []:
    	return None
    for m in range(1900,2001):
        if m < birth[0]:
            alive_every_year.append(0)
        else:
            count = 0
            for o in new_l:
                if m in o:
                    count +=1
            alive_every_year.append(count)

    for m in range(len(alive_every_year)):
        if alive_every_year[m] == max(alive_every_year):
            return m+1900



def people2(l):
    alive_every_year = []
    for year in range(1900,2001):
        count = 0
        for birth, death in l:
            if birth <= year < death:
                count +=1
        alive_every_year.append(count)

    return alive_every_year.index(max(alive_every_year)) + 1900



def people3(l):
    birth = sorted([m[0] for m in l])[::-1]
    death = sorted([m[1] for m in l])[::-1]
    alive = {}
    population = 0
    if l == []:
    	return None
    while True:
    	# Let people get born
    	next_death = death[-1]
    	while birth and birth[-1] < next_death:
    		last_birth = birth.pop()
    		population += 1
    	alive[last_birth] = population
    	# When there is no more people to get born we stop
    	if not birth:
    		break
    	# Let people die
    	next_birth = birth[-1]
    	while death[-1] <= next_birth:
    		death.pop()
    		population -= 1
    return max(alive.items(), key=lambda x: x[1])[0]
    
print people1([]) #None
print people2([]) #1900
print people3([]) #None
print people1([[1911,1958],[1923,1941],[1932,1982],[1977,1987],[1921,1945],[1918,1997],[1905,1915]]) #1932
print people2([[1911,1958],[1923,1941],[1932,1982],[1977,1987],[1921,1945],[1918,1997],[1905,1915]]) #1932
print people3([[1911,1958],[1923,1941],[1932,1982],[1977,1987],[1921,1945],[1918,1997],[1905,1915]]) #1932
print people1([[1911,1958],[1912,1959],[1913,1960]]) #1913
print people2([[1911,1958],[1912,1959],[1913,1960]]) #1913
print people3([[1911,1958],[1912,1959],[1913,1960]]) #1913
