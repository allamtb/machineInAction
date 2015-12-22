from pattern.web import Wikipedia
article=Wikipedia().search('python')
for section in article.sections:
    print section.tilte

