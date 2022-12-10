import configparser

COW_GROUP = 15
LINK = "https://st.scrdairy.com/"
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
USER, PASSWORD, FARM = config.get("DEMO", 'Email'), config.get("DEMO", "Password"), config.get("DEMO", "FarmID")