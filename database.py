# connecting database
from sqlalchemy import create_engine, text

db_conn_string = "mysql+pymysql://7wx4q7vlaxmzkf5c0jpb:pscale_pw_2VltpEPEiFnU9A9J0ZLF76hrkwQYeQNlUwtinP27Kxk@aws.connect.psdb.cloud/careers?charset=utf8mb4"


engine = create_engine(db_conn_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

# connection to execute command
# result -> cursor type
# result.all() -> list type
# result.all()[0] -> row

# function to map values
keys = ['id','title','location','salary','currency','responsibilities','requirements']

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))  

  result_dict = []
  for row in result.all():
    row_val_ls = list(row)
    result_dict.append(dict(zip(keys,row_val_ls)))

  print(result_dict)
  
  # result_all = result.all()
  # print(result_all)
  # print(result_all[1][6])
  
  # first_result_dict = dict(result_all[0])
  # print(type(first_result_dict))
  # print(first_result_dict)
  