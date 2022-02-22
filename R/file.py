import readline


with open("bos-points.csv",'w') as po:
    with open("bos-val.txt",'w') as val:
        with open("boston.csv",'r') as b1:
            line = b1.readline()
            # line = line.strip()
            while(line):
                line = line.split(',')
                po.write(','.join(line[:-1]))
                po.write('\n')
                val.write(line[-1])
                # val.write('\n')
                line = b1.readline()

