import re
class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto!")

    def valida_telefone(self, telefone):
        padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado
    def __str__(self):
        return self.format_numero()


# Caracteres	Descrição	Exemplos
# []	Define um range ou um grupo de caracteres	[0-9]; [a-z]; [abc]
# *	Marca nenhuma, uma ou mais ocorrências	sol*
# {}	Quantidade de repetições de uma ocorrência definida	[abc]{5}
# \d	Qualquer número de 0 até 9	\d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	\w{10}
# |	Um ou outro	@$
# ()	Captura e agrupa	(\w{4})