## Adicionar items ao dicionario , verificar 
## se mesmo existe , senao adciona.
## ADCIONAR OU APAGAR ITENS OU ESTOQUE
Dic_estoque = {}

Valida_item = False
Valida_qt = False

Dic_item = input("DIGITE O PRODUTO EM ESTOQE: ").lower()
Valida_item == Dic_estoque.get(Dic_item)
if Dic_item not in (Valida_item):
    print("ESTE PRODUTO JA TEM NO ESTOQUE")
    Item_sn = input("DESEJA ACRESENNTAR MAIS NO ESTOQUE- > (S OU N): ").lower()
    if Item_sn == "s":
        Sn_qt = input("DIGITE A QUANTIDADE DE PRODUTO A ACRESENTAR EM ESTOQUE: ")
        Dic_estoque.keys()

Dic_qt = input("DIGITE A QUANTIDADE DO PODUTO: ")