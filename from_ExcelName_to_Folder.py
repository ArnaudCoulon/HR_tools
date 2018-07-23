#import des packages

import pandas as pd
import os

path_file = "your path"
path_folder = "your path"

effectif = pd.read_excel(path)
effectifs_bis =pd.DataFrame(effectif)

i=0
while i < 245 :
    folderName = effectifs_bis["Nom"][i]
    i=i+1
    os.makedirs("C:/Users/984098/Collaborateurs/"+folderName)
