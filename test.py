from datetime import datetime

def fecha():
	now = datetime.now()
	print("Hoy es", '%s-%s-%s' % (now.year, now.month, now.day))
	
def main():
	print("Prueba de integración definitiva")
	fecha()

main()