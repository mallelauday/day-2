StudentID=input("Enter the Student Id:")
EmailID=input("Enter the Email id:")
Password=input("Enter the password:")
ReferralCode=input("Enter the referral code:")
stu=0
email=0
password=0
referral=0
if StudentID[0:3]=="CSE" and StudentID[3]=='-' and StudentID[4:7].isdigit():
    stu=1
if '@'in EmailID and '.'in EmailID and EmailID[0]!='@' and EmailID[len(EmailID)-1]!='@' and EmailID[-4:]=='.edu':
    email=1
if len(Password)>=8 and 'A'<=Password[0]<='Z' and ( Password.count("0") + Password.count("1") + Password.count("2") + Password.count("3") + Password.count("4") + Password.count("5") + Password.count("6") + Password.count("7") + Password.count("8") + Password.count("9")>=1):
    password=1
if ReferralCode[0:3]=="REF" and '0'<=ReferralCode[3:5]<='9' and ReferralCode[5]=='@':
    referral=1
if stu==1 and password==1 and referral==1 and email==1:
    print("APPROVED")
else :
    print("REJECTED")
