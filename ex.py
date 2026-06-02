from b_ac1 import BankAccount
from loan_ac1 import LoanAccount

mybank = BankAccount("Chan Taiman","123456",0,1000)
mybank.greeting()
mybank.setLoan(2000)
loanacc = LoanAccount(mybank.getCust(),mybank.getAccNum(),0.05,mybank.getLoan(),mybank.getBal())
loanacc.retLoan(500)
loanacc.check_balance()
loanacc.debit_interest()
loanacc.check_balance()
