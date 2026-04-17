path = "datasets/bitly_usagov/example.txt"

with open(path) as f:
  print(f.readline())

import json
with open(path) as f:
    records = [json.loads(line) for line in f]

 records[0]

time_zones = [rec["tz"] for rec in records if "tz" in rec]

time_zones[:10]
 
['America/New_York',
 'America/Denver',
 'America/New_York',
 'America/Sao_Paulo',
 'America/New_York',
 'America/New_York',
 'Europe/Warsaw',
 '',
 '',
 '']

 
 def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts   


from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts


counts = get_counts(time_zones)
counts["America/New_York"]
len(time_zones)


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
  
top_counts(counts)
from collections import Counter

counts = Counter(time_zones)
counts.most_common(10)
import seaborn as sns
subset = tz_counts.head()
sns.barplot(y=subset.index, x=subset.to_numpy())


frame["a"][1]
frame["a"][50]
frame["a"][51][:50]  # long line




