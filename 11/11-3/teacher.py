from employee import Employee

teacher = Employee('Elena', 'Mixailovna', 14000)
print(teacher.annual_salary)
teacher.give_raise(7000)
print(teacher.annual_salary)