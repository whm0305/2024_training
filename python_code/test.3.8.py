places = ["ShanDong", "GuangZhou", "GuangXi", "Beijing", "Shanghai"]

print(places, "原始排列顺序")
print(sorted(places), "sorted()按字母顺序打印列表")
print(places, "再次打印该列表 排列顺序未变")
print(sorted(places, reverse = True), "sorted()按与字母顺序相反的顺序打印列表")
print(places,"再次打印该列表 核实排列顺序未变")
places.reverse()
print(places, "reverse()修改列表元素的排列顺序")
places.reverse()
print(places, "reverse()再次修改列表元素的排列顺序 已恢复到原来的排列顺序。")
places.sort()
print(places, "sort()修改该列表，使其元素按字母顺序排列")