#DEBUG: Detailed information, typically of interest only when diagnosing problems.
import time

#INFO: Confirmation that things are working as expected.

#WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space is low'). The software is still working as expected.

#ERROR: Due to a more serious problem, the software has not been able to perform some function.

#CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


# 📌 الخلاصة:
#
# DEBUG → أدق التفاصيل للتشخيص.
#
# INFO → كل شيء تمام.
#
# WARNING → في شيء مش طبيعي، لكن البرنامج مستمر.
#
# ERROR → خطأ منع وظيفة معينة.
#
# CRITICAL → البرنامج نفسه ممكن يتوقف.



# import logging
# logging.basicConfig(filename="abd log",level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
#
# def add(x,y):
#     return x+y
#
#
# add_result=add(4,6)
# logging.debug(add_result)
#
# logging.basicConfig(filename="emloyee.log",level=logging.INFO,format='%(levelname)s:%(message)s')
# class Employee:
#
#     """A sample Employee class"""
#
#     def __init__(self, first, last):
#
#         self.first = first
#
#         self.last = last
#
#         logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))
#
#     @property
#
#     def email(self):
#
#         return '{}.{}@email.com'.format(self.first, self.last)
#
#     @property
#
#     def fullname(self):
#
#         return '{} {}'.format(self.first, self.last)
#
# emp_1 = Employee('John', 'Smith')
#
# emp_2 =Employee('Corey', 'Schafer')
# emp_3 =Employee('Corey', 'Schafer')


print(time.time())
