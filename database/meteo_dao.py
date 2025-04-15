from database.DB_connect import DBConnect
#from model.situazione import Situazione


class MeteoDao():


    '''
    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result
        '''


    @staticmethod
    def getUmiditaMedia(mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT s.Localita, AVG(s.Umidita) as media
                    FROM situazione s 
                    WHERE MONTH(Data) = %s
                    GROUP BY s.Localita"""


        cursor.execute(query, (mese,))
        res = dict()
        for row in cursor:
            res[row["Localita"]] = row["media"]


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getUmiditaMesePrimiGiorni(mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.Localita, s.`Data`, s.Umidita
                    FROM situazione s 
                    WHERE MONTH(s.Data) = %s AND DAY(s.Data) < 16
                    ORDER BY s.Data ASC"""

        cursor.execute(query, (mese,))
        res = dict()
        for row in cursor:
            if row["Localita"] in res:
                res[row["Localita"]].append((row["Data"], row["Umidita"]))
            else:
                res[row["Localita"]] = [(row["Data"], row["Umidita"])]
        cursor.close()
        cnx.close()
        return res




if __name__ == '__main__':
    sitauzioni = MeteoDao.getUmiditaMesePrimiGiorni(2)
    print(sitauzioni)
    print(len(sitauzioni))






