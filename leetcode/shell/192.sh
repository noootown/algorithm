# https://leetcode.com/problems/word-frequency/description/
# http://bit.ly/2qkAjxl
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'