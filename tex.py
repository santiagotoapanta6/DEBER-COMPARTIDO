from  textblob import TextBlob
text = '''La historia empieza cuando Harry es dejado en la casa de sus Tios, los Dursley, por Rubeus Hagrid, Albus Dumbledore y Minerva McGonnagall.
Alli mencionan que Lord Voldemort, el mago mas tenebroso de esos tiempos habia sido vencido, luego de intentar matar a Harry Potter.
Harry sobrevivio a la maldicion asesina, con no otra secuela que una cicatriz con forma de rayo en la frente. Poco antes de su cumpleanios Harry recibe una carta de Hogwarts, pero no logra abrirla o causa de su tio,
que no quiere que el chico se entere de que puede hacer magia. Los esfuerzos de Vernon no prosperan, y siguen llegando cartas, traidas extraniamente por lechuzas.
Para que no haya mas disturbios con las cartas, la familia Dursley con Harry se mudan a una casita en una islita. El dia de cumpleanios de Harry,
todavia en esa casita, llega el gigantesco Hagrid a entregarle la carta personalmente, y a desearle feliz cumpleaños. Vernon se tiene que dar por vencido,
y Harry se entera de toda la verdad. La carta decia que Harry estaba invitado a participar del primer año en el Colegio Hogwarts de Magia y Hechizeria.
Harry se entusiasma por salir de su vida como muggle, de escaparse de los Dursley, a un lugar donde todos serian como el. Hagrid lleva a Harry al Callejon Diagon 
a comprar sus cosas para el colegio. Harry, con el Guardian de Llaves de Hogwarts, va al banco de los magos, Gringotts,
donde descubre que sus padres le habian dejado una gran fortuna. Luego, por “asuntos de Hogwarts” van a la camara 713 y Hagrid se lleva un paquete misterioso… 
Harry compra una varita, libros, y Hagrid le regala a Hedwig, una lechuza. Luego empieza el año en Hogwarts. Al llegar Harry descubre que hay cuatro casas; 
Gryffindor, Slytherin, Ravenclaw y Hufflepuff, y que va a ser asignador a una. Ron Weasley, un chico que habia conocido en el tren que los llevaba al Colegio,
le dice que en Slytherin estaban los magos malos, y Harry desea no entrar a esa casa. Finalmente termina con Ronald en Gryffindor, 
y el que acaba en Slytherin es Draco Malfoy, un chico que habia insultado a Ron.'''

## ASI EVITAMOS QUE SE IMPRIMA VARIAS VECES EL TEXTO TRADUCIDO
blob1 = TextBlob(text)
##blob2 = TextBlob(text1)
blob1.tags
##blob2.tags
blob1.noun_phrases
##blob2.noun_phrases
##for sentence in blob1.sentences:
print ("#############-------- TRADUCCION ----##########################")
print (blob1.translate (to = "en")) ##"en" en esta parte se pone el idionma al que se quiere traducir
for sentence in blob1.sentences:
	print(sentence.sentiment.polarity)
##for sentence in blob2.sentences:
##	print(sentence.sentiment.polarity)
##	print (blob2.translate (to = "en"))
