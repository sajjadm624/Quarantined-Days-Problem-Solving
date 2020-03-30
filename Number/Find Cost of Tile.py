def main():
	n = int(input("Enter per unit title cost of tile"))
	heightTile = int(input("Enter the Height of tile"))
	widthTile = int(input("Enter the Width of tile"))
	TileArea = heightTile*widthTile

	Height = int(input("Enter the height of covering area"))
	Width = int(input("Entwr the width of covering area"))
	CoveringArea = Height*Width
	TotalNumofTile = int(CoveringArea/TileArea)


	print (n*TotalNumofTile)

if __name__ == '__main__':
	main()