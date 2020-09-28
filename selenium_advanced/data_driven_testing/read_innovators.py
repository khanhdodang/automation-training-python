import csv

print("\nBasic Usage of csv.reader()\n")

with open('innovators.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

'''
CSV files with Custom Delimiters
By default, a comma is used as a delimiter in a CSV file. However, some CSV files can use delimiters other than a comma. Few popular ones are | and \t.

Suppose the innovators.csv file in Example 1 was using tab as a delimiter. To read the file, we can pass an additional delimiter parameter to the csv.reader() function.
'''

print("\nCSV files with Custom Delimiters\n")

with open('innovators.csv', 'r') as file:
  reader = csv.reader(file, delimiter = '\t')
  for row in reader:
    print(row)

print("\nCSV files with initial spaces\n")
'''
Some CSV files can have a space character after a delimiter. When we use the default csv.reader() function to read these CSV files, we will get spaces in the output as well.

To remove these initial spaces, we need to pass an additional parameter called skipinitialspace. Let us look at an example:
'''
with open('people.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)
  for row in reader:
    print(row)

print("\nCSV files with quotes\n")
'''
Some CSV files can have quotes around each or some of the entries.

Using csv.reader() in minimal mode will result in output with the quotation marks.

In order to remove them, we will have to use another optional parameter called quoting.

Let's look at an example of how to read the above program.
'''
with open('quotes.csv', 'r') as file:
  reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
  for row in reader:
    print(row)

'''
As you can see, we have passed csv.QUOTE_ALL to the quoting parameter. It is a constant defined by the csv module.

csv.QUOTE_ALL specifies the reader object that all the values in the CSV file are present inside quotation marks.

There are 3 other predefined constants you can pass to the quoting parameter:

csv.QUOTE_MINIMAL - Specifies reader object that CSV file has quotes around those entries which contain special characters such as delimiter, quotechar or any of the characters in lineterminator.
csv.QUOTE_NONNUMERIC - Specifies the reader object that the CSV file has quotes around the non-numeric entries.
csv.QUOTE_NONE - Specifies the reader object that none of the entries have quotes around them.
'''

print("\nRead CSV files using dialect\n")

csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('office.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, dialect='myDialect')
  for row in reader:
    print(row)

'''
The CSV file has initial spaces, quotes around each entry, and uses a | delimiter.

Instead of passing three individual formatting patterns, let's look at how to use dialects to read this file.
From this example, we can see that the csv.register_dialect() function is used to define a custom dialect. It has the following syntax:

csv.register_dialect(name[, dialect[, **fmtparams]])
The custom dialect requires a name in the form of a string. Other specifications can be done either by passing a sub-class of Dialect class, or by individual formatting patterns as shown in the example.

While creating the reader object, we pass dialect='myDialect' to specify that the reader instance must use that particular dialect.

The advantage of using dialect is that it makes the program more modular. Notice that we can reuse 'myDialect' to open other files without having to re-specify the CSV format.
'''

print("\nRead CSV files with csv.DictReader()\n")
'''
The objects of a csv.DictReader() class can be used to read a CSV file as a dictionary.
'''
with open("people.csv", 'r') as file:
  csv_file = csv.DictReader(file)
  for row in csv_file:
    print(dict(row))

'''
As we can see, the entries of the first row are the dictionary keys. And, the entries in the other rows are the dictionary values.

Here, csv_file is a csv.DictReader() object. The object can be iterated over using a for loop. The csv.DictReader() returned an OrderedDict type for each row. That's why we used dict() to convert each row to a dictionary.

Notice that we have explicitly used the dict() method to create dictionaries inside the for loop.

print(dict(row))
Note: Starting from Python 3.8, csv.DictReader() returns a dictionary for each row, and we do not need to use dict() explicitly.

The full syntax of the csv.DictReader() class is:

csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
'''

print("\nUsing csv.Sniffer class\n")
'''
The Sniffer class is used to deduce the format of a CSV file.

The Sniffer class offers two methods:

sniff(sample, delimiters=None) - This function analyses a given sample of the CSV text and returns a Dialect subclass that contains all the parameters deduced.
An optional delimiters parameter can be passed as a string containing possible valid delimiter characters.

has_header(sample) - This function returns True or False based on analyzing whether the sample CSV has the first row as column headers.
'''

with open('office.csv', 'r') as csvfile:
  sample = csvfile.read(64)
  has_header = csv.Sniffer().has_header(sample)
  print(has_header)

  deduced_dialect = csv.Sniffer().sniff(sample)

with open('office.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, deduced_dialect)

  for row in reader:
    print(row)

'''
As you can see, we read only 64 characters of office.csv and stored it in the sample variable.

This sample was then passed as a parameter to the Sniffer().has_header() function. It deduced that the first row must have column headers. Thus, it returned True which was then printed out.

Similarly, sample was also passed to the Sniffer().sniff() function. It returned all the deduced parameters as a Dialect subclass which was then stored in the deduced_dialect variable.

Later, we re-opened the CSV file and passed the deduced_dialect variable as a parameter to csv.reader().

It was correctly able to predict delimiter, quoting and skipinitialspace parameters in the office.csv file without us explicitly mentioning them.
'''
