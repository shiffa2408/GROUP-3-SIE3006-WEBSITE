

# read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# filter the DataFrame to only include rows where the species name is 'Drosophila melanogaster' or 'Drosophila simulans'
df = df[(df['species name'] == 'Drosophila melanogaster') | (df['species name'] == 'Drosophila simulans')]

# print out the gene names
print(df['gene name'])




