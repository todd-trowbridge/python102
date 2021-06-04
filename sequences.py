languages = ['python', 'javascript', 'html', 'css']
empty_list = []
lhs = 0
rhs = 2
for lang in languages[lhs:rhs]:
  print(lang)
  if lang == 'html':
    print('found it')
    break