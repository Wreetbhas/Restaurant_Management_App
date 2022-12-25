def extract_history():
    fp=open('transaction.txt','r')
    lines=fp.readlines()
    fp.close()

    trans = {}
    t_code = 1

    for line in lines:
        data = line.split(",")
        date,time,amt,status = data[0],data[1],data[2],data[3]
        trans[t_code] = {'date':date,'time':time,'amt':amt,'status':status}
        t_code += 1

    return trans

def update_transaction(date_time,amt):
    fp=open('transaction.txt','a')
    fp.write("{},{},{},{}".format(date_time.date(),date_time.time(),amt,'Success\n'))
    fp.close()