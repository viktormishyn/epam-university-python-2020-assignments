# Swap words "reasonable" and "unreasonable" in quote "The reasonable man adapts himself to the world; the unreasonable
# one persists in trying to adapt the world to himself"
# Do not use <string>.replace() function or similar

quote = "The reasonable man adapts himself to the world; " \
        "the unreasonable one persists in trying to adapt the world to himself"

lst = quote.split()

reasonable = lst.index('reasonable')
unreasonable = lst.index('unreasonable')

lst[reasonable] = 'unreasonable'
lst[unreasonable] = 'reasonable'

quote = ' '.join(lst)

print(quote)
