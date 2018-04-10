# https://leetcode.com/problems/valid-phone-numbers/description/
# http://bit.ly/2qk0MLr

awk '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/' file.txt
