import flet as ft
import aoo_clinica.models.model_flet_controls as modelos


# Classe que contém todos os controles da tela (view) de início
class ViewInicio:
    def __init__(self):
        # As instâncias dos controles devem ser criadas aqui, como atributos da instância
        self.caixa_texto = modelos.CaixaDeTexto(label='lista', largura=200, tamanho_texto=15)
        self.caixa_escolha = modelos.CaixaDeEscolha(label='teste', largura=200, tamanho_texto=15)

        self.caixa_escolha.adicionar_novo_item('Opção 1')
        self.caixa_escolha.adicionar_novo_item('Opção 2')
        self.caixa_escolha.adicionar_novo_item('Opção 3')
        self.caixa_escolha.adicionar_novo_item('Opção 4')
        self.caixa_escolha.adicionar_novo_item('Opção 5')

        self.botao_texto = modelos.BotaoSomenteTexto(texto='Botao', funcao_do_botao=lambda e: print('oi')).get_botao

        # Essa deve ser a última linha do método __init__. Esse atributo é quem contém a view e deve ser chamado
        # quando quisermos acessá-la.
        self.view = self._get_view()

    def _get_view(self):
        return ft.View(
            route='/inicio',
            controls=[
                # A view deve ser construída aqui dentro, utilizando os atributos definidos no __init__
                self.caixa_texto.get_controle,
                self.caixa_escolha.get_controle,
                self.botao_texto
            ]
        )
