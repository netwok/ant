def pgnfix(text, src='ICC'):
    res = []
    sites = {'ICC': 'Internet Chess Club','LIC': 'lichess.com','CDM': 'chess.com'}
    if src == 'ICC':
        list1 = text.split('</td></tr><tr><td>')
        for line in list1:
            linar = line.split('.</td><td class="fbshare-notation">')[1].split('</td><td class="fbshare-notation">')
            res.append(linar)
        for i in range(len(res[-1])):
            res[-1][i] = res[-1][i].replace('</td></tr>','')
        return res
    else:
        print('Please specify a valid source from one of the following abbreviations:', *sites, sep='\n')
pgnfix(text, 'LIC')
