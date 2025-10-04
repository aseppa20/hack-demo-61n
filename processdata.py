import mysql.connector as mysqlc
import data_init
import json
import random

class truck:
    def __init__(self, regnumber: str, location: tuple = (-1, -1), confidence: float = 0):
        self.location = location
        self.regnumber = regnumber
        self.confidence = confidence

def handle_data():
    ajoneuvot = mysqlc.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="root",
        database="auto_demo")

    tulli = mysqlc.connect(
        host="127.0.0.1",
        port=3308,
        user="root",
        password="root",
        database="tulli_demo")

    yritys = mysqlc.connect(
        host="127.0.0.1",
        port=3309,
        user="root",
        password="root",
        database="yritys_demo")

    # poison = mysqlc.connect(
    #     host="127.0.0.1",
    #     port=3310,
    #     user="root",
    #     password="root")

    central = mysqlc.connect(
        host="127.0.0.1",
        port=3311,
        user="root",
        password="root",
        database="demo_demo")

    ajoneuvot_cur = ajoneuvot.cursor(buffered=True)
    tulli_cur = tulli.cursor(buffered=True)
    yritys_cur = yritys.cursor(buffered=True)
    # poison_cur = poison.cursor()
    central_cur = central.cursor(buffered=True)

    ajoneuvot_cur.execute("SELECT * FROM Ajoneuvot")

    for row in ajoneuvot_cur: # pyright: ignore[reportGeneralTypeIssues]
        confidence = 40
        new_truck = truck(str(row[0])) # pyright: ignore[reportArgumentType]
        autojson = json.dumps(str(row))
        tulli_cur.execute(f"SELECT * FROM Tulli WHERE Rekisteri='{row[0]}'") # pyright: ignore[reportArgumentType]
        tullijson = json.dumps(str(tulli_cur.fetchall()))
        if "{}" in tullijson or '[]' in tullijson:
            confidence += 20
        yritys_cur.execute(f"SELECT * FROM Kuljetusyritys WHERE Rekisteri='{row[0]}'") # pyright: ignore[reportArgumentType]
        yritysjson = json.dumps(str(tulli_cur.fetchall()))
        if "'{}'" not in yritysjson or "'[]'" not in yritysjson:
            confidence += 20
        
        new_truck.confidence = confidence

        count_jarvenpaa = autojson.count("Järvenpää")
        count_jarvenpaa += tullijson.count("Järvenpää")
        count_jarvenpaa += yritysjson.count("Järvenpää")

        count_helsinki = autojson.count("Helsinki")
        count_helsinki += tullijson.count("Helsinki")
        count_helsinki += yritysjson.count("Helsinki")

        count_vantaa = autojson.count("Vantaa")
        count_vantaa += tullijson.count("Vantaa")
        count_vantaa += yritysjson.count("Vantaa")

        count_espoo = autojson.count("Espoo")
        count_espoo += tullijson.count("Espoo")
        count_espoo += yritysjson.count("Espoo")

        count_kaun = autojson.count("Kauniainen")
        count_kaun += tullijson.count("Kauniainen")
        count_kaun += yritysjson.count("Kauniainen")

        count_nurmi = autojson.count("Nurmijärvi")
        count_nurmi += tullijson.count("Nurmijärvi")
        count_nurmi += yritysjson.count("Nurmijärvi")

        # Very naive, find highest propability where the truck is by counting occurances. Not a good way to fuse data, but I got no better idea to implement
        
        highest_count = max((count_helsinki, count_espoo, count_jarvenpaa, count_kaun, count_nurmi, count_vantaa))
        
        if highest_count == 0:
            new_truck.location = (-1, -1)
        elif highest_count == count_helsinki:
            new_truck.location = (random.randint(66,72), random.randint(45,52))
        elif highest_count == count_espoo or highest_count == count_kaun:
            new_truck.location = (random.randint(58,66), random.randint(24,32))
        elif highest_count == count_vantaa:
            new_truck.location = (random.randint(42,49), random.randint(50,60))
        elif highest_count == count_jarvenpaa:
            new_truck.location = (random.randint(12,17), random.randint(64,70))
        try:
            central_cur.execute(f"INSERT INTO Central(Rekisteri, autoJSON, tulliJSON, yritysJSON, locationX, locationY, confidence) VALUES ('{new_truck.regnumber}', {autojson}, {tullijson}, {yritysjson}, {new_truck.location[0]}, {new_truck.location[1]}, {new_truck.confidence});")
        except mysqlc.IntegrityError:
            print("Duplicate found, but ignored")

    # Close connection
    ajoneuvot.close()
    tulli.close()
    yritys.close()
    central.commit()
    central.close()

def create_data_for_heatmap() -> list:
    
    list_of_locations = []

    central = mysqlc.connect(
        host="127.0.0.1",
        port=3311,
        user="root",
        password="root",
        database="demo_demo")
    
    central_cur = central.cursor(buffered=True)

    central_cur.execute("SELECT locationX, locationY, confidence FROM Central")

    for row in central_cur: # pyright: ignore[reportGeneralTypeIssues]
        location = (row[0], row[1]) # pyright: ignore[reportArgumentType]
        if int(row[2]) < 0 or location[0] == -1 or location[1] == -1: # pyright: ignore[reportArgumentType]
            pass
        elif int(row[2]) > 59: # pyright: ignore[reportArgumentType]
            list_of_locations.append(location)
            list_of_locations.append(location)
        else:
            list_of_locations.append(location)
    
    central.close()
    return list_of_locations

def create_data_for_helsinki() -> str:
    
    html = ""

    central = mysqlc.connect(
        host="127.0.0.1",
        port=3311,
        user="root",
        password="root",
        database="demo_demo")
    
    central_cur = central.cursor(buffered=True)

    central_cur.execute("SELECT locationX, locationY, confidence, Rekisteri FROM Central")

    for row in central_cur: # pyright: ignore[reportGeneralTypeIssues]
        location = (row[0], row[1]) # pyright: ignore[reportArgumentType]
        if location[0] >= 67 and location[0] <= 72 and location[1] >= 47 and location[1] <= 52:
            if row[2] >= 80:
                html += f"<span style='color:green;'>High confidence truck: {row[3]}</span><br />"
            elif row[2] >= 60:
                html += f"<span style='color:yellow;'>Mid confidence truck: {row[3]}</span><br />"
            else:
                html += f"<span style='color:red;'>Low confidence truck: {row[3]}</span><br />"
        
    central.close()
    return html

def init_demo(create_tables=False, insert_data=False):
    ajoneuvot = mysqlc.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="root",
        database="auto_demo")

    tulli = mysqlc.connect(
        host="127.0.0.1",
        port=3308,
        user="root",
        password="root",
        database="tulli_demo")

    yritys = mysqlc.connect(
        host="127.0.0.1",
        port=3309,
        user="root",
        password="root",
        database="yritys_demo")

    # poison = mysqlc.connect(
    #     host="127.0.0.1",
    #     port=3310,
    #     user="root",
    #     password="root")

    central = mysqlc.connect(
        host="127.0.0.1",
        port=3311,
        user="root",
        password="root",
        database="demo_demo")

    ajoneuvot_cur = ajoneuvot.cursor()
    tulli_cur = tulli.cursor()
    yritys_cur = yritys.cursor()
    # poison_cur = poison.cursor()
    central_cur = central.cursor()

    if create_tables:
        ajoneuvot_cur.execute("""CREATE TABLE Ajoneuvot (
            Rekisteri VARCHAR(10) PRIMARY KEY,
            Merkki TEXT NOT NULL,
            Malli TEXT NOT NULL,
            Valmistusvuosi INT,
            Rekisterointi_maa TEXT,
            Viime_sijainti TEXT,
            Status TEXT
            );""")

        tulli_cur.execute(""" CREATE TABLE Tulli (
            ID VARCHAR(10) PRIMARY KEY,
            Ylityspaikka TEXT NOT NULL,
            Suunta TEXT NOT NULL,
            Maa TEXT,
            pvm TIMESTAMP,
            Tulli_tunnus VARCHAR(20),
            Tulli_sijainti TEXT,
            Rekisteri VARCHAR(10),
            Maatunnus VARCHAR(10),
            Status BOOLEAN ); """)

        yritys_cur.execute("""CREATE TABLE Kuljetusyritys (
            ID VARCHAR(10) PRIMARY KEY,
            Rekisteri VARCHAR(10),
            Kuljettaja TEXT,
            Lahto TEXT,
            Maaranpaa TEXT,
            Kuormantyyppi TEXT,
            Lahtoaika TIMESTAMP,
            Saapumisaika TIMESTAMP,
            Status TEXT);""")
        
        central_cur.execute("""CREATE TABLE Central (
            Rekisteri VARCHAR(10) PRIMARY KEY,
            autoJSON LONGTEXT,
            tulliJSON LONGTEXT,
            yritysJSON LONGTEXT,
            locationX SMALLINT,
            locationY SMALLINT,
            confidence SMALLINT);
""")
    
    if insert_data:
        ajoneuvot_cur.execute(data_init.init_ajoneuvot_table())
        tulli_cur.execute(data_init.init_tulli_table())
        yritys_cur.execute(data_init.init_yritys_table())

    ajoneuvot.close()
    tulli.close()
    yritys.close()
    central.close()

if __name__ == "__main__":
    #init_demo(create_tables=True)
    #handle_data()
    print(create_data_for_heatmap())
