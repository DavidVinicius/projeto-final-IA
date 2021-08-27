from PIL import Image, ImageFile, ImageOps
import numpy as np

from math import floor

import pickle

#importação do modelo
with open('model/mlp_model.pkl', 'rb') as fid:
    model = pickle.load(fid)

#converte imagem para matriz
#converte matriz para vetor
im = Image.open('bw_image.png')
#im = ImageOps.invert(im).convert("L")
#im = im.resize((28, 28))
im.save('test1.png')
#quit()
#imagem_vetor_pre = np.asarray(list(map(lambda x: int(x), list(im.getdata()))))
#print(imagem_vetor_pre)
#im = ImageOps.invert(im).convert("1")
#im.save('test.png')
#quit()
#quit()
imagem_matriz = np.matrix(im.getdata())
#print(imagem_matriz)
#imagem_vetor = np.asarray(list(map(lambda x: int(x), list(imagem_matriz))))
imagem_vetor = imagem_matriz.getA1()
#imagem_vetor = np.asarray([round((x * 16) / 255.0) for x in imagem_vetor])

print(imagem_vetor)
#quit()

#converte vetor para vetor numpy
I = np.array([imagem_vetor])
print(I)


#np.savetxt("foo.txt", imagem_vetor)
print(I.shape)

#quit()
classe = model.predict(I)
print("Classe Predita: {}".format(str(classe)))
