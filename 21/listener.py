from typing import List ,Protocol, Any

#Observer interface
class Observer(Protocol):
    def update(self,data:Any)->None:
        pass

#Subject (Observable)
class Subject:
    def __init__(self):
        self._observers:List[Observer]=[]

    def attach(self,observer:Observer)->None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self,observer:Observer)->None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self,data:Any)->None:
        for observer in self._observers:
            observer.update(data)

class EmailAlert(Observer):
    def update(self,data:Any) ->None:
        print(f"EmailAlert: Notified with data: {data}")

class SMSAlert(Observer):
    def update(self,data:Any) ->None:
        print(f"SMSAlert: Notified with data: {data}")

if __name__=="__main__":
    subject=Subject()
    email_observer=EmailAlert()
    sms_observer=SMSAlert()


    subject.attach(email_observer)
    subject.attach(sms_observer)
    subject.notify("Temperature is above threshold")

    subject.detach(email_observer)

    subject.notify("Temperature is back to normal")