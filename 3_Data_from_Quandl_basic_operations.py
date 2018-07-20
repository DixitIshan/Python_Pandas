import Quandl

api_key = 'yoursuperamazingquandlAPIkey'

df = Quandl.get('heregoesthequandlcode', authtoken = api_key)

print(df.head())

#READING FROM A WEB PAGE HTML
fiddy_states = pd.read_html('here goes the url link of the website')
print(fiddy_states)

#PRINTING A SPECIFIC DATAFRAME FROM THE PARSED HTML LIST
print(fiddy_states[0])

#PRINTING A SPECIFIC COLUMN FROM THE ABOVE PARSED DATAFRAME
print(fiddy_states[0][0])

#STARTING TO LOOP FROM THE FIRST VALUE OF THE FIRST COLUMN OF TEH DATAFRAME
for item in fiddy_states[0][0][1:]:
	print(str(item))