For those using Python 3.5+ you can now use a glob recursively with the use of ** and the recursive flag.

Here's an example replacing hello with world for all .txt files:

for filepath in glob.iglob('./**/*.txt', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('hello', 'world')
    with open(filepath, "w") as file:
        file.write(s)


