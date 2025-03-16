TD ransomware:Salma Nahrou

Question1:

L'algorithme XOR utilisé pour le chiffrement n'est pas très sécurisé. En effet, si l'on dispose à la fois d'une version chiffrée et d'une version non chiffrée  du même fichier, il est possible de retrouver la clé de chiffrement. 

Question2:

Il n'est pas conseillé de hacher directement le sel et la clé, car cela n'apporte pas de réelle sécurité supplémentaire. Le sel et la clé sont déjà des valeurs générées aléatoirement et uniques, et les hacher ne compliquerait pas leur décryptage.un HMAC sert principalement à garantir l'intégrité et l'authenticité des données, ce qui n'est pas l'objectif ici, puisque le chiffrement des fichiers reste la priorité.

Question3:

Vérifier l'existence d'un fichier token.bin avant de créer un nouveau fichier est important pour éviter de perdre des données de chiffrement précédemment générées. Si ce fichier existe déjà, cela permet d'éviter de l'écraser et de rendre impossible le déchiffrement des fichiers précédemment chiffrés.

Question4:
Pour s'assurer que la clé fournie est correcte, on compare le token dérivé à partir du sel et de la clé candidate avec le token stocké à l'origine. Si ces deux valeurs correspondent, cela signifie que la clé est valide et que l'utilisateur peut procéder au déchiffrement des fichiers.