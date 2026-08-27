import random

# ordem = int(input("qual a ordem da matriz: "))
# if ordem >= 2:
#     while True:
#         m = []
#         for i in range(ordem):
#             linha = []
#             for j in range(ordem):
#                 num = random.randint(0,9)
#                 linha.append(num)
#             m.append(linha)
#         break
#     dp = []
#     ds = []
#
#     for i in range(ordem):
#         for j in range(ordem):
#             print(m[i][j],end=" ")
#             if i == j: #dp
#                 dp.append(m[i][j])
#             elif i + j == (ordem - 1): #ds
#                 ds.append(m[i][j])
#         print("")
#     maior_DP = max(dp)
#     menor_Ds = min(ds)
#     media = (maior_DP + menor_Ds) / 2
#     print(f'media = {media:.2f}')
# else:
#     print("erro")

ordem = int(input("qual a ordem da matriz: "))
if ordem >= 2:
    while True:
        m = []
        for i in range(ordem):
            linha = []
            for j in range(ordem):
                num = random.randint(0,30)
                linha.append(num)
            m.append(linha)
        break
    dp = []
    ds = []
    abdp = []
    acdp = []
    for i in range(ordem):
        for j in range(ordem):
            print(m[i][j],end=" ")
            if i == j: #dp
                dp.append(m[i][j])
                if i + j == (ordem - 1):  # ds
                    ds.append(m[i][j])
            elif i + j == (ordem - 1): #ds
                ds.append(m[i][j])
                if i > j:
                    abdp.append(m[i][j])
                elif i < j:
                    acdp.append(m[i][j])
            elif i > j:
                abdp.append(m[i][j])
            elif i < j:
                acdp.append(m[i][j])
        print("")

    print(f"DP {dp}")
    print(f"DS {ds}")
    print(f"ABAIXO DP {abdp}")
    print(f"ACIMA DP {acdp}")
else:
    print("erro")