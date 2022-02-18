import psycopg2
import requests, json
class psql:
    def __init__(self, host,database,user,password):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def insertHospitalQuery(self,name,address,city,state,zipcode,x,y):
        try:
            self.cur.execute("""
                                INSERT INTO "appFolder_hospital"(hospital_name, hospital_address1, hospital_city, hospital_state, hospital_zipcode, hospital_x, hospital_y)
                                 VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                             ,(name,address,city,state,zipcode,x,y))
            self.conn.commit()
        except(Exception,psycopg2.DatabaseError) as error:
            print(error)
    def dbClose(self):
        self.conn.close()
        print('Database connection closed')

###-----------------------------------------------###
def getJson(request):

    response = requests.get(request).text
    # print(response)
    response_info = json.loads(response)
    features = response_info['features'] # attributes: {'NAME': ~~~ }, 'geometry':{ ~~~ }
    return features

    # for dict in features:
    #     info = dict['attributes'] # {'NAME': ~~~ }
    #     # print(info)
    #     print(info['NAME'])
    #     print(info['ADDRESS'])
    # # print(features[0])
    # # print(response_info['features'])
    # # print(response_info)
if __name__ == '__main__':

    db = psql("localhost","vaccinecenter","postgres","admin")
    # db.dbClose()
    features =getJson("https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/rest/services/Hospitals_1/FeatureServer/0/query?where=1%3D1&outFields=NAME,ADDRESS,CITY,STATE,ZIP&outSR=4326&f=json")
    for dict in features:
        info = dict['attributes']
        position = dict['geometry']
        db.insertHospitalQuery(info['NAME'],info['ADDRESS'],info['CITY'],info['STATE'],info['ZIP'],position['x'],position['y'])
        # Hospital address1 : info['ADDRESS']
        # Hospital city : info['CITY']
        # Hospital state : info['STATE']
        # Hospital zipcode : info['ZIP']
        #Hospital x : position['x']
        #Hospital y : position['y']
