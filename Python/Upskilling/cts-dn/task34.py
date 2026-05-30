def getSalary(data, dept, name):
    if dept in data and name in data[dept]:
        salary = data[dept][name]
        print(salary)
        return salary
    else:
        print("Department or employee not found")
        return None
company_data = {
    "HR": {"HP": 50000,
           "Kriti": 55000
    },
    "IT": {"saje": 75000,
           "flower": 62000
    }
}
getSalary(company_data, "HR", "HP")
getSalary(company_data, "IT", "saje")

     



