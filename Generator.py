list = ("text")

def all_variants():
    for item in list:
            yield item




a = all_variants()
for i in a:
    print(i)
