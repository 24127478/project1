def readFile(fileName: str) -> str:
    content = ""
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not found."
    return content

def main():
    fileName = input("Enter the file name: ")
    print(readFile(fileName))

if __name__ == "__main__":
    main()
