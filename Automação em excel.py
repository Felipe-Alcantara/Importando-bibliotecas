import xlwings as xw

# Abre o Excel
app = xw.App(visible=True)

# Abre o arquivo Excel
wb = app.books.open('relatorio_excel.xlsx')  # Substitua 'seuarquivo.xlsx' pelo nome do seu arquivo
sheet = wb.sheets['Planilha1']  # Substitua 'Planilha1' pelo nome da sua planilha

# Célula da qual você deseja obter a cor
celula = sheet.range('A1')

# Obtém a cor de fundo da célula
cor = celula.api.Interior.Color

# Fecha o Excel
# app.quit()

# Exibe a cor em formato RGB (Red, Green, Blue)
print(f'A cor da célula A1 é: {cor}')
