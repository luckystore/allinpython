from com.CreditNotifier.CreditProcessorHelper import CreditProcessorHelper

helper = CreditProcessorHelper()
helper.CreditProcessorHelper("localhost","kiranmekanuri@gmail.com","venkeykiran","kiranmekanuri@gmail.com",
                             'localhost',"root","password","mysql")
EmailDetailsList = helper.read_unsent_notifications()
for EmailDetails in EmailDetailsList:
    print("invoker email:",EmailDetails.email)
    helper.sendEmailNotification(EmailDetails)
