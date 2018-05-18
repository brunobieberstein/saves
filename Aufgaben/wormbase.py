# -*- coding: utf-8 -*-
data = open('S:/Public/PM_21/daf-16_only_down_simplemine.txt')
my_file = open('wormbase.html', 'w')
print('<html>', file=my_file)
print('<body>', file=my_file)
for line in data:
    x = line.split('\t')[:2]
    print('<p><a href="https://wormbase.org/species/c_elegans/gene/'+x[1]+'">'+ x[0]+  '</a></p>', file = my_file)
print('</body>', file=my_file)
print('</html>', file=my_file)
data.close()
my_file.close()