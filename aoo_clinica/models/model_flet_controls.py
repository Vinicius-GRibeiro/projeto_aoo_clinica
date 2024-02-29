import flet as ft

RAIO_DA_BORDA = 15
TAMANHO_TEXTO = 15
ALTURA_PADRAO = 50
LARGURA_PADRAO = 100


class CaixaDeTexto:
    def __init__(self, label: str, largura: int = LARGURA_PADRAO, altura: int = ALTURA_PADRAO,
                 tamanho_texto: int = TAMANHO_TEXTO):
        self._label = label
        self._largura = largura
        self._altura = altura
        self._tamanho_texto = tamanho_texto
        self.get_controle = self._get_caixa_de_texto()

    def _get_caixa_de_texto(self) -> ft.TextField:
        return ft.TextField(
            label=self._label,
            border_color=ft.colors.PRIMARY,
            border_radius=RAIO_DA_BORDA,
            width=self._largura,
            height=self._altura,
            text_size=self._tamanho_texto,
            label_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD
            )
        )


class CaixaDeEscolha:
    def __init__(self, label: str, largura: int = LARGURA_PADRAO, altura: int = ALTURA_PADRAO,
                 tamanho_texto: int = TAMANHO_TEXTO):
        self._label = label
        self._largura = largura
        self._altura = altura
        self._tamanho_texto = tamanho_texto
        self._opcoes = []
        self.get_controle = self._get_caixa_de_escolha()

    def adicionar_novo_item(self, item) -> None:
        self._opcoes.append(
            ft.dropdown.Option(item)
        )

    def _get_caixa_de_escolha(self) -> ft.Dropdown:
        return ft.Dropdown(
            label=self._label,
            border_color=ft.colors.PRIMARY,
            border_radius=RAIO_DA_BORDA,
            width=self._largura,
            height=self._altura,
            text_size=self._tamanho_texto,
            label_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD
            ),
            options=self._opcoes
        )


class BotaoSomenteTexto:
    def __init__(self, texto: str, funcao_do_botao,
                 icone: str = None, largura: int = LARGURA_PADRAO, altura: int = ALTURA_PADRAO):
        self._texto = texto
        self._icone = icone
        self._altura = altura
        self._largura = largura
        self._funcao_do_botao = funcao_do_botao
        self.get_botao = self._get_botao()

    def _get_botao(self) -> ft.TextButton:
        return ft.TextButton(
            content=ft.Text(
                value=self._texto,
                size=TAMANHO_TEXTO,
                weight=ft.FontWeight.BOLD
            ),
            style=ft.ButtonStyle(
                overlay_color='transparent',
                color={
                    ft.MaterialState.DEFAULT: ft.colors.PRIMARY,
                    ft.MaterialState.PRESSED: ft.colors.SECONDARY
                },
            ),
            icon=self._icone,
            icon_color=ft.colors.PRIMARY,
            width=self._largura,
            height=self._altura,
            on_click=self._funcao_do_botao
        )
