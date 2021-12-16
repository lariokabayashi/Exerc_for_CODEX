
def is_valid(cnpj):
    #sees if the cnpj is valid or not, based in the equation given by the wikipedia link: https://pt.wikipedia.org/wiki/Cadastro_Nacional_da_Pessoa_Jur%C3%ADdica
    v1 = 5*cnpj[0] + 4*cnpj[1]  + 3*cnpj[2]  + 2*cnpj[3]
    v1 += 9*cnpj[4] + 8*cnpj[5]  + 7*cnpj[6]  + 6*cnpj[7]
    v1 += 5*cnpj[8] + 4*cnpj[9] + 3*cnpj[10] + 2*cnpj[11]
    v1 = 11 - (v1 % 11)
    if v1 >= 10 :
        v1 = 0

    v2 = 6*cnpj[0] + 5*cnpj[1] + 4*cnpj[2] + 3*cnpj[3]
    v2 += 2*cnpj[4] + 9*cnpj[5] + 8*cnpj[6]  + 7*cnpj[7]
    v2 += 6*cnpj[8] + 5*cnpj[9] + 4*cnpj[10] + 3*cnpj[11]
    v2 += 2*cnpj[12]
    v2 = 11 - (v2 % 11)
    if v2 >= 10:
        v2 = 0
    if v1 == cnpj[12] and v2 == cnpj[13]:
        return 1
    return -1

def transform_int(cnpj):
    #transform a list of strings in a list of int
    j = 0
    new_cnpj = []
    for i in range (0,len(cnpj)):
        if cnpj[i].isnumeric():
            new_cnpj.append(int (cnpj[i]))
            j += 1
    return new_cnpj

#cnpj = [valid cnpj, not valid cnpj, valid cnpj, valid cnpj, not valid cnpj]
cnpj = ["03.778.130/0001-48", "09567230841210", "11.444.777/0001-61", "59.242.798/0001-20", "24.982.134/0002-12"]
for i in range (0, len(cnpj)):
    cnpj_int = transform_int(cnpj[i])
    digitosVerif = is_valid(cnpj_int)
    if (digitosVerif == 1):
        print(f'{cnpj[i]} is a well-formed CNPJ')
    else: 
        print(f'{cnpj[i]} is not a well-formed CNPJ')
