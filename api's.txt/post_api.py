from flask import Flask ,request, render_template,jsonify
import mysql.connector
mydb = mysql.connector.connect(
      host="localhost",
  user="root",
  password="root",
  database="OrderBookSys"
)

app=Flask(__name__)
@app.route("/")
def hello():
    return  ("hello world")
@app.route('/getStocks', methods=['GET'])
def get_stocks():
     mycursor = mydb.cursor()
     mycursor.execute("SELECT * FROM orderbooksys.order")
     return jsonify( mycursor.fetchall())

@app.route('/placeOrder', methods=['POST'])
def place_order():
     mycursor = mydb.cursor()
     body=request.json
     #  print(body)
     sql = "INSERT INTO `orderbooksys`.`order` (`Stock_id`, `order_id`, `Customer_id`, `Order_type`, `price`, `quantity`) VALUES ("+str(body["stockId"])+","+str(body["orderId"])+","+str(body["customerId"])+",'" +str(body["orderType"])+"'," +str(body["price"])+"," +str(body["quantity"])+");"
     print(sql)

     mycursor.execute(sql)
     mydb.commit()
     return "order placed"
app.run(debug=True)


