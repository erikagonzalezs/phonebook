def imprimir_menu():
	print "1. Imprimir contactos"
	print "2. Anadir un nuevo contacto"
	print "3. ELiminar un contacto"
	print "4. Buscar un contacto"
	print "5. Imprimir contactos buenos"
	print "6. Imprimir contactos malos"
	print "7. Salir"

agenda = {}
menu_opcion = 0
listAmigos = 0
listEnemigos = 0
imprimir_menu()

while menu_opcion != 7:
	menu_opcion = input("Elija una opcion: ")
	if menu_opcion == 1:
		print "Agenda"
		for x in agenda.keys():
			print "Nombre: ",x, "\nNumero: ",agenda[x][0],"\nDireccion: ",agenda[x][1],"\nEstado: ",agenda[x][2]
		print
	elif menu_opcion == 2:
		print "Anadir nuevo contacto"
		name = raw_input("Nombre: ")
		phone = raw_input("Numero: ")
		add = raw_input("Direccion: ")
		estado = raw_input("Estado: ")
		agenda[name] = phone, add, estado
		if estado == "amigo":
			listAmigos = listAmigos + 1
		elif estado == "enemigo":
			listEnemigos = listEnemigos + 1
	elif menu_opcion == 3:
		print "ELiminar un contacto"
		name = raw_input("Nombre: ")
		if agenda.has_key(name):
			del agenda[name]
			print "El contacto ", name," fue eliminado exitosamente"
		else:
			print name," no fue encontrado"
	elif menu_opcion == 4:
		print "Buscar un contacto"
		name = raw_input("Nombre: ")
		if agenda.has_key(name):
			print "Numero: ",agenda[name][0],"\nDireccion: ",agenda[name][1],"\nEstado: ",agenda[name][2]
		else:
			print name," no fue encontrado"
	elif menu_opcion == 5:
		if listAmigos == 0:
			print "No tiene contactos que sean amigos"
		else:
			for j in agenda.keys():
				print "Contactos que me caen bien :)"
				if agenda[j][2] == "amigo":
					print "Nombre: ",j,"\nNumero: ",agenda[j][0],"\nDireccion: ",agenda[j][1],"\nEstado: ",agenda[j][2]
			print
	elif menu_opcion == 6:
		if listEnemigos == 0:
			print "No tiene contactos que sean enemigos"
		else:
			for k in agenda.keys():
				print "Contactos que me caen mal :("
				if agenda[k][2] == "enemigo":
					print "Nombre: ",k,"\nNumero: ",agenda[k][0],"\nDireccion: ",agenda[k][1],"\nEstado: ",agenda[k][2]
			print
	elif menu_opcion == 7:
		exit()
	elif menu_opcion != 7:
		imprimir_menu();