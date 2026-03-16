import math
import numpy as np
import joblib
from django.conf import settings
from django.shortcuts import render
from .forms import ClientDetailsForm

# Load the pre-trained model
model = joblib.load('static/regresser2081905.joblib')

def LoanAmountPredict(request):
    if request.method == 'POST':
        form = ClientDetailsForm(request.POST)
        if form.is_valid(): 
            # Extract form data
            name = form.cleaned_data['name']
            gender = form.cleaned_data['sex']
            marital_status = form.cleaned_data['marital']
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']
            family_income = form.cleaned_data['family_income']
            HomeValue = form.cleaned_data['home_value']
            period = form.cleaned_data['tenure']
            interest = form.cleaned_data['interest']

            # Validate inputs
            if salary < 0 or family_income < 0 or HomeValue < 0:
                form.add_error(None, "Income and home value must be non-negative.")
                return render(request, 'loanamount.html', {'form': form})

            # Calculate derived features
            MonthlyIncome = round(float(salary + family_income), 2)
            ELoanAmount = round(0.7 * HomeValue, 2)
            MaxEmi = MonthlyIncome / 2

            # Calculate MaxLoanAmount
            #Calculation of MaxLoanAmount
            emi = MaxEmi
            t = period * 12
            r = interest / 1200
            r1 = (1+r)
            r1 = math.exp(math.log(r1)*t)
            deno = r1
            num = r1-1
            factor=(num/deno)
            MaxLoanAmount = ((emi * factor ) / r)
            MaxLoanAmount = round(MaxLoanAmount, 2)
           

            #Other Features
            period = period * 12
            ELoanToMaxLoan = ELoanAmount / MaxLoanAmount

            #Saving Data in other variable
            homevalue = HomeValue
            time = t
            monthlyincome = MonthlyIncome
            eloanamount = ELoanAmount
            maxemi = MaxEmi
            maxloanamount = MaxLoanAmount


            #Apply Log Transformation
            HomeValue = np.log1p(HomeValue)
            MonthlyIncome = np.log1p(MonthlyIncome)
            ELoanAmount = np.log1p(ELoanAmount)
            MaxEmi = np.log1p(MaxEmi)
            MaxLoanAmount = np.log1p(MaxLoanAmount)


            #Features Selection for Target Prediction
            features = [[HomeValue, MonthlyIncome, MaxEmi, ELoanAmount, MaxLoanAmount, ELoanToMaxLoan]]

            #Make the Prediction
            prediction = model.predict(features)
            result = prediction[0]
            result = np.expm1(result)
            result = int(result)
            if result >= eloanamount:
                result = eloanamount
            else:
                result = maxloanamount
            result = round(result, -5)    


            #Create Dictionary
            client_details = {
                'name': name,
                'age':age,
                'gender':gender,
                'marital': marital_status,
                'tenure': period,
                'interest':interest,
                'monthlyincome':monthlyincome,
                'homevalue': homevalue,
                'time': time,
                'maxloanamount': maxloanamount,
                'maxemi': maxemi,
                'eloanamount': eloanamount,
                'result': result
            }

            return render(request, 'loanamount.html', {'form': form, 'client': client_details})
        else:
            # If form is invalid, render the form with errors
            return render(request, 'loanamount.html', {'form': form})
    else:
        form = ClientDetailsForm()

    return render(request, 'loanamount.html', {'form': form})