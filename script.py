import re
import datetime
import collections

total_requests = 0
year_count = 0

file_name= 'path/to/file'
oct_count = 0
nov_count = 0
dec_count = 0
jan_count = 0
feb_count = 0
mar_count = 0
apr_count = 0
may_count = 0
jun_count = 0
jul_count = 0
aug_count = 0
sep_count = 0
oct95_count = 0
jan_match = 0
feb_match = 0
mar_match = 0
apr_match = 0
may_match = 0
jun_match = 0
jul_match = 0
aug_match = 0
sep_match = 0
oct_match = 0
oct95_match = 0
nov_match = 0
dec_match = 0

f= open("http_access_log.log", "r")
for line in f:
    if 'Oct/1994' in line:
        oct_count += 1

    elif 'Nov/1994' in line:
        nov_count += 1

    elif 'Dec/1994' in line:
        dec_count += 1

    elif 'Jan/1995' in line:
        jan_count += 1

    elif 'Feb/1995' in line:
        feb_count += 1

    elif 'Mar/1995' in line:
        mar_count += 1

    elif 'Apr/1995' in line:
        apr_count += 1

    elif 'May/1995' in line:
        may_count += 1

    elif 'Jun/1995' in line:
        jun_count += 1

    elif 'Jul/1995' in line:
        jul_count += 1

    elif 'Aug/1995' in line:
        aug_count += 1

    elif 'Sep/1995' in line:
        sep_count += 1

    else:
        oct95_count += 1

print(f'October 1994 requests:', oct_count)
print(f'November 1994 requests:', nov_count)
print(f'December 1994 requests:', dec_count)
print(f'January 1995 requests:', jan_count)
print(f'February 1995 requests:', feb_count)
print(f'March 1995 requests:', mar_count)
print(f'April 1995 requests:', apr_count)
print(f'May 1995 requests:', may_count)
print(f'June 1995 requests:', jun_count)
print(f'July 1995 requests:', jul_count)
print(f'August 1995 requests:', aug_count)
print(f'September 1995 requests:', sep_count)
print(f'October 1995 requests:', oct95_count)
print()
print()

pages = {}

f= open("http_access_log.log", "r")
mon = 0
tue = 0
wed = 0
thur = 0
fri = 0
sat = 0
sun = 0

f= open("http_access_log.log", "r")
for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 4:
    continue
  date = pieces[1].split(':')
  date = date[0]
  days = datetime.datetime.strptime(date, '%d/%b/%Y')

  weekday = datetime.datetime.weekday(days)


  if weekday == 0:
    mon += 1
  
  elif weekday == 1:
    tue += 1
  
  elif weekday == 2:
    wed += 1
  
  elif weekday == 3:
    thur += 1

  elif weekday == 4:
    fri += 1

  elif weekday == 5:
    sat += 1

  elif weekday == 6:
    sun += 1

  
  if 'Jan' in line:
      jan_match += 1
  if 'Feb' in line:
      feb_match += 1
  if 'Mar' in line:
      mar_match += 1
  if 'Apr' in line:
      apr_match += 1
  if 'May' in line:
      may_match += 1
  if 'Jun' in line:
      jun_match += 1
  if 'Jul' in line:
      jul_match += 1
  if 'Aug' in line:
      aug_match += 1
  if 'Sep' in line:
      sep_match += 1
  if 'Oct/1994' in line:
      oct_match += 1
  if 'Oct/1995' in line:
      oct95_match += 1
  if 'Nov' in line:
      nov_match += 1
  if 'Dec' in line:
      dec_match += 1

  filename = pieces[2]

  if filename in pages:
    pages[filename] += 1
  else:
    pages[filename] = 1

average_mon = mon / 52
average_tue = tue / 52
average_wed = wed / 52
average_thur = thur / 52
average_fri = fri / 52
average_sat = sat / 52
average_sun = sun / 52

formatted_mon = "{:.2f}".format(average_mon)
formatted_tue = "{:.2f}".format(average_tue)
formatted_wed= "{:.2f}".format(average_wed)
formatted_thur = "{:.2f}".format(average_thur)
formatted_fri = "{:.2f}".format(average_fri)
formatted_sat = "{:.2f}".format(average_sat)
formatted_sun = "{:.2f}".format(average_sun)

print(f'The average number of requests on Monday was {formatted_mon}')
print(f'The average number of requests on Tuesday was {formatted_tue}')
print(f'The average number of requests on Wednesday was {formatted_wed}')
print(f'The average number of requests on Thursday was {formatted_thur}')
print(f'The average number of requests on Friday was {formatted_fri}')
print(f'The average number of requests on Saturday was {formatted_sat}')
print(f'The average number of requests on Sunday was {formatted_sun}')
print()
print()

print(f'The number of requests made in January 1995 was:', jan_match)
print(f'The number of requests made in February 1995 was: {feb_match}')
print(f'The number of requests made in March 1995 was: {mar_match}')
print(f'The number of requests made in April 1995 was: {apr_match}')
print(f'The number of requests made in May 1995 was: {may_match}')
print(f'The number of requests made in June 1995 was: {jun_match}')
print(f'The number of requests made in July 1995 was: {jul_match}')
print(f'The number of requests made in August 1995 was: {aug_match}')
print(f'The number of requests made in September 1995 was: {sep_match}')
print(f'The number of requests made in October 1994 was: {oct_match}')
print(f'The number of requests made in October 1995 was: {oct_match}')
print(f'The number of requests made in November 1994 was: {nov_match}')
print(f'The number of requests made in December 1994 was: {dec_match}')
print()
print()


unsuccessful_count = 0
f= open("http_access_log.log", "r")
for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 3:
    continue
  if pieces[3] == '400':
    unsuccessful_count += 1
    continue
  if pieces[3] == '403':
    unsuccessful_count += 1
    continue
  if pieces[3] == '404':
    unsuccessful_count += 1
unsuccessful = (unsuccessful_count/726736)*100
formatted_unsuccessful = "{:.2f}".format(unsuccessful)

print('Percent of requests unsuccessful:',formatted_unsuccessful,'%')

redirected_count = 0
f= open("http_access_log.log", "r")
for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 3:
    continue
  if pieces[3] == '300':
    redirected_count += 1
    continue
  if pieces[3] == '304':
    redirected_count += 1
    continue
  if pieces[3] == '302':
    redirected_count += 1
redirected = (redirected_count/726736)*100
formatted_redirected = "{:.2f}".format(redirected)

print('Percent of requests redirected:',formatted_redirected,'%')

f= open("http_access_log.log", "r")
for line in f:
  if "Oct" in line:
    open('oct.txt', 'a').writelines(line)

  if "Nov" in line:
   open('nov.txt', 'a').writelines(line)

  if "Dec" in line:
    open('dec.txt', 'a').writelines(line)

  if "Jan" in line:
   open('jan.txt', 'a').writelines(line)

  if "Feb" in line:
   open('feb.txt', 'a').writelines(line)

  if "Mar" in line:
   open('mar.txt', 'a').writelines(line)

  if "Apr" in line:
   open('apr.txt', 'a').writelines(line)

  if "May" in line:
   open('may.txt', 'a').writelines(line)

  if "Jun" in line:
   open('jun.txt', 'a').writelines(line)

  if "Jul" in line:
   open('jul.txt', 'a').writelines(line)

  if "Aug" in line:
   open('aug.txt', 'a').writelines(line)

  if "Sep" in line:
   open('sep.txt', 'a').writelines(line)



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



#least common

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
for count in counter.most_common()[-3:]: 
    print( 'The least common files are:', '%s %s' % (count))

logfile.close()