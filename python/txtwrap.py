import textwrap

txt = '''   Although never is often better than *right* now.If the implementation 
is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those
'''

#print("************ No dedent ************")
# removes enters
no_dedent = textwrap.fill(txt)
# print(no_dedent)

# dedent
# removes indent, keep the enters
dedent = textwrap.dedent(txt).strip()
# print(dedent)

# fill, column width
fill = textwrap.fill(dedent, width=40)
# print(fill)

# controlling indent
ctr_indent = textwrap.fill(txt, initial_indent="    ", subsequent_indent="")
# print(ctr_indent)

# shortening text
short = textwrap.shorten(
    "Namespaces are one honking great idea", width=25, placeholder="...")
print(short)
