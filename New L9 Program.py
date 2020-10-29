#Brian Onieal

#L9 Program

stockSymbol=input("Input stock symbol: ")

numberShares=int(input("Input number of shares to purchase: "))

buyPrice=float(input("Input price of stock: "))

sellPrice=float(input("Input the sell price of the stock: "))


#Below are the purchase calculations

buyTotal=numberShares * buyPrice        #Price multiplied by number of shares

buyCommission=buyTotal *.02             #Commission of 2% for share purchase

buyProfit= buyTotal + buyCommission     #Total profit from share purchase


sellProfit=sellPrice * numberShares     #Profit for selling shares

sellCommission=sellProfit *.02          #Commission of 2% for selling shares

sellTotal=sellProfit+sellCommission     #Total profit from share sale


totalCommission=buyCommission + sellCommission      #Commission total

totalProfit=sellTotal + sellCommission              #Profit recieved from selling   

totalAmount=sellProfit - buyTotal - totalCommission #Total made or lost


#Below are the output statements
print()
print("The total paid for", stockSymbol, "is:" +str(buyTotal))          #Price paid without commission

print("The commission for stock purchase is: "+str(buyCommission))      #Commission for share purchase

print("Total profit recieved from selling shares is: "+str(totalProfit))#Profit recieved from selling

print("Total commission from selling shares is: "+str(sellCommission))  #Commission from selling shares

print("Your amount made or lost is: "+str(totalAmount))                 #Total amount made or lost

