#most common
import collections

logfile = open("http_access_log.log", "r")

clean_log=[]

for line in logfile:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

# get the Top 50 most popular URLs
for count in counter.most_common(3):
    print("The top 3 files requested are: ", str(count[1]) + "	" + str(count[0]))

logfile.close()


