import csv
import re
list =[]
with open('Wikipedia_topics.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        list.append(row[0])


finaList =[]
for topic in list:
    final = re.search(r'_[iI]nternational_[Aa]irport$', topic)
    if final:
        finaList.append(topic)


newlist =finaList