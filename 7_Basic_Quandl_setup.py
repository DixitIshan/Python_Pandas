import Quandl

api_key = 'yoursuperamazingquandlAPIkey'

df = Quandl.get('heregoesthequandlcode', authtoken = api_key)

print(df.head())

#READING FROM A WEB PAGE HTML
read_pages = pd.read_html('here goes the url link of the website')
print(read_pages)


#PRINTING A SPECIFIC DATAFRAME FROM THE PARSED HTML LIST
print(read_pages[0])


#PRINTING A SPECIFIC COLUMN FROM THE ABOVE PARSED DATAFRAME
print(read_pages[0][0])


#STARTING TO LOOP FROM THE FIRST VALUE OF THE FIRST COLUMN OF TEH DATAFRAME
for item in read_pages[0][0][1:]:
	print(str(item))