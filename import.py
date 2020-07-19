import zipfile
import shutil

with open("./mse_paths.txt", "r") as paths:
	for line in paths:
		path = line.replace("\n","")
		dirname = path.split("/")[-1].replace(".mse-set","")
		shutil.rmtree(dirname, ignore_errors = True)
		with zipfile.ZipFile(path) as zip_ref:
			zip_ref.extractall(dirname)