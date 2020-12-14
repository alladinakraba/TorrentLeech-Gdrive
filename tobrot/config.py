from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1306351743:AAFHYAkdVjd1xWjzFWclkRk7jGwdMbVIgN4"
    APP_ID = 1140241
    API_HASH = "8790da9a62ae66d0847cd3da7fd54aff"
    OWNER_ID = 762900336
    AUTH_CHANNEL = [-1001388845022]
    DESTINATION_FOLDER = "0000000000" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive
client_id = 305259590179-plk0ir2vlioakkjkkje7rr99e67a2lfu.apps.googleusercontent.com
client_secret = nWGnqywCvYKjzyPVmJGMJZpI
scope = drive
root_folder_id = 1764Mg8vw2-Qm82Jc_DzzgzoAIHEtYm1o
token = {"access_token":"ya29.a0AfH6SMCvyUuAXGK8URUlszUmWUpDwsOd623dltdKMB9Y0iasGigonoqghGKg2dCoUGTR_3hnYuLYfyp9dhacPKkQ5El0mLQKL02f24TahTG-vQQnbXDtSAdP_KWoBQpt1SddoU7P2QPdpX11syl_b7TFkZZps19fZyhSCQUbUvo","token_type":"Bearer","refresh_token":"1//0gQ_G2kGCGxf9CgYIARAAGBASNwF-L9Ir9V8Dj-KGQwv8-aAZpdIaN4kxMAHcuAYq6a2BzZO4w7QHUJNkkbn3vIzCRdbZPuhwlKA","expiry":"2020-12-03T17:42:25.2985968+05:30"}
team_drive = 0AEUoeG8XHOixUk9PVA"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...