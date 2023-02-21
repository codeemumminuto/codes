import instaloader
from random import randint

L = instaloader.Instaloader()
username = "meuusuario"
password = "minhasenha"

# Carregando Sessão / Realizanod Login
try:
    L.context.log("Tentando carregar a sessão...")
    L.load_session_from_file(username)
    if not L.context.is_logged_in:
        L.context.log("A sessão não é válida.")
        L.context.session_filename = None
except FileNotFoundError:
    L.context.log("Não foi possível carregar a sessão. Criando uma nova sessão...")

if not L.context.is_logged_in:
    try:
        L.context.log("Fazendo login...")
        L.context.login(username, password)
        L.save_session_to_file()
        L.context.log("Sessão criada e salva.")
    except instaloader.exceptions.BadCredentialsException:
        L.context.log("Não foi possível fazer login. Credenciais inválidas.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        L.context.log("Não foi possível fazer login. É necessária autenticação de dois fatores.")
    except Exception as e:
        L.context.log(f"Não foi possível fazer login. {str(e)}")

# Inicio do programa de sorteio
# Carrega a postagem
post_code = "codigodapostagem" #https://instagram.com/p/XycK982qe/
post = instaloader.Post.from_shortcode(L.context, post_code)
# Carrega os comentários e pega a quantidade de comentários
comments = list(post.get_comments())
max = len(comments)

# Sorteia e imprime
random_number = randint(0, max-1)
print(f"Dono do comentário: {comments[random_number].owner.username}")
print(f"Comentário do usuário: {comments[random_number].text}")
