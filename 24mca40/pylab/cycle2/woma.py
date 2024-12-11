lst=input("enter a list of words(space seperated):").split()
maxlength=max(len(word) for word in lst)
lg_word=[word for word in lst if len(word)==maxlength]
print(f"largest word:{lg_word},size:{maxlength}")
