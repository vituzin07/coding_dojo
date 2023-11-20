from flask import Flask, render_template
# Questão 1, primeiro item
import random
#O módulo de random é usado para gera numeros aleatorios e para importa-lo é preciso usar o comando import

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template('pedra_papel_tesoura.html', mensagem='', opcao_computador='', opcao_jogador='')

@app.route("/<opcao_jogador>")
def checar_opcao(opcao_jogador):
    mensagem = ''

    # Questão 1, segundo item
    opcao_computador = random.randint(0, 2)
   
    # Questão 1, terceiro item
    match opcao_computador:
      case 0:
        opcao_computador = "pedra"
      case 1:
        opcao_computador = "papel"
      case 2:
        opcao_computador = "tesoura"
    
    # Questão 2, primeiro item
    print(opcao_jogador)
    # Questão 2, segundo item
    if ((opcao_computador=="pedra" and opcao_jogador=="papel") or
        (opcao_computador=="papel" and opcao_jogador=="tesoura") or
        (opcao_computador=="tesoura" and opcao_jogador=="pedra")):
      mensagem = "Jogador venceu!"
      print(mensagem)
    else:
      mensagem = 'Computador venceu!'

    # Questão 2, terceiro item
    if opcao_computador==opcao_jogador:
      mensagem= 'Empate!'
      print(mensagem)
  
    return render_template('pedra_papel_tesoura.html', mensagem=mensagem, opcao_computador=opcao_computador, opcao_jogador=opcao_jogador)

@app.route("/extra")
def acessar_extra():
  return render_template('extra.html')