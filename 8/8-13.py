def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


new_profile = build_profile('aleksey', 'zaitcev', place_of_birthday='USSR', hello='hi', poker='NO')

print(new_profile)
