ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


#your code here

# List : ordonnee et indexe comme un tableau classique
ft_list[1] = "World!"

# tuple : ordonnee et indexe comme un tableau classique mais immutable on doit tout remplacer
ft_tuple = ("Hello", "France!")

# set : non ordonnee et non indexe, pas de doublon, on doit supprimer et ajouter
ft_set.remove("tutu!")
ft_set.add("Le Havre!")

# dict : stockage de paire cle/valeur, non ordonnee et non indexee, on remplace la valeur via la clef
ft_dict["Hello"] = "42 | Le Havre!"

print(ft_list)
print(ft_tuple)
print(ft_set) #print peut afficher dans un ordre different a chaque execution on peut remplacer par print(sorted(ft_set)) pour forcer l'ordre
#print(sorted(ft_set))
print(ft_dict)