def pgnfix_print(text, src='ICC'):
  sites = {'ICC': 'Internet Chess Club','LIC': 'lichess.com','CDM': 'chess.com'}
  if src == 'ICC':
    list1 = text.replace('</td></tr><tr><td>',' ').replace('</td><td class="fbshare-notation">',' ').replace('</td></tr>','').replace('<tr><td>','')
    print(list1)
  else:
    print('Please specify a valid source from one of the following abbreviations:', **sites, sep='\n')
