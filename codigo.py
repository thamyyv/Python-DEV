# botão de chat
# popup para entrar no chat
# quando entrar no chat;
    # a mensagem que você entrou no site
    # o campo e o botão de enviar mensaggens
# a cada mensagem enviada:
    # Nome: Texto da mensagem 

import flet as ft

def main(pagina):
    texto = ft.Text("ZapZaperson")
    chat = ft.Column()
    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensaggem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensaggem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat",
                                         size=12, italic=True, color=ft.colors.BLUE_ACCENT_200))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto":campo_mensagem.value, "usuario":nome_usuario.value, "tipo": "mensagem"})
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open=False
        pagina.remove(botao_iniciar) 
        pagina.remove(texto)      
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
            ) )
        pagina.update()

    

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao ZapZaperson"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
                    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main)