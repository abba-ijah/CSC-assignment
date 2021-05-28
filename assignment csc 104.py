def menu():
    tb = input("\n1. Airtime-Self \n2. Airtime-Others \n3. Transfer-UBA \n4. Transfer-Other Banks \n5. Transfer-UBA Prepaid \n6. Check your account balance \n7. Pay Bills \n8. Next")
def men():
    print("\nPlease enter your four digit PIN")
    print("Enter 0 to return to MAIN")
    m = int(input(""))
def me():
    print("\nPlease enter destination phone line or the last four digits of the number : ")
    print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
    m = int(input(""))
def m():
    print("\n1. Increase Limit \n2. Buy Data Self \n3. Buy Data Others \n4. Cardless Withdrawal \n5. Banking Services \n6. Next \n0. To go BACK")
ta = input("Please type in the bank USSD code for UBA : ")
if(ta=="919"):
    print("\nYou have entered the code for UBA")
    print("\n1. Airtime-Self \n2. Airtime-Others \n3. Transfer-UBA \n4. Transfer-Other Banks \n5. Transfer-UBA Prepaid \n6. Check your account balance \n7. Pay Bills \n8. Next")
    tb = input("Select one option : ")
    if(tb=="1"):
        print("\nPlease enter your four digit PIN")
        print("Enter 0 to return to MAIN")
        m = input("")
        if(m=="0"):
            menu()
        elif(m=="1","2","3","4","5","6","7","8","9"):
            print("\nPlease enter amount (50 - 10000)")
            print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
            y = int(input(""))
            if(y<50):
                print("\nWrong input")
            elif(y>10000):
                print("\nWrong input")
            elif(y=="00"):
                   men()
            elif(y=="0"):
                    menu()
            elif(y=="1","2","3","4","5","6","7","8","9"):
                print("\nTransaction successful")     
            else:
                print("\nWrong input")
        else: 
            print("\nWrong input")
    elif(tb=="2"):
                    print("\nPlease enter your four digit PIN")
                    print("Enter 0 to return to MAIN")
                    m = input("")
                    if(m=="0"):
                        menu()
                    elif(m=="1","2","3","4","5","6","7","8","9"):
                        print("\nPlease enter destination phone line or the last four digits of the number")
                        print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                        y = input("")
                        if(y=="00"):
                             men()
                        elif(y=="0"):
                            menu()
                        elif(y=="1","2","3","4","5","6","7","8","9"):
                            print("\nPlease enter amount (50 - 10000)")
                            print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                            y = int(input(""))
                            if(y<50):
                                print("\nWrong input")
                            elif(y>10000):
                                print("\nWrong input")
                            elif(y=="00"):
                                men()
                            elif(y=="0"):
                                menu()
                            elif(y=="1","2","3","4","5","6","7","8","9"):
                                print("\nWould you like to save this beneficiary? \n \n")
                                print("1. Yes \n2. No \n00. To go BACK \n0. To return to MAIN")
                                y = input("")
                                if(y=="00"):
                                    men()
                                elif(y=="0"):
                                    menu()
                                elif(y=="1"):
                                    print("\nBeneficiary save")
                                    print("Transaction successful")
                                elif(y=="2"):
                                    print("\nTransaction successful")
                                else:
                                    print("\nWrong input")
                            else:
                                print("\nWrong input")
                        else:
                            print("\nWrong input")
                    else:
                        print("\nWrong input")
    elif(tb=="3"):
        print("\nPlease enter your four digit PIN")
        print("\nEnter 0 to return to MAIN")
        m = input("")
        if(m=="0"):
            menu()
        elif(m=="1","2","3","4","5","6","7","8","9"):
            print("\nPlease enter UBA account number or name of the beneficiary")
            print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
            y = input("")
            if(y=="00"):
                men()
            elif(y=="0"):
                menu()
            elif(y=="1","2","3","4","5","6","7","8","9"):
                print("\nPlease enter amount (50 - 10000)")
                print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                y = int(input(""))
                if(y<50):
                    print("\nWrong input")
                elif(y>10000):
                    print("\nWrong input")
                elif(y=="00"):
                    men()
                elif(y=="0"):
                    menu()
                elif(y=="1","2","3","4","5","6","7","8","9"):
                    print("\nWould you like to save this beneficiary? \n \n")
                    print("1. Yes \n2. No \n00. To go BACK \n0. To return to MAIN")
                    y = input("")
                    if(y=="00"):
                        men()
                    elif(y=="0"):
                        menu()
                    elif(y=="1"):
                        print("\nBeneficiary saved")
                        print("Transaction successful")
                    elif(y=="2"):
                        print("\nTransaction successful")
                    else:
                        print("\nWrong input")                  
                else:
                    print("\nWrong input")
        else:
            print("\nWrong input")
    elif(tb=="4"):
        print("\nPlease enter your four digit PIN")
        print("Enter 0 to return to MAIN")
        m = input("")
        if(m=="0"):
            menu()
        elif(m=="1","2","3","4","5","6","7","8","9"):
            print("\nPlease enter bank account number or name of beneficiary : ")
            print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
            y = input("")
            if(y=="00"):
                 men()
            elif(y=="0"):
                menu()
            elif(y=="1","2","3","4","5","6","7","8","9"):
                print("\nPlease select bank : \n1. First Bank \n2. Zenith Bank \n3. GT Bank \n4. JAIZ Bank \n5. Access Bank")
                print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                t = input("Select one option : ")
                if(t=="00"):
                    men()
                elif(t=="0"):
                    menu()
                elif(t=="1","2","3","4","5","6","7","8","9"):
                    print("\nSend money to ",y,".""\nPlease enter amount(amount greater than NGN20,000 will require Secure Pass):")
                    print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                    t = int(input(""))
                    if(t>20000):
                        print("\nPlease type Secure Pass")
                        w = int(input(""))
                        print("\nTransaction successful")
                    elif(t=="00"):
                        men()
                    elif(t=="0"):
                        menu()
                    elif(t=="1","2","3","4","5","6","7","8","9"):
                        print("\nWould you like to save this beneficiary? \n \n")
                        print("1. Yes \n2. No \n00. To go BACK \n0. To return to MAIN")
                        y = input("")
                        if(y=="00"):
                            men()
                        elif(y=="0"):
                            menu()
                        elif(y=="1"):
                            print("\nBeneficiary saved")
                            print("Transaction successful")
                        elif(y=="2"):
                            print("\nTransaction successful")
                        else:
                            print("\nWrong input")
                    else:
                        print("\nWrong input")
                else:
                    print("\nWrong input")
            else:
                print("\nWrong input")
        else:
            print("\nWrong input")
    elif(tb=="5"):
        print("\nPlease enter your four digit PIN")
        print("Enter 0 to return to MAIN")
        m = input("")
        if(m=="0"):
            menu()
        elif(m=="1","2","3","4","5","6","7","8","9"):
            print("\nPlease enter card client id (full 10 digits) or name of beneficiary")
            print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
            t = input("")
            if(t=="00"):
                men()
            elif(t=="0"):
                menu()
            elif(t=="1","2","3","4","5","6","7","8","9"):
                print("\nWould you like to save this beneficiary? \n \n")
                print("1. Yes \n2. No \n00. To go BACK \n0. To return to MAIN")
                y = input("Select one option : ")
                if(y=="00"):
                    men()
                elif(y=="0"):
                    menu()
                elif(y=="1"):
                    print("\nBeneficiary saved")
                    print("Transaction successful")
                elif(y=="2"):
                    print("\nTransaction successful")
                else:
                    print("\nWrong input")
            else:
                print("\nWrong input")
        else:
            print("\nWrong input")
    elif(tb=="6"):
        print("\nTransaction fee of N10 applies. \nDo you wish to continue?")
        print("1. Yes \n2. No \n00. To go BACK")
        u  = input("Select one option : ")
        if(u=="00"):
            menu()
        elif(u=="1"):
            print("\nAn SMS will be sent to you shortly")
        elif(u=="2"):
            print("\nThank you")
        else:
            print("\nWrong input")
    elif(tb=="7"):
        print("\nPlease enter your four digit PIN")
        print("Enter 0 to return to MAIN")
        m = input("")
        if(m=="0"):
            menu()
        elif(m=="1","2","3","4","5","6","7","8","9"):
            print("\nPlease select: \n1. Cable TV \n2. Betting/Lottery \n3. Electricity - Prepaid \n4. Electricity - Postpaid \n5. Tolls \n \n6. Next \n00. Back \n0. Main")
            i = input("Select one option : ")
            if(i=="1"):
                print("\nPlease select: \n1. Startimes \n2. MyTV Smart Payment \n3. Consat Subscription \n4. TrendTV \n5. Cable Africa Network TV \n \n6. Next \n00. Back \n0. Main")
                o = input("Select one option : ")
                if(o=="1"):
                    print("\nPlease enter smartcard/ewallet number: \n00. To go BACK \n0. To return to MENU")
                    p = input("")
                    if(p=="00"):
                        men()
                    elif(p=="0"):
                        menu()
                    elif(p=="1","2","3","4","5","6","7","8","9"):
                        print("\nPlease enter amount")
                        print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                        y = int(input(""))
                        if(y=="00"):
                            men()
                        elif(y=="0"):
                            menu()
                        elif(y=="1","2","3","4","5","6","7","8","9"):
                            print("\nWould you like to save this beneficiary? \n \n")
                            print("1. Yes \n2. No \n00. To go BACK \n0. To return to MAIN")
                            y = input("")
                            if(y=="00"):
                                men()
                            elif(y=="0"):
                                menu()
                            elif(y=="1"):
                                print("\nBeneficiary saved")
                                print("Transaction successful")
                            elif(y=="2"):
                                print("\nTransaction successful")
                            else:
                                print("\nWrong input")
                        else:
                            print("\nWrong input")
                    else:
                        print("\nWrong input")
                elif(o=="2"):
                    print("\nPlease enter smartcard number : \n00. To go BACK \n0. To return to MENU")
                    a = input("")
                    if(a=="00"):
                        men()
                    elif(a=="0"):
                        menu()
                    elif(a=="1","2","3","4","5","6","7","8","9"):
                        print("\nPlease enter amount")
                        print("Enter 00 to go BACK \nEnter 0 to return to MAIN")
                        s = int(input(""))
                        if(s=="00"):
                            men()
                        elif(s=="0"):
                            menu()
                        elif(s=="1","2","3","4","5","6","7","8","9"):
                            print("\nWould you like to save this beneficiary? \n \n")
                            print("1. Yes \n2. No \n00. To go BACK \n0. To return to MAIN")
                            d = input("Select one option : ")
                            if(d=="00"):
                                men()
                            elif(d=="0"):
                                menu()
                            elif(d=="1"):
                                print("\nBeneficiary saved")
                                print("Transaction successful")
                            elif(d=="2"):
                                print("\nTransaction successful")
                            else:
                                print("\nWrong input")
                        else:
                            print("\nWrong input")
                    else:
                        print("\nWrong input")
    elif(tb=="8"):
        print("\n1. Increase Limit \n2. Buy Data Self \n3. Buy Data Others \n4. Cardless Withdrawal \n5. Banking Services \n6. Next \n0. To go BACK")
        f = input("Select one option : ")
        if(f=="6"):
            print("\n1. PayAttitude \n2. Generate OTP \n3. Mini Statement \n4. Open account \n5. PIN setup \n \n6. Life Style \n \n7. Delete beneficiary \n \n00. To go BACK")
            f = input("Select one option : ")
            if(f=="00"):
                m()
            else:
                print("OKAY")
        elif(f=="0"):
            menu()
        else:
            print("OKAY")
    else:
        print("Wrong input")                
else:
    print("Wrong input")
                
                
                            
                            
                            
                 
                       
        
    
      
