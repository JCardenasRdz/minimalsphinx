# %% open text file in read mode
file = 'mysqlcode'
text_file = open(f'./SQL/{file}.sql', 'r')
sql = text_file.read()

# %%
code_in_md = f"""
#{file}
```SQL
{sql}
```
"""
with open(f'../docs/{file}.md', "w") as text_file:
    text_file.write(code_in_md)
    
    
# %%




text_file = open("sample.txt", "w")


n = text_file.write('Welcome to pythonexamples.org')
text_file.close()
# %%
