from weasyprint import HTML
HTML('./resume.html').write_pdf('resume.pdf')
# x = HTML('./resume.html')
# print(x)
