color_list1 = input("Enter colors for list 1 separated by commas: ").split(',')
color_list2 = input("Enter colors for list 2 separated by commas: ").split(',')


color_list1 = [color.strip() for color in color_list1]
color_list2 = [color.strip() for color in color_list2]
print("color_list1 is:",color_list1)
print("color_list2 is :",color_list2)
unique_colors = [color for color in color_list1 if color not in color_list2]
print("Colors in color_list1 but not in color_list2:", unique_colors)

