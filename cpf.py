from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    #verifica se o cpf é valido com 11 numeros
    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida!")

    #habilita a função PRINT e retorna o cpf como string
    def __str__(self):
        return self.format_cpf()

    #formata o cpf
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)