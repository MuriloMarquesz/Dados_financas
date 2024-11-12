from yahoo_fin import stock_info as si

def gerar_arquivo_excel(codigo_acao, data_inicial, data_final):
    data = si.get_data(codigo_acao, data_inicial, data_final)
    data.to_csv(f"{codigo_acao}_{data_final}.csv")



codigo_acao = input('Digite o nome da Ação: ')
data_inicial = input('Digite a data de inicio: ')
data_final = input('Digite a data final: ')


gerar_arquivo_excel(codigo_acao, data_inicial, data_final)

