prefix = ''
suffix = ''

with open('Movie Data.txt', 'r') as source:
    with open('Formatted Movie Data.txt', 'w') as destination:
        for line in source:
            destination.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))