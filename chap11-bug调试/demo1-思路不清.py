lst = [{'rating': [97, 20], 'id': 123460, 'type': ['asd', 'asd'], 'title': 'askjdashldh',
        'actors': ['adf', 'fdsag', 'dfsag']},
       {'rating': [93, 26], 'id': 1235460, 'type': ['ahfhgd', 'adgd'], 'title': 'askjsdgdgldh',
        'actors': ['aFAf', 'fdsAFag', 'dfsshfgag']},
       {'rating': [27, 25], 'id': 12354560, 'type': ['awrd', 'aszc'], 'title': 'askjasFh',
        'actors': ['adf', 'fjjjjg', 'hgfdjj']}]
name = input('输入：')
for it in lst:
    if name in it['actors']:
        print(it)
        print(it['title'])
        # break
