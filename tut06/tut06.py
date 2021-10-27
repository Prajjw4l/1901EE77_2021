import re
import os 
import shutil

#shutil module used here to copy file from one destination to other 

def get_final_name(s_name, season_num, episode_num, episode_name, f_extension):
    new_file_name = s_name
    new_file_name += " - Season " + season_num
    new_file_name += " Episode " + episode_num
    new_file_name += episode_name
    new_file_name += f_extension

def regex_renamer():

    #input from the user
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    series = ["", "Breaking Bad", "Game of Thrones", "Lucifer"]
    path_w = os.path.join("wrong_srt", series[webseries_num])
    path_num = os.path.join("corrected_srt", series[webseries_num])

    if not os.path.exists(path_num):
        os.makedirs(path_num)
    incorrect_files = os.listdir(path_w)
    for f in incorrect_files:		
        shutil.copyfile(os.path.join(path_w, f),os.path.join(path_num, f))
        temp_list = re.findall(r"\d+",f)
        season_num = temp_list[0]
        temp_list = re.findall(r"\d+",f)
        episode_num = temp_list[1]
        temp_list = re.findall(r"\..{3}$",f)
        f_extension = temp_list[0]
        episode_name = ""
        if webseries_num != 1:
            episode_name = re.findall(r"[\w\s]+",f)[2]
            episode_name = episode_name.strip()
            episode_name = " - "+episode_name
        s_len = len(season_num)
        while season_padding > s_len:
            season_num = '0' + season_num
            s_len += 1
        e_len = len(episode_num)
        while episode_padding > e_len:
            episode_num = '0' + episode_num
            e_len += 1
        fin_name = get_final_name(series[webseries_num], season_num, episode_num, episode_name, f_extension)
        os.rename(os.path.join(path_num, f), os.path.join(path_num, fin_name))

regex_renamer()