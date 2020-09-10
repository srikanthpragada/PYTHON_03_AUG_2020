from django.shortcuts import render
from django.http import HttpResponse
import requests
import sqlite3


# Create your views here.

def home(request):
    return HttpResponse("<h1>Demo Application</h1>")


def index(request):
    return render(request, 'index.html')


def country_info(request):
    code = request.GET['code']
    response = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
    if response.status_code == 200:
        return render(request, 'country.html', {'country': response.json()})
    else:
        return render(request, 'country.html', {'message': 'Sorry! Country not found!'})


def list_employees(request):
    try:
        con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
        cur = con.cursor()
        cur.execute("select * from employees")
        employees = cur.fetchall()
        con.close()
        return render(request, 'employees.html', {'employees': employees})
    except Exception as ex:
        print("Error :", ex)
        return render(request, 'employees.html', {'employees': None})


def add_employee(request):
    if request.method == "GET":
        return render(request, 'add_employee.html')
    else:
        # Process data sent from client
        fullname = request.POST['fullname']
        job = request.POST['job']
        salary = request.POST['salary']
        try:
            con = sqlite3.connect(r"c:\classroom\aug3\hr.db")
            cur = con.cursor()
            cur.execute("insert into employees(name,job,salary) values(?,?,?)",
                        (fullname, job, salary))
            con.commit()
            con.close()
            return render(request, 'add_employee.html',
                          {'message': f'Added {fullname} Successfully!'})
        except Exception as ex:
            print("Error :", ex)
            return render(request, 'add_employee.html',
                          {'message': 'Sorry! Could not add employee!'})
