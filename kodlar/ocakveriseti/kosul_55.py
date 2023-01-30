humidity = "low"
temperature = "high"

if humidity == "low" and temperature == "high":
    print("It's a hot desert.")
elif humidity == "low" and temperature == "low":
    print("It's an arctic desert.")
elif humidity == "high" and temperature == "high":
    print("It's a tropical forest.")
else:
    print("I don't know!")