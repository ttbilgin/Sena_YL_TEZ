tomorrow = "snowy"

match tomorrow:
    case "warm":
        print("I'll go to the sea.")
    case "very hot":
        print("I'll go to the forest.")
    case "snowy":
        print("I'll build a snowman.")
    case "rainy":
         print("I'll stay home.")
    case _:
        print("Weather not recognized.")