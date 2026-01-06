import time

def main():
	t = time.time()
	print(f"Seconds since January 1, 1970: {t:,.4f} or {t:,.2e}  in scientific notation")  # Affiche le nombre de secondes depuis le 1er janvier 1970
	print( time.strftime("%b %d %Y", time.localtime(t)))

if __name__ == "__main__":
	main()

#%b → mois abrégé (Oct)
#%d → jour
#%Y → année