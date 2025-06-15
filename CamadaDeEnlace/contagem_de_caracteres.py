def contagemDeQuadros(mensagem):
    m = str(len(mensagem)) + mensagem
    return m

def flagsComInsercao(mensagem):
    novaMensagem = ""
    for i in range(0, len(mensagem)):
        if mensagem[i] == "@":
            novaMensagem += "/@"
        else:
            novaMensagem += mensagem[i]
    novaMensagem = "@" + novaMensagem + "@"
        
    return novaMensagem

