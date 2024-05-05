def check(wrd1,wrd2):
  if wrd1==wrd2:
    print(f'{wrd1} and {wrd2} are anagrams')
  else:
    print(f'{wrd1} and {wrd2} are not anagrams')

wrd1 = 'players'
wrd2= 'parsley'
check(wrd1,wrd2)