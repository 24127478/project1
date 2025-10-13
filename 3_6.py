text = "Hôm nay trời đẹp."

with open("output.txt", "wb") as file:
    writes = file.write(text.encode("utf-8"))
