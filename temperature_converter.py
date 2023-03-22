while True:
    menu = int(input("1) fahrenheit to celsius  2) celsius to farenheit   3)exit : "))

    if menu == 1:
         fahrenheit = float(input('Enter temperature in Fahrenheit : '))
         celsius = (fahrenheit - 32.0) * (5.0/9.0)
         #System.out.println(fahrenheit = " degrees fahrenheit is " + celsius = "
         #print("화씨 %.2lf도는 섭씨 %.2lf도 입니다" % (fahrenheit, celsius))
         #print(f"화씨 {fahrenheit:.2f}도는 섭씨 {celsius:.2f}도 입니다")
         print("화씨 {0:.2f}도는 섭씨 {1:.2f}도 입니다".format(fahrenheit, celsius))
    elif menu ==2:
         #(0°C × 9/5) + 32 = 32°F
         celsius = float(input('Enter temperature in celsius : '))
         fahrenheit = (celsius - 32.0) * (5.0 / 9.0)
         print(f"{celsius:.2f} degrees Celsius is {fahrenheit:.2f} degrees Farenheit.")
    elif menu == 3:
        break # exit(1)
    else :
        print("program finished!")



# (0°C × 9/5) + 32 = 32°F
