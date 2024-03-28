import xlwings as xw

# Cria um novo arquivo Excel
wb = xw.Book()
wb.save('relatorio_excel.xlsx')

# Cria uma nova planilha chamada 'Planilha1'
if 'Planilha1' not in [sht.name for sht in wb.sheets]:
    sheet = wb.sheets.add('Planilha1')
else:
    sheet = wb.sheets['Planilha1']

# Célula da qual você deseja obter a cor
celula = sheet.range('A1')

# Obtém a cor de fundo da célula
cor = celula.api.Interior.Color

# Converte a cor para formato RGB
cor_rgb = (cor % 256, cor // 256 % 256, cor // 65536 % 256)

print(f'A cor da célula A1 é: {cor_rgb}')
