from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console



app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1= Jogo('Skyrim', 'RPG', 'PC, PS4, XBOX')
    jogo2= Jogo('Genshin Impact', 'Gacha', 'PC, Mobile')
    jogo3= Jogo('League of Legends', "MOBA", "PC")
    lista = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)


app.run()