import random
def random_macheader():
    '''
    Generate random mac vendors headers.
    '''
    lst = list()
    io_file = open('macs.txt').readlines()
    for line in range(len(io_file)):
        varmist = io_file[line].split('-')[1].replace(' ', '')
        lst.append(varmist)
    return random.choice(lst)

# Create other parts of mac address. 
create_other = lambda : "%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ranac = f'{random_macheader()}:{create_other()}'
print(ranac)