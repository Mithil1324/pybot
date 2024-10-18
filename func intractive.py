
import google.generativeai as genai


genai.configure(api_key = 'AIzaSyCLxDGc76Qcqg6RFfd0Wt2_Ht-YYq733GQ')
c = {"persona":"your name is tim you are a menu guide or restaurent for my restaurent MINE",
     "obj":"you are a menu guide , you want to ans for the prompt given by user by searching it in my database, if user didnt give input as related to food tell that i am here to ans you about our menu in our restaurent so ask about it, if you didnt get the data about some unknown food in the database you tell that sorry we didnt have that ,tell the data asked about the food asked byt the user ",
     "instruction":"you are menu guide for my restaurent MINE you need to give the data asked by the user , you should only take the information from the database MINE if the useer asked any other food which is not in the database you tell them that sorry we dont have that,if they asked irrelavent to the topic food tell them i am here to tell the info of food in our restaurent so ask about ",
     "output":"i want the output in the form of dictionary",
     "example":"{'user':'I need to know about the price of Dosa in your restuarant','assistant':'Price of Dosa is Rs.70'}",
     "remember":"all of the above information given, the code must be printes inside"}
c=str(c)  
import mysql.connector
def access_for_food_details():  
    connection = mysql.connector.connect(
        host="localhost",
        database="foodmenu",
        user="root",
        password="Mithil24@!"
    )
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM items"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    if rows :
        return rows[0] 
    else :
        None
model = genai.GenerativeModel("gemini-1.5-flash",system_instruction=c,tools=[access_for_food_details])
l=[]
ch = model.start_chat(enable_automatic_function_calling=True, history=l)
while (True):
    ques = input("enter ur ques:")
    ans = ch.send_message(ques)
    l.append({"role":"user","parts":ques})
    l.append({"role":"model","parts":ans})
    if "stop" in ques:
        break
    else:
        print(ans.text)
