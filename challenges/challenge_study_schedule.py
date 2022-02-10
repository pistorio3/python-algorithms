def study_schedule(permanence_period, target_time):
    try:
        online_students = 0
        for checkin, checkout in permanence_period:
            if checkin <= target_time <= checkout:
                online_students += 1
        return online_students
    except TypeError:
        return None

# https://stackoverflow.com/questions/16021571/iterating-quickly-through-list-of-tuples
