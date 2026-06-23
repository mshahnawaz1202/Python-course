def main():
    try:
        a=int(input("Enter a Number : "))
        # print(a)
        print(f"The Value is {a}")
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am in Finally")
        



main()

# finally is mostly used in functions it always run even if function returns