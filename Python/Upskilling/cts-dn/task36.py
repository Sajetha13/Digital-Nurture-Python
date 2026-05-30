def get_common_skills(s1, s2):
    if not isinstance(s1, set) or not isinstance(s2, set):
        print("Error")
        return None
        
    common = s1 & s2
    print(common)
    return common

skills_a = {"Python", "SQL", "Git"}
skills_b = {"Java", "SQL", "Git", "C++"}

get_common_skills(skills_a, skills_b)
get_common_skills(skills_a, {"SQL", "Git"})