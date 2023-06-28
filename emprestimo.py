emp= int(input(' Qual o valor do emprestimo ?')) 
parc = int(input( ' quantas parcelas ? ' ))
J = emp * 0.2
total = + J
valor_parcela = total / parc
print(f' Vou pagar {parc} parcelas de {valor_parcela: .2f} cada.' )