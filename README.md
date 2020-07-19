# MSE files of the YGOPro Bionicle Expansion
This repository tracks the contents of the various .mse-set files in which the cards for the YGOPro Bionicle Expansion are designed.  
The `import` and `export` scripts are used to convert data between Magic Set Editor's .mse-set package format and the more git-friendly directory format.

Lua Script Repository: https://github.com/BarnacleYoghurt/ygopro-bionicle-expansion  
For further details and downloads see https://www.ygopro.co/Forum/tabid/95/g/posts/t/29447/Custom-Bionicle-cards

## How to use
* To use `import` and `export`, you must create a file named `mse_paths.txt` in the repository's root directory. This file holds the paths of the source/target .mse-set files, absolute or relative, one per line.
* Before committing, use `python import.py` to get changes made in Magic Set Editor
* After pulling changes from elswhere, use ``python export.py` to make those changes available in Magic Set Editor
* Any directory matching a file listed in `mse_paths.txt` will be deleted before importing, others will not be touched