# how on earth does this shit work??
g, m = open('input.txt').read(), 'SAMX'

for f, l, s in (sum, 4, (1,140,141,142)), (all, 3, (140,142)):
    print(sum(f(g[i-x::x][:l] in (m[:l], m[:l][::-1]) for x in s) for i in range(len(g))))