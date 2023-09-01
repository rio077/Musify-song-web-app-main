import pymongo, cloudinary

mongoURI="mongodb+srv://Naman00:257917Coder@cluster1.jj52hn0.mongodb.net/?retryWrites=true&w=majority"
client=pymongo.MongoClient(mongoURI)
x_token_env="1"
orgKey="1"
db=client["Musify"]

Login=db["Login"]
SignUp=db["SignUp"]
Songs=db["Songs"]


cloudinary.config(
  cloud_name = "dwpjitown",
  api_key = "427843121278645",
  api_secret = "eubGg5OHrF1YmcU4xxcaz2ZQfJU",
  secure = True
)