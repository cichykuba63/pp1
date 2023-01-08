def f(human_age):
    dog_age = 0

    if human_age < 3:
        dog_age += human_age * 10
    else:
        dog_age += 20
        dog_age += (human_age - 2) * 4

    return dog_age
