
import memory_profiler as mem_profile
import random
import time

names = ["John", "Ram", "Shusil"]
majors = ["Math", "Java", "Python"]

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result_list = []
    for i in range(num_people):
        person = {
            'id':i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result_list.append(person)
    return  result_list


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.time()
people = people_list(100000)
t2 = time.time()


# t1 = time.time()
# people = people_generator(100000)
# t2 = time.time()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))
