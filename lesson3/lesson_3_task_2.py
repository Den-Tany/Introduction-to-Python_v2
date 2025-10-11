from smartphone import Smartphone
catalog=[
    Smartphone("Урал", "У-124", "+79654828765"),
    Smartphone("Нева", "Н-65946", "+7968755867"),
    Smartphone("Вятка", "Вятка1", "+7925866897"),
    Smartphone("Siemens", "C-35", "+7925687126"),
    Smartphone("Sony", "Yula", "+79325614862")
]
length=len(catalog)
for result in range(0, length):
    catalog[result].printCat()
    