def http_status(status):
    match status:
        case 20:
            print(" ")
        case 100:
            print("")
        case 300:
            print(" ")
        case _:
            print("")


            