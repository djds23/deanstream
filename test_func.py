import models

def format_data(db_size,result):
    '''input a number of units,a database and a list, and return the format with paths'''
    if db_size == 0:
        return result
    else:
        result.append([
                 models.Video.query.get(db_size).get_webm(),
                models.Video.query.get(db_size).get_mp4()
        ])
        format_data(db_size-1,result)

db_size= len(models.Video.query.all())
print format_data(db_size,[])

