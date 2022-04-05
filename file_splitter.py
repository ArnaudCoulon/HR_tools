#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import os


# In[31]:


file = input("Entrez le nom du fichier ")
#file = "IP_agents.xlsx"


dtype_dic= {'Matricule Paie': str,
            'Matricule GA' : str,
            'Matricule' : str,
            'Matricule GT' :str,
            'Matricule  GA' : str,
            'Matricule GA':str}

df = pd.read_excel(file,dtype = dtype_dic)


# In[32]:


print("Voici la liste des colonnes :")
for col in df.columns:
    print(col)


# In[24]:


df


# In[27]:


col = input("Entrez le nom de la colonne de base pour le découpage ")
#col = "Région actuelle"


# In[28]:


libelle = df[[col]]
libelle.drop_duplicates(keep = 'first', inplace=True)
libelle=pd.DataFrame(libelle)


# In[29]:


prefixe = input("Entrez le nom du préfixe au fichier ")
#prefixe = "IP_agent - "


# In[30]:


if not os.path.exists(prefixe):
    os.makedirs(prefixe)

"""
for i in libelle[col] :
    writer = pd.ExcelWriter(prefixe+" - "+i+".xlsx")
    print(i,"en cours de traitement")
    df_temp = df[(df[col] == i)]
    df_temp.to_excel(writer, index = False)
    writer.save()

          """

for i in libelle[col] :
    writer = pd.ExcelWriter(os.path.join(prefixe, prefixe+" - "+i+".xlsx"))
    print(i,"en cours de traitement")
    df_temp = df[(df[col] == i)]
    df_temp.to_excel(writer, index = False)
    writer.close()
    
    
print("Traitement terminé")

