# connecting database
from sqlalchemy import create_engine, text




def load_jobs_from_db():
  
  # list to map values
  keys = ['id','title','location','salary','currency','responsibilities','requirements']
  
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))  
  
    jobs = []
    for row in result.all():
      row_val_ls = list(row)
      jobs.append(dict(zip(keys,row_val_ls)))
  
    return jobs

print(load_jobs_from_db())

# connection to execute command
# result -> cursor type
# result.all() -> list type
# result.all()[0] -> row


  
  # result_all = result.all()
  # print(result_all)
  # print(result_all[1][6])
  
  # first_result_dict = dict(result_all[0])
  # print(type(first_result_dict))
  # print(first_result_dict)
  