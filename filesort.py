import re

def sortfiles(filenames_list):
    nums = []
    done = []
    for el in filenames_list:
        reg = re.search('([A-Za-z]+)([0-9]+)\.([a-z]+)', el)
        if reg != None:
            nums.append(int(reg.group(2)))
    filenames = []
    for num in sorted(nums):
        for word in filenames_list:
            r = re.search('t' + str(num) + '.',word)
            if num not in done:
                if r != None:
                    filenames.append(word)
                    done.append(num)
            else:
                continue
    return filenames