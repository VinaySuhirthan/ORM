# Ex02 Django ORM Web Application
## Date: 13-11-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

<br>
<br>
<br>
<br>

![image](https://github.com/user-attachments/assets/a9b45219-c434-4894-a038-27c7287bc8cb)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

## admin.py
```
from django.contrib import admin
from .models import Bank_loan,Bank_loanAdmin
admin.site.register(Bank_loan,Bank_loanAdmin)
```
## models.py
```
from django.db import models
from django.contrib import admin
class Bank_loan(models.Model):
    Customer_Name=models.CharField(max_length=100)
    Customer_Age=models.IntegerField()
    Loan_Amount=models.IntegerField()
    Loan_Type=models.CharField(max_length=100)
    Loan_Duration=models.DateField()

class Bank_loanAdmin(admin.ModelAdmin):
    list_display=('Customer_Name','Customer_Age','Loan_Amount','Loan_Type','Loan_Duration')
```

## OUTPUT

![bankloan](https://github.com/user-attachments/assets/2a1544cb-034a-4981-b6af-1ab383a4452b)

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

![user](https://github.com/user-attachments/assets/dddb5a1a-4c64-4c1d-b316-664a292e89b8)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
