#1.
my_f = open('test.txt', 'w')
line = input('Enter the text: \n')
while line:
    my_f.writelines(line)
    line = input('Enter the text: \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()


#2.
my_file = open('file_2.txt', 'r')
content = my_file.read()
print(f'File content: \n {content}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
print(f'Amount of lines in the text - {len(content)}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Amount of symbols {i + 1} -th line {len(content[i])}')
my_file = open('file_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'General amount of words - {len(content)}')
my_file.close()

# ------------------------------------3-----------------------------
'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''


with open('salary.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Salary less than 20 - {poor}, average salary - {sum(map(int, sal)) / len(sal)}')

#4. Не поняла эту часть задания, но надеюсь, что-то дельное да получилось: При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open('file_4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

#5.
def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Enter the numbers splited with space: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in the file')
    except ValueError:
        print('Incorrect input. Error of input-output')
summary()

#6.
import json

subj = {}
with open('file_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Amount of hourse for subject:\n {subj}')

#7.
import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0

with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average income: {prof_aver:.2f}')
    else:
        print(f"Average income doesn't exist. Everyone works at a lose.")
    pr = {'Average income': round(prof_aver)}
    profit.update(pr)
    print(f'The income of each company - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'File with the extension json was created with the following content:\n '
          f' {js_str}') 