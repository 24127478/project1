def readFile(fileName: str) -> str:
    content = ""
    try:
        with open(fileName, 'r') as file:
            content += file.read()
    except FileNotFoundError:
        content = "File not found."
    return content
def main():
    fileName = input("Enter the file name: ")
    content = readFile(fileName)
    open ("output.txt", "w").write(content)

if __name__ == "__main__":
    main()