import re
line = 'booooobby123'

gread_regx_str = '.*?(b.*b).*'
match_obj = re.match(gread_regx_str, line)
if match_obj:
    print('非贪婪匹配从前往后'+match_obj.group(1))

not_gread_regx_str = '.*(b.*b).*'
match_obj = re.match(not_gread_regx_str, line)
if match_obj:
    print('贪婪匹配从后往前'+match_obj.group(1))


not_gread_regx_str2 = '.*?(b.*?b).*'
match_obj = re.match(not_gread_regx_str2, line)
if match_obj:
    print('非贪婪匹配从后往前'+match_obj.group(1))