from PIL import Image
import os

# Diretório onde estão as imagens originais
diretorio_original = '.'
# Diretório onde você deseja salvar as imagens redimensionadas
diretorio_destino = '.'
# Tamanho desejado para as imagens redimensionadas
novo_tamanho = (300, 400)

# Lista todos os arquivos na pasta original
for filename in os.listdir(diretorio_original):
    # Verifica se o arquivo é uma imagem
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Abre a imagem original
        with Image.open(os.path.join(diretorio_original, filename)) as img:
            # Redimensiona a imagem sem perder qualidade
            img_resized = img.resize(novo_tamanho, Image.LANCZOS)
            
            # Salva a imagem redimensionada no diretório de destino
            novo_nome = os.path.splitext(filename)[0] + '_.png'
            img_resized.save(os.path.join(diretorio_destino, novo_nome), 'PNG')

print("Redimensionamento concluído!")
