import pydf

pdf = pydf.generate_pdf('<h1>Meu pdf gerado em python<h1>')
with open('criarPDF.pdf', 'wb') as f:
    f.write(pdf)