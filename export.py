import zipfile
import os

with open("./mse_paths.txt", "r") as paths:
	for line in paths:
		path = line.replace("\n","")
		dirname = path.split("/")[-1].replace(".mse-set","")
		with zipfile.ZipFile(path, "w") as zip_ref:
			for elem in os.listdir(dirname):
				zip_ref.write(dirname + "/" + elem, elem)