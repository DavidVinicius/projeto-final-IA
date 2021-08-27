from keras import load_model

model = load_model('model/model.h5')

#model.predict_classes(train_images)

im = Image.open('bw_image.png')
imagem_matriz = np.matrix(im.getdata())
imagem_vetor = imagem_matriz.getA1()

print(imagem_vetor)
