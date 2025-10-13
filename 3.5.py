def printFunction1() -> str:
    return "I'm a student."

def printFunction2()-> str:
    ans = round(1/7,5)
    return str(ans)

def sum2Num (num1 : int, num2 : int) -> int:
    return num1 + num2

def readFile(fileName: str) -> str:
    content = ""
    try:
        with open(fileName, 'r') as file:
            content += file.read()
    except FileNotFoundError:
        content = "File not found."
    return content

def main():
    bt1 = printFunction1()
    bt2 = printFunction2()
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = sum2Num(num1, num2)
    fileName = input("Enter the file name: ")
    content = readFile(fileName)
    with open ("output.txt", "w", encoding="utf-8") as file:
        file.write(f"{bt1}\n{bt2}\nThe sum of {num1} and {num2} is {result}\nFile content: {content}")

if __name__ == "__main__":
    main()
